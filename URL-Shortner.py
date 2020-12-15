import pyshorteners

link = input ("Enter: ")
shortener = pyshorteners.Shortener()
x = shortener.tinyurl.short(link)
print(x)
