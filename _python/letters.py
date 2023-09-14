from re import sub

# defs
def increase_letter(pattern, letter):
	out = sub(f'[^{letter}]*{letter}', '', pattern)
	if len(out):
		return out[0]
	else:
		return None

def increase_word(pattern, word):
	word = [l for l in word]
	for letter in range(len(word)-1, -1, -1):
		word[letter] = increase_letter(pattern, word[letter])
		if word[letter] is None:
			word[letter] = pattern[0]
		else:
			return ''.join(word)
	return None

def checker(word):
	mx = 0
	cur = 1
	prev = ''
	for l in word:
		if prev == l:
			cur += 1
		else:
			cur = 1
			prev = l
		if cur>mx:
			mx = cur
	return mx

def own_process(data):
	if checker(data) < 3:
		print(data)


# code
inp = 'abcdefx'

for length in range(2,6):
	word = ''.join([inp[0] for n in range(length)])
	end_word = ''.join([inp[-1] for n in range(length)])

	while word != end_word:
		own_process(word)
		word = increase_word(inp, word)
	own_process(word)
