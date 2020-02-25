n = int(raw_input())

if n<10: n *= 10

new_num = n
count = 0
while True:
  new_num = str(new_num)
  if len(new_num) == 1:
    a = b = int(new_num)
  else :
    a = int(new_num[1])
    b = int(new_num[0])+int(new_num[1])
  if b>=10: b = b%10
  new_num = a*10 + b
  count += 1
  if n == new_num: break

print count