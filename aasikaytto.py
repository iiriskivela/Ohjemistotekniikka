import aasimaaritelmat as am

def nayta_tila(aasin_tila):
    """Tulostaa aasin tilan."""
    ika=aasin_tila["IKÄ"]
    raha=aasin_tila["RAHA"]
    print(f"Aasi on {ika} vuotta vanha ja rahaa on {raha} mk")
    print("Kylläisyys: ", aasin_tila["KYLLÄISYYS"])
    print("Onnellisuus: ", aasin_tila["ONNELLISUUS"])
    print("Jaksaminen: ", aasin_tila["JAKSAMINEN"])
    if aasin_tila["ELÄKE"] is True:
        print("Aasi on jäänyt eläkkeelle.")

    return 0

def pyyda_syote(aasin_tila):
    """Näyttää käyttäjälle aasin tilaa vastaavat mahdolliset syötteet ja kysyy uutta
syötettä kunnes käyttäjä antaa laillisen syötteen. Saatu syöte palautetaan."""
    if aasin_tila["ELÄKE"] is False:
        print("Valinnat:", ", ".join(am.VALINNAT))
    else:
        print("Valinnat:", ", ".join(am.ELAKEVALINNAT))
    while True:
        syote = input("Anna seuraava valinta: ")
        if syote == "":
            return syote
        if aasin_tila["ELÄKE"] is False:
            for valinta in am.VALINNAT:
                if syote == valinta:
                    return syote
        elif aasin_tila["ELÄKE"] is True:
            for e_valinta in am.ELAKEVALINNAT:
                if syote == e_valinta:
                    return syote
        print("Virheellinen syöte")
