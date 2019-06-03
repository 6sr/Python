# Reverse each word of a Sentence individually

def reverseWordSentence(Sentence):
	words = Sentence.split(" ")
	newWords = [word[::-1] for word in words]
	newSentence = " ".join(newWords)
	return newSentence

while True:
	print(reverseWordSentence(str(input()))
	response = input("Do you want to exit (Y/N) : ")
	if response == 'n' or response == 'N':
		break

