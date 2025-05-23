from pathlib import Path

putanja = Path("dnevnik.txt")
if not putanja.exists():
    print("Datoteka ne postoji.")
else:
    with open(putanja, "r", encoding="utf-8") as fajl:
        tekst = fajl.read()

    broj_karaktera = len(tekst)
    reci = tekst.split()
    broj_reci = len(reci)
    broj_recenica = len([r for r in tekst.split(".") if r.strip() != ""])
    najduza_rec = max(reci, key=len)
    prosecna_duzina = round(sum(len(r) for r in reci) / broj_reci, 2)

    with open("izvestaj.txt", "w", encoding="utf-8") as izvestaj:
        izvestaj.write(f"Broj karaktera: {broj_karaktera}\n")
        izvestaj.write(f"Broj reči: {broj_reci}\n")
        izvestaj.write(f"Broj rečenica: {broj_recenica}\n")
        izvestaj.write(f"Najduža reč: {najduza_rec} ({len(najduza_rec)} karaktera)\n")
        izvestaj.write(f"Prosečna dužina reči: {prosecna_duzina} karaktera\n")
