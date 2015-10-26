import urllib 

def read_text():
	quotes = open(src, "r")
	contents_file = quotes.read()
	print contents_file
	quotes.close()
	profanity_check(contents_file)

def profanity_check(text_check)
	connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" + text_check)
	output = connection.read()
	print output
	connection.close()

read_text()