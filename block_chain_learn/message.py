import datetime
import hashlib


class Message:
    def __init__(self, data):
        self.hash = None
        self.pre_hash = None
        self.timestamp = datetime.datetime.now()
        self.size = len(data.encode('utf-8'))  # 数据长度
        self.data = data
        self.payload_hash = self._hash_payload()

    def _hash_payload(self):
        val = str(self.timestamp) + str(self.data)  # hash(time+data)
        hash_val = val.encode('utf-8')
        return hashlib.sha256(hash_val).hexdigest()

    def _hash_message(self):  # hash(pre_hash + hash(time+data))
        val = str(self.pre_hash) + str(self.payload_hash)
        hash_val = val.encode('utf-8')
        return hashlib.sha256(hash_val).hexdigest()

    def seal(self):  # 密封
        self.hash = self._hash_message()  # 对应数据锁定,对于交易前的链锁定

    def validate(self):
        if self.payload_hash != self._hash_payload():  # 判断是否有人修改
            raise invalidMessage("交易数据与时间被修改" + str(self))
        if self.hash != self._hash_message():  # 判断消息链
            raise invalidMessage("交易的哈希链被修改" + str(self))

    def __repr__(self):
        mystr = "hash:{}, pre_hash:{}, data:{}".format(self.hash,
                                                       self.pre_hash,
                                                       self.data)
        return mystr

    def link(self, message):
        self.pre_hash = message.hash  # 链接


class invalidMessage(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
