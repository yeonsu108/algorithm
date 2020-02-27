def IsHansu(n):
  if n <= 0:
    return 0
  elif n < 10:
    return 1
  else :
    n = str(n)
    d = int(n[1]) - int(n[0])
    for i in range(len(n)-1):
      if int(n[i+1]) - int(n[i]) != d:
        return 0
    return 1

input_num = int(raw_input())
count = 0
for i in range(input_num):
  if IsHansu(i+1):
    count += 1
print count