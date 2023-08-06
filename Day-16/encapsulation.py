# Here I am showing Encapsulation in python 

class Students:
   def __init__(self, name, rank, numbers):
      self.name = name
      self.rank = rank
      self.numbers = numbers

   def info(self):
      print("I am "+self.name +","+ " I got a", self.rank)

st1 = Students("Asif", "A+", 100)
st2 = Students("Babul", "A", 70)
st3 = Students("Cabbit", "A-", 60)
st4 = Students("Dia", "B", 50)


st1.info()
st2.info()
st3.info()
st4.info()