# Here I am showing Iterator in python

# Iterator demo
fruits = ("apple", "banana", "cherry")
name = iter(fruits)

print(next(name))
print(next(name))
print(next(name))

# Create an Iterator
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

my_numbers = MyNumbers()
my_iter = iter(my_numbers)

for num in my_iter:
    if num > 10:
        break
    print(num)


# StopIteration in Iterator
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration
    
my_numbers = MyNumbers()
my_iter = iter(my_numbers)

for num in my_iter:
    print(num)