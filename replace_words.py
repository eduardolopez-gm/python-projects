def replace_word():
    string = 'Hi, nice to meet you you'
    word_to_replace = input('Enter the word to replace: ')
    word_replacement = input('Enter the word replacement: ')
    print(string.replace(word_to_replace, word_replacement))


replace_word()