# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 下午3:59
# @Author  : Sulong
# @File    : threading_basics.py
# @Software: PyCharm

from multiprocessing import Pool,Lock
import os, time, random
from multiprocessing import Process
import multiprocessing
import time



# 对于操作系统来说，一个任务就是一个进程（Process），比如打开一个浏览器就是启动一个浏览器进程，打开一个记事本就启动了一个记事本进程，打开两个记事本就启动了两个记事本进程，打开一个Word就启动了一个Word进程。
# 有些进程还不止同时干一件事，比如Word，它可以同时进行打字、拼写检查、打印等事情。在一个进程内部，要同时干多件事，就需要同时运行多个“子任务”，我们把进程内的这些“子任务”称为线程（Thread）。


# 由于每个进程 至少要干一件事  故 每个进程必定存在一个线程
#
# 多任务实现:
# 多进程模式；  每个进程对应一个线程  启动多个 进程
# 多线程模式；  每个进程对应多个线程  启动一个进程 即启动多个线程
# 多进程+多线程模式。 每个进程对应多个线程 启动多个进程

'''1.进程与多进程'''


# 子进程永远返回0，而 父进程返回子进程的ID
# 识别子进程与父进程
def fork():
	print('Process (%s) start...' % os.getpid())
	pid = os.fork()
	if pid == 0:
		# 子进程只需要调用getppid()就可以拿到父进程的ID
		print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
	else:
		#  我(父进程)刚刚创建了一个子进程
		print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

'''**进程的创建用multiprocessing模块'''
def run_proc(name):
	# 输出传入姓名并打印当前进程号
	print('Run child process %s (%s)'%(name,os.getpid()))


# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：

def long_time_task(name):
	# 启动一个进程
	print('Run task %s (%s)...' % (name, os.getpid()))
	start = time.time()
	# 睡随机时间
	time.sleep(random.random() * 3)
	end = time.time()
	print('Task %s runs %0.2f seconde' % (name, (end - start)))


# subprocess 模块 可以控制子进程（外部进程，不与父进程绑定）
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup','www.python.org'])
# print('Exit code',r)



'''2.线程与多线程'''


# isAlive(): 返回线程是否活动的。
# getName(): 返回线程名。
# setName(): 设置线程名。


#  threading模块
def sleep_3():
	time.sleep(3)


def sleep_5():
	time.sleep(5)


def hello_world():
	for i in range(100):
		print('hello world')


def hello_say(str_1, str_2):
	for i in range(10):
		print(str_1, str_2)


def booth(tid):
	global i
	# 默认互斥锁是 open状态
	global lock
	while True:
		# 获取锁 并锁定该锁
		lock.acquire()
		if i != 0:
			i = i - 1
			print("窗口:", tid, ",剩余票数:", i)
			time.sleep(1)
		else:
			print("Thread_id", tid, "No more tickets")
			os._exit(0)
		# 线程执行完毕 互斥锁 释放
		lock.release()
		time.sleep(1)


def worker(interval):
	n = 5
	while n > 0:
		print("The time is {0}".format(time.ctime()))
		time.sleep(interval)
		n -= 1

def task1(msg):
	print('task1:hello,%s' %(msg))
	time.sleep(1)


def task2(msg):
	print('task2:hello,%s' %(msg))
	time.sleep(1)


def task3(msg):
	print('task3:hello,%s' %(msg))
	time.sleep(1)

# 多进程共享资源lock
def  task4(lock,f):
	with lock:
		f = open(f,'w+')
		f.write('hello')
		time.sleep(1)
		f.close()

def task5(lock,f):
	lock.acquire()
	try:
		f = open(f,'a+')
		time.sleep(1)
		f.write('world!')
	except Exception as e :
		print(e)
	finally:
		f.close()
		lock.release()

def task_6(n):
	return n**2
# 杨辉三角
def triangles():
	a =[1]
	while True:
		yield a
		a = a=[sum(i) for i in zip([0] + a,a + [0])]
		# a.append(0)
		# a =[a[i-1] + a[i] for i in range(len(a))]





