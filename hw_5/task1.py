# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = ''
text_list = input().split()
for i in range (len(text_list)):
    if 'абв' not in text_list[i]:
        text += text_list[i] + ' '
print(text)