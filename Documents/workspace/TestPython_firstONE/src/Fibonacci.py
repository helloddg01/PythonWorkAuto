#!/user/bin/env python
# -*- coding: utf-8 -*-

import time
#from StdSuites.AppleScript_Suite import result

def fbis(num):
    result=[0,1]
    for i in range(num-2):
        result.append(result[-2]+result[-1])
    return result

def main():
    result=fbis(10)
    fobj=open('/Users/ddg01/Documents/workspace/TestPython_firstONE/src/result.txt','w+')
    for i,num in enumerate(result):
        print u"第 %d个数是： %d" % (i, num)
        fobj.write("%d" %num)
        time.sleep(1)
if __name__=='__main__':
    main()
    
    