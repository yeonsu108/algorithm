def IsGroupWord(word):
  word = str(word)
  for i in word:
    word = word.lstrip(i)
    if word.find(i) > 0:
      return False
  return True

count = 0
for i in range(int(raw_input())):
  if IsGroupWord(raw_input()):
    count += 1
print count