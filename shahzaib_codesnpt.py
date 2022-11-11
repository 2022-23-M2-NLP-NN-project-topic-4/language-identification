#characters for each language

print("Character Counts in each Language")
characters = {}
for l in lang:
    languageCharacter = set()
    #get corpus filtered by language
    corpus = data_trim[data_trim.language==l]['Text']
    for i in corpus:
        languageCharacter.update(set(i))
    characters[l] = languageCharacter
for i in characters.keys():
    print(i , ": " , len(characters[i]))



# special characters before Processing
# Character Counts in each Language
# Estonian :  140
# Swedish :  147
# Thai :  363
# Tamil :  242
# Dutch :  114
# Japanese :  2574
# Turkish :  274
# Latin :  322
# Urdu :  295
# Indonesian :  261
# Portugese :  129
# French :  130
# Chinese :  4124
# Korean :  2478
# Hindi :  306
# Spanish :  170
# Pushto :  298
# Persian :  186
# Romanian :  195
# Russian :  123
# English :  166
# Arabic :  159