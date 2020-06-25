import os
from time import sleep
import feature

os.system("cls")
statusloading=feature.loadData()
opsi=0
if statusloading:
	loginSuccess=feature.login()
	if loginSuccess:
		print("Welcome!")
		sleep(1)
		while opsi!=6:
			os.system("cls")
			feature.menu()
			print("")
			try :
				opsi=int(input("Masukan Opsi (1-6): "))
			except ValueError:
				print("")
				print("Mohon Untuk Memasukan Angka 1-6!")
				print("")
				input("Enter To Exit")
			else :
				print("")
				if opsi==6:
					print("Anda Telah Keluar Dari Aplikasi Kontak")
					break
				elif opsi==1:
					feature.tampilData()
				elif opsi==2:
					feature.inputData()
				elif opsi==3:
					feature.hapusData()
				elif opsi==4:
					feature.cariData()
				elif opsi==5:
					feature.editData()
				else:
					print("Mohon untuk Memasukan Angka 1-6!\n")
					input("Enter To Exit")
	else:
		print("Login Gagal")
else:
	print("JSON FILE ERROR !!!")

