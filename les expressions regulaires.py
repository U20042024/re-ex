import re

# Exercice 1
def search_word_in_string(word, text):
    return bool(re.search(fr'\b{re.escape(word)}\b', text))

# Exercice 2
def contains_digits(s):
    return bool(re.search(r'\d', s))

# Exercice 3
def replace_spaces_with_dashes(s):
    return re.sub(r'\s', '-', s)

# Exercice 4
def is_valid_phone_number(phone_number):
    return bool(re.match(r'\d{2}-\d{3}-\d{4}', phone_number))

# Exercice 5
def is_valid_email(email):
    return bool(re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email))

# Example usage:
word_result = search_word_in_string('apple', 'I have an apple.')
print(word_result)

digit_result = contains_digits('Hello123')
print(digit_result)

space_result = replace_spaces_with_dashes('Replace spaces with dashes')
print(space_result)

phone_result = is_valid_phone_number('12-345-6789')
print(phone_result)

email_result = is_valid_email('example@email.com')
print(email_result)