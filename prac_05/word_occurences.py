import operator

text = "this is a collection of words of nice words this is a fun thing it is"
print("Text: {}".format(text))
words = text.split()
words_frequency = {}
for word in words:
    try:
        words_frequency[word] += 1
    except KeyError:
        words_frequency[word] = 1

words = list(words_frequency.keys())

words.sort()

longest_word = max((len(word) for word in words))

for word in words:
    print("{:{}} : {}".format(word, longest_word, words_frequency[word]))