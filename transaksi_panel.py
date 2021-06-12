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
        query = self.conn.set_query("SELECT * FROM `transaksi`")
        hasil = query.fetchall()
        rowCount = self.conn.get_rowcount()

        self.tabelTransaksi.DeleteRows(0, rowCount)
        self.tabelTransaksi.AppendRows(len(hasil))

        for i in range (len(hasil)):
            for j in range(len(hasil[i])):
                field = str(hasil[i][j])
                self.tabelTransaksi.SetCellValue(i, j, field)

        self.tabelTransaksi.AutoSize()

    def btnDelOnButtonClick( self, event ):
        id = self.textCtrlId.GetValue()
        query = self.conn.set_query("DELETE FROM `transaksi` WHERE idTransaksi = '%s'" % (id))

        if wx.MessageBox("Delete Transaksi?", "Confirm", wx.YES_NO | wx.NO_DEFAULT, self) == wx.YES:
            if (query.commit()):
                wx.MessageBox("Berhasil")

    def btnUpdateOnButtonClick( self, event ):
        id = self.textCtrlId.GetValue()
        tgl = self.textCtrlTgl.GetValue()
        idBrg = self.textCtrlIdBrg.GetValue()
        nama = self.textCtrlNamaBrg.GetValue()
        kuantitas = self.textCtrlKuantitas.GetValue()
        hrg = self.textCtrlHrg.GetValue()
        ket = self.textCtrlKet.GetValue()
        value = (tgl, idBrg, nama, kuantitas, hrg, ket, id)
        query = self.conn.set_query("UPDATE `transaksi` SET `tanggal`=%s,`idBrg`=%s,`nama barang`='%s',`kuantitas`=%s,`harga`=%s,`keterangan`='%s' WHERE idTransaksi = '%s'" % (value))
        if wx.MessageBox("Update Transaksi?", "Confirm", wx.YES_NO | wx.NO_DEFAULT, self) == wx.YES:
            if (query.commit()):
                wx.MessageBox("Berhasil")

    def btnRefreshOnButtonClick( self, event ):
        self.showOnTabel()

    def btnEditOnButtonClick( self, event ):
        self.enableTextCtrl(enable=True)

    def showOnTextControl(self, row):
        id = self.tabelTransaksi.GetCellValue(row,0)
        tgl = self.tabelTransaksi.GetCellValue(row,1)
        idBrg = self.tabelTransaksi.GetCellValue(row,2)
        namaBrg = self.tabelTransaksi.GetCellValue(row,3)
        kuantitas = self.tabelTransaksi.GetCellValue(row,4)
        hrg = self.tabelTransaksi.GetCellValue(row,5)
        ket = self.tabelTransaksi.GetCellValue(row,6)

        self.textCtrlId.SetValue(id)
        self.textCtrlTgl.SetValue(tgl)
        self.textCtrlIdBrg.SetValue(idBrg)
        self.textCtrlNamaBrg.SetValue(namaBrg)
        self.textCtrlKuantitas.SetValue(kuantitas)
        self.textCtrlHrg.SetValue(hrg)
        self.textCtrlKet.SetValue(ket)

        self.enableTextCtrl(enable=False)

    def clearText(self):
        self.textCtrlIdBrg.SetValue('')
        self.textCtrlNamaBrg.SetValue('')
        self.textCtrlHrg.SetValue('')
        self.textCtrlKuantitas.SetValue('')
        self.textCtrlKet.SetValue('')

    def tabelTransaksiOnGridCmdSelectCell( self, event ):
        row = event.GetRow()
        self.showOnTextControl(row)

    def enableTextCtrl(self, enable=None):
        if enable is True:
            self.textCtrlId.Disable()
            self.textCtrlTgl.Enable()
            self.textCtrlIdBrg.Enable()
            self.textCtrlNamaBrg.Enable()
            self.textCtrlKuantitas.Enable()
            self.textCtrlHrg.Enable()
            self.textCtrlKet.Enable()
        else:
            self.textCtrlId.Disable()
            self.textCtrlTgl.Disable()
            self.textCtrlIdBrg.Disable()
            self.textCtrlNamaBrg.Disable()
            self.textCtrlKuantitas.Disable()
            self.textCtrlHrg.Disable()
            self.textCtrlKet.Disable()

    #menu

    def btnProdukOnButtonClick( self, event ):
        panel.Init.transaksi.Hide()
        panel.Init.produk.Show()

    def btnLogoutOnButtonClick( self, event ):
        panel.Init.transaksi.Hide()
        panel.Init.login.Show()

    def btnAddOnButtonClick( self, event ):
        panel.Init.transaksi.Hide()
        panel.Init.addTransaksi.Show()



