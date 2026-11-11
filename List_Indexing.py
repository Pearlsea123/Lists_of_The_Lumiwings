#================================== List Indexing ================================
print("================================== List Indexing ================================")
def worder(lumiwing):
    Aetherwings= 0
    Lister= []
    for word in lumiwing:
        if len(word) > 1 and word[0] == word[-1]:
            Aetherwings += 1
            Lister.append(word)
    print("List of words which are same on first and last letter", Lister)
    return Aetherwings
lumiwing= ['Lumiwings', "aba", '1221', '12321', 'kcekhc/lqqk', 'jkvhlwhello', 'hiiamhi']
print(worder(lumiwing))
