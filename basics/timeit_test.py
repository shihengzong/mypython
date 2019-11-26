import timeit 

print(timeit.timeit(stmt= 'list(i**2 for i in normal_list)',setup = 'normal_list=range(10000)',number=10))
#0.3437936799875755
print(timeit.repeat(stmt= 'list(i**2 for i in normal_list)', setup='normal_list=range(10000)',repeat=2,number=10))
#[0.33649995761778984, 0.3394490767789293]
#setup 为复合语句
print(timeit.timeit(stmt= 'list(i**2 for i in normal_list)',setup = 'a=10000;normal_list=range(a)',number=10))
#0.33272367424748817
print(timeit.repeat(stmt= 'list(i**2 for i in normal_list)', setup='a=10000;normal_list=range(a)',repeat=2,number=10))
#[0.3323106610316342, 0.3356380911962764]

def func():
    normal_list=range(10000)
    L = [i**2 for i in normal_list]

#stmt为函数
print(timeit.timeit("func()", setup="from __main__ import func",number=10))
#0.12436874684622312
print(timeit.repeat("func()", setup="from __main__ import func",repeat=2,number=10))
#[0.12142133435126468, 0.12079555675148601]

# placekitten.com