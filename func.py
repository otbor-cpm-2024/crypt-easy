# easy_crypt
def easy_crypt(text):
  print(''.join(chr((ord(x) - ord('0') + 10231942) % (ord('}') - ord('0') + 1) + ord('0')) for x in text))
