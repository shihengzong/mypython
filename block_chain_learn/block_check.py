import datetime
import hashlib


# msglist:[hash:9fc99da4d0e58e4d363c5e4d0ceb8a0b1d6b3935ead0a21e6f2c7aad0d516856, pre_hash:None, data:msg-001],  timestamp:None,  hash:None,   pre_sh:None
class Block:
    def __init__(self, *args):  # args (blocks)
        self.msglist = []  # 存储所有交易记录
        self.timestamp = None  # 存储多个记录最终锁定的时间
        self.hash = None
        self.pre_hash = None
        if args:
            for arg in args:
                self.add_message(arg)

    def add_message(self, msg):  # 新增交易信息
        # 把消息链接到列表对应位置
        if len(self.msglist) > 0:
            msg.link(self.msglist[-1])
        msg.seal()
        msg.validate()
        self.msglist.append(msg)

    def link(self, block):  # 链接
        self.pre_hash = block.hash

    def seal(self):  # 密封
        self.timestamp = datetime.datetime.now()
        self.hash = self._hash_block()

    def _hash_block(self):
        val = str(self.pre_hash) + str(self.timestamp) + str(
            self.msglist[-1].hash)
        hash_val = val.encode('utf-8')
        return hashlib.sha256(hash_val).hexdigest()

    def validate(self):  # 校验
        if self.hash != self._hash_block():  # 判断消息链
            raise invalidMessage("交易的哈希链被修改" + str(self))

    def __str__(self):
        return "msglist:{},timestamp:{},hash:{},pre_sh:{}".format(
            self.msglist, self.timestamp, self.hash, self.pre_hash)


import message
msg = message.Message("msg-001")
b = Block(msg)
print(b)
