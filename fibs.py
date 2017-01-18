class fibs:
    def __init__(self,n=10000,num=10):
        self.a = 0
        self.b = 1
        self.n = n
        self.num = num
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
	#if(self.a > self.n):
	 #   raise StopIteration
        if(self.count == self.num):
            raise StopIteration
        self.count += 1
        return self.a
f = fibs(num=12)
for each in f:
    print(f.a)
