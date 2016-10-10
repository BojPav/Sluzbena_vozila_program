print "<<--Dobrodosli v program za upravljanje s sluzbenimi vozili-->>" + "\n"


class Vozila(object):
    def __init__(self, znamka, model, stevilo_prevozenih_kilometrov, datum_zadnjega_servisa):
        self.znamka = znamka
        self.model = model
        self.kilometri = stevilo_prevozenih_kilometrov
        self.servis = datum_zadnjega_servisa


def main():

    sluzbena_vozila_datoteka = open("sl_vozila.txt", "r+")

    seznam_vozila = []

    for item in sluzbena_vozila_datoteka:

        znamka, model, kilometri, servis = item.split(";")

        vozilo = Vozila(znamka=znamka, model=model, stevilo_prevozenih_kilometrov=kilometri,
                        datum_zadnjega_servisa=servis)

        seznam_vozila.append(vozilo)
    while True:
        vprasanje = raw_input("Izberite redno stevilko: " + "\n"
                          "\n"
                          "1. ogled voznega parka" + "\n"
                          "2. urejanje stevila prevozenih kilometrov za izbrano vozilo " + "\n"
                          "3. urejanje datuma zadnjega servisa za izbrano vozilo" + "\n"
                          "4. novo vozilo na seznam" + "\n"
                          "5. izbrisati vozilo s seznama" + "\n"
                          "6. izlaz iz programa" + "\n"
                          "(1/2/3/4/5/6)>: ")

        if vprasanje == "1":
            ogled_vozila(seznam_vozila)
        elif vprasanje == "2":
            urejanje_km(seznam_vozila)
        elif vprasanje == "3":
            urejanje_servis(seznam_vozila)
        elif vprasanje == "4":
            dodaj_novo_vozilo(seznam_vozila)
        elif vprasanje == "5":
            brisanje_vozila(seznam_vozila)
        elif vprasanje == "6":
            break
        else:
            print "Vas vnos je bil napacen. Poskusite ponovno..."

    shrani_izmene(seznam_vozila, sluzbena_vozila_datoteka)

    sluzbena_vozila_datoteka.close()


def ogled_vozila(vozilo):
        print open("sl_vozila.txt").read()



def urejanje_km(vozilo):

    ogled_vozila(vozilo)

    vozilo_index = int(raw_input("Vpisite index vozila koje zelite urejati(0 >=): "))

    task = vozilo[vozilo_index]

    print "Izbrali ste: "
    print "Vozilo: " + task.znamka
    print "Model: " + task.model
    print "Km: " + task.kilometri
    print "Servis: " + task.servis

    novo_km = raw_input("Vpisite novo km: ")

    task.kilometri = novo_km

    print "Prevozeni kiometri za izbrano vozilo so urejeni!"

    main()


def urejanje_servis(vozilo):

    ogled_vozila(vozilo)

    vozilo_index = int(raw_input("Vpisite index vozila koje zelite urejati(0 >=): "))

    task = vozilo[vozilo_index]

    print "Izbrali ste: "
    print "Vozilo: " + task.znamka
    print "Model: " + task.model
    print "Km: " + task.kilometri
    print "Servis: " + task.servis

    new_servis = raw_input("Vpisite nov datum servisa: ")
    task.servis = new_servis
    print "Datum servisa za izbrano vozilo je urejen!"


def dodaj_novo_vozilo(vozilo):

    znamka = raw_input("Vpiste znamko: ")
    model = raw_input("Vpisite model: ")
    kilometri = raw_input("Vpisite km: ") + "km"
    servis = raw_input("Vpisite datum zadnjega servisa: ")

    novo_vozilo = Vozila(znamka=znamka, model=model,
                         stevilo_prevozenih_kilometrov=kilometri, datum_zadnjega_servisa=servis)

    vozilo.append(novo_vozilo)

    print "Novo vozilo je dodano na seznam!"


def brisanje_vozila(vozilo):

    ogled_vozila(vozilo)

    st_vozila = int(raw_input("Katero vozilo zelite izbrisati?(0 >=): "))

    del vozilo[st_vozila]

    print "Uspesno ste izbrisali izbrano vozilo!"


def shrani_izmene(seznam_vozila, sluzbena_vozila_datoteka):

    sluzbena_vozila_datoteka.close()
    sluzbena_vozila_datoteka = open("sl_vozila.txt", "w")

    for item in seznam_vozila:
        sluzbena_vozila_datoteka.write(item.znamka + " ; " + item.model + " ; " + item.kilometri + " ; " + item.servis)

if __name__ == "__main__":
    main()

    print "END"
