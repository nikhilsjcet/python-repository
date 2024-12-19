words="apple,banana,apple,orange,banana,apple"
s=words.split(",")
word_count={}

for word in s:
    word_count[word]= word_count.get(word,0) + 1
print(word_count)