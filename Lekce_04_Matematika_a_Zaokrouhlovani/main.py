
# ÚLOHA 1: Zvětšovač (použij +=)
cislo = int(input("Zadej číslo: "))
# Sem doplň kód:

cislo += 10
print(cislo)

# ÚLOHA 2: Útrata (zaokrouhli na 2 místa)
celkem = float(input("Celková suma (Kč): "))
lidi = int(input("Počet lidí: "))
# Sem doplň výpočet a print s round():

x = round(celkem/lidi, 2)
print(f"Každý musí zaplatit {x}")

# ÚLOHA 3: Plocha kruhu (zaokrouhli na celé číslo)
r = float(input("Zadej poloměr: "))
# plocha = 3.14 * r * r
# Sem doplň kód:

S = round(3.14 * (r*r))
print(f"Plocha kruhu je {S}")
