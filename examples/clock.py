from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from threading import Thread
import time
import tkst

timeFont = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.otf", 60)
dateFont = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMono.otf", 30)

def updateDisplay(display):
	img = Image.new('RGB', (display.width, display.height), color=(0, 0, 0))
	draw = ImageDraw.Draw(img)
	
	# retrieve and format the current time and date
	currentTime = datetime.now()
	minute = str(currentTime.minute) if currentTime.minute >= 10 else "0"+str(currentTime.minute)
	hour = str(currentTime.hour) if currentTime.hour >= 10 else "0"+str(currentTime.hour)
	day = str(currentTime.day) if currentTime.day >= 10 else "0"+str(currentTime.day)
	month = str(currentTime.month) if currentTime.month >= 10 else "0"+str(currentTime.month)
	year = str(currentTime.year) if currentTime.year >= 10 else "0"+str(currentTime.year)
	formattedTime = hour+":"+minute
	formattedDate = day+"/"+month+"/"+year

	# add the time and date to the image
	textWidth, textHeight = draw.textsize(formattedTime, timeFont)
	draw.text(((display.width-textWidth)/2, 60), formattedTime, font=timeFont, fill=(255, 255, 255))
	textWidth, textHeight = draw.textsize(formattedDate, dateFont)
	draw.text(((display.width-textWidth)/2, 150), formattedDate, font=dateFont, fill=(255, 255, 255))

	# update the display, wait until the next minute, and update the display again
	try:
		display.display(img)
		time.sleep(60-currentTime.second)
		updateDisplay(display)
	except:
		return

def __main__():
	disp = tkst.Display(tkst.TK)
	thrd = Thread(target=updateDisplay, args=[disp,])
	thrd.start()
	disp.start()

	thrd.join()
	exit(0)

if __name__ == "__main__":
	__main__()