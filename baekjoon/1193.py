X = input()
sum = int((2 * (X-1) + 0.25) ** 0.5 + 1.5)
a = X - (sum-2) * (sum-1) / 2
if sum % 2 == 1:
  print str(a) + "/" + str(sum-a)
else:
  print str(sum-a) + "/" + str(a)