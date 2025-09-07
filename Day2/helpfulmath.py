s = input()
numbers = s.split("+")         # ["3", "2", "1"]
numbers.sort()                 # ["1", "2", "3"]
print("+".join(numbers))       # "1+2+3"
