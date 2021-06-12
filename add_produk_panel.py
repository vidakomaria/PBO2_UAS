import wx
import database
import panel
import wxFrame

class panelAddProduk(wxFrame.wxAddProdukPanel):
    def __init__(self, parent):
        wxFrame.wxAddProdukPanel.__init__(self, parent)
        self.conn = database.Database()

    def btnAddOnButtonClick( self, event ):
        nama = self.textCtrlNamaBrg.GetValue()
        merk = self.textCtrlMerk.GetValue()
        hrg = self.textCtrlHrg.GetValue()
        stok = self.textCtrlStok.GetValue()
        value = (nama, merk, hrg, stok)
        query = self.conn.set_query ("INSERT INTO `produk`(`nama barang`, `merk`, `harga`, `stok`) VALUES (%s,%s,%s,%s)",value)

        if (query.commit().get_rowcount() > 0):
            wx.MessageBox("Data Transaksi berhasil ditambahkan")
            self.clearText()
        else:
            wx.MessageBox("Data Transaksi gagal Ditambah", "Gagal" | wx.ICON_ERROR)

    def clearText(self):
        self.textCtrlNamaProduk.SetValue('')
        self.textCtrlMerk.SetValue('')
        self.textCtrlHrg.SetValue('')
        self.textCtrlStok.SetValue('')

    def btnTransaksiOnButtonClick( self, event ):
        panel.Init.addProduk.Hide()
        panel.Init.transaksi.Show()

    def btnProdukOnButtonClick( self, event ):
        panel.Init.addProduk.Hide()
        panel.Init.produk.Show()

    def btnLogoutOnButtonClick( self, event ):
        panel.Init.addProduk.Hide()
        panel.Init.login.Show()
