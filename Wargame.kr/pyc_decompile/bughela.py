# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.4.3 (default, Nov 28 2017, 16:41:13) 
# [GCC 4.8.4]
# Embedded file name: bughela.py
# Compiled at: 2015-02-09 07:13:20
import time
from sys import exit
from hashlib import sha512

def main():
    print 'import me :D'


def GIVE_ME_FLAG(flag):
    if flag[:43] != 'http://wargame.kr:8080/pyc_decompile/?flag=':
        die()
    flag = flag[43:]
    now = time.localtime(time.time())
    seed = time.strftime('%m/%d/HJEJSH', time.localtime())
    hs = sha512(seed).hexdigest()
    start = now.tm_hour % 3 + 1
    end = start * (now.tm_min % 30 + 10)
    ok = hs[start:end]
    if ok != flag:
        die()
    print 'GOOD!!!'


def die():
    print 'NOPE...'
    exit()


if __name__ == '__main__':
    main()
# okay decompiling bughela.pyc
