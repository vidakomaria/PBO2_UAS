import wx
import WX.wx as frame
import database.database as database

class PanelLogin (frame.wxLoginPanel):
    def __init__(self, parent):
        frame.wxLoginPanel.__init__(self, parent)
        self.conn = database.Database()

    def btnLoginOnButtonClick(self, event):
        idPegawai = self.textCtrlIdPeg.GetValue()
        password = self.textCtrlPassword.GetValue()
        nama = "kasir1"
        query = self.conn.set_query("SELECT * FROM admin WHERE id_pegawai = '%s'" % (idPegawai))
        result = query.fetchone()
        if (result is not None):
            print(result)
            if result[3]== password:
                wx.MessageBox("Login Berhasil")
                print("login")
            else:
                self.textCtrlPassword.SetValue('')
