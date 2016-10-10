__author__ = 'guojiewei'

import  functools
# def log(func):
#     def wrapper(*args , **kw):
#         # print("call %s():" % func.__name__)
#         print 'call %s():' % func.__name__
#         return func(*args , **kw)
#     return wrapper;
#
# @log
# def now():
#     print("log info------")


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper
@log
def now():
    print '2013-12-25'



# def log2(func,*args, **kw):
#     print func
#     print
#     # print 'func1111 %s():' %func.__name__
#     def wrapper(*args, **kw):
#         print 'call %s():' % func.__name__
#         return func(*args, **kw)
#     return wrapper
# @log2
# def now2(*args, **kw):
#     print args



# def log3(text):
#     print 'log info %s:' %text
#     def decoder(func):
#         print 'call info %s ():' % func.__name__
#         def wrapper(*args, **kw):
#             return func(*args,**kw)
#         return wrapper
#     return decoder
#
# @log3('excute')
# def now3(name):
#     print('hello world %s:' % name)




if __name__ == '__main__':
    f = log(now)
# f= now3('jway')
#     print(now.__name__)
#     print(f)
    f2=now;
    print(f())
    print(f2())

