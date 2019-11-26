import hashlib
import datetime


# 生成一个自定义区块
class custom_chain:
    def __init__(self, index, timestamp, data, pre_hash):
        self.index = index  # 当前块的索引
        self.timestamp = timestamp  # 当前块的生成时间
        self.data = data  # 当前块的交易数据
        self.pre_hash = pre_hash  # 上一个块的hash
        self.self_hash = self.hash_block()  # 当前块的hash

    def hash_block(self):
        sha = hashlib.sha512()  # 加密算法
        data_str = str(self.index) + str(self.timestamp) + str(
            self.data) + str(self.pre_hash)
        sha.update(data_str.encode('utf-8'))
        return sha.hexdigest()


# 创世块
def create_first_block():
    return custom_chain(0, datetime.datetime.now(), 'first_block', '0')


# 别的块
def create_other_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = datetime.datetime.now()
    this_data = 'other block and index=' + str(this_index)
    pre_hash = last_block.self_hash
    return custom_chain(this_index, this_timestamp, this_data, pre_hash)


# test
# 生成一个区块链列表
block_chain_list = [create_first_block()]
currt_block = block_chain_list[0]  # 当前块
# 产生100次交易,每一次生成一个区块
for i in range(100):
    new_block = create_other_block(currt_block)
    block_chain_list.append(new_block)
    currt_block = new_block
    print(currt_block.index, currt_block.timestamp, currt_block.pre_hash,
          currt_block.self_hash, currt_block.data)
