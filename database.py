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
                # print("Berhasil Terhubung ")
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

    def closeconn(self):
        if self.db.is_connected():
            self.commit.close()
            self.db.close()
            print("Koneksi ditutup")


# instance class database
# db = Database()
# val = ("182410102056", "Denta", "Teknologi Informasi")
# if ( db.set_query("INSERT INTO mahasiswa (nim, nama, prodi) VALUES (%s, %s, %s)", val)\
#         .execute()\
#         .get_rowcount() > 0 ):
#     print("Ada data yang ditambahkan")


#
# tes lihat semua data : CRUD (Read)
# db.set_query(string_query="select * from admin")
# print(db.get_tablecolumn())
# print("Hasil :", db.fetchall())
#
# # tes tambah data : CRUD (Create)
db = Database()

# val = (nama, kuantitas, harga)
#
# query = db.set_query ("INSERT INTO `transaksi`(`nama barang`, `kuantitas`, `harga`) VALUES (%s,%s,%s)",val)
# query.commit()
# print(db.set_query().execute().get_rowcount())
# db.execute()
# db.get_rowcount()

