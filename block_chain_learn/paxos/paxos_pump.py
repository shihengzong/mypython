import threading  # 线程
import pickle  # 对象序列化
import socket
import queue


class MessagePump(threading.Thread):
    # 初始化
    def __init__(self, owner, port, timeout=3):
        self.owner = owner
        threading.Thread.__init__(self)
        self.abort = False  # 没有终止
        self.timeout = timeout
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Udp通信
        # 通信参数
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 200000)
        self.socket.bind('127.0.0.1', port)  # 通信地址和端口
        self.socket.settimeout(self.timeout)  # 超时设置
        self.queue = queue.Queue()  # 队列
        self.helper = MessagePump.Mphelper(self)  # 接收消息

    # 运行主线程
    def run(self):
        self.helper.start()  # 开启接受消息的线程
        while not self.abort:  # 线程还在进行
            msg = self.waitForMsg()  # 获取等待的消息
            self.owner.recvMessage(msg)

    # 等待消息
    def waitForMsg(self):
        try:
            msg = self.queue.get(True, 3)  # 获取数据3秒超时
            return msg
        except Exception as e:
            print(e)
            return None

    # 发送消息
    def sendMsg(self, msg):
        msg_byte = pickle.load(msg)
        addr = ("127.0.0.1", msg.to)
        self.socket.sendto(msg_byte, addr)
        return True

    def doAbort(self):
        # 设置状态为放弃
        self.abort = True

    # 开启socket线程
    class Mphelper(threading.Thread):
        def __init__(self, owner):
            self.owner = owner
            threading.Thread.__init__(self)

        def run(self):
            # 只要所有者的线程还没结束,就一直持续接收消息
            while not self.owner.abort:
                try:
                    # 接受socket消息
                    (byte_recv, addr) = self.owner.socket.recvfrom(2048)
                    # 反序列化消息成对象
                    msg_obj = pickle.load(byte_recv)
                    msg_obj.addr = addr[1]
                    # 把消息对象加入队列
                    self.owner.queue.put(msg_obj)
                except Exception as e:
                    print(e)
