def count_words(words):
    result = {}
    counter = 0
    for i in range(0, len(words)):
        for j in range(0, len(words)):
            if (words[i] == words[j]) and (words[i] not in result.values()):
                counter += 1
        result[words[i]] = counter
        counter = 0
    return result
print(count_words(["words", "are", "meaningful", "words", "words", "are"]))
