import login_panel
import produk_panel
import transaksi_panel
import add_transaksi_panel
import add_produk_panel

class Init:
    login = login_panel.panelLogin
    transaksi = transaksi_panel.panelTransaksi
    produk = produk_panel.PanelProduk
    addTransaksi = add_transaksi_panel.panelAddTransaksi
    addProduk = add_produk_panel.panelAddProduk

    @staticmethod
    def base (parent):
        Init.login = login_panel.panelLogin(parent)
        Init.transaksi = transaksi_panel.panelTransaksi(parent)
        Init.produk = produk_panel.PanelProduk(parent)
        Init.addTransaksi = add_transaksi_panel.panelAddTransaksi(parent)
        Init.addProduk = add_produk_panel.panelAddProduk(parent)
        Init.initPanel()

    @staticmethod
    def initPanel():
        Init.login.Hide()
        Init.transaksi.Hide()
        Init.produk.Hide()
        Init.addTransaksi.Hide()
        Init.addProduk.Hide()