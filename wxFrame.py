# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class Frame
###########################################################################

class Frame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 630,430 ), style = wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_SIZE, self.FrameOnSize )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def FrameOnSize( self, event ):
		event.Skip()


###########################################################################
## Class wxLoginPanel
###########################################################################

class wxLoginPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 630,430 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 144, 144, 144 ) )

		bSizer38 = wx.BoxSizer( wx.VERTICAL )

		bSizer27 = wx.BoxSizer( wx.VERTICAL )


		bSizer27.Add( ( 0, 0), 0, 0, 5 )


		bSizer38.Add( bSizer27, 1, wx.EXPAND, 5 )

		bSizer36 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"LOGIN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		self.m_staticText6.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Britannic Bold" ) )

		bSizer36.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer38.Add( bSizer36, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer31 = wx.BoxSizer( wx.VERTICAL )

		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText10 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"ID Pegawai", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_staticText10.Wrap( -1 )

		self.m_staticText10.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Times New Roman" ) )

		bSizer21.Add( self.m_staticText10, 0, wx.ALL, 6 )

		self.textCtrlIdPeg = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
		bSizer21.Add( self.textCtrlIdPeg, 0, 0, 5 )


		bSizer31.Add( bSizer21, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer23 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText8 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		self.m_staticText8.Wrap( -1 )

		self.m_staticText8.SetFont( wx.Font( 14, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Times New Roman" ) )

		bSizer23.Add( self.m_staticText8, 0, wx.ALL, 6 )

		self.textCtrlPassword = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), wx.TE_PASSWORD )
		bSizer23.Add( self.textCtrlPassword, 0, wx.ALL, 5 )


		bSizer31.Add( bSizer23, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel7.SetSizer( bSizer31 )
		self.m_panel7.Layout()
		bSizer31.Fit( self.m_panel7 )
		bSizer38.Add( self.m_panel7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer26 = wx.BoxSizer( wx.VERTICAL )

		self.btnLogin = wx.Button( self, wx.ID_ANY, u"LOGIN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnLogin.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Barlow" ) )
		self.btnLogin.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.btnLogin.SetBackgroundColour( wx.Colour( 0, 103, 206 ) )

		bSizer26.Add( self.btnLogin, 0, wx.TOP|wx.BOTTOM|wx.RIGHT|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer38.Add( bSizer26, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer28 = wx.BoxSizer( wx.VERTICAL )


		bSizer28.Add( ( 0, 0), 0, 0, 5 )


		bSizer38.Add( bSizer28, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer38 )
		self.Layout()

		# Connect Events
		self.btnLogin.Bind( wx.EVT_BUTTON, self.btnLoginOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnLoginOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class wxTransaksiPanel
###########################################################################

class wxTransaksiPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 630,430 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		self.SetMaxSize( wx.Size( 900,600 ) )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Transaksi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Barlow SemiBold" ) )

		bSizer30.Add( self.m_staticText31, 0, 0, 5 )


		bSizer14.Add( bSizer30, 1, wx.ALIGN_CENTER_VERTICAL, 5 )

		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button37 = wx.Button( self, wx.ID_ANY, u"Transaksi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button37.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Barlow Medium" ) )

		bSizer41.Add( self.m_button37, 0, wx.ALL, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Produk", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button6.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Barlow Medium" ) )

		bSizer41.Add( self.m_button6, 0, wx.ALL, 5 )

		self.m_button9 = wx.Button( self, wx.ID_ANY, u"Logout", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button9.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Barlow Medium" ) )
		self.m_button9.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button9.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )

		bSizer41.Add( self.m_button9, 0, wx.ALL, 5 )


		bSizer14.Add( bSizer41, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer13.Add( bSizer14, 0, wx.EXPAND, 5 )

		self.m_panel13 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel13.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		bSizer36 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText24 = wx.StaticText( self.m_panel13, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		bSizer36.Add( self.m_staticText24, 0, wx.ALL, 5 )


		self.m_panel13.SetSizer( bSizer36 )
		self.m_panel13.Layout()
		bSizer36.Fit( self.m_panel13 )
		bSizer13.Add( self.m_panel13, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel10 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer74 = wx.BoxSizer( wx.VERTICAL )

		self.m_button12 = wx.Button( self.m_panel10, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button12.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Barlow Medium" ) )
		self.m_button12.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button12.SetBackgroundColour( wx.Colour( 0, 103, 206 ) )

		bSizer74.Add( self.m_button12, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.m_panel10.SetSizer( bSizer74 )
		self.m_panel10.Layout()
		bSizer74.Fit( self.m_panel10 )
		bSizer20.Add( self.m_panel10, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		bSizer38 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel11 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer62 = wx.BoxSizer( wx.VERTICAL )

		bSizer77 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText63 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"Id Transaksi", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText63.Wrap( -1 )

		self.m_staticText63.SetFont( wx.Font( 11, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Times New Roman" ) )

		bSizer77.Add( self.m_staticText63, 0, wx.ALL, 5 )

		self.textCtrlId = wx.TextCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer77.Add( self.textCtrlId, 0, wx.ALL, 5 )


		bSizer62.Add( bSizer77, 0, 0, 5 )

		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText64 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"Tanggal", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText64.Wrap( -1 )

		self.m_staticText64.SetFont( wx.Font( 11, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Times New Roman" ) )

		bSizer32.Add( self.m_staticText64, 0, wx.ALL, 5 )

		self.textCtrlTgl = wx.TextCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer32.Add( self.textCtrlTgl, 0, wx.ALL, 5 )


		bSizer62.Add( bSizer32, 0, 0, 5 )

		bSizer33 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText66 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"Id Barang", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText66.Wrap( -1 )

		self.m_staticText66.SetFont( wx.Font( 11, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Times New Roman" ) )

		bSizer33.Add( self.m_staticText66, 0, wx.ALL, 5 )

		self.textCtrlIdBrg = wx.TextCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer33.Add( self.textCtrlIdBrg, 0, wx.ALL, 5 )


		bSizer62.Add( bSizer33, 0, 0, 5 )

		bSizer34 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText281 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"Nama Barang", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText281.Wrap( -1 )

		self.m_staticText281.SetFont( wx.Font( 11, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Times New Roman" ) )

		bSizer34.Add( self.m_staticText281, 0, wx.ALL, 5 )

		self.textCtrlNamaBrg = wx.TextCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer34.Add( self.textCtrlNamaBrg, 0, wx.ALL, 5 )


		bSizer62.Add( bSizer34, 0, 0, 5 )

		bSizer35 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText291 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"Kuantitas", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText291.Wrap( -1 )

		self.m_staticText291.SetFont( wx.Font( 11, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Times New Roman" ) )

		bSizer35.Add( self.m_staticText291, 0, wx.ALL, 5 )

		self.textCtrlKuantitas = wx.TextCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer35.Add( self.textCtrlKuantitas, 0, wx.ALL, 5 )


		bSizer62.Add( bSizer35, 0, 0, 5 )

		bSizer361 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText301 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"Harga", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText301.Wrap( -1 )

		self.m_staticText301.SetFont( wx.Font( 11, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Times New Roman" ) )

		bSizer361.Add( self.m_staticText301, 0, wx.ALL, 5 )

		self.textCtrlHrg = wx.TextCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer361.Add( self.textCtrlHrg, 0, wx.ALL, 5 )


		bSizer62.Add( bSizer361, 0, 0, 5 )

		bSizer37 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText65 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"Keterangan", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText65.Wrap( -1 )

		self.m_staticText65.SetFont( wx.Font( 11, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Times New Roman" ) )

		bSizer37.Add( self.m_staticText65, 0, wx.ALL, 5 )

		self.textCtrlKet = wx.TextCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer37.Add( self.textCtrlKet, 0, wx.ALL, 5 )


		bSizer62.Add( bSizer37, 0, 0, 5 )

		bSizer76 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button34 = wx.Button( self.m_panel11, wx.ID_ANY, u"Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button34.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Barlow Medium" ) )

		bSizer76.Add( self.m_button34, 0, wx.ALL, 5 )

		self.m_button35 = wx.Button( self.m_panel11, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button35.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Barlow Medium" ) )

		bSizer76.Add( self.m_button35, 0, wx.ALL, 5 )


		bSizer62.Add( bSizer76, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel11.SetSizer( bSizer62 )
		self.m_panel11.Layout()
		bSizer62.Fit( self.m_panel11 )
		bSizer38.Add( self.m_panel11, 0, wx.ALL, 5 )

		self.m_panel12 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer64 = wx.BoxSizer( wx.VERTICAL )

		bSizer66 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button24 = wx.Button( self.m_panel12, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer66.Add( self.m_button24, 0, wx.ALL, 5 )

		self.m_button23 = wx.Button( self.m_panel12, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer66.Add( self.m_button23, 0, wx.ALL, 5 )


		bSizer64.Add( bSizer66, 0, wx.ALIGN_RIGHT, 5 )

		self.tabelTransaksi = wx.grid.Grid( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.tabelTransaksi.CreateGrid( 1, 7 )
		self.tabelTransaksi.EnableEditing( True )
		self.tabelTransaksi.EnableGridLines( True )
		self.tabelTransaksi.EnableDragGridSize( False )
		self.tabelTransaksi.SetMargins( 0, 0 )

		# Columns
		self.tabelTransaksi.AutoSizeColumns()
		self.tabelTransaksi.EnableDragColMove( False )
		self.tabelTransaksi.EnableDragColSize( True )
		self.tabelTransaksi.SetColLabelSize( 30 )
		self.tabelTransaksi.SetColLabelValue( 0, u"Id Transaksi" )
		self.tabelTransaksi.SetColLabelValue( 1, u"Tanggal" )
		self.tabelTransaksi.SetColLabelValue( 2, u"Id Barang" )
		self.tabelTransaksi.SetColLabelValue( 3, u"Nama Barang" )
		self.tabelTransaksi.SetColLabelValue( 4, u"Kuantitas" )
		self.tabelTransaksi.SetColLabelValue( 5, u"Harga" )
		self.tabelTransaksi.SetColLabelValue( 6, u"Ket" )
		self.tabelTransaksi.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabelTransaksi.AutoSizeRows()
		self.tabelTransaksi.EnableDragRowSize( True )
		self.tabelTransaksi.SetRowLabelSize( 30 )
		self.tabelTransaksi.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tabelTransaksi.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.tabelTransaksi.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Times New Roman" ) )

		bSizer64.Add( self.tabelTransaksi, 0, wx.ALL, 5 )


		self.m_panel12.SetSizer( bSizer64 )
		self.m_panel12.Layout()
		bSizer64.Fit( self.m_panel12 )
		bSizer38.Add( self.m_panel12, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer20.Add( bSizer38, 1, wx.EXPAND, 5 )


		bSizer13.Add( bSizer20, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer13 )
		self.Layout()

		# Connect Events
		self.m_button37.Bind( wx.EVT_BUTTON, self.btnTransaksiOnButtonClick )
		self.m_button6.Bind( wx.EVT_BUTTON, self.btnProdukOnButtonClick )
		self.m_button9.Bind( wx.EVT_BUTTON, self.btnLogoutOnButtonClick )
		self.m_button12.Bind( wx.EVT_BUTTON, self.btnAddOnButtonClick )
		self.m_button34.Bind( wx.EVT_BUTTON, self.btnUpdateOnButtonClick )
		self.m_button35.Bind( wx.EVT_BUTTON, self.btnDelOnButtonClick )
		self.m_button24.Bind( wx.EVT_BUTTON, self.btnEditOnButtonClick )
		self.m_button23.Bind( wx.EVT_BUTTON, self.btnRefreshOnButtonClick )
		self.tabelTransaksi.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.tabelTransaksiOnGridCmdSelectCell )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnTransaksiOnButtonClick( self, event ):
		event.Skip()

	def btnProdukOnButtonClick( self, event ):
		event.Skip()

	def btnLogoutOnButtonClick( self, event ):
		event.Skip()

	def btnAddOnButtonClick( self, event ):
		event.Skip()

	def btnUpdateOnButtonClick( self, event ):
		event.Skip()

	def btnDelOnButtonClick( self, event ):
		event.Skip()

	def btnEditOnButtonClick( self, event ):
		event.Skip()

	def btnRefreshOnButtonClick( self, event ):
		event.Skip()

	def tabelTransaksiOnGridCmdSelectCell( self, event ):
		event.Skip()


###########################################################################
## Class wxAddTransaksiPanel
###########################################################################

class wxAddTransaksiPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 630,430 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		self.SetMaxSize( wx.Size( 900,600 ) )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Transaksi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Barlow SemiBold" ) )

		bSizer30.Add( self.m_staticText31, 0, 0, 5 )


		bSizer14.Add( bSizer30, 1, wx.ALIGN_CENTER_VERTICAL, 5 )

		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button37 = wx.Button( self, wx.ID_ANY, u"Transaksi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button37.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Barlow Medium" ) )

		bSizer41.Add( self.m_button37, 0, wx.ALL, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Produk", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button6.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Barlow Medium" ) )

		bSizer41.Add( self.m_button6, 0, wx.ALL, 5 )

		self.m_button9 = wx.Button( self, wx.ID_ANY, u"Logout", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button9.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Barlow Medium" ) )
		self.m_button9.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button9.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )

		bSizer41.Add( self.m_button9, 0, wx.ALL, 5 )


		bSizer14.Add( bSizer41, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer13.Add( bSizer14, 0, wx.EXPAND, 5 )

		self.m_panel13 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel13.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		bSizer36 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText24 = wx.StaticText( self.m_panel13, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		bSizer36.Add( self.m_staticText24, 0, wx.ALL, 5 )


		self.m_panel13.SetSizer( bSizer36 )
		self.m_panel13.Layout()
		bSizer36.Fit( self.m_panel13 )
		bSizer13.Add( self.m_panel13, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer62 = wx.BoxSizer( wx.VERTICAL )

		bSizer32 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText64 = wx.StaticText( self, wx.ID_ANY, u"Tanggal", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText64.Wrap( -1 )

		self.m_staticText64.SetFont( wx.Font( 11, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Times New Roman" ) )

		bSizer32.Add( self.m_staticText64, 0, wx.ALL, 5 )

		self.textCtrlTgl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer32.Add( self.textCtrlTgl, 0, wx.ALL, 5 )


		bSizer62.Add( bSizer32, 0, 0, 5 )

		bSizer33 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText66 = wx.StaticText( self, wx.ID_ANY, u"Id Barang", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText66.Wrap( -1 )

		self.m_staticText66.SetFont( wx.Font( 11, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Times New Roman" ) )

		bSizer33.Add( self.m_staticText66, 0, wx.ALL, 5 )

		self.textCtrlIdBrg = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer33.Add( self.textCtrlIdBrg, 0, wx.ALL, 5 )


		bSizer62.Add( bSizer33, 0, 0, 5 )

		bSizer34 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText281 = wx.StaticText( self, wx.ID_ANY, u"Nama Barang", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText281.Wrap( -1 )

		self.m_staticText281.SetFont( wx.Font( 11, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Times New Roman" ) )

		bSizer34.Add( self.m_staticText281, 0, wx.ALL, 5 )

		self.textCtrlNamaBrg = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer34.Add( self.textCtrlNamaBrg, 0, wx.ALL, 5 )


		bSizer62.Add( bSizer34, 0, 0, 5 )

		bSizer35 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText291 = wx.StaticText( self, wx.ID_ANY, u"Kuantitas", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText291.Wrap( -1 )

		self.m_staticText291.SetFont( wx.Font( 11, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Times New Roman" ) )

		bSizer35.Add( self.m_staticText291, 0, wx.ALL, 5 )

		self.textCtrlKuantitas = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer35.Add( self.textCtrlKuantitas, 0, wx.ALL, 5 )


		bSizer62.Add( bSizer35, 0, 0, 5 )

		bSizer361 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText301 = wx.StaticText( self, wx.ID_ANY, u"Harga", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText301.Wrap( -1 )

		self.m_staticText301.SetFont( wx.Font( 11, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Times New Roman" ) )

		bSizer361.Add( self.m_staticText301, 0, wx.ALL, 5 )

		self.textCtrlHrg = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer361.Add( self.textCtrlHrg, 0, wx.ALL, 5 )


		bSizer62.Add( bSizer361, 0, 0, 5 )

		bSizer37 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText65 = wx.StaticText( self, wx.ID_ANY, u"Keterangan", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText65.Wrap( -1 )

		self.m_staticText65.SetFont( wx.Font( 11, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Times New Roman" ) )

		bSizer37.Add( self.m_staticText65, 0, wx.ALL, 5 )

		self.textCtrlKet = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer37.Add( self.textCtrlKet, 0, wx.ALL, 5 )


		bSizer62.Add( bSizer37, 0, 0, 5 )


		bSizer13.Add( bSizer62, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer74 = wx.BoxSizer( wx.VERTICAL )

		self.m_button12 = wx.Button( self, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button12.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Barlow Medium" ) )
		self.m_button12.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button12.SetBackgroundColour( wx.Colour( 0, 103, 206 ) )

		bSizer74.Add( self.m_button12, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer13.Add( bSizer74, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer13 )
		self.Layout()

		# Connect Events
		self.m_button37.Bind( wx.EVT_BUTTON, self.btnTransaksiOnButtonClick )
		self.m_button6.Bind( wx.EVT_BUTTON, self.btnProdukOnButtonClick )
		self.m_button9.Bind( wx.EVT_BUTTON, self.btnLogoutOnButtonClick )
		self.m_button12.Bind( wx.EVT_BUTTON, self.btnAddOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnTransaksiOnButtonClick( self, event ):
		event.Skip()

	def btnProdukOnButtonClick( self, event ):
		event.Skip()

	def btnLogoutOnButtonClick( self, event ):
		event.Skip()

	def btnAddOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class wxProdukPanel
###########################################################################

class wxProdukPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 630,430 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		self.SetMaxSize( wx.Size( 900,600 ) )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Produk", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Barlow SemiBold" ) )

		bSizer30.Add( self.m_staticText31, 0, 0, 5 )


		bSizer14.Add( bSizer30, 1, wx.ALIGN_CENTER_VERTICAL, 5 )

		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button37 = wx.Button( self, wx.ID_ANY, u"Transaksi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button37.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Barlow Medium" ) )

		bSizer41.Add( self.m_button37, 0, wx.ALL, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Produk", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button6.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Barlow Medium" ) )

		bSizer41.Add( self.m_button6, 0, wx.ALL, 5 )

		self.m_button9 = wx.Button( self, wx.ID_ANY, u"Logout", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button9.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Barlow Medium" ) )
		self.m_button9.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button9.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )

		bSizer41.Add( self.m_button9, 0, wx.ALL, 5 )


		bSizer14.Add( bSizer41, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer13.Add( bSizer14, 0, wx.EXPAND, 5 )

		self.m_panel13 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel13.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		bSizer36 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText24 = wx.StaticText( self.m_panel13, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		bSizer36.Add( self.m_staticText24, 0, wx.ALL, 5 )


		self.m_panel13.SetSizer( bSizer36 )
		self.m_panel13.Layout()
		bSizer36.Fit( self.m_panel13 )
		bSizer13.Add( self.m_panel13, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel10 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer74 = wx.BoxSizer( wx.VERTICAL )

		self.m_button12 = wx.Button( self.m_panel10, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button12.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Barlow Medium" ) )
		self.m_button12.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button12.SetBackgroundColour( wx.Colour( 0, 103, 206 ) )

		bSizer74.Add( self.m_button12, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		self.m_panel10.SetSizer( bSizer74 )
		self.m_panel10.Layout()
		bSizer74.Fit( self.m_panel10 )
		bSizer20.Add( self.m_panel10, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		bSizer38 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel11 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer62 = wx.BoxSizer( wx.VERTICAL )

		bSizer77 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText63 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"Id Produk", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText63.Wrap( -1 )

		self.m_staticText63.SetFont( wx.Font( 11, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Times New Roman" ) )

		bSizer77.Add( self.m_staticText63, 0, wx.ALL, 5 )

		self.textCtrlIdProduk = wx.TextCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer77.Add( self.textCtrlIdProduk, 0, wx.ALL, 5 )


		bSizer62.Add( bSizer77, 0, 0, 5 )

		bSizer34 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText281 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"Nama Produk", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText281.Wrap( -1 )

		self.m_staticText281.SetFont( wx.Font( 11, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Times New Roman" ) )

		bSizer34.Add( self.m_staticText281, 0, wx.ALL, 5 )

		self.textCtrlNamaProduk = wx.TextCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer34.Add( self.textCtrlNamaProduk, 0, wx.ALL, 5 )


		bSizer62.Add( bSizer34, 0, 0, 5 )

		bSizer35 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText291 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"Merk", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText291.Wrap( -1 )

		self.m_staticText291.SetFont( wx.Font( 11, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Times New Roman" ) )

		bSizer35.Add( self.m_staticText291, 0, wx.ALL, 5 )

		self.textCtrlMerk = wx.TextCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer35.Add( self.textCtrlMerk, 0, wx.ALL, 5 )


		bSizer62.Add( bSizer35, 0, 0, 5 )

		bSizer361 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText301 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"Harga", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText301.Wrap( -1 )

		self.m_staticText301.SetFont( wx.Font( 11, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Times New Roman" ) )

		bSizer361.Add( self.m_staticText301, 0, wx.ALL, 5 )

		self.textCtrlHrg = wx.TextCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer361.Add( self.textCtrlHrg, 0, wx.ALL, 5 )


		bSizer62.Add( bSizer361, 0, 0, 5 )

		bSizer37 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText65 = wx.StaticText( self.m_panel11, wx.ID_ANY, u"Stok", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText65.Wrap( -1 )

		self.m_staticText65.SetFont( wx.Font( 11, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Times New Roman" ) )

		bSizer37.Add( self.m_staticText65, 0, wx.ALL, 5 )

		self.textCtrlStok = wx.TextCtrl( self.m_panel11, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer37.Add( self.textCtrlStok, 0, wx.ALL, 5 )


		bSizer62.Add( bSizer37, 0, 0, 5 )

		bSizer76 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button34 = wx.Button( self.m_panel11, wx.ID_ANY, u"Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button34.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Barlow Medium" ) )

		bSizer76.Add( self.m_button34, 0, wx.ALL, 5 )

		self.m_button35 = wx.Button( self.m_panel11, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button35.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Barlow Medium" ) )

		bSizer76.Add( self.m_button35, 0, wx.ALL, 5 )


		bSizer62.Add( bSizer76, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel11.SetSizer( bSizer62 )
		self.m_panel11.Layout()
		bSizer62.Fit( self.m_panel11 )
		bSizer38.Add( self.m_panel11, 0, wx.ALL, 5 )

		self.m_panel12 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer64 = wx.BoxSizer( wx.VERTICAL )

		bSizer66 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button24 = wx.Button( self.m_panel12, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer66.Add( self.m_button24, 0, wx.ALL, 5 )

		self.m_button23 = wx.Button( self.m_panel12, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer66.Add( self.m_button23, 0, wx.ALL, 5 )


		bSizer64.Add( bSizer66, 0, wx.ALIGN_RIGHT, 5 )

		self.tabelProduk = wx.grid.Grid( self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.tabelProduk.CreateGrid( 1, 5 )
		self.tabelProduk.EnableEditing( True )
		self.tabelProduk.EnableGridLines( True )
		self.tabelProduk.EnableDragGridSize( False )
		self.tabelProduk.SetMargins( 0, 0 )

		# Columns
		self.tabelProduk.AutoSizeColumns()
		self.tabelProduk.EnableDragColMove( False )
		self.tabelProduk.EnableDragColSize( True )
		self.tabelProduk.SetColLabelSize( 30 )
		self.tabelProduk.SetColLabelValue( 0, u"Id Produk" )
		self.tabelProduk.SetColLabelValue( 1, u"Nama Produk" )
		self.tabelProduk.SetColLabelValue( 2, u"Merk" )
		self.tabelProduk.SetColLabelValue( 3, u"Harga" )
		self.tabelProduk.SetColLabelValue( 4, u"Stok" )
		self.tabelProduk.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabelProduk.AutoSizeRows()
		self.tabelProduk.EnableDragRowSize( True )
		self.tabelProduk.SetRowLabelSize( 30 )
		self.tabelProduk.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tabelProduk.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.tabelProduk.SetFont( wx.Font( 10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Times New Roman" ) )

		bSizer64.Add( self.tabelProduk, 0, wx.ALL, 5 )


		self.m_panel12.SetSizer( bSizer64 )
		self.m_panel12.Layout()
		bSizer64.Fit( self.m_panel12 )
		bSizer38.Add( self.m_panel12, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer20.Add( bSizer38, 1, wx.EXPAND, 5 )


		bSizer13.Add( bSizer20, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer13 )
		self.Layout()

		# Connect Events
		self.m_button37.Bind( wx.EVT_BUTTON, self.btnTransaksiOnButtonClick )
		self.m_button6.Bind( wx.EVT_BUTTON, self.btnProdukOnButtonClick )
		self.m_button9.Bind( wx.EVT_BUTTON, self.btnLogoutOnButtonClick )
		self.m_button12.Bind( wx.EVT_BUTTON, self.btnAddOnButtonClick )
		self.m_button34.Bind( wx.EVT_BUTTON, self.btnUpdateOnButtonClick )
		self.m_button35.Bind( wx.EVT_BUTTON, self.btnDelOnButtonClick )
		self.m_button24.Bind( wx.EVT_BUTTON, self.btnEditOnButtonClick )
		self.m_button23.Bind( wx.EVT_BUTTON, self.btnRefreshOnButtonClick )
		self.tabelProduk.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.tabelTransaksiOnGridCmdSelectCell )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnTransaksiOnButtonClick( self, event ):
		event.Skip()

	def btnProdukOnButtonClick( self, event ):
		event.Skip()

	def btnLogoutOnButtonClick( self, event ):
		event.Skip()

	def btnAddOnButtonClick( self, event ):
		event.Skip()

	def btnUpdateOnButtonClick( self, event ):
		event.Skip()

	def btnDelOnButtonClick( self, event ):
		event.Skip()

	def btnEditOnButtonClick( self, event ):
		event.Skip()

	def btnRefreshOnButtonClick( self, event ):
		event.Skip()

	def tabelTransaksiOnGridCmdSelectCell( self, event ):
		event.Skip()


###########################################################################
## Class wxAddProdukPanel
###########################################################################

class wxAddProdukPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 630,430 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		self.SetMaxSize( wx.Size( 900,600 ) )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Produk", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		self.m_staticText31.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Barlow SemiBold" ) )

		bSizer30.Add( self.m_staticText31, 0, 0, 5 )


		bSizer14.Add( bSizer30, 1, wx.ALIGN_CENTER_VERTICAL, 5 )

		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button37 = wx.Button( self, wx.ID_ANY, u"Transaksi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button37.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Barlow Medium" ) )

		bSizer41.Add( self.m_button37, 0, wx.ALL, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Produk", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button6.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Barlow Medium" ) )

		bSizer41.Add( self.m_button6, 0, wx.ALL, 5 )

		self.m_button9 = wx.Button( self, wx.ID_ANY, u"Logout", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button9.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Barlow Medium" ) )
		self.m_button9.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button9.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )

		bSizer41.Add( self.m_button9, 0, wx.ALL, 5 )


		bSizer14.Add( bSizer41, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer13.Add( bSizer14, 0, wx.EXPAND, 5 )

		self.m_panel13 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel13.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )

		bSizer36 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText24 = wx.StaticText( self.m_panel13, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		bSizer36.Add( self.m_staticText24, 0, wx.ALL, 5 )


		self.m_panel13.SetSizer( bSizer36 )
		self.m_panel13.Layout()
		bSizer36.Fit( self.m_panel13 )
		bSizer13.Add( self.m_panel13, 0, wx.EXPAND |wx.ALL, 5 )

		bSizer62 = wx.BoxSizer( wx.VERTICAL )

		bSizer34 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText281 = wx.StaticText( self, wx.ID_ANY, u"Nama Produk", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText281.Wrap( -1 )

		self.m_staticText281.SetFont( wx.Font( 11, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Times New Roman" ) )

		bSizer34.Add( self.m_staticText281, 0, wx.ALL, 5 )

		self.textCtrlNamaProduk = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer34.Add( self.textCtrlNamaProduk, 0, wx.ALL, 5 )


		bSizer62.Add( bSizer34, 0, 0, 5 )

		bSizer35 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText291 = wx.StaticText( self, wx.ID_ANY, u"Merk", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText291.Wrap( -1 )

		self.m_staticText291.SetFont( wx.Font( 11, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Times New Roman" ) )

		bSizer35.Add( self.m_staticText291, 0, wx.ALL, 5 )

		self.textCtrlMerk = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer35.Add( self.textCtrlMerk, 0, wx.ALL, 5 )


		bSizer62.Add( bSizer35, 0, 0, 5 )

		bSizer361 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText301 = wx.StaticText( self, wx.ID_ANY, u"Harga", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText301.Wrap( -1 )

		self.m_staticText301.SetFont( wx.Font( 11, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Times New Roman" ) )

		bSizer361.Add( self.m_staticText301, 0, wx.ALL, 5 )

		self.textCtrlHrg = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer361.Add( self.textCtrlHrg, 0, wx.ALL, 5 )


		bSizer62.Add( bSizer361, 0, 0, 5 )

		bSizer37 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText65 = wx.StaticText( self, wx.ID_ANY, u"Stok", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.m_staticText65.Wrap( -1 )

		self.m_staticText65.SetFont( wx.Font( 11, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Times New Roman" ) )

		bSizer37.Add( self.m_staticText65, 0, wx.ALL, 5 )

		self.textCtrlStok = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer37.Add( self.textCtrlStok, 0, wx.ALL, 5 )


		bSizer62.Add( bSizer37, 0, 0, 5 )


		bSizer13.Add( bSizer62, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer74 = wx.BoxSizer( wx.VERTICAL )

		self.m_button12 = wx.Button( self, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button12.SetFont( wx.Font( 11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Barlow Medium" ) )
		self.m_button12.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button12.SetBackgroundColour( wx.Colour( 0, 103, 206 ) )

		bSizer74.Add( self.m_button12, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer13.Add( bSizer74, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer13 )
		self.Layout()

		# Connect Events
		self.m_button37.Bind( wx.EVT_BUTTON, self.btnTransaksiOnButtonClick )
		self.m_button6.Bind( wx.EVT_BUTTON, self.btnProdukOnButtonClick )
		self.m_button9.Bind( wx.EVT_BUTTON, self.btnLogoutOnButtonClick )
		self.m_button12.Bind( wx.EVT_BUTTON, self.btnAddOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnTransaksiOnButtonClick( self, event ):
		event.Skip()

	def btnProdukOnButtonClick( self, event ):
		event.Skip()

	def btnLogoutOnButtonClick( self, event ):
		event.Skip()

	def btnAddOnButtonClick( self, event ):
		event.Skip()


