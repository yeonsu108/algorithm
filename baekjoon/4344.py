c = int(raw_input())

for i in range(c):
  input_arr = raw_input().split()
  total = 0
  for j in range(int(input_arr[0])):
    total += int(input_arr[j+1])
  avg = total / float(input_arr[0])
  count = 0
  for j in range(int(input_arr[0])):
    if int(input_arr[j+1]) > avg :
      count += 1
  print "%.3f%%" %(count / float(input_arr[0]) * 100)