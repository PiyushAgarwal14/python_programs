from translate import Translator
translator= Translator(to_lang="ja")
try:
    with open('module/test.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        # print(translation)
    with open('module/test-ja.txt', mode='w') as my_file2:
        my_file2.write(translation)
except FileNotFoundError as e:
    print('Check your file path')    