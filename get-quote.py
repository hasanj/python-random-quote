import random

def entry_point_method():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()


  last = len(quotes) - 1
  #randint both endpoints are inclusive
  rnd = random.randint(0, last)
  print(quotes[rnd])

if __name__== "__main__":
  entry_point_method()
