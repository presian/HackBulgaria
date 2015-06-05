def hash_them(keys, values):
    result = {}
    for i in range(0, len(keys)):
        if i < len(values):
            result[keys[i]] = values[i]
        else:
            result[keys[i]] = None
    return result

print(hash_them(["Ivan", "Maria"], [1, 2]))
print(hash_them(["Ivan", "Maria"], [1]))
