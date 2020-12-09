from random import randint

def make_pair(names):
    liste = []
    for i in range(len(names)-1):
        liste.append(names[i])
        liste.append(names[i+1])
    return liste

    
def split_names(names):
    return names.split(", ")

x = input('Entrez les noms des participant(e)s, séparés par des virgules: ')
noms = x.split(", ")
make_pair(noms)
print()
split_names(noms)