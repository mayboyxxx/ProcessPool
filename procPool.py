# -*- coding:utf-8 -*-
#coding=utf-8


from multiprocessing import Pool
import time

def func(args):
    time.sleep(1)
    print("%s------------->%s" % (args,time.ctime()))


if __name__=="__main__":
    p1 = Pool(2)

    for i in range(10):
        p1.apply_async(func=func,args=(i,))

    p1.close()
   # time.sleep(2)
   # p1.terminate()
    p1.join()
    print("ending")