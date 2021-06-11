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

    def btnTmbhOnButtonClick( self, event ):
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

    def btnDeleteOnButtonClick( self, event ):
        id = self.textCtrlIdUpdate.GetValue()
        query = self.conn.set_query("DELETE FROM `transaksi` WHERE id = '%s'" % (id))

        if wx.MessageBox("Delete Transaksi?", "Confirm", wx.YES_NO | wx.NO_DEFAULT, self) == wx.YES:
            if (query.commit()):
                wx.MessageBox("Berhasil")

    def btnUpdateOnButtonClick( self, event ):
        id = self.textCtrlIdUpdate.GetValue()
        nama = self.textCtrlNamaBrgUpdate.GetValue()
        kuantitas = self.textCtrlKuantitasUpdate.GetValue()
        hrg = self.textCtrlHrgUpdate.GetValue()
        value = (nama, kuantitas, hrg, id)
        query = self.conn.set_query("UPDATE `transaksi` SET `nama barang` = %s, `kuantitas` = %s, `harga`= %s) WHERE id = '%s'" % (value))

        if wx.MessageBox("Delete Transaksi?", "Confirm", wx.YES_NO | wx.NO_DEFAULT, self) == wx.YES:
            if (query.commit()):
                wx.MessageBox("Berhasil")

    def btnRefreshOnButtonClick( self, event ):
        self.showOnTabel()

    def btnEditOnButtonClick( self, event ):
        self.enableTextCtrl(enable=True)

    def showOnTextControl(self, row):
        id = self.tabelTransaksi.GetCellValue(row,0)
        namaBrg = self.tabelTransaksi.GetCellValue(row,1)
        kuantitas = self.tabelTransaksi.GetCellValue(row,2)
        hrg = self.tabelTransaksi.GetCellValue(row,3)

        self.textCtrlIdUpdate.SetValue(id)
        self.textCtrlNamaBrgUpdate.SetValue(namaBrg)
        self.textCtrlKuantitasUpdate.SetValue(kuantitas)
        self.textCtrlHrgUpdate.SetValue(hrg)

        self.enableTextCtrl(enable=False)

    def clearText(self):
        self.textCtrlNamaBrgTrans.SetValue('')
        self.textCtrlHrgTrans.SetValue('')
        self.textCtrlKuantitasTrans.SetValue('')

    def tabelTransaksiOnGridCmdSelectCell( self, event ):
        row = event.GetRow()
        self.showOnTextControl(row)

    def enableTextCtrl(self, enable=None):
        if enable is True:
            self.textCtrlIdUpdate.Enable()
            self.textCtrlNamaBrgUpdate.Enable()
            self.textCtrlKuantitasUpdate.Enable()
            self.textCtrlHrgUpdate.Enable()
        else:
            self.textCtrlIdUpdate.Disable()
            self.textCtrlNamaBrgUpdate.Disable()
            self.textCtrlKuantitasUpdate.Disable()
            self.textCtrlHrgUpdate.Disable()

