# Představ si, že spravuješ e-shop s elektronikou.
# Zde jsou ceny produktů v jednom nákupním košíku:

ceny_kosiku = [1250.50, 499.00, 120.80, 5600.00, 890.00]
# --------------------------------------------------------------------------

# ÚLOHA 1: Základní přehled
# Vypiš do konzole:
# a) Kolik položek je v košíku (použij len)
# b) Kolik stojí nejlevnější produkt (použij min)
# c) Kolik stojí nejdražší produkt (použij max)

print(f"Počet položek: {len(ceny_kosiku)} Kč")
# Sem doplň zbytek:

print(f"Nejlevnější položka stojí: {min(ceny_kosiku)} Kč")

print(f"Nejdražší položka stojí: {max(ceny_kosiku)} Kč")

# ÚLOHA 2: Celková tržba
# Spočítej celkovou cenu celého košíku (použij sum)
# Výsledek vypiš a zaokrouhli na celé koruny.

# Sem doplň kód:

print(f"Celková cena košíku je: {round(sum(ceny_kosiku))} Kč")

# ÚLOHA 3: Průměrná cena
# Vypočítej průměrnou cenu produktu v košíku.
# Průměr = součet / počet
# Výsledek vypiš zaokrouhlený na 2 desetinná místa pomocí f-stringu (:.2f)

# Sem doplň kód:

print(f"Průměrná cena košíku je: {(sum(ceny_kosiku)/len(ceny_kosiku)):.2f} Kč")

# BONUSOVÁ ÚLOHA: Rozdíl
# Vypočítej, o kolik korun je nejdražší položka dražší než ta nejlevnější.
# Výsledek vypiš.

# Sem doplň kód:

print(f"Nejdražší a nejlevněší položka se liší o: {max(ceny_kosiku)-min(ceny_kosiku)} Kč")
