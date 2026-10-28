
def hitung_rata_rata(nilai):
    if len(nilai) == 0:
        return 0

    return sum(nilai) / len(nilai)


# Test case
data_1 = [80, 90, 70]
data_2 = [60, 80, 100]
data_3 = []

print("Rata-rata data 1:", hitung_rata_rata(data_1))
print("Rata-rata data 2:", hitung_rata_rata(data_2))
print("Rata-rata data 3:", hitung_rata_rata(data_3))
