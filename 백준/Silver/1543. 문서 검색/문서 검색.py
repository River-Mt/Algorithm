import sys
import re

docs = sys.stdin.readline().rstrip()
word = sys.stdin.readline().rstrip()
wordLen = len(word)
docsLen = len(docs)

match = re.findall(word, docs)

print(len(match))

