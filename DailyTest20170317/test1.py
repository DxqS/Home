# coding:utf-8
'''
Created on 2017/3/17.

@author: chk01
'''


# items = [1, 2, 3, 4]
# it = iter(items)
# print it.next()
# print it.next()


class Letters(object):
    def __init__(self):
        self.current = 'a'

    def next(self):
        if self.current > 'z':
            raise StopIteration
        result = self.current
        self.current = chr(ord(result) + 1)
        return result

    def __iter__(self):
        return self


letter = Letters()
for i in letter:
    print i
