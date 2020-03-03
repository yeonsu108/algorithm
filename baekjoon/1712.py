fCost, vCost, price = map(int, raw_input().split())
if vCost >= price: print "-1"
else: print fCost / (price - vCost) + 1