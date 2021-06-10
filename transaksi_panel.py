import wx
import wxFrame
import database

class panelTransaksi (wxFrame.wxTransaksiPanel):
    def __init__(self, parent):
        wxFrame.wxTransaksiPanel.__init__(self, parent)
        self.conn = database.Database()

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
