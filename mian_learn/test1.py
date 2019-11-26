import time
import datetime


class MyLearnTest:
    # 封装 三目运算
    def judge(self, bool, a, b):
        return (bool and [a] or [b])[0]

    # 反向遍历
    def reversed_test(self):
        a = [1, 2, 3, 4, 5, 6]
        for v in reversed(a):
            print(v)

    # 输出下标
    def enumerate_test(self):
        for k, v in enumerate(a):
            print("k:{},v:{}".format(k, v))

    # 浅拷贝和深拷贝
    def copy_test(self):
        import copy
        a_copy = [1, 2, 3, 4, ['a', 'b', 'c']]
        b_copy = a_copy  # 地址引用
        c_copy = copy.copy(a_copy)  # 改变地址,但是数组中的对象地址不变
        d_copy = copy.deepcopy(a_copy)  # 改变地址,复制一份属性值
        print(b_copy)
        print(c_copy)
        print(d_copy)

    # 装饰器(给函数添加前后工作内容,例如 说明,时间等)
    def timer(func):
        def calcTime(*args, **kwargs):
            start = time.time()
            func(*args, **kwargs)
            end = time.time()
            print("time consuming :{}".format(end - start))

        return calcTime

    @timer
    def de_test(self):
        sum = 0
        for v in range(100000):
            sum += v
            print("sum: %s" % sum)

    def with_test(self):
        print("开始读取 with_test.txt 文件内容 ...")
        # with 关键字 语句实质是上下文管理
        # 1、文件操作。2、进程线程之间互斥对象。3、支持上下文其他对象
        with open('D:/python_install/workspace/mian_learn/with_test.txt') as f:
            print(f.read())
        print(f.closed)

    def time_test(self):
        current_time = datetime.datetime.now()  # 当前日期
        print(current_time)
        time2 = time.time()  # 时间戳
        print(time2)

    def split_test(self):
        sentence = "this is a sentence .this is a sentence .this is a sentence ."
        # 按单词分割
        split_list = sentence.split()
        for v in split_list:
            print(v)

        # 按"."分割
        split_list = sentence.split(".")
        for v in split_list:
            print(v)

        # 每个单词出现几次
        # Counter({'is': 3, 'a': 3, 'sentence': 3, '.this': 2, 'this': 1, '.': 1})
        from collections import Counter
        counts = Counter(sentence.split())
        print(counts)

    # 检测是否字符串只由数字组成     
    def isdigit_test(self):
        isdigit_str = "1235646"
        # True
        print(isdigit_str.isdigit())

    # 反转字符串
    # u evol i
    def str_reverse_test(self):
        # 方法一
        demo_str = "i love u"
        print(demo_str[::-1])
        # 方法二
        list_str = list(demo_str)
        list_str.reverse()
        print("".join(list_str))
        # 方法三
        print(self.stack_demo(demo_str))   

    def stack_demo(self,demo_str):
        list_stack = list(demo_str)
        result_str = ""
        while len(list_stack)>0:
            result_str += list_stack.pop()
        return result_str
       

my_test = MyLearnTest()
# my_test.de_test()
# my_test.with_test()
# my_test.time_test()
# my_test.split_test()
# my_test.isdigit_test()
my_test.str_reverse_test()