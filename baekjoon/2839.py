N = input()
n5 = N/5
for i in range(n5, -1, -1):
  if (N - 5 * i) % 3 == 0:
    print (N - 5*i) / 3 + i
    break
else:
  print -1