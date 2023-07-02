python
import re

# Проверка соответствия строки шаблону
pattern = r'^[A-Za-z]+$'
string = 'Hello'
match = re.match(pattern, string)
if match:
    print('Строка соответствует шаблону')
else:
    print('Строка не соответствует шаблону')

# Поиск всех совпадений в строке
pattern = r'\d+'
string = '123 abc 456 def'
matches = re.findall(pattern, string)
print(matches)

# Замена совпадений в строке
pattern = r'\d+'
string = '123 abc 456 def'
replacement = 'X'
new_string = re.sub(pattern, replacement, string)
print(new_string)

# Разделение строки на подстроки по шаблону
pattern = r'\s+'
string = 'Hello   world!'
parts = re.split(pattern, string)
print(parts)
