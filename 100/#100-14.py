#!/usr/bin/python3
#encoding:utf-8

# 题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
#
# 程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
# (1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
# (2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
# (3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。


import math
#关于如何跳出循环重2开始的哪一点没有弄明白
#使用while控制是否继续检测输入数字，在其中使用for控制对每个因子的检测
#引入y作为对输入的n是否继续检测做判断

# def reduceNum(n):
#     print '{} = '.format(n),
#     if not isinstance(n, int) or n <= 0 :
#         print '请输入一个正确的数字 !'
#         exit(0)
#     elif n in [1] :
#         print '{}'.format(n)
#     while n not in [1] : # 循环保证递归
#         for index in xrange(2, n + 1) :
# 			#xrange这个迭代器每次都是从头开始迭代，不像range继续迭代
#           #在python3中xrange就是range
#             if n % index == 0:
#                 n /= index # n 等于 n/index
#                 if n == 1:
#                     print index
#                 else : # index 一定是素数
#                     print '{} *'.format(index),
#                 break


n=int(input("num"))
m=n
if n<0:
		print("wrong number")
elif n in[1]:
		print (n)
y=1
#引入y作为对输入的n是否继续检测做判断
while(y):
    for i in range(2,int(math.sqrt(n)+1)):
    # for i in range(2, n + 1):
     if  n % i == 0:
        n=int(n/i);
        print(i)
        print(" ")
        break
    else :
        y=0
        if m==n:
            print("sushu")
        else:
            print(n)
