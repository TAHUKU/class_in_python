class Kue:
    def __init__(self, jenis_kue, rasa, semua_ukuran):
        self.jenis_kue = jenis_kue
        self.rasa = rasa
        self.ukuran = semua_ukuran
        
    def Jenis_ukuran(self):
        print(f"kue {self.jenis_kue} dengan rasa {self.rasa} ukuran: {self.ukuran}")
        
kue_saya = Kue("donat", "keju", "kecil")
kue_dia = Kue("pizaa", "coklat", "besar")

kue_saya.Jenis_ukuran()
kue_dia.Jenis_ukuran()



        