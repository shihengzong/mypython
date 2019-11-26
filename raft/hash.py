# 哈希
import hashlib

my_hash = hashlib.sha256()
# 123456 的 哈希码
my_hash.update("123456".encode("utf-8"))
result = my_hash.hexdigest()
print(result)