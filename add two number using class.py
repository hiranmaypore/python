class hello:
    def __init__(self, m, n): #this needs m and n
      self.g = m
      self.h = n

    def hi(self, x, y):
      a = x + self.g
      b = x + self.h #use self to access other class members
      return a, b
  
m = 100
n = 200
obj = hello(m, n) #pass m and n to the constructor
c = obj.hi(10, 11)
print(c)