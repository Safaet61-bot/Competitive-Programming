word=input().strip()
upper=0

for i in word:
    if i.isupper():
        upper+=1
if upper>len(word)-upper:
    print(word.upper())
else:
    print(word.lower())