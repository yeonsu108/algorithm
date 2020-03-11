for i in range(input()):
  H, W, N = map(int, raw_input().split())
  w = (N-1) / H + 1
  h = N % H
  if h: print w + h*100
  else: print w + H*100