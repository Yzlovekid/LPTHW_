a = int(raw_input('please enter a number larger than20'))
x = list(range(2,a + 1))
list = []
for elem in x:
  if a % elem == 0:
    list.append(elem)
    
print list