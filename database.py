import mysql.connector
from mysql.connector import Error as MysqlError

class Database:
    def __init__(self):
        self.db = None
        self.cursor = None
        try:
            self.db = mysql.connector.connect(host='localhost', database='data_baju',user='root',password='')
            if self.db.is_connected():
                # db_info = self.db.get_server_info()
                print("Berhasil Terhubung ")
                self.cursor = self.db.cursor()
        except MysqlError as error:
            print("Tidak bisa terhubung database ", error)

    def set_query(self, string_query, value = None):
        self.cursor.execute(string_query, value )
        return self

    def commit(self):
        self.db.commit()
        return self

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchall(self):
        return self.cursor.fetchall()

    def get_tablecolumn(self, tabel = ""):
        self.set_query("SELECT * FROM %s LIMIT 1;"%(tabel))
        self.fetchone()
        return [i[0] for i in self.cursor.description]

    def get_rowcount(self):
        return self.cursor.rowcount

    # def closeconn(self):
    #     if self.db.is_connected():
    #         self.commit.close()
    #         self.db.close()
    #         print("Koneksi ditutup")


# instance class database
# db = Database()
# val = ("182410102056", "Denta", "Teknologi Informasi")
# if ( db.set_query("INSERT INTO mahasiswa (nim, nama, prodi) VALUES (%s, %s, %s)", val)\
#         .execute()\
#         .get_rowcount() > 0 ):
#     print("Ada data yang ditambahkan")

# # tes tambah data : CRUD (Create)
db = Database()

# val = (nama, kuantitas, harga)
#
# query = db.set_query ("INSERT INTO `transaksi`(`nama barang`, `kuantitas`, `harga`) VALUES (%s,%s,%s)",val)
# query.commit()
# print(db.set_query().execute().get_rowcount())
# db.execute()
# db.get_rowcount()

# tes lihat semua data : CRUD (Read)
# query = db.set_query("select * from transaksi")
# hasil = query.fetchall()
# #
# # print(query.get_tablecolumn())
# for i in hasil:
#     print(i)
# print("Hasil :", hasil)
# print(db.get_tablecolumn(tabel="transaksi"))

# query = db.set_query("select * from `transaksi`")
# hasil = query.fetchall()
# print(hasil)
# for i in range (len(hasil)):
#     for j in range(len(hasil[i])):
#         field = hasil[i][j]
#         print(field)

# id = 5
# query = db.set_query("DELETE FROM `transaksi` WHERE id = '%s'" % (id))
# #
# if (query.commit()):
#     print('didelete')
# else:
#     print('gagal')

id = (2)
nama = str("nama")
kuantitas = int(12)
hrg = int(10)
value = (nama, kuantitas, hrg, id)
query = db.set_query("UPDATE `transaksi` SET `nama barang`=%s,`kuantitas`=%s,`harga`=%s WHERE id = '%s'" % (value))
up = input("update?")
if up == "y":
    if (query.commit()):
        print("Berhasil")