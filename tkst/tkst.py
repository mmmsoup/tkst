### custom exceptions
class DisplayError(Exception):
	def __init__(self, message):
		self.message = message
		super().__init__(self.message)
	def __str__(self):
		return f'{self.message}'

### variables for referencing display output type
ST = 0
TK = 1

### load required modules
import time
from PIL import Image, ImageDraw, ImageFont

_modules_st = False
_modules_tk = False

try:
	import ST7789
	_modules_st = True
except:
	pass

try:
	import tkinter
	from PIL import ImageTk
	_modules_tk = True
except:
	pass

if not _modules_st and not _modules_tk:
	raise ImportError("unable to import modules for tkinter or st7789")

### main display object
class Display:
	def __init__(self, dispOut):
		if dispOut == ST and not _modules_st:
			raise ImportError("unable to create st7789 display: was unable to load required modules (ST7789)")
		if dispOut == TK and not _modules_tk:
			raise ImportError("unable to create tkinter display: was unable to load required modules (tkinter)")

		self.output = dispOut
		self.width = 240
		self.height = 240
		self.isRunning = False
		if self.output == ST:
			self.root = ST7789.ST7789(port=0, cs=ST7789.BG_SPI_CS_FRONT, dc=9, backlight=19, spi_speed_hz=80000000)
		elif self.output == TK:
			self.root = tkinter.Tk()
			self.root.withdraw()
			self.root.attributes("-type", "dialog") # make this window floating on tiling wms like i3 and bspwm
			self.root.geometry(str(self.width)+"x"+str(self.height))
			self.root.title("ST7789 preview")
			self.root.resizable(False, False)

			self._rootImage = None
			self._rootImageLabel = tkinter.Label(self.root, image=self._rootImage)
			self._rootImageLabel.place(relx=0.5, rely=0.5, anchor="center")
		else:
			raise DisplayError("invalid value for display output")
	
	def start(self):
		if not self.isRunning:
			self.isRunning = True

			if self.output == ST:
				self.root.begin()
				while True:
					time.sleep(5)
			elif self.output == TK:
				self.root.deiconify()
				self.root.mainloop()
				self.isRunning = False
		else:
			raise DisplayError("display is already running")

	def stop(self):
		if self.isRunning:
			if self.output == ST:
				pass
			elif self.output == TK:
				self.root.withdraw()
				self.root.quit()
			self.isRunning = False
		else:
			raise DisplayError("display is not running")
	
	def awaitStart(self):
		while not self.isRunning:
			pass

	def display(self, image):
		if self.isRunning:
			if self.output == ST:
				self.root.display(image)
			elif self.output == TK:
				self._rootImage = ImageTk.PhotoImage(image=image)
				self._rootImageLabel.config(image=self._rootImage)
		else:
			raise DisplayError("display is not running")