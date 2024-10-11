print("sveicināti!")

zetoni=0

while zetoni<15:
    print(f"ir {zetoni} žetoni!")

    met=int(input("cik žetonus ievietosi?:"))

    zetoni+=met # zetoni=zetoni+met

zetoni=zetoni-15

print(f"paņem kafiju un {zetoni} žetonu atlikums!☕")