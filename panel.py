import login_panel
import transaksi_panel

class Init:
    login = login_panel.panelLogin
    transaksi = transaksi_panel.panelTransaksi
    @staticmethod
    def base (parent):
        Init.login = login_panel.panelLogin(parent)
        Init.transaksi = transaksi_panel.panelTransaksi(parent)
        Init.initPanel()

    @staticmethod
    def initPanel():
        Init.login.Hide()
        Init.transaksi.Hide()