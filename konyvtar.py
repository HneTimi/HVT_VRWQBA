import csv

class Book_HVT:
    def __init__(self, cim, szerzo, ev):
        self.cim = cim
        self.szerzo = szerzo
        self.ev = ev

    def __str__(self):
        return f"{self.cim} - {self.szerzo} ({self.ev})"


def mentes_HVT(konyvek, fajlnev="konyvek.csv"):
    with open(fajlnev, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for k in konyvek:
            writer.writerow([k.cim, k.szerzo, k.ev])


def betolt_HVT(fajlnev="konyvek.csv"):
    konyvek = []
    try:
        with open(fajlnev, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for sor in reader:
                if len(sor) == 3:
                    konyvek.append(Book_HVT(sor[0], sor[1], sor[2]))
    except FileNotFoundError:
        pass
    return konyvek