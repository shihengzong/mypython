import threading
import time

def say_hello(i):
	print("这是第{}个线程".format(i))

def timer(func):
	def custom_func(*args,**kwargs):
		start = time.time()
		func(*args,**kwargs)
		end = time.time()
		print("cost time :{}".format(end-start))
	return custom_func

@timer
def threading_test():
	for i in range(100000):
		threading.Thread(target=say_hello(i)).start()

threading_test()