for _ in range(input()):
  x1, y1, r1, x2, y2, r2 = map(int, raw_input().split())
  l = ((x2-x1) ** 2 + (y2-y1) ** 2) ** 0.5

  if l < r1 or l < r2:
    d = abs(r1-r2)
  else: d = 2 * l - r1 - r2
  if x1==x2 and y1==y2 and r1==r2: print "-1"
  elif d < l : print "2"
  elif d == l: print "1"
  elif d > l: print "0"