if __name__ == '__main__':
	g = triangles()
	for n in range(10):
		print(next(g))


	p1 = Process(target=task1, args=('one',))
	p2 = Process(target=task2, args=('two',))
	p3 = Process(target=task3, args=('three',))
	start = time.time()

	p1.start()
	p2.start()
	p3.start()

	print("The number of CPU is:" + str(multiprocessing.cpu_count()))
	for p in multiprocessing.active_children():
		print("child p.name: " + p.name + "\tp.id: " + str(p.pid))

	p1.join()
	p2.join()
	p3.join()

	end = time.time()
	print('3 processes take %s seconds' % (end - start))

	print('*****' * 10)
	# 创建run_proc(sulong) 进程
	a = multiprocessing.Process(target=run_proc,args=('sulong',))
	a.start()
	print('p.pid',a.pid)
	print('p.name',a.name)
	print('p.is_alive',a.is_alive())
	print('p.terminate', a.terminate())
	print('*****'*10)
	# # 创建worker(3) 进程
	# p = multiprocessing.Process(target=worker, args=(3,))
	# p.start()
	# print('p.pid',p.pid)
	# print('p.name',p.name)
	# print('p.is_alive',p.is_alive())

	print('Parent process2 %s.' % os.getpid())
	# 创建进程run_proc,传参
	p = Process(target=run_proc, args=('test',))
	print('Child process will start.')
	p.start()
	p.join()
	print('Child process end.')
	print('Parent process3 %s.' % os.getpid())

# fork()
	'''进程池'''
	print('*****'*10)
	print('Parent process %s.' % os.getpid())
	# 定义一个进程池 个数为4
	p = Pool(18)
	# 执行 8个进程
	# 根据输出结果看出 在县城池中只有四个进程位置 谁先执行完毕 则下一个进程 进入该进程执行
	for i in range(0, 18):
		p.apply_async(long_time_task, args=(i,))
	print('Waiting for all subprocesses done...')
	p.close()
	p.join()
	print('All subprocesses done.')
	print('******'*10)

	'''进程池中get用法 回调函数'''
	# pool_6 = multiprocessing.Pool
	# res_1 = []
	#
	# for i in range(6):
	# 	res_6 = pool_6.apply_async(task_6,args=(i,))
	# 	res_1.append(res_6)
	# print("进程池当中创建的对象列表是")
	# for r in res_1:
	# 	print(r)
	# print(len(res_1))
	#
	# print("进程当中任务的返回结果")
	# for r in res_1:
	# 	print(r.get())
	#
	# print('*********'*8)

	lock  =Lock()
	fn = './file.txt'

	start_time4 = time.time()
	p1 = multiprocessing.Process(target=task4,args=(lock,fn,))
	p2 = multiprocessing.Process(target=task5,args=(lock,fn,))

	p1.start()
	p2.start()
	p1.join()
	p2.join()

	end_time4=time.time()
	print('time cost :%s seconds' %(end_time4-start_time4))

	with open(fn,'r') as f :
		for x in f.readlines():
			print(x)



	# '''利用多线程改造'''
	# start_time_1 = time.time()
	# print('threading start sleep 3')
	# thread_1 = threading.Thread(target=sleep_3) # 实例化一个线程对象
	# thread_1.start()  # 使线程执行这个函数
	# print('threading start sleep 5')
	# thread_2 = threading.Thread(target=sleep_5)
	# thread_2.start()
	# thread_1.join()
	# thread_2.join()
	# end_time_1 = time.time()
	# print(str(end_time_1 - start_time_1) + ' s')
	# # start_time = time.time()
	# print('start sleep 3')
	# sleep_3()
	# print('start sleep 5')
	# sleep_5()
	# end_time = time.time()
	# print(str(end_time - start_time) + ' s')
	# i = 19
	# # 创建锁
	# lock = threading.Lock()
	# for k in range(1, 10):
	# 	# 这里参数传递的是一个元组 单数字元素元组定义加 逗号
	# 	new_thread = threading.Thread(target=booth, args=(k,))
	# 	new_thread.start()

	# 线程传参
	# hello_say = threading.Thread(target=hello_say,
	# 							 args=('hello', 'world'))  # args 后面跟的是一个元组，如果没有参数可以不写，如果有参数就直接在元组里按顺序添加就行了
	# hello_say.start()
	# hello_say.join()


	# 守护线程表示为 '不重要' 即 在进程退出的时候，不用等待这个线程退出 默认线程为非守护线程
# hello = threading.Thread(target=hello_world)
# hello.daemon = True # 设置为守护线程
# hello.start()
# hello.join()







