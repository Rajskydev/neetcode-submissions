from typing import List

def count_unique_words(words: List[str]) -> int:
    not_unique_count = len(words) - len(set(words))
    unique_count = len(words) - not_unique_count
    return unique_count


# do not modify code below this line
print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))
