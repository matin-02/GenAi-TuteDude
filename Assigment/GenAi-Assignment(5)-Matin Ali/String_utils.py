# Task 2  : Creating a modules String_utils with the capitalize_word, reverse_string and word_count function
# and call it in main.py
def capitalize_word(text):
    return text.title()

def reverse_string(text):
    return text[::-1]

def word_count(text):
    return len(text.split())