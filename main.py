import tkinter as tk
from tkinter import messagebox, Listbox, END, Scrollbar
from konyvtar import Book, mentes, betolt

konyvek = betolt()


def hozzaad():
    cim = entry_cim.get()
    szerzo = entry_szerzo.get()
    ev = entry_ev.get()

    if not cim or not szerzo or not ev:
        messagebox.showwarning("Hiba", "Minden mezőt ki kell tölteni!")
        return

    uj = Book(cim, szerzo, ev)
    konyvek.append(uj)
    frissit()

    entry_cim.delete(0, END)
    entry_szerzo.delete(0, END)
    entry_ev.delete(0, END)


def torol():
    try:
        index = lista.curselection()[0]
        konyvek.pop(index)
        frissit()
    except:
        messagebox.showwarning("Hiba", "Nincs kijelölt könyv!")


def mentes():
    mentes(konyvek)
    messagebox.showinfo("Siker", "A könyvek elmentve!")


def frissit():
    lista.delete(0, END)
    for k in konyvek:
        lista.insert(END, str(k))

ablak = tk.Tk()
ablak.title("Könyvtárkezelő program")
ablak.geometry("600x500")

tk.Label(ablak, text="Cím:").pack()
entry_cim = tk.Entry(ablak, width=40)
entry_cim.pack()

tk.Label(ablak, text="Szerző:").pack()
entry_szerzo = tk.Entry(ablak, width=40)
entry_szerzo.pack()

tk.Label(ablak, text="Kiadás éve:").pack()
entry_ev = tk.Entry(ablak, width=40)
entry_ev.pack()

tk.Button(ablak, text="Könyv hozzáadása", command=hozzaad).pack(pady=5)
tk.Button(ablak, text="Kijelölt törlése", command=torol).pack(pady=5)
tk.Button(ablak, text="Mentés CSV-be", command=mentes).pack(pady=5)

gordito = Scrollbar(ablak)
gordito.pack(side=tk.RIGHT, fill=tk.Y)

lista = Listbox(ablak, width=60, height=12, yscrollcommand=gordito.set)
lista.pack()

gordito.config(command=lista.yview)

frissit()

ablak.mainloop()