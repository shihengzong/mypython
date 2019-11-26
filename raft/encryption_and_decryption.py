# 加密 和 解密

# 对称加密
# 类似于      1+1=2   2-1=1

import base64
import pyDes

Des_KEY = "thisakey"  # 设置加密salt,必须是长度为8
Des_PASSWORD = "12345678"  # 加密密码,必须是长度为8
data = '123456'


def DESEncrypt(value, key) -> str:
    des_key = pyDes.des(key,
                        pyDes.CBC,
                        Des_PASSWORD,
                        pad=None,
                        padmode=pyDes.PAD_PKCS5)

    des_result = des_key.encrypt(data)
    res = base64.b64encode(des_result).decode("utf-8")
    return res


def DESDecrypt(value, key) -> str:
    des_key = pyDes.des(key,
                        pyDes.CBC,
                        Des_PASSWORD,
                        pad=None,
                        padmode=pyDes.PAD_PKCS5)
    # 将str转成base64
    input = base64.b64decode(value)
    res = des_key.decrypt(input).decode("utf-8")
    return res


des_pwd = DESEncrypt(data, Des_KEY)
print(des_pwd)

my_pwd = DESDecrypt(des_pwd, Des_KEY)
print(my_pwd)

# 非对称加密
# 129 * 13 = 1677
# 1677 % 1000 = 677
# 677 * 77 = 52129
# 52129 % 1000 = 129
# summary: = 129 * 13 * 77 % 1000 % 1000

# ps: 取模和乘除的优先级相同 (13相当于公钥,77相当于私钥)
# 13 * 77 = 1001
# 1 % 1000 = 1001 % 1000 = 1
# a * (1 % 1000) = a * 1001 % 1000
# a = a * 13 * 77 % 1000

import rsa  # 非对称加密解密
import chardet
public_key, private_key = rsa.newkeys(1024)
print(public_key)
print(private_key)

msg = "this is a message"
crypt_res = rsa.encrypt(msg.encode("utf-8"), public_key)  # 获取公钥,并使用公钥加密
print("加密后", chardet.detect(crypt_res))
decrypt_res = rsa.decrypt(crypt_res, private_key).decode("utf-8")  # 使用私钥解密
print("解密后:", decrypt_res)
