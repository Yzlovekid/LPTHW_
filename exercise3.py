a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
  if i < 5:
    print i

b = int(raw_input('enter a number'))
new_list = []
for i in a:
  if i < b:
    new_list.append(i)
    
print new_list
