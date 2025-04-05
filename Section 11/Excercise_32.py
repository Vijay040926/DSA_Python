def count_word_frequency(sentence):
    word_count={}
    words=sentence.split()
    for word in words:
        word = word.lower().strip('.,!?;:')
        word_count[word]=word_count.get(word,0)+1
    return word_count
sentence="Hello World Hello"
res=count_word_frequency(sentence)
print(res)