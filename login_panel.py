import wx
import wxFrame
import database
import panel

class panelLogin (wxFrame.wxLoginPanel):
    def __init__(self, parent):
        wxFrame.wxLoginPanel.__init__(self, parent)
        self.conn = database.Database()

    def btnLoginOnButtonClick(self, event):
        # idPegawai = self.textCtrlIdPeg.GetValue()
        # password = self.textCtrlPassword.GetValue()
        # query = self.conn.set_query("SELECT * FROM admin WHERE id_pegawai = '%s'" % (idPegawai))
        # result = query.fetchone()
        # if (result is not None):
        #     if result[3]== password:
        #         wx.MessageBox("Login Berhasil")
        #         self.textCtrlPassword.SetValue('')
        #         panel.Init.login.Hide()
        #         panel.Init.transaksi.Show()
        #     else:
        #         self.textCtrlPassword.SetValue('')
        #         wx.MessageBox("Password Salah", "Warning", wx.OK | wx.ICON_ERROR)
        # else:
        #     wx.MessageBox("ID Pegawai tidak ditemukan", "Warning" , wx.OK| wx.ICON_ERROR)

        panel.Init.login.Hide()
        panel.Init.transaksi.Show()
