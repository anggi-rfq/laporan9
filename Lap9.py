from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///database.db", echo=False)
Base = declarative_base()

class Jadwal(Base):
    __tablename__ = "jadwal_matkul"
    id = Column(Integer, primary_key=True)
    nama_matkul = Column(String)
    hari = Column(String)
    jam = Column(String)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def tambah(): 
    nama = input("Nama Matkul: ")
    hari = input("Hari: ")
    jam = input("Jam: ")
    session.add(Jadwal(nama_matkul=nama, hari=hari, jam=jam))
    session.commit()
    print("Jadwal berhasil ditambahkan.")

def tampil(): 
    for j in session.query(Jadwal).all():
        print(f"{j.id}. {j.nama_matkul} - {j.hari}, jam {j.jam}")

def ubah(): 
    id = int(input("ID yang diubah: "))
    j = session.query(Jadwal).filter_by(id=id).first()
    if j:
        j.nama_matkul = input(f"Nama Matkul [{j.nama_matkul}]: ") or j.nama_matkul
        j.hari = input(f"Hari [{j.hari}]: ") or j.hari
        j.jam = input(f"Jam [{j.jam}]: ") or j.jam
        session.commit()
        print("Jadwal diubah.")
    else:
        print("jadwal tidak ada.")

def hapus(): 
    id = int(input("ID yang dihapus: "))
    j = session.query(Jadwal).filter_by(id=id).first()
    if j:
        session.delete(j)
        session.commit()
        print("Jadwal berhasil dihapus.")
    else:
        print("Jadwal tidak ditemukan.")

def cari():
    nama = input("Masukkan nama matkul yang dicari: ")
    hasil = session.query(Jadwal).filter(Jadwal.nama_matkul.like(f"%{nama}%")).all()
    if hasil:
        print("--- Hasil Pencarian ---")
        for j in hasil:
            print(f"{j.id}. {j.nama_matkul} - {j.hari}, jam {j.jam}")
    else:
        print("Jadwal tidak ditemukan.")

if __name__ == "__main__":
    while True:
        print("\n[1] Tambah  [2] Tampil  [3] Ubah  [4] Hapus  [0] Keluar")
        menu = input("Pilih menu: ")
        if menu == "1": tambah()
        elif menu == "2": tampil()
        elif menu == "3": ubah()
        elif menu == "4": hapus()
        elif menu == "0": break
        else: print("Pilihan tidak valid.")

