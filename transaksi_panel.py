import wx
import wxFrame
import database
import panel

class panelTransaksi (wxFrame.wxTransaksiPanel):
    def __init__(self, parent):
        wxFrame.wxTransaksiPanel.__init__(self, parent)
        self.conn = database.Database()
        self.showOnTabel()

    def showOnTabel(self):
        print ('showontabel')
        query = self.conn.set_query("select * from `transaksi`")
        hasil = query.fetchall()
        print(hasil)
        rowCount = self.conn.get_rowcount()

        self.tabelTransaksi.DeleteRows(0, rowCount)
        self.tabelTransaksi.AppendRows(len(hasil))

        for i in range (len(hasil)):
            for j in range(len(hasil[i])):
                field = str(hasil[i][j])
                self.tabelTransaksi.SetCellValue(i, j, field)

        self.tabelTransaksi.AutoSize()

    def btnTmbhTransOnButtonClick( self, event ):
        nama = self.textCtrlNamaBrgTrans.GetValue()
        kuantitas = self.textCtrlKuantitasTrans.GetValue()
        hrg = self.textCtrlHrgTrans.GetValue()
        value = (nama, kuantitas, hrg)
        query = self.conn.set_query ("INSERT INTO `transaksi`(`nama barang`, `kuantitas`, `harga`) VALUES (%s,%s,%s)",value)

        if (query.commit().get_rowcount() > 0):
            wx.MessageBox("Data Transaksi berhasil ditambahkan")
            self.clearText()
        else:
            wx.MessageBox("Data Transaksi gagal Ditambah", "Gagal" | wx.ICON_ERROR)

    def clearText(self):
        self.textCtrlNamaBrgTrans.SetValue('')
        self.textCtrlHrgTrans.SetValue('')
        self.textCtrlKuantitasTrans.SetValue('')
