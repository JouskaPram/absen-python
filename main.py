print("="*20)
print("Keterangan:")
print("H = hadir")
print("I = izin")
print("S = sakit")
print("A = alfa/tanpa keterangan")
print("="*20)

def absensi_siswa(students): 
  jumlah = {}
  jumlah_hadir = 0
  jumlah_sakit = 0
  jumlah_izin = 0
  jumlah_alfa = 0

  for student in students:
    
    status = input(student + " (H/S/I/A): ")
    jumlah[student] = status

    if status == "H":
      jumlah_hadir += 1
    elif status == "S":
      jumlah_sakit += 1
    elif status == "I":
      jumlah_izin += 1
    elif status == "A":
      jumlah_alfa += 1

  print("\nAbsensi siswa:")
  for student, status in jumlah.items():
    if status == 'H':
      print(student+": Hadir")
    elif status == "S":
      print(student+": Sakit")
    elif status == "I":
      print(student+": Izin")
    elif status == "A":
      print(student+": Alfa")
  
  jumlah_siswa = len(students)
  persentase_hadir = jumlah_hadir / jumlah_siswa * 100
  persentase_izin = jumlah_izin / jumlah_siswa * 100
  persentase_sakit = jumlah_sakit / jumlah_siswa * 100
  persentase_alfa = jumlah_alfa / jumlah_siswa * 100
  print("\nJumlah siswa yang hadir: " + str(jumlah_hadir)+ " ("+"{:.2f}%" ")".format(persentase_hadir))
  print("Jumlah siswa yang sakit: " + str(jumlah_sakit)+ " ("+"{:.2f}%" ")".format(persentase_sakit))
  print("Jumlah siswa yang izin: " + str(jumlah_izin)+ " ("+"{:.2f}%" ")".format(persentase_izin))
  print("Jumlah siswa yang Alfa: " + str(jumlah_alfa)+ " ("+"{:.2f}%" ")".format(persentase_alfa))


students = ["Pram", "Dita", "Adit", "Mrap", "Raidan","Pramud","DeDita"]
absensi_siswa(students)