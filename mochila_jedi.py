mochila = ['Binoculares', 'Creditos', 'Sable de luz', 'Laser']

def usar_fuerza(mochila, pos):
    if(pos< len(mochila)):
        if(mochila[pos] == 'Sable de luz'):
            return pos
        else:
            return usar_fuerza(mochila, pos+1)
    else:
        return -1
