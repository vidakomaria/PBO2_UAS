import wx
import database
import wxFrame
import panel


class panelAddTransaksi(wxFrame.wxAddTransaksiPanel):
    def __init__(self, parent):
        wxFrame.wxAddTransaksiPanel.__init__(self, parent)
        self.conn = database.Database()

    def btnAddOnButtonClick( self, event ):
        tgl = self.textCtrlTgl.GetValue()
        idBrg = self.textCtrlIdBrg.GetValue()
        nama = self.textCtrlNamaBrg.GetValue()
        kuantitas = self.textCtrlKuantitas.GetValue()
        hrg = self.textCtrlHrg.GetValue()
        ket = self.textCtrlKet.GetValue()
        value = (tgl, idBrg, nama, kuantitas, hrg, ket)
        query = self.conn.set_query ("INSERT INTO `transaksi`(`tanggal`, `idBrg`, `nama barang`, `kuantitas`, `harga`, `keterangan`) VALUES (%s,%s,%s,%s,%s,%s)",value)

        if (query.commit()):
            wx.MessageBox("Data Transaksi berhasil ditambahkan")
            self.clearText()
        else:
            wx.MessageBox("Data Transaksi gagal Ditambah", "Gagal" | wx.ICON_ERROR)

    def clearText(self):
        self.textCtrlIdBrg.SetValue('')
        self.textCtrlNamaBrg.SetValue('')
        self.textCtrlHrg.SetValue('')
        self.textCtrlKuantitas.SetValue('')
        self.textCtrlKet.SetValue('')

    def btnProdukOnButtonClick( self, event ):
        panel.Init.addTransaksi.Hide()
        panel.Init.produk.Show()

    def btnLogoutOnButtonClick( self, event ):
        panel.Init.addTransaksi.Hide()
        panel.Init.login.Show()

    def btnTransaksiOnButtonClick( self, event ):
        panel.Init.addTransaksi.Hide()
        panel.Init.transaksi.Show()
