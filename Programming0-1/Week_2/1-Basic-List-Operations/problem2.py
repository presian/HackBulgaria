languages = ['Python', 'Ruby']
languages.append('C++')
languages.append('Java')
languages.append('C#')
languages.insert(0, 'Haskell')
languages.append('Go')
print(languages[0])
print(languages[1])
print(languages[4])
index = languages.index('C#')
languages[index] = 'F#'
print(languages)
print(languages[len(languages)-1])

print('Is Haskell in the list: ' + str('Haskell' in languages))
print('Is Ruby in the list: ' + str('Ruby' in languages))
print('Is Go in the list: ' + str('Go' in languages))
print('Is Rust in the list: ' + str('Rust' in languages))