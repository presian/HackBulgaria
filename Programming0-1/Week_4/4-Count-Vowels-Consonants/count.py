def count_vowels_consonants(word):
    vowels_counter = 0
    consonants_counter = 0
    vowels = list("aeiouyAEIOUY")
    for letter in word:
        if letter in vowels:
            vowels_counter += 1
        else:
            consonants_counter += 1
    result = {}
    result["vowels"] = vowels_counter
    result["consonants"] = consonants_counter
    return result
print(count_vowels_consonants("aaaAcccD"))
