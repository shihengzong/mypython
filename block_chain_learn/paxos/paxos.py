class Paxos_Message:
    # 常量
    MSG_ACCEPTOR_AGREE = 0  # 追随者约定
    MSG_ACCEPTOR_ACCEPT = 1  # 追随者接受
    MSG_ACCEPTOR_REJECT = 2  # 追随者拒绝(网络不通)
    MSG_ACCEPTOR_UNACCEPT = 3  # 追随者不同意
    MSG_ACCEPT = 4  # 接受
    MSG_PEOPOSE = 5  # 提议
    MSG_EXT_PROPOSE = 6  # 额外提议
    MSG_HEARTBEAT = 7  # 心跳,每隔一段时间同步消息

    # %消息初始化会有一个命令%
    def __init__(self, command=None):
        self.command = command

    def copyAsReply(self, msg):
        self.proposalid = msg.proposalid  # 提议id
        self.instanceid = msg.instanceid  # 当前id
        self.to = msg.to  # 发送给谁
        self.source = msg.source  # 消息来源
        self.value = msg.value  # 消息内容
