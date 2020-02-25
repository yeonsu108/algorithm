a = raw_input().split()
for x in range(len(a)):
  a[x] = int(a[x])

a.sort()
print a[len(a)/2]