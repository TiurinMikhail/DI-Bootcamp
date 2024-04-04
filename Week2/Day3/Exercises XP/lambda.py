numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_numbers = sorted(numbers, key=lambda x: (x% 2 == 0,x))
print(sorted_numbers)

words = ['applea', 'pearaa', 'banana', 'cherrya']
sorted_words = sorted(words, key=lambda word: (len(word), word.count('a')))
print(sorted_words)

