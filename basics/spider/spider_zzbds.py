import re

string = '''fold,
fish.
silver#
fish?
tytr
'''
# 匹配 fish
result = re.search(r'fish',string)
print(result)

# 匹配 . 
result = re.search(r'\.',string)
print(result)

# 匹配 第一个英文字母 
result = re.search(r'[a-z]',string)
print(result)

# 匹配 第一个英文字母 
result = re.search(r'[0-1]\d\d|2[0-4]\d|25[0-5]',"254")
print(result)

result = re.findall(r'\w{1,9}',string)
print(result)

result = re.findall(r'12.+\.jpg',"12346789dkjshfjsdkdgh.jpggdkjgl")
print(result)

str = '''img src="" attr="36103" data-original="https://imgsa.baidu.com/forum/wh%3D200%2C90%3B/sign=5703a70054b5c9ea62a60be1e5099a39/1a6722600c3387448860be775e0fd9f9d62aa0dc.jpg'''
# result = re.findall(r'img class="j_retract"[.]*src="\.jpg',str)
result = re.findall(r'img src="" .+data-original="(.+\.jpg)',str)
print(result)