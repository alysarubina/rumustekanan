def hitung_tekanan(F, A):
    P = F / A
    return P

def hitung_gaya(P, A):
    if A == 0:
        return None
    F = P * A
    return F

def hitung_luas_permukaan(F, P):
    A = F / P
    return A

def main():
    print("Program untuk menghitung tekanan")
    print("1: Hitung tekanan (Pa)")
    print("2: Hitung gaya (N)")
    print("3: Hitung luas permukaan (m^2)")

    pilihan = input("Masukkan pilihan 1/2/3: ")

    if pilihan == "1":
        F = float(input("Masukkan nilai gayanya dalam N: "))
        A = float(input("Masukkan nilai luas permukaannya dalam m^2: "))
        P = hitung_tekanan(F, A)
        print(f"Tekanannya sebesar: {P:.2f} Pa")

    elif pilihan == "2":
        P = float(input("Masukkan nilai tekanannya dalam Pa: "))
        A = float(input("Masukkan nilai luas permukaannya dalam m^2: "))
        F = hitung_gaya(P, A)
        print(f"Gayanya sebesar: {F:.2f} N")

    elif pilihan == "3":
        F = float(input("Masukkan nilai gayanya dalam N: "))
        P = float(input("Masukkan nilai tekanannya dalam Pa: "))
        A = hitung_luas_permukaan(F, P)
        print(f"Luas permukaannya sebesar: {A:.2f} m^2")

    else:
        print("Pilihan tidak sesuai, silahkan pilih 1/2/3")

if __name__ == "__main__":
    main()
    