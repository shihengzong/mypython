# 节点数据更新，节点的网络共识
import hashlib  # 信息安全加密
import json  # json格式
import time  # 时间模块
from urllib.parse import urlparse  # 网络编码解码
from uuid import uuid4  # 生成唯一序列号
import requests  # 网络请求
from flask import Flask, jsonify, request  # flask网络请求
from typing import Any, Dict, List, Optional  # 数据结构


class ZshCoinBlockChain:
    # %初始化%
    def __init__(self):
        self.chain = []  # 区块链管理多个区块（每一个块是一个字典）
        self.current_transactions = []  # 交易列表
        self.new_block(pre_hash="创始块", proof=100)  # 创建创始区块
        self.nodes = set()  # 保存网络中其他节点

    # %创建一个区块，返回一个字典类型（交易数据）%
    def new_block(self, proof: int, pre_hash: Optional[str]) -> Dict[str, Any]:
        block = {
            "index": len(self.chain) + 1,  # 索引
            "timestamp": time.time(),  # 当前时间
            "transactions": self.current_transactions,  # 交易记录
            "proof": proof,  # 工作量证明
            "pre_hash": pre_hash or self.hash(self.chain[-1]),  # 前一个块的hash
        }
        self.current_transactions = []  # 交易记录加入区块链以后就被清空
        self.chain.append(block)  # 区块加入链中
        return block

    # %加密算法%
    @staticmethod
    def hash(block: Dict[str, Any]) -> str:
        block_byte = json.dumps(block, sort_keys=True).encode()
        hash_str = hashlib.sha256(block_byte).hexdigest()  # 十六进制的哈希编码
        return hash_str

    # %生成交易信息，加入到下一个待挖的区块%
    def new_transations(self, sender: str, receiver: str, amount: int) -> int:
        transation = {
            "sender": sender,  # 付款方账户
            "receiver": receiver,  # 收款方账户
            "amount": amount,  # 数量
        }
        self.current_transactions.append(transation)  # 加入到交易列表
        return self.last_block["index"] + 1  # 索引标记交易数量

    # %最后一个区块%
    @property
    def last_block(self) -> Dict[str, Any]:
        return self.chain[-1]

    # %工作量证明（挖矿成功，获取奖励）%
    def proof_of_work(self, last_proof: int) -> int:
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof = proof + 1
        return proof

    # %工作证明校验(！！挖矿！！)%
    @staticmethod
    def valid_proof(last_proof: int, proof: int) -> bool:
        guess = f'{last_proof*proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[-4:] == "1234"

    # %区块链校验%
    def valid_chain(self, chain: List[Dict[str, Any]]) -> bool:
        # 从创始块开始校验  （创世：1   1：2   2：3）
        last_block = chain[0]
        current_index = 1
        while current_index < len(chain):
            block = chain[current_index]  # 第一个区块
            # (校验hash)判断第一个区块的pre_hash和创始块的hash 是否相等
            if block["pre_hash"] != self.hash(last_block):
                return False
            # 工作量校验
            if not self.valid_proof(last_block["proof"], block["proof"]):
                return False
            last_block = block
            current_index = current_index + 1
        return True

    # %加入其他节点，用于更新%
    def regist_node(self, addr: str):  # 加入其他网络节点,用于更新
        now_url = urlparse(addr)
        self.nodes.add(now_url.netloc)  #增加网络节点

    # %共识算法%
    def resolve_conflicts(self):
        # 网络中多个节点,取出最长的(最长代表交易数最多,也就是最新的)
        all_node = self.nodes  # 取出所有节点
        new_chain = None
        max_len = len(self.chain)
        for node in all_node:
            res = requests.get(f"http://{node}/chain")
            if res.status_code == 200:
                length = res.json()["length"]  # 取出长度
                chain = res.json()["chain"]  # 取出区块链
                if length > max_len and self.valid_chain(chain):
                    max_len = length
                    new_chain = chain
        if new_chain:
            self.chain = new_chain
            return True
        return False


if __name__ == "__main__":
    app = Flask(__name__)  # 初始化flask框架

    @app.route("/")
    def zsh_page():
        return "welcome to zsh_coin !"

    zsh_coin = ZshCoinBlockChain()  # 创建一个网络节点
    node_id = str(uuid4()).replace("-", "")  # 产生密钥
    print("当前钱包地址是:", node_id)

    @app.route("/chain")
    def zsh_chain():
        res = {
            "chain": zsh_coin.chain,
            "length": len(zsh_coin.chain),
        }
        return jsonify(res), 200

    @app.route("/mine")
    def zsh_mine():
        zsh_coin.new_transations(sender="0", receiver=node_id, amount=10)
        last_block = zsh_coin.last_block
        last_proof = last_block["proof"]
        proof = zsh_coin.proof_of_work(last_proof)

        block = zsh_coin.new_block(proof, None)  # 增加一个区块
        res = {
            "message": "新的区块创建",
            "index": block["index"],
            "transactions": block["transactions"],
            "proof": block["proof"],
            "pre_hash": block["pre_hash"],
        }
        return jsonify(res, 200)

    @app.route("/new_transactions", methods=["POST"])  # 创建一个交易
    def new_transactions():
        req = request.get_json()  # 获取请求的json数据
        required = ["sender", "receiver", "amount"]
        if not all(key in req for key in required):
            return "数据不完整", 400
        index = zsh_coin.new_transations(req["sender"], req["receiver"],
                                         req["amount"])
        res = {"message": f"交易加入到区块{index}"}
        return jsonify(res, 200)

    @app.route("/new_node", methods=["POST"])  # 注册节点
    def new_node():
        req = request.get_json()  # 获取请求的json数据
        req_nodes = req.get("nodes")  # 解析json
        if req_nodes is None:
            return "参数有误!", 400
        for node in req_nodes:
            zsh_coin.regist_node(node)
        res = {"message": "新增网络节点成功", "node": list(zsh_coin.nodes)}
        return jsonify(res, 200)

    @app.route("/refresh_node", methods=["POST"])  # 共识算法刷新确保数据一致性
    def refresh_node():
        replace = zsh_coin.resolve_conflicts()
        if replace:
            res = {"message": "刷新成最新数据", "current-chain": zsh_coin.chain}
        else:
            res = {"message": "当前已是最新", "current-chain": zsh_coin.chain}
        return jsonify(res, 200)

    app.run("127.0.0.1", port=50001)
