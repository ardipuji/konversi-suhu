# Def konversi suhu dari Selsius ke Fahrenheit, Reamur, dan Kelvin
def konversi_suhu(selsius):
    Fahrenheit = (selsius * 1.8) + 32
    reamur = 0.8 * selsius
    kelvin = selsius + 273.15
    return Fahrenheit, reamur, kelvin

# Input dan output program
print("\n========== PROGRAM KONVERSI SUHU ==========")
selsius = float(input("Masukkan suhu dalam Selsius untuk dikonversi ke Fahrenheit, Reamur, dan Kelvin: "))
print("\n=========== HASIL KONVERSI SUHU ===========")
print(f"Suhu dalam Selsius      : {selsius}°C")
print(f"Suhu dalam Fahrenheit   : {konversi_suhu(selsius)[0]}°F")
print(f"Suhu dalam Reamur       : {konversi_suhu(selsius)[1]}°R")
print(f"Suhu dalam Kelvin       : {konversi_suhu(selsius)[2]} K")
print("===========================================")