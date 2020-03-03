# a = [0,1,2,4]

def MinCount(n):
  if n == 1: return 1
  a = [0, 1, 2]
  count = 2
  while a[2] < n:
    count += 1
    a.append( a[2] + (a[2]-a[0])/2 + 1 )
    a = a[1:]
  #  print a
  return count
    
  # i = 0
  # global a
  # for i in range(len(a)):
  #   if a[i] > n:
  #     return i
  # while a[i] < n:
  #   a.append(a[i]+1+(a[i]-a[i-1])/2)
  #   i += 1
  # return i

for i in range(input()):
  start, end = raw_input().split()
  print MinCount(int(end)-int(start))