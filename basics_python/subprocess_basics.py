# -*- coding: utf-8 -*-
# @Time    : 2018/4/18 下午4:38
# @Author  : Sulong
# @File    : subprocess_basics.py

# http://www.jb51.net/article/133941.htm
# https://blog.csdn.net/songfreeman/article/details/50735045
# https://www.cnblogs.com/breezey/p/6673901.html

# @Software: PyCharm

import subprocess
# print(help(subprocess))
'''
# 创建一个新的进程让其执行另外的程序，并与它进行通信，获取标准的输入、标准输出、标准错误以及返回码等
# 创建附加进程
subprocess通过子进程来执行外部指令，并通过input/output/error管道，获取子进程的执行的返回信息
'''

# 1.call
# 执行命令 返回状态吗  shell = True  允许shell 命令式是字符串形式
# 执行一个外部命令，但该方法不能返回执行的结果，只能返回执行的状态码： 成功（0） 或 错误（非0）
print(subprocess.call(['ls','-1']))
print(subprocess.call("ls -l",shell=True))
print(subprocess.call("pwd"))
a = subprocess.call("pwd")
print(a)  # 只是输出 0

# 2. check_call()
# 通过check_call  检测命令的执行结果  如果不成功则返回异常
try:
	subprocess.check_call('lsst -t',shell=True)
except subprocess.CalledProcessError as err:
	print('Command Error')
finally:
	print('kill')

print('************************************************')
# 3.subprocess.check_output() 方法
output=subprocess.check_output("ls -l",shell=True)
print(output.decode('utf-8'))

print('************************************************')


# 4. Popen 类

# 主要参数说明：
# args：args should be a string, or a sequence of program arguments.也就是说必须是一个字符串或者序列类型（如：字符串、list、元组），用于指定进程的可执行文件及其参数。如果是一个序列类型参数，则序列的第一个元素通常都必须是一个可执行文件的路径。当然也可以使用executeable参数来指定可执行文件的路径。
# stdin,stdout,stderr：分别表示程序的标准输入、标准输出、标准错误。有效的值可以是PIPE，存在的文件描述符，存在的文件对象或None，如果为None需从父进程继承过来，stdout可以是PIPE，表示对子进程创建一个管道，stderr可以是STDOUT，表示标准错误数据应该从应用程序中捕获并作为标准输出流stdout的文件句柄。
# shell：如果这个参数被设置为True，程序将通过shell来执行。
# env：它描述的是子进程的环境变量。如果为None，子进程的环境变量将从父进程继承而来。

# 4.1 与进程的单向通信
print(subprocess.Popen("ls -1",shell=True))
# 通过Popen()方法调用命令后执行的结果,可以设置stdout值为PIPE，再调用communicate()获取结果
proc = subprocess.Popen(['echo','"Stdout"'],stdout=subprocess.PIPE)

# communicate返回标准输出或标准出错信息
stdout_value = proc.communicate()
print(stdout_value)

ls = subprocess.Popen(['ls','-1'],stdout=subprocess.PIPE)
ls_value = ls.communicate()
print(ls_value)

# 返回结果为byte类型
print(ls_value[0])

# 4.2 与进程双向通信 双进程
int_va = subprocess.Popen('cat',shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
hello_world = 'hello world'.encode('utf-8')
#  写入到管道
int_va.stdin.write(hello_world)
value = int_va.communicate()
print(value)

procs = subprocess.Popen(['python3'],stdin=subprocess.PIPE,stdout=subprocess.PIPE, stderr=subprocess.PIPE,)
procs.stdin.write('print("helloworld")'.encode('utf-8'))
out_value,err_value = procs.communicate()
# Popen.communicate()方法用于和子进程交互：发送数据到stdin，并从stdout和stderr读数据，直到收到EOF。等待子进程结束。
print(out_value)
print(err_value)


