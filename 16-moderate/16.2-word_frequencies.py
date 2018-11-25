def word_frequencies(word, book):
	d=dict()
	word=word.lower()
	words=book.split()
	words=list(w.lower() for w in words)
	print(words)
	
	for w in words:
		if w in d:
			d[w]+=1
		else:
			d[w]=1
	print(d)
	if word in d:
		return d[word]
	else:
		return 0
	
if __name__=="__main__":
	print(word_frequencies("am", "I am Adwaith also I am Gupta"))
	
