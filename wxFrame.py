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

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer32 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel12 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer34 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText6 = wx.StaticText( self.m_panel12, wx.ID_ANY, u"LOGIN", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer34.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_panel12.SetSizer( bSizer34 )
		self.m_panel12.Layout()
		bSizer34.Fit( self.m_panel12 )
		bSizer32.Add( self.m_panel12, 1, wx.EXPAND |wx.ALL, 5 )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"ID Pegawai", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		fgSizer2.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.textCtrlIdPeg = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.textCtrlIdPeg, 0, wx.ALL, 5 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		fgSizer2.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.textCtrlPassword = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		fgSizer2.Add( self.textCtrlPassword, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btnLogin = wx.Button( self, wx.ID_ANY, u"LOGIN", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.btnLogin, 0, wx.ALL, 5 )


		bSizer32.Add( fgSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


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

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 579,435 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel6.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		bSizer30 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText31 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Transaksi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		bSizer30.Add( self.m_staticText31, 0, wx.ALL, 5 )


		self.m_panel6.SetSizer( bSizer30 )
		self.m_panel6.Layout()
		bSizer30.Fit( self.m_panel6 )
		bSizer14.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_button37 = wx.Button( self, wx.ID_ANY, u"Transaksi", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button37, 0, wx.ALL, 5 )

		self.m_button6 = wx.Button( self, wx.ID_ANY, u"Produk", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button6, 0, wx.ALL, 5 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"Supplier", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button7, 0, wx.ALL, 5 )

		self.m_button9 = wx.Button( self, wx.ID_ANY, u"Logout", wx.DefaultPosition, wx.DefaultSize, 0 )
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

		self.m_staticText281 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Nama Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText281.Wrap( -1 )

		bSizer26.Add( self.m_staticText281, 0, wx.ALL, 5 )

		self.m_staticText291 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Kuantitas", wx.DefaultPosition, wx.DefaultSize, 0 )
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
		self.m_grid2.SetColLabelValue( 1, u"Nama Barang" )
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

		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"Nama Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
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
		fgSizer5.Add( self.m_button91, 0, wx.ALL, 5 )

		self.m_button8 = wx.Button( self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_button8, 0, wx.ALL, 5 )


		bSizer15.Add( fgSizer5, 1, wx.EXPAND, 5 )


		bSizer13.Add( bSizer15, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer13 )
		self.Layout()

	def __del__( self ):
		pass


###########################################################################
## Class wxProdukPanel
###########################################################################

class wxProdukPanel ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 579,435 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
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

		self.m_button45 = wx.Button( self, wx.ID_ANY, u"Produk", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button45, 0, wx.ALL, 5 )

		self.m_button7 = wx.Button( self, wx.ID_ANY, u"Supplier", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button7, 0, wx.ALL, 5 )

		self.m_button9 = wx.Button( self, wx.ID_ANY, u"Logout", wx.DefaultPosition, wx.DefaultSize, 0 )
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
		fgSizer5.Add( self.m_button91, 0, wx.ALL, 5 )

		self.m_button8 = wx.Button( self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_button8, 0, wx.ALL, 5 )


		bSizer15.Add( fgSizer5, 1, wx.EXPAND, 5 )


		bSizer13.Add( bSizer15, 1, wx.EXPAND, 5 )

		self.m_panel61 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel61.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		bSizer301 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText311 = wx.StaticText( self.m_panel61, wx.ID_ANY, u"Transaksi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText311.Wrap( -1 )

		bSizer301.Add( self.m_staticText311, 0, wx.ALL, 5 )


		self.m_panel61.SetSizer( bSizer301 )
		self.m_panel61.Layout()
		bSizer301.Fit( self.m_panel61 )
		bSizer13.Add( self.m_panel61, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer13 )
		self.Layout()

	def __del__( self ):
		pass


###########################################################################
## Class wxSuplierPanel1
###########################################################################

class wxSuplierPanel1 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 579,435 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
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
		fgSizer5.Add( self.m_button91, 0, wx.ALL, 5 )

		self.m_button8 = wx.Button( self, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.m_button8, 0, wx.ALL, 5 )


		bSizer15.Add( fgSizer5, 1, wx.EXPAND, 5 )


		bSizer13.Add( bSizer15, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer13 )
		self.Layout()

	def __del__( self ):
		pass


