letters = 'abcdefghijklmnopqrstuvwxyz ,.!?-\n\t'
key = 'zombie'
a = letters
text = '''
'''
for char in key:
  a = a.replace(char, '')
a = key + a
a += a.upper()
b = letters
b += letters.upper()
for char in text:
  print(end=a[b.index(char)])
