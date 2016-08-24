#!/usr/bin/env python3

from tkinter import *
from tkinter.ttk import *

class emmerGUI:

	# emmer GUI Globals

	def __init__(self, master):

		self.upfromme=master

		# Create Frame
		frame = Frame(master)
		frame.grid(column=0, row=0)

		tabs = Notebook(frame)

		# Adding Content Frames
		self.cmframe = LabelFrame(text="Current Market")
		self.histframe = LabelFrame(text="Historical Data")
		self.pressframe = LabelFrame(frame, text="Market Pressure")
		self.orderframe = LabelFrame(frame, text="Orders")
		self.fundsframe = LabelFrame(frame, text="Funds")

		tabs.add(self.cmframe, text="Current Market")
		tabs.add(self.histframe, text="Historical Data")
		tabs.add(self.orderframe, text="Orders")
		tabs.add(self.pressframe, text="Market Pressure")
		tabs.add(self.fundsframe, text="Funds")
		tabs.grid(row=0, column=0)

	        #Menu
		self.menu = Menu(master)
		master.config(menu = self.menu)
		self.filemenu = Menu(self.menu)
		self.menu.add_cascade(label="File")

