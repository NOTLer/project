import random as r
with open('text.txt', 'r', encoding='utf-8') as f1:
	lines = f1.readlines()
	print(lines[r.randint(0, len(lines) -1 )])