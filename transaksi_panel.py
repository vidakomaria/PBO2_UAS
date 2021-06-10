import wx
import wxFrame
import database

class panelTransaksi (wxFrame.wxTransaksiPanel):
    def __init__(self, parent):
        wxFrame.wxTransaksiPanel.__init__(self, parent)
        self.conn = database.Database()
