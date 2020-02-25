n, x = raw_input().split()
n = int(n)
x = int(x)

input_arr = raw_input().split()

a = ""
for i in range(n):
  if(int(input_arr[i]) < x): a += input_arr[i] + " "

print a