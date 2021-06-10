import wx
import WX.wx as frame
import login_panel as pLogin

class Init:
    login = pLogin.PanelLogin
    @staticmethod
    def base (parent):
        Init.login = pLogin.PanelLogin(parent)
        Init.initPanel()

    @staticmethod
    def initPanel():
        Init.login.Hide()

class Frame (frame.Frame):
    def __init__(self, parent):
        frame.Frame.__init__(self, parent)
        Init.base(self)
        Init.login.Show()


app = wx.App()
frame = Frame(parent=None)
frame.Show()
app.MainLoop()