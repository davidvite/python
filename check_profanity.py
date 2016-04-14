import urllib

def read_text():
	quotes = open("/Users/davidvite/Documents/Professional/python/movie_quotes.txt")
	contents_of_file = quotes.read()
	print(contents_of_file)
	quotes.close()
	check_profanity(contents_of_file)

#Note that it just recognizes lower case and not capitalize words.
def check_profanity(text_to_check):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
	ouput = connection.read()
	print(ouput)
	connection.close()
	if "true" in ouput:
		print("Bad Words Alert")
	elif "false" in ouput:
		print("You are a good boy, no bad words")
	else:
		print("Could not scan the document properly")

read_text()


