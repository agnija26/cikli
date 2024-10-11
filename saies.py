SpeletajaVards=input("Ievadi savu vārdu: ")

SpeletajaVards=SpeletajaVards.lower()
#"mainīgais.lower()" - konvertē visus burtu simbolus par mazajiem burtiem.

SpeletajaVards=SpeletajaVards.capitalize()
#"mainīgais.capitalize()" - simbolu virknē pirmo burtu konvertē par lielo burtu.
print(SpeletajaVards)

vards1="čība"

burtuSK=len(vards1)
#len - saskaita virknē simbolu skaitu.
minejums=input(f"Uzraksti vārdu pareizi - {vards1[3]}{vards1[0]}{vards1[2]}{vards1[1]}: ")
#mainigais[burta pozīcija] - simbolu virkne sākās ar indeksu - 0.

minejums=minejums.lower()

if minejums==vards1:
    print("Uzminēji vārdu!")
else:
    print("Neuzminēji vārdu!")