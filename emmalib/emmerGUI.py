#!/usr/bin/env python3

from tkinter import *
from tkinter.ttk import *

class emmerGUI:

	# emmer GUI Globals

	def __init__(self, master):

		self.upfromme=master

		# Create Frame

		#  -------------
		#  NAV | QUERY
		#  -------------
		#  DBs | RESULTS
		#  -------------

		navigationFrame = Frame(master)
		queryFrame = Frame(master)
		databaseFrame = Frame(master)
		resultsFrame = Frame(master)
		navigationFrame.grid(column=0, row=0)
		queryFrame.grid(column=1, row=0)
		databaseFrame.grid(column=0, row=1)
		resultsFrame.grid(column=1, row=1)

		# Default UI Elements
		## Navigation Tree
		self.navigationTitle = Label(navigationFrame, text="Navigation")
		self.navigationTitle.pack()
		self.navigationTree = Treeview(navigationFrame)
		self.navigationTree.pack()
		self.navigationTree_vertscroll = Scrollbar(navigationFrame, orient="vertical", command=self.navigationTree.yview)
		self.navigationTree_vertscroll.pack()

		self.navigationTree_horzscroll = Scrollbar(navigationFrame, orient='horizontal', command=self.navigationTree.xview)
		self.navigationTree_horzscroll.pack()

		self.navigationTree_RootElement = self.navigationTree.insert('', 'end', text="Database", open=True)
		
		## Query Text Box
		self.queryTitle = Label(navigationFrame, text="Query")
		self.queryTextBox = Entry(queryFrame)
		self.queryTitle.pack()
		self.queryTextBox.pack()

	        #Menu
		self.menu = Menu(master)
		master.config(menu = self.menu)
		self.filemenu = Menu(self.menu)
		self.menu.add_cascade(label="File")

