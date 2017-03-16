#!/usr/bin/python

import hashlib

with open('stanovy', 'r') as f:
  text = f.read();

toHash = "".join(text.split());
print(toHash)

print(str(len(toHash)) + " charakterov bez medzier a tabulatorov prezeniem cez sha256")

print('hash256 stanov je:')
nasHash = hashlib.sha256(toHash).hexdigest()

with open('hash.txt', 'w') as f:
  f.write(nasHash)

print(nasHash)
