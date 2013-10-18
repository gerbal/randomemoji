from bs4 import BeautifulSoup


soup = BeautifulSoup(open("emoji-cheet-sheet.html"))
emojilist = []

for emoji in soup.find_all('span'):
	print emoji.string
	emojilist += [str(emoji.string)]
print emojilist

output = open("output",'w')
output.write(str(emojilist))
output.close
#print emojilist