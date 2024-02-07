def flames():
  Name1 = input('Enter the first name: ')
  Name2 = input('Enter the second name: ')
  N1 = [*Name1]
  N2 = [*Name2]
  for i in N1:
    if i in N2:
      N1.remove(i)
      N2.remove(i)
  num_chars = len(N1) + len(N2)
  flames = ["Friends", "Lovers", "Affectionate", "Marriage", "Enemies", "Sister"]
  j = num_chars % len(flames)
  while len(flames) > 1:
    flames.pop(j)
    j = (j + num_chars) % len(flames)
  return flames[0]
print(flames())

