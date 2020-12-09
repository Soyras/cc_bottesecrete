def make_pair(names):
    for i in range(len(names)-1):
        print(f'Paire n°{i+1}: {names[i]}, {names[i+1]}')        
    
def

x = input('Entrez les noms des participant(e)s, séparés par des virgules: ')
noms = x.split(", ")
make_pair(noms)