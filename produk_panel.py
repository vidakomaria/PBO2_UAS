import wx
import wxFrame
import database
import panel

class PanelProduk(wxFrame.wxProdukPanel):
    def __init__(self, parent):
        wxFrame.wxProdukPanel.__init__(self, parent)
        self.conn = database.Database()
        self.showOnTabel()

    def showOnTabel(self):
        query = self.conn.set_query("SELECT * FROM `produk`")
        hasil = query.fetchall()
        print(hasil)
        rowCount = self.conn.get_rowcount()

        self.tabelProduk.DeleteRows(0, rowCount)
        self.tabelProduk.AppendRows(len(hasil))

        for i in range (len(hasil)):
            for j in range(len(hasil[i])):
                field = str(hasil[i][j])
                self.tabelProduk.SetCellValue(i, j, field)

        self.tabelProduk.AutoSize()

    def btnDelOnButtonClick( self, event ):
        id = self.textCtrlIdProduk.GetValue()
        query = self.conn.set_query("DELETE FROM `produk` WHERE id = '%s'" % (id))

        if wx.MessageBox("Delete Produk?", "Confirm", wx.YES_NO | wx.NO_DEFAULT, self) == wx.YES:
            if (query.commit()):
                wx.MessageBox("Berhasil")

    def btnUpdateOnButtonClick( self, event ):
        id = self.textCtrlIdProduk.GetValue()
        nama = self.textCtrlNamaProduk.GetValue()
        merk = self.textCtrlMerk.GetValue()
        hrg = self.textCtrlHrg.GetValue()
        stok = self.textCtrlStok.GetValue()
        value = (nama, merk, hrg, stok, id)
        query = self.conn.set_query("UPDATE `produk` SET `nama barang`='%s',`merk`=%s,`harga`=%s,`stok`=%s WHERE id = '%s'" % (value))
        if wx.MessageBox("Update Produk?", "Confirm", wx.YES_NO | wx.NO_DEFAULT, self) == wx.YES:
            if (query.commit()):
                wx.MessageBox("Berhasil")

    def btnRefreshOnButtonClick( self, event ):
        self.showOnTabel()

    def btnEditOnButtonClick( self, event ):
        self.enableTextCtrl(enable=True)

    def showOnTextControl(self, row):
        id = self.tabelProduk.GetCellValue(row,0)
        namaBrg = self.tabelProduk.GetCellValue(row,1)
        merk = self.tabelProduk.GetCellValue(row,2)
        hrg = self.tabelProduk.GetCellValue(row,3)
        stok = self.tabelProduk.GetCellValue(row,4)

        self.textCtrlIdProduk.SetValue(id)
        self.textCtrlNamaProduk.SetValue(namaBrg)
        self.textCtrlMerk.SetValue(merk)
        self.textCtrlHrg.SetValue(hrg)
        self.textCtrlStok.SetValue(stok)

        self.enableTextCtrl(enable=False)

    def clearText(self):
        self.textCtrlNamaProduk.SetValue('')
        self.textCtrlMerk.SetValue('')
        self.textCtrlHrg.SetValue('')
        self.textCtrlStok.SetValue('')

    def tabelTransaksiOnGridCmdSelectCell( self, event ):
        row = event.GetRow()
        self.showOnTextControl(row)

    def enableTextCtrl(self, enable=None):
        if enable is True:
            self.textCtrlIdProduk.Disable()
            self.textCtrlNamaProduk.Enable()
            self.textCtrlMerk.Enable()
            self.textCtrlHrg.Enable()
            self.textCtrlStok.Enable()
        else:
            self.textCtrlIdProduk.Disable()
            self.textCtrlNamaProduk.Disable()
            self.textCtrlMerk.Disable()
            self.textCtrlHrg.Disable()
            self.textCtrlStok.Disable()

    #menu
    def btnTransaksiOnButtonClick( self, event ):
        panel.Init.produk.Hide()
        panel.Init.transaksi.Show()

    def btnLogoutOnButtonClick( self, event ):
        panel.Init.produk.Hide()
        panel.Init.login.Show()

    def btnAddOnButtonClick( self, event ):
        panel.Init.produk.Hide()
        panel.Init.addProduk.Show()

