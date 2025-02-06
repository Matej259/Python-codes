# Studna válcového tvaru má hloubku hs (m), poloměr skruží r (m)
# a vzdálenost hladiny vody od povrchu studny d (m).
# Napiš funkci, která spočítá objem vody ve studni v metrech krychlových.

r = float(input("Zadej poloměr studny: "))
hs = float(input("Zadej výšku studny: "))
d = float(input("Zadej vzdálenost hladiny od povrchu: "))

def objemValce(polomer_podstavy, vyska_valce):
    return (3.14159265358979 * polomer_podstavy ** 2) * vyska_valce

V = objemValce(r, hs - d)