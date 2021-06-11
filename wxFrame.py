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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE_BOX|wx.TAB_TRAVERSAL )

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

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		self.SetBackgroundColour( wx.Colour( 144, 144, 144 ) )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer32 = wx.BoxSizer( wx.VERTICAL )

		bSizer34 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"LOGIN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		self.m_staticText6.SetFont( wx.Font( 18, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Britannic Bold" ) )

		bSizer34.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer32.Add( bSizer34, 1, wx.EXPAND, 5 )

		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"ID Pegawai", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		gSizer3.Add( self.m_staticText10, 0, wx.EXPAND|wx.ALL, 6 )

		self.textCtrlIdPeg = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.textCtrlIdPeg, 0, wx.ALL, 5 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		gSizer3.Add( self.m_staticText8, 0, wx.ALL|wx.EXPAND, 6 )

		self.textCtrlPassword = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		gSizer3.Add( self.textCtrlPassword, 0, wx.ALL, 5 )


		gSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btnLogin = wx.Button( self, wx.ID_ANY, u"LOGIN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnLogin.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.btnLogin.SetBackgroundColour( wx.Colour( 0, 103, 206 ) )

		gSizer3.Add( self.btnLogin, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 5 )


		bSizer32.Add( gSizer3, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer3.Add( bSizer32, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.SetSizer( bSizer3 )
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

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 746,490 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer30 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Transaksi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		bSizer30.Add( self.m_staticText31, 0, 0, 5 )


		bSizer14.Add( bSizer30, 1, wx.ALIGN_CENTER_VERTICAL, 5 )

		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button37 = wx.Button( self, wx.ID_ANY, u"Transaksi", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer41.Add( self.m_button37, 0, wx.ALL, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Produk", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer41.Add( self.m_button6, 0, wx.ALL, 5 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"Supplier", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer41.Add( self.m_button7, 0, wx.ALL, 5 )

		self.m_button9 = wx.Button( self, wx.ID_ANY, u"Logout", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button9.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button9.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )

		bSizer41.Add( self.m_button9, 0, wx.ALL, 5 )


		bSizer14.Add( bSizer41, 1, wx.EXPAND, 5 )


		bSizer13.Add( bSizer14, 0, 0, 5 )

		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel8 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel8.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer36 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText24 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Tambah Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		bSizer36.Add( self.m_staticText24, 0, wx.ALL, 5 )


		self.m_panel8.SetSizer( bSizer36 )
		self.m_panel8.Layout()
		bSizer36.Fit( self.m_panel8 )
		bSizer20.Add( self.m_panel8, 0, wx.EXPAND |wx.ALL, 5 )

		gSizer1 = wx.GridSizer( 0, 3, 0, 0 )

		self.m_staticText281 = wx.StaticText( self, wx.ID_ANY, u"Nama Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText281.Wrap( -1 )

		gSizer1.Add( self.m_staticText281, 0, wx.ALL, 5 )

		self.textCtrlNamaBrgTrans = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.textCtrlNamaBrgTrans, 0, wx.ALL, 5 )

		self.m_button12 = wx.Button( self, wx.ID_ANY, u"Tambah Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button12.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button12.SetBackgroundColour( wx.Colour( 0, 103, 206 ) )

		gSizer1.Add( self.m_button12, 0, wx.ALL, 5 )

		self.m_staticText291 = wx.StaticText( self, wx.ID_ANY, u"Kuantitas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText291.Wrap( -1 )

		gSizer1.Add( self.m_staticText291, 0, wx.ALL, 5 )

		self.textCtrlKuantitasTrans = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.textCtrlKuantitasTrans, 0, wx.ALL, 5 )


		gSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText301 = wx.StaticText( self, wx.ID_ANY, u"Harga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText301.Wrap( -1 )

		gSizer1.Add( self.m_staticText301, 0, wx.ALL, 5 )

		self.textCtrlHrgTrans = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.textCtrlHrgTrans, 0, wx.ALL, 5 )


		bSizer20.Add( gSizer1, 0, 0, 5 )


		bSizer13.Add( bSizer20, 0, wx.EXPAND, 5 )

		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

		self.tabelTransaksi = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.tabelTransaksi.CreateGrid( 5, 4 )
		self.tabelTransaksi.EnableEditing( True )
		self.tabelTransaksi.EnableGridLines( True )
		self.tabelTransaksi.EnableDragGridSize( False )
		self.tabelTransaksi.SetMargins( 0, 0 )

		# Columns
		self.tabelTransaksi.AutoSizeColumns()
		self.tabelTransaksi.EnableDragColMove( False )
		self.tabelTransaksi.EnableDragColSize( True )
		self.tabelTransaksi.SetColLabelSize( 30 )
		self.tabelTransaksi.SetColLabelValue( 0, u"ID" )
		self.tabelTransaksi.SetColLabelValue( 1, u"Nama Barang" )
		self.tabelTransaksi.SetColLabelValue( 2, u"Kuantitas" )
		self.tabelTransaksi.SetColLabelValue( 3, u"Harga" )
		self.tabelTransaksi.SetColLabelValue( 4, wx.EmptyString )
		self.tabelTransaksi.SetColLabelValue( 5, wx.EmptyString )
		self.tabelTransaksi.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabelTransaksi.AutoSizeRows()
		self.tabelTransaksi.EnableDragRowSize( True )
		self.tabelTransaksi.SetRowLabelSize( 80 )
		self.tabelTransaksi.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tabelTransaksi.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer15.Add( self.tabelTransaksi, 0, wx.ALL, 5 )

		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button24 = wx.Button( self, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_button24, 0, wx.ALL, 5 )


		gSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText292 = wx.StaticText( self, wx.ID_ANY, u"ID", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText292.Wrap( -1 )

		gSizer2.Add( self.m_staticText292, 0, wx.ALL, 5 )

		self.textCtrlIdUpdate = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.textCtrlIdUpdate, 0, wx.ALL, 5 )

		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"Nama Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		gSizer2.Add( self.m_staticText28, 0, wx.ALL, 5 )

		self.textCtrlNamaBrgUpdate = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.textCtrlNamaBrgUpdate, 0, wx.ALL, 5 )

		self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"Kuantitas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )

		gSizer2.Add( self.m_staticText29, 0, wx.ALL, 5 )

		self.textCtrlKuantitasUpdate = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.textCtrlKuantitasUpdate, 0, wx.ALL, 5 )

		self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"Harga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )

		gSizer2.Add( self.m_staticText30, 0, wx.ALL, 5 )

		self.textCtrlHrgUpdate = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.textCtrlHrgUpdate, 0, wx.ALL, 5 )

		self.m_button91 = wx.Button( self, wx.ID_ANY, u"Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button91.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button91.SetBackgroundColour( wx.Colour( 0, 103, 206 ) )

		gSizer2.Add( self.m_button91, 0, wx.ALL, 5 )

		self.m_button8 = wx.Button( self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button8.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button8.SetBackgroundColour( wx.Colour( 251, 0, 0 ) )

		gSizer2.Add( self.m_button8, 0, wx.ALL, 5 )

		self.m_button23 = wx.Button( self, wx.ID_ANY, u"Refresh", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_button23, 0, wx.ALL, 5 )


		bSizer15.Add( gSizer2, 0, wx.EXPAND, 5 )


		bSizer13.Add( bSizer15, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer13 )
		self.Layout()

		# Connect Events
		self.m_button12.Bind( wx.EVT_BUTTON, self.btnTmbhTransOnButtonClick )
		self.m_button24.Bind( wx.EVT_BUTTON, self.btnEditTransOnButtonClick )
		self.m_button91.Bind( wx.EVT_BUTTON, self.btnUpdateOnButtonClick )
		self.m_button8.Bind( wx.EVT_BUTTON, self.btnDeleteOnButtonClick )
		self.m_button23.Bind( wx.EVT_BUTTON, self.btnRefreshOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnTmbhTransOnButtonClick( self, event ):
		event.Skip()

	def btnEditTransOnButtonClick( self, event ):
		event.Skip()

	def btnUpdateOnButtonClick( self, event ):
		event.Skip()

	def btnDeleteOnButtonClick( self, event ):
		event.Skip()

	def btnRefreshOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class wxProdukPanel
###########################################################################

class wxProdukPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 722,487 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel6.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		bSizer30 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText31 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Produk", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		bSizer30.Add( self.m_staticText31, 0, wx.ALL, 5 )


		self.m_panel6.SetSizer( bSizer30 )
		self.m_panel6.Layout()
		bSizer30.Fit( self.m_panel6 )
		bSizer14.Add( self.m_panel6, 1, wx.ALL, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Transaksi", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button6, 0, wx.ALL, 5 )

		self.m_button45 = wx.Button( self, wx.ID_ANY, u"Produk", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button45, 0, wx.ALL, 5 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"Supplier", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button7, 0, wx.ALL, 5 )

		self.m_button9 = wx.Button( self, wx.ID_ANY, u"Logout", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button9.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button9.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )

		bSizer14.Add( self.m_button9, 0, wx.ALL, 5 )


		bSizer13.Add( bSizer14, 0, wx.EXPAND, 5 )

		self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel7.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel8 = wx.Panel( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel8.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer36 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText24 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Tambah Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		bSizer36.Add( self.m_staticText24, 0, wx.ALL, 5 )


		self.m_panel8.SetSizer( bSizer36 )
		self.m_panel8.Layout()
		bSizer36.Fit( self.m_panel8 )
		bSizer20.Add( self.m_panel8, 0, wx.EXPAND |wx.ALL, 5 )

		fgSizer9 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer26 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText281 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Nama Produk", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText281.Wrap( -1 )

		bSizer26.Add( self.m_staticText281, 1, wx.ALL, 5 )

		self.m_staticText291 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Kualitas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText291.Wrap( -1 )

		bSizer26.Add( self.m_staticText291, 1, wx.ALL, 5 )

		self.m_staticText301 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Harga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText301.Wrap( -1 )

		bSizer26.Add( self.m_staticText301, 1, wx.ALL, 5 )


		fgSizer9.Add( bSizer26, 1, wx.EXPAND, 5 )

		bSizer27 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl16 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer27.Add( self.m_textCtrl16, 0, wx.ALL, 5 )

		self.m_textCtrl171 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer27.Add( self.m_textCtrl171, 0, wx.ALL, 5 )

		self.m_textCtrl181 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer27.Add( self.m_textCtrl181, 0, wx.ALL, 5 )


		fgSizer9.Add( bSizer27, 1, wx.EXPAND, 5 )

		bSizer28 = wx.BoxSizer( wx.VERTICAL )

		self.m_button12 = wx.Button( self.m_panel7, wx.ID_ANY, u"Tambah Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button12.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button12.SetBackgroundColour( wx.Colour( 0, 103, 206 ) )

		bSizer28.Add( self.m_button12, 0, wx.ALL, 5 )


		fgSizer9.Add( bSizer28, 1, wx.EXPAND, 5 )


		bSizer20.Add( fgSizer9, 1, wx.EXPAND, 5 )


		self.m_panel7.SetSizer( bSizer20 )
		self.m_panel7.Layout()
		bSizer20.Fit( self.m_panel7 )
		bSizer13.Add( self.m_panel7, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_grid2 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid2.CreateGrid( 5, 4 )
		self.m_grid2.EnableEditing( True )
		self.m_grid2.EnableGridLines( True )
		self.m_grid2.EnableDragGridSize( False )
		self.m_grid2.SetMargins( 0, 0 )

		# Columns
		self.m_grid2.AutoSizeColumns()
		self.m_grid2.EnableDragColMove( False )
		self.m_grid2.EnableDragColSize( True )
		self.m_grid2.SetColLabelSize( 30 )
		self.m_grid2.SetColLabelValue( 0, u"ID" )
		self.m_grid2.SetColLabelValue( 1, u"Nama Produk" )
		self.m_grid2.SetColLabelValue( 2, u"Kuantitas" )
		self.m_grid2.SetColLabelValue( 3, u"Harga" )
		self.m_grid2.SetColLabelValue( 4, wx.EmptyString )
		self.m_grid2.SetColLabelValue( 5, wx.EmptyString )
		self.m_grid2.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid2.AutoSizeRows()
		self.m_grid2.EnableDragRowSize( True )
		self.m_grid2.SetRowLabelSize( 80 )
		self.m_grid2.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid2.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer15.Add( self.m_grid2, 1, wx.ALL|wx.EXPAND, 5 )

		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"Nama Produk", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		fgSizer5.Add( self.m_staticText28, 0, wx.ALL, 5 )

		self.m_textCtrl17 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_textCtrl17, 0, wx.ALL, 5 )

		self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"Kuantitas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )

		fgSizer5.Add( self.m_staticText29, 0, wx.ALL, 5 )

		self.m_textCtrl18 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_textCtrl18, 0, wx.ALL, 5 )

		self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"Harga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )

		fgSizer5.Add( self.m_staticText30, 0, wx.ALL, 5 )

		self.m_textCtrl19 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_textCtrl19, 0, wx.ALL, 5 )

		self.m_button91 = wx.Button( self, wx.ID_ANY, u"Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button91.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button91.SetBackgroundColour( wx.Colour( 0, 103, 206 ) )

		fgSizer5.Add( self.m_button91, 0, wx.ALL, 5 )

		self.m_button8 = wx.Button( self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button8.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button8.SetBackgroundColour( wx.Colour( 251, 0, 0 ) )

		fgSizer5.Add( self.m_button8, 0, wx.ALL, 5 )


		bSizer15.Add( fgSizer5, 1, wx.EXPAND, 5 )


		bSizer13.Add( bSizer15, 0, 0, 5 )


		self.SetSizer( bSizer13 )
		self.Layout()

	def __del__( self ):
		pass


###########################################################################
## Class wxSuplierPanel1
###########################################################################

class wxSuplierPanel1 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 705,496 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel6.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		bSizer30 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText31 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Produk", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		bSizer30.Add( self.m_staticText31, 0, wx.ALL, 5 )


		self.m_panel6.SetSizer( bSizer30 )
		self.m_panel6.Layout()
		bSizer30.Fit( self.m_panel6 )
		bSizer14.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Transaksi", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button6, 0, wx.ALL, 5 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"Produk", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button7, 0, wx.ALL, 5 )

		self.m_button46 = wx.Button( self, wx.ID_ANY, u"Suplier", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button46, 0, wx.ALL, 5 )

		self.m_button9 = wx.Button( self, wx.ID_ANY, u"Logout", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button9.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button9.SetBackgroundColour( wx.Colour( 0, 0, 0 ) )

		bSizer14.Add( self.m_button9, 0, wx.ALL, 5 )


		bSizer13.Add( bSizer14, 0, wx.EXPAND, 5 )

		self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel7.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel8 = wx.Panel( self.m_panel7, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel8.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ) )

		bSizer36 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText24 = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Tambah Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		bSizer36.Add( self.m_staticText24, 0, wx.ALL, 5 )


		self.m_panel8.SetSizer( bSizer36 )
		self.m_panel8.Layout()
		bSizer36.Fit( self.m_panel8 )
		bSizer20.Add( self.m_panel8, 0, wx.EXPAND |wx.ALL, 5 )

		fgSizer9 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer9.SetFlexibleDirection( wx.BOTH )
		fgSizer9.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer26 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText281 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Nama Produk", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText281.Wrap( -1 )

		bSizer26.Add( self.m_staticText281, 0, wx.ALL, 5 )

		self.m_staticText291 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Kualitas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText291.Wrap( -1 )

		bSizer26.Add( self.m_staticText291, 0, wx.ALL, 5 )

		self.m_staticText301 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Harga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText301.Wrap( -1 )

		bSizer26.Add( self.m_staticText301, 0, wx.ALL, 5 )


		fgSizer9.Add( bSizer26, 1, wx.EXPAND, 5 )

		bSizer27 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl16 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer27.Add( self.m_textCtrl16, 0, wx.ALL, 5 )

		self.m_textCtrl171 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer27.Add( self.m_textCtrl171, 0, wx.ALL, 5 )

		self.m_textCtrl181 = wx.TextCtrl( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer27.Add( self.m_textCtrl181, 0, wx.ALL, 5 )


		fgSizer9.Add( bSizer27, 1, wx.EXPAND, 5 )

		bSizer28 = wx.BoxSizer( wx.VERTICAL )

		self.m_button12 = wx.Button( self.m_panel7, wx.ID_ANY, u"Tambah Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button12.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button12.SetBackgroundColour( wx.Colour( 0, 103, 206 ) )

		bSizer28.Add( self.m_button12, 0, wx.ALL, 5 )


		fgSizer9.Add( bSizer28, 1, wx.EXPAND, 5 )


		bSizer20.Add( fgSizer9, 1, wx.EXPAND, 5 )


		self.m_panel7.SetSizer( bSizer20 )
		self.m_panel7.Layout()
		bSizer20.Fit( self.m_panel7 )
		bSizer13.Add( self.m_panel7, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_grid2 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid2.CreateGrid( 5, 4 )
		self.m_grid2.EnableEditing( True )
		self.m_grid2.EnableGridLines( True )
		self.m_grid2.EnableDragGridSize( False )
		self.m_grid2.SetMargins( 0, 0 )

		# Columns
		self.m_grid2.AutoSizeColumns()
		self.m_grid2.EnableDragColMove( False )
		self.m_grid2.EnableDragColSize( True )
		self.m_grid2.SetColLabelSize( 30 )
		self.m_grid2.SetColLabelValue( 0, u"ID" )
		self.m_grid2.SetColLabelValue( 1, u"Nama Produk" )
		self.m_grid2.SetColLabelValue( 2, u"Kuantitas" )
		self.m_grid2.SetColLabelValue( 3, u"Harga" )
		self.m_grid2.SetColLabelValue( 4, wx.EmptyString )
		self.m_grid2.SetColLabelValue( 5, wx.EmptyString )
		self.m_grid2.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid2.AutoSizeRows()
		self.m_grid2.EnableDragRowSize( True )
		self.m_grid2.SetRowLabelSize( 80 )
		self.m_grid2.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid2.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer15.Add( self.m_grid2, 1, wx.ALL|wx.EXPAND, 5 )

		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"Nama Produk", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )

		fgSizer5.Add( self.m_staticText28, 0, wx.ALL, 5 )

		self.m_textCtrl17 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_textCtrl17, 0, wx.ALL, 5 )

		self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"Kuantitas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )

		fgSizer5.Add( self.m_staticText29, 0, wx.ALL, 5 )

		self.m_textCtrl18 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_textCtrl18, 0, wx.ALL, 5 )

		self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"Harga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )

		fgSizer5.Add( self.m_staticText30, 0, wx.ALL, 5 )

		self.m_textCtrl19 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_textCtrl19, 0, wx.ALL, 5 )

		self.m_button91 = wx.Button( self, wx.ID_ANY, u"Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button91.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button91.SetBackgroundColour( wx.Colour( 0, 103, 206 ) )

		fgSizer5.Add( self.m_button91, 0, wx.ALL, 5 )

		self.m_button8 = wx.Button( self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button8.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.m_button8.SetBackgroundColour( wx.Colour( 251, 0, 0 ) )

		fgSizer5.Add( self.m_button8, 0, wx.ALL, 5 )


		bSizer15.Add( fgSizer5, 1, wx.EXPAND, 5 )


		bSizer13.Add( bSizer15, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer13 )
		self.Layout()

	def __del__( self ):
		pass


