def deco(func):
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
        res = []
        for i in args:
            if type(i) == str:
                res.append(i.upper())
        for k,v in kwargs.items():
            if type(v) == str:
                res.append(v.upper())
        return res
    return wrapper
@deco
def test(*args,**kwargs): return None
print(test(222, 'aaa', 'bbb', 'ccc', 11, a='abc', b='bcd', c='cde', d=111))

