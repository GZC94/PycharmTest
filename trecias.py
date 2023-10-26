print("\nPajamos/išlaidos 1.0")
pajamos = []
islaidos = []
islaidu_eilute = []
pajamu_eilute = []
i = []
p = []

while True:
    # meniu
    print("\nKokį veiksmą norėsite atlikti (įveskite 1,2,3,4,5,q)?"
          "\n1. Įvesti pajamas.\n"
          "2. Įvesti išlaidas.\n"
          "3. Atspausdinti išlaidų eilutes.\n"
          "4. Atspausdinti pajamų eilutes.\n"
          "5. Atspausdinti statistiką.\n"
          "6. Tam tikro mėnesio statistika.\n"
          "Išeiti - q\n")
    ivestis = input(">>>")
    if ivestis == "q":
        print(f"Įvedėte {ivestis}, programa baigia darbą.")
        break
    # išlaidos
    if ivestis == "1":
        menuo = input("Įveskite mėnesio pavadinimą:")
        paskirtis = input("Įveskite išlaidų paskirtį:")
        suma = input("Įveskite išleistą sumą: ")
        islaidu_eilute = [menuo, paskirtis, float(suma)]
        islaidos.append(islaidu_eilute)
    # pajamos
    if ivestis == "2":
        menuo = input("Įveskite mėnesio pavadinimą:")
        paskirtis = input("Įveskite kaip gautos pajamos:")
        suma = input("Įveskite gautą sumą: ")
        pajamu_eilute = [menuo, paskirtis, float(suma)]
        pajamos.append(pajamu_eilute)
    # išlaidų eilučių printas
    if ivestis == "3":
        print(islaidos)
    # pajamų eilučių printas
    if ivestis == "4":
        print(pajamos)
    # statistika
    if ivestis == "5":
        for el in pajamos:
            p.append(el[2])
        for el in islaidos:
            i.append(el[2])
        print(f"Viso išleidote: {sum(i)}")
        print(f"Viso uždirbote: {sum(p)}")
        print(f"Uždarbio ir išlaidų skirtumas: {sum(i) - sum(p)}")
    # mėnesio statistika
    if ivestis == "6":
        men_pa = []
        men_is = []
        menuo = input("Įveskite kokio mėnesio išlaidas ir pajamas norite sužinoti")
        for el in pajamos:
            if el[0] == menuo:
                men_pa.append(el[2])
        for el in islaidos:
            if el[0] == menuo:
                men_is.append(el[2])
        print(f"Jūsų pasirinkto mėnesio išlaidos:{sum(men_is)}")
        print(f"Jūsų pasirinkto mėnesio pajamos:{sum(men_pa)}")