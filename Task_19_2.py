class Fibonacci:
    def __init__(self):
        self.a = 1
        self.b = 1
    def __iter__(self):
        return self
    def __next__(self):
        fib = self.a
        self.a, self.b = self.b, self.a + self.b
        return fib

f = Fibonacci()
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
