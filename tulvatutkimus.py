import haravasto as h

def piirra_kentta():
    """jee"""
    h.tyhjaa_ikkuna()
    h.piirra_tausta()
    h.aloita_ruutujen_piirto()
    for y, rivi in enumerate(lista):
        for x, sarake in enumerate(rivi):
            if lista[y][x] == "x":
                h.lisaa_piirrettava_ruutu("x", int(x) * 40, int(y) * 40)
            elif lista[y][x] == " ":
                h.lisaa_piirrettava_ruutu(" ", int(x) * 40, int(y) * 40)
            elif lista [y][x] == "0":
                h.lisaa_piirrettava_ruutu("0", int(x) * 40, int(y) * 40)
    h.piirra_ruudut()

def main(lista):
    """jee taas"""
    h.lataa_kuvat("/Users/virvekivela/Downloads/spritet-2")
    h.luo_ikkuna(len(lista[0]) * 40, len(lista) * 40)
    h.aseta_piirto_kasittelija(piirra_kentta)
    h.aloita()

def tulvataytto(lista, x, y):
    """jee lol"""
    pituus = len(lista)
    leveys = len(lista[0])
    planeetta = ([x, y])
    if lista[y][x] == "x":
        pass
    else:
        while len(planeetta) > 0:
            luku = planeetta.pop(-1)
            lista[luku[1]][luku[0]] == "0"
            luku_x = [luku[0] - 1, luku[0], luku[0] + 1]
            luku_y = [luku[0] - 1, luku[0], luku[0] + 1]
            for rivi in luku_y:
                for sarake in luku_x:
                    if pituus > rivi and leveys > sarake >= 0:
                        if lista[rivi][sarake] == " ":
                            planeetta.append[(sarake, rivi)]
                        else:
                            pass

lista = [
    [" ", " ", " ", "x", " ", " ", " ", " ", " ", " ", " ", "x", " "],
    [" ", " ", "x", "x", " ", " ", " ", "x", " ", " ", " ", "x", " "],
    [" ", "x", "x", " ", " ", " ", " ", "x", " ", " ", "x", "x", " "],
    ["x", "x", "x", "x", "x", " ", " ", "x", " ", "x", " ", " ", " "],
    ["x", "x", "x", "x", " ", " ", " ", " ", "x", " ", "x", " ", " "],
    [" ", " ", "x", " ", " ", " ", " ", " ", " ", "x", " ", " ", " "]
]

if __name__ == "__main__":
    tulvataytto(lista, 2, 4)
    main(lista)
