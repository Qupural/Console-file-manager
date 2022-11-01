import time
def decor(f):
    def newdef(*args, **kwargs):
        start = time.time()
        print ('_/\_'*9)
        result = f(*args, **kwargs)
        end = time.time()
        print ('#'*50, '\nВремя выполнения:{} секунд\n'.format(end- start),'#'*50)
        print('_/\_'*9 )

        return result
    return newdef
