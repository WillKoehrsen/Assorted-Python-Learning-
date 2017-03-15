from tkinter import *
from PIL import Image, ImageTk

# Frame is a class within tkinter
class Window(Frame):
	def __init__(self, master = None):
		Frame.__init__(self, master)

		# main frame	
		self.master = master

		self.init_window()

	# have a frame, and within the frame put windows
	def init_window(self):
		# title of the window
		self.master.title("Functional Window")
		# adjust dimensions as needed, packing into frame
		self.pack(fill= BOTH, expand = 1)
		
		# add a menu
		# go from specific function to general, up through hierarchy
		# Menu is a class in tkinter
		# menu is an object we create
		menu = Menu(self.master)
		self.master.config(menu=menu)

		file = Menu(menu)
		file.add_command(label= 'Save')
		file.add_command(label= 'Exit', command= self.client_exit)
		
		Properties = Menu(menu)
		Properties.add_command(label= 'Maximize', command= self.maximize)
		
		edit = Menu(menu)
		# If we add parenthesis to showImage(), the function will automatically be called
		edit.add_command(label='Show Image', command=self.showImage)
		edit.add_command(label='Show Text', command=self.showText)

		menu.add_cascade(label= 'File', menu=file)
		menu.add_cascade(label= 'Properties', menu = Properties)
		menu.add_cascade(label= 'Edit', menu=edit)

		# Button is a class within tkinter
		#quitButton = Button(self, text = "Quit", command=self.client_exit)
		# place at upper left of screen
		#quitButton.place(x = 0, y= 0)

	def client_exit(self):
		exit()

	def maximize(self):
		toplevel = self.winfo_toplevel()
		toplevel.wm_state('zoomed')

	def showImage(self):
		#Image and ImageTk are from pillow (PIL) image module
		load = Image.open('LightSail.jpg')
		render = ImageTk.PhotoImage(load)

		# Label is a class witin tkinter
		img = Label(self, image= render)
		img.image = render
		img.place(x = 0 , y = 0)
		hlp = Label(self, text = 'Maximize the window under properties to view the full image.')
		hlp.pack()

	def showText(self):
		text = Label(self, text= 'This is some helpful information.')
		text.pack()

# root window, the window is within a frame
root = Tk()
# size of window
root.geometry("400x400+500+200")

app = Window(root)

# generates window
root.mainloop()