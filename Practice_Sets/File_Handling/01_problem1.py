f = open("poem.txt")

text = f.read()

if "twinkle" in text.lower():
    print("The Poem contains the word \'Twinkle\'")
else:
    print("The Poem doesnot contain the word \'Twinkle\'")

f.close()