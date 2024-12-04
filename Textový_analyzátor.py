"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Petr Přibyl
email: petrpribyl91@outlook.com
"""
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# Databáze zaregitrovaných uživatelů
zaregistrovani_uzivatele = {
    "bob": 123, 
    "ann": "pass123", 
    "mike": "password123", 
    "liz": "pass123"
    }

jmeno = input("Enter your username: ")
heslo = input("Enter your password: ")

# Ověření uživatelského jména a hesla
if jmeno in zaregistrovani_uzivatele and str(zaregistrovani_uzivatele[jmeno]) == heslo:
    print("=" * 40)
    print(f"Username: {jmeno} \nPassword: {heslo} \nWelcome to the app, {jmeno}. We have {len(TEXTS)} texts to be analyzed.")
    print("=" * 40)
else:
    print(f"Username: {jmeno} \nPassword: {heslo} \nUnregistered user, terminating the program..")
    exit()

# Uživatelský výběr
vyber_textu = input("Enter a number between 1 and 3 to select: ")

# Kontrola, zda je vstup číslo a v rozsahu
if vyber_textu.isdigit() and 1 <= int(vyber_textu) <= len(TEXTS):
    vyber_index = int(vyber_textu) - 1
    print("=" * 40)
    print(TEXTS[vyber_index])
else:
    print("Invalid selection, terminating the program..")
    exit()

# Analýza textu
slova = [slovo.strip(".,!?") for slovo in TEXTS[vyber_index].split()]
pocet_slov = len(slova)
slova_titlecase = sum(1 for slovo in slova if slovo.istitle())
slova_uppercase = sum(1 for slovo in slova if slovo.isupper())
slova_lowercase = sum(1 for slovo in slova if slovo.islower())
cisla_v_textu = sum(1 for slovo in slova if slovo.isdigit())
soucet_cisel = sum(int(slovo) for slovo in slova if slovo.isdigit())

# Výstup statistik
print("=" * 40)
print(f"There are {pocet_slov} words in the selected text.")
print(f"There are {slova_titlecase} titlecase words.")
print(f"There are {slova_uppercase} uppercase words.")
print(f"There are {slova_lowercase} lowercase words.")
print(f"There are {cisla_v_textu} numeric strings.")
print(f"The sum of all the numbers is {soucet_cisel}.")
print("=" * 40)

# Histogram délek slov
delky_slov = {}
for slovo in slova:
    delka = len(slovo)
    delky_slov[delka] = delky_slov.get(delka, 0) + 1

print(f"{'LEN':<5}| {'OCCURRENCES':<20}| {'NR.':<5}")
print("-" * 40)
for delka, pocet in sorted(delky_slov.items()):
    print(f"{delka:<5}| {'*' * pocet:<20}| {pocet:<5}")