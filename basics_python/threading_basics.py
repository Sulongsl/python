# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 下午3:59
# @Author  : Sulong
# @File    : threading_basics.py
# @Software: PyCharm

import os


# 对于操作系统来说，一个任务就是一个进程（Process），比如打开一个浏览器就是启动一个浏览器进程，打开一个记事本就启动了一个记事本进程，打开两个记事本就启动了两个记事本进程，打开一个Word就启动了一个Word进程。
# 有些进程还不止同时干一件事，比如Word，它可以同时进行打字、拼写检查、打印等事情。在一个进程内部，要同时干多件事，就需要同时运行多个“子任务”，我们把进程内的这些“子任务”称为线程（Thread）。


# 由于每个进程 至少要干一件事  故 每个进程必定存在一个线程
#
# 多任务实现:
# 多进程模式；  每个进程对应一个线程  启动多个 进程
# 多线程模式；  每个进程对应多个线程  启动一个进程 即启动多个线程
# 多进程+多线程模式。 每个进程对应多个线程 启动多个进程


# 子进程永远返回0，而 父进程返回子进程的ID
def fork():
	print('Process (%s) start...' % os.getpid())
	pid = os.fork()
	if pid == 0:
		# 子进程只需要调用getppid()就可以拿到父进程的ID
		print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
	else:
		#  我(父进程)刚刚创建了一个子进程
		print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：

from multiprocessing import Pool
import os, time, random
# from threading import

def long_time_task(name):
	# 启动一个进程
	print('Run task %s (%s)...' % (name, os.getpid()))
	start = time.time()
	time.sleep(random.random() * 3)
	end = time.time()
	print('Task %s runs %0.2f seconde' % (name, (end - start)))

import subprocess

# subprocess 模块 可以控制子进程（外部进程，不与父进程绑定）

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup','www.python.org'])
print('Exit code',r)

# if __name__ == '__main__':
	# print('Parent process %s.' % os.getpid())
	# # 定义一个进程池 个数为4
	# p = Pool(4)
	# # 执行 8个进程
	# # 根据输出结果看出 在县城池中只有四个进程位置 谁先执行完毕 则下一个进程 进入该进程执行
	# for i in range(0, 8):
	# 	p.apply_async(long_time_task, args=(i,))
	# print('Waiting for all subprocesses done...')
	# p.close()
	# p.join()
	# print('All subprocesses done.')

