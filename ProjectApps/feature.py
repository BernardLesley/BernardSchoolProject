import os
from json import load,dump
from time import sleep
from getpass import getpass

fileUser="user.json"
fileKontak="kontak.json"
user={}
kontak={}

def loadData():
	global user,kontak
	with open(fileUser) as f:
		user=load(f)
	with open(fileKontak) as f:
		kontak=load(f)
	return True

def saveData():
	with open (fileUser,'w') as f:
		dump(user,f)
	with open(fileKontak,'w') as f:
		dump(kontak,f)
	return True

def login():
	counter=1
	Username=input("Masukan Username :")
	password=getpass("Masukan Password :")
	datacheck=False
	passcheck=False
	if Username in user :
		datacheck=True
		passcheck=(user[Username]==password)
	else :
		datacheck=False
		passcheck=False

	while (not datacheck) or (not passcheck) :
		counter+=1
		if counter>3 :
			return False
		print("Kombinasi Username atau Password Salah")
		Username=input("Masukan Username :")
		password=getpass("Masukan Password :")
		if Username in user :
			datacheck=True
			passcheck=(user[Username]==password)
		else :
			datacheck=False
			passcheck=False
	else :
		print("")
		print("Login Sukses")
		return True

def menu():
	print("Selamat Datang Di Aplikasi Kontak")
	print("=================================")
	print("1. Lihat Kontak")
	print("2. Input Kontak Baru")
	print("3. Hapus Kontak")
	print("4. Cari Kontak")
	print("5. Edit Kontak")
	print("6. Keluar")

def tampilData():
	print("Database Kontak")
	print("===============")
	if len(kontak)>0:
		for idkontak in kontak:
			print(f"ID :{idkontak}\tNama Depan : {kontak[idkontak][0]}\tNama Belakang : {kontak[idkontak][1]}\tNo. HP : {kontak[idkontak][2]}\tEmail : {kontak[idkontak][3]}")
	else:
		print("Tidak Ada Kontak Untuk Ditampilkan")
	print("")
	input("Enter To Exit")

def inputData():
	print("Input Kontak Baru")
	print("=================")
	info=[]
	namaDepan=input("Masukan Nama Depan Anda \t: ")
	if namaDepan=="":
		print("Nama Depan Tidak Boleh Kosong!!!")
	else :
		namaBelakang=input("Masukan Nama Belakang Anda \t: ")
		noTelp=input("Masukan Nomor Telepon Anda \t: ")
		if noTelp=="":
			print("Nomor Telepon Tidak Boleh Kosong!!!")
		else:
			email=(f"{namaDepan}.{namaBelakang}@igs.com")
			idkontak=(f"igs-{noTelp[0:5]}")
			count=1
			while idkontak in kontak:
				count+=1
				idkontak=idkontak[0:9]
				idkontak=idkontak+(f"_{count}")
			info.append(namaDepan)
			info.append(namaBelakang)
			info.append(noTelp)
			info.append(email)
			kontak[idkontak]=info
			saveData()
			print("")
			print("Generating ID and Email From System....")
			sleep(0.5)
			print("")
			print(f"ID Anda : {idkontak} dan Email Anda : {email}")
	print("")
	input("Enter to Exit")

def hapusData():
	print("Menghapus Kontak")
	print("================")
	datahapusRAW=input("Masukan ID : igs-")
	datahapus="igs-"+datahapusRAW
	print("")
	if datahapus in kontak:
		del kontak[datahapus]
		print(f"Menghapus Kontak...")
		print("")
		sleep(0.5)
		print(f"Kontak Dengan ID:{datahapus} Berhasil Dihapus")
	else:
		sleep(0.5)
		print("Kontak Tidak Ditemukan")
	saveData()
	print("")
	input("Enter to Exit")

def cariData():
	print("Mencari Kontak")
	print("==============")
	datacariRAW=input("Masukan ID : igs-")
	datacari="igs-"+datacariRAW
	print("")
	print(f"Mencari Kontak...")
	print("")
	sleep(0.5)
	if datacari in kontak:
		print(f"Kontak Dengan ID:{datacari} Berhasil Ditemukan")
		print("")
		idkontak=datacari
		print("Rincian Kontak : ")
		print(f"ID:{idkontak}\tNama Depan:{kontak[idkontak][0]}\tNama Belakang :{kontak[idkontak][1]}\tNo. HP:{kontak[idkontak][2]}\tEmail:{kontak[idkontak][3]}")
	else:
		print("Kontak Tidak Ditemukan")
	saveData()
	print("")
	input("Enter to Exit")

def editData():
	print("Mengedit Kontak")
	print("=================")
	dataeditRAW=input("Masukan ID : igs-")
	dataedit="igs-"+dataeditRAW
	print("")
	print(f"Mencari Kontak...")
	print("")
	sleep(0.5)
	if dataedit in kontak:
		print(f"Kontak Dengan ID:{dataedit} Berhasil Ditemukan")
		print("")
		print(f"Rincian Kontak : ")
		idkontak=dataedit
		print(f"ID:{idkontak}\tNama Depan:{kontak[idkontak][0]}\tNama Belakang :{kontak[idkontak][1]}\tNo. HP:{kontak[idkontak][2]}\tEmail:{kontak[idkontak][3]}")
		info=[]
		print("")
		namaDepan=input("Masukan Nama Depan Baru \t: ")
		if namaDepan=="":
			print("Nama Depan Tidak Boleh Kosong!!!")
		else:
			namaBelakang=input("Masukan Nama Belakang Baru \t: ")
			noTelp=input("Masukan Nomor Telepon Baru \t: ")
			if noTelp=="":
				print("Nomor Telepon Tidak Boleh Kosong!!!")
			else:
				email=(f"{namaDepan}.{namaBelakang}@igs.com")
				info.append(namaDepan)
				info.append(namaBelakang)
				info.append(noTelp)
				info.append(email)
				kontak[idkontak]=info
				saveData()
				print("")
				print(f"Mengedit Kontak...")
				print("")
				sleep(0.5)
				print(f"Kontak Dengan ID:{dataedit} Berhasil Diedit")
				print(f"Email Baru : {email}")
	else:
		print("Kontak Tidak Ditemukan")
	print("")
	input("Enter to Exit")

