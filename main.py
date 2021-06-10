import wx
import wxFrame
import panel

class Frame (wxFrame.Frame):
    def __init__(self, parent):
        wxFrame.Frame.__init__(self, parent)
        panel.Init.base(self)
        panel.Init.login.Show()

    def FrameOnSize( self, event ):
        panel.Init.login.SetSize(self.GetSize())
        panel.Init.transaksi.SetSize(self.GetSize())


app = wx.App()
frame = Frame(parent=None)
frame.Show()
app.MainLoop()