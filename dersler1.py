print("""

[1]Toplama
[2]Çıkarma
[3]Çarpma
[4]Bölme
[5]Üs ALma
[Q]Çıkış

	""")

giris = input("yapacağınız işlemi girin:")

if giris  == "1":
	x=input("ilk sayı:")
	x=float(x)
	y=input("ikinci sayı:")
	y=float(y)
	print("===============================")
	print("işemin sonucu bu",(x+y))
	print("===============================")

elif giris == "2":
	x=input("ilk sayı:")
	x=float(x)
	y=input("ikinci sayı:")
	y=float(y)
	print("===============================")
	print("işemin sonucu bu",(x-y))
	print("===============================")

elif giris == "3":
	x=input("ilk sayı:")
	x=float(x)
	y=input("ikinci sayı:")
	y=float(y)
	print("===============================")
	print("işemin sonucu bu",(x*y))
	print("===============================")

elif giris == "4":
	x=input("ilk say:ı")
	x=float(x)
	y=input("ikinci sayı:")
	y=float(y)
	print("===============================")
	print("işemin sonucu bu",(x/y))
	print("===============================")

elif giris == "5":
	x=input("Taban:")
	x=float(x)
	y=input("Üs:")
	y=float(y)
	print("===============================")
	print("işemin sonucu bu",(x**y))
	print("===============================")
elif giris == "q" or giris=="Q":
	print("===============================")
	print("çıkılıyor...")
	print("===============================")
	quit()
else:
	print("===============================")
	print("Hatalı girdin!")
	print("===============================")
	quit()
