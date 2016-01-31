##functional stuff in python.

#_apply (func:function,LOI:List) -> List
def _apply(func,LOI):
    return [func(item) for item in LOI]


def _apply_example():
    print(_apply(lambda x: 2*x**3,[1,2,3,4,5]))


#times (x:number) -> function
def times(x):
    return lambda y: x*y

def times_example():
    times2 = times(2)
    print(_apply(times2,[2,4,6,8,0]))
    times5 = times(5)
    print(_apply(times5,[1,3,5,7,9]))


#compose (f:function,g:function) -> function
def compose(f,g):
    return lambda x: f(g(x))

def compose_example():
    times3 = times(3)
    times4 = times(4)
    times12 = compose(times3,times4)
    print(_apply(times12,[0,1,2,3,4,5,6,7,8,9]))


#making a list with a clear function.
class MyList:
    def __init__(self):
        self. l = []
    def get(self):
        return self.l
    def clear(self):
        self.l = []
    def add(self,i):
        self.l.append(i)


#curry (func:function,midret: Any) -> function
#this function violates state immutability
#but does do the job of currying only using one object.
def curry(func,midret = None):
    args = MyList()
    if(func.func_code.co_argcount == 0):
        return func
    def app(x):
        args.add(x)
        try:
            r = func(*args.get())
            args.clear()
            return r
        except TypeError:
            return midret
    return app



def curry_example():
    @curry
    def add(x,y,z):
        return x + y + z

    print(add(1))
    print(add(2))
    print(add(3))


##curry with immutable data
def cons(item,tupp):
    return tuple([item]) + tupp

def CURRY(func,args = ()):
    if(func.func_code.co_argcount == 0):
        return func
    def app(x):
        try:
            return func(*cons(x,args))
        except TypeError:
            return CURRY(func,cons(x,args))

    return app


def CURRY_example():
    @CURRY
    def mult(a,b,c,d):
        return a * b * c * d

    m1 = mult(1)
    print(m1)
    m2 = m1(2)
    print(m2)
    m3 = m2(3)
    print(m3)
    m4 = m3(4)
    print(m4)

    print(mult(2)(3)(4)(5))
