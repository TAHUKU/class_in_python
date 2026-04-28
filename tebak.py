tebak = input("Masukan huruf saja: ")
try:
    angka = int(input("Masukan angka saja: "))
    print(f'angka yang anda masukan {len(str(angka))} angka yaitu angka {angka}')

except ValueError:
    print("ini bukan angka")
print(f'huruf yang anda masukan {len(tebak)} huruf, yaitu huruf {tebak}')


