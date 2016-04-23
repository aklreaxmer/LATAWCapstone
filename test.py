import nltk
from nltk.text import Text
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers

id = input("Input gutenberg id to load: ")
text=strip_headers(load_etext(id)).strip()
raw_input("Enter to print text preview...")
print(text[:1000])

text = text.split()
text=Text(text)
def ask():
	test = raw_input("Which analysis to perform ('list' to see list): ")
	if(test == "list"):
		print("concordance, dispersionplot, wordcount, lexicaldiversity, frequency, collocations")
		ask()
	if(test == "concordance"):
		conc = raw_input("word: ")
		text.concordance(conc)
		ask()
	if(test == "dispersionplot"):
		disp = []
		keepasking = True;
		i=0;
		while(keepasking):
			input = raw_input("word " + str(i) + " (blank to stop): ")
			if(len(input) > 0):
				disp.append(input)
			else:
				keepasking = False;
			i = i + 1
		text.dispersion_plot(disp)
		ask()
	if(test == "wordcount"):
		while(True):
			input = raw_input("What word? (Blank if done): ")
			if(len(input) < 1):
				break
			else:
				print(text.count(input))
		ask()

ask()
