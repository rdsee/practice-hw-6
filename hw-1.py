#1
user_list = [1, 2, 3, 3, 1, 1, 5, 3, 2, 4]
print(f'Stock list: {user_list}')

user_set = set(user_list)
print(f'Set list: {user_set}')
print('\n')

#2
num1 = [2, 3, 1, 1, 4, 5, 6]
num2 = [3, 2, 1, 4, 5, 6, 7, 3, 3, 2, 1, 1, 5]
num1_set = set(num1)
num2_set = set(num2)
print(f'Num set list: {num1_set}')
print(f'Num set list: {num2_set}')

multiset = num1_set.intersection(num2_set)
print(f'Equal nums: {len(multiset)}')
print('\n')

#3
user_count = int(input('Enter number of sentences: '))

sentence_list = []
for i in range(user_count):
    sentence = (input(f'Enter your {i + 1} sentence: ', ))
    stock_words = sentence.lower().split()
    sentence_list.extend(stock_words)

print(f'Sentence list: {sentence_list}')
words = set(sentence_list)
print(f'Sentence set list: {words}')
print(f'Count of unique words: {len(words)}')



