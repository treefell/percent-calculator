

MINIMAL_PERCENT = 0.01

coca = [["eau gazéifiée", -1],["sucre",30.1], ["colorant:E150d", -1], ["acidifiant: acide phosphorique", -1], ["arômes naturels", -1], ["arôme caféine", -1]]

nocciolata = [["Sucre", -1], ["pâte de noisettes", 18.5], ["huile de tournesol", -1], ["lait écrémé en poudre", -1], ["cacao maigre en poudre", 6.5], ["beurre de cacao", -1], ["émulsifiant: lécithine de soja", -1], ["extrait de vanille", -1]]

paindemie_bio_LaBoulangère = [["Farine de BLE", 51, -1], ["eau", -1, -1], ["levain de BLE et de SEIGLE", 9.6, -1], ["huile de tournesol", 4.4, -1], ["sucre de canne roux", -1, -1], ["levure", -1, -1], ["graines de tournesol décortiquées", 3.3, -1], ["graines de lin brun", 2.7, -1], ["flocons de BLE", 2.7, -1], ["farine de SEIGLE", 1.6, -1], ["graines de millet décortiquées", 1.6, -1], ["gluten de BLE", -1, -1], ["sel",-1, -1], ["arôme naturel (contient alcool)",-1, -1], ["farine d'ORGE maltée torréfiée", 0.2, -1]]


def total(liste_ingredient):
    total = 0
    for ingredient in liste_ingredient:
        total += ingredient[2]
    return total

def max_percent(total, max):
    localtotal = 100 - total
    localmax = localtotal if max + total > 100 else max 

    return (localmax)

def min_percent(min):
    localmin = min if min > MINIMAL_PERCENT else MINIMAL_PERCENT
    return (localmin)


def search_min_percent(liste_ingredient):
    prev_min = 0
    for ingredient in reversed(liste_ingredient):
        min = ingredient[1] if ingredient[1] > prev_min else prev_min
        ingredient[2] = min_percent(min)
        prev_min = ingredient[2]
    return liste_ingredient

    
def search_max_percent(liste_ingredient, total):
    max = 0
    for ingredient in liste_ingredient:
        if ingredient[1] > -1 :
            max += ingredient[1]
        else :
            ratio = total - ingredient[2] if max > total - ingredient[2] else max
            ingredient[1] = 100 - ratio
    return liste_ingredient


if __name__ == "__main__":
    list_ingredient = search_min_percent(paindemie_bio_LaBoulangère)
    total = total(list_ingredient)
    list_ingredient = search_max_percent(list_ingredient, total)
    print(list_ingredient)
