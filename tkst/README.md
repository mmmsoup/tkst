# **tkst**
# About
Preview projects using the ST7789 spi display (and [corresponding python library](https://github.com/pimoroni/st7789-python)) on your desktop with tkinter. Read more [here](https://github.com/mmmsoup/tkst#readme).

jump to...
- [Doc](#Doc)
- [Usage](#Usage)
- [Examples](#Examples)

# Doc
## Display
- ### tkst.Display(displayType)
    main class that provides methods for interacting with a display
    #### parameters
    - #### _displayType_
        a tkst [display type](#Display-Types) ([tkst.ST](#tkst.ST) or [tkst.TK](#tkst.TK))
    #### methods
    - #### _tkst.Display().start()_
        starts the display. For [tkst.TK](#tkst.TK) displays it calls tkinter's _mainloop()_ function, and for [tkst.ST](#tkst.ST) it calls ST7789's _begin()_ function. Since _mainloop()_ is blocking, _tkst.Display().start()_ will block regardless of display type to ensure code works with either.
    - #### _tkst.Display().awaitStart()_
        blocks until _tkst.Display().start()_ has started the display. This is likely unnecessary, as the display starts very quickly, however if you receive a [tkst.DisplayError](#tkst.DisplayError) when first calling _tkst.Display().display()_, then it might be a good idea to use this.
    - #### _tkst.Display().stop()_
        stops the display. Any attempts to update the display after calling _tkst.Display().stop()_ will result in a [tkst.DisplayError](#tkst.DisplayError).
    - #### _tkst.Display().display(image)_
        display a _PIL.Image_ image on the display.
    #### properties
    - #### _tkst().Display().output_
        a tkst [display type](#Display-Types) ([tkst.ST](#tkst.ST) or [tkst.TK](#tkst.TK)).
    - #### _tkst().Display().width_
        the width of the display (240px).
    - #### _tkst().Display().hegiht_
        the height of the display (240px).
    - #### _tkst().Display().isRunning_
        a boolean describing whether the display is currently running or not.
    - #### _tkst().Display().root_
        the root window on which any image is drawn. It is of type _tkinter.Tk()_ window if _tkst().Display().output_ is [tkst.TK](#tkst.TK), or _ST7789.ST7789()_ if _tkst().Display().output_ is [tkst.ST](#tkst.ST).

## Display Types
- ### tkst.ST
    display type corresponding to a physical ST7789 display. Requires the ST7789 module to be installed; if it is not, a [tkst.DisplayError](#tkst.DisplayError) will be raised.

- ### tkst.TK
    display type corresponding to a tkinter window. Requires the tkinter module to be installed; if it is not, a [tkst.DisplayError](#tkst.DisplayError) will be raised.

## Errors
- ### tkst.DisplayError
    a general error used by this module, will be raised if methods like [tkst.Display().start()](#tkst.Display().start()) are called while the display is active, or if [tkst.Display().display()](#tkst.Display().display(image)) is called after the display is stopped.

# Usage
- Firstly import the tkst module (you'll also want to use Pillow and threading)
```python
import tkst
from PIL import Image, ImageDraw, ImageFont
from threading import Thread
```
- Define a function to be the target of the thread we're going to create
```python
def updateDisplay(display):
    display.awaitStart()
    img = Image.new('RGB', (display.width, display.height), color=(0, 0, 0)) # the image we're going to display
    draw = ImageDraw.Draw(img) # a way for us to add text etc on top of the image
    draw.text((0,0), "hello, world!", font="/usr/share/fonts/gnu-free/FreeMono.otf", fill=(255, 255, 255)) # add some sample text to our image
    display.display(img) # show this image on the display
```
- Set up a main function where we initialise the display and set everything going
```python
def __main__():
    d = tkst.Display(tkst.TK) # just change tkst.TK to tkst.ST when you want to display it on the ST7789
    t = Thread(target=updateDisplay, args=[d,]) # thread to set the picture on the display, has to be threaded as tkst.Display().start() is blocking
    t.start() # start the updater thread
    d.start() # start the display

if __name__ == "__main__": # fancy way of starting the main function
    __main__()
```
- Et vóila! That's your first program that you can easily test on your computer before displaying it on an ST7789.

# Examples
Check out a couple of examples on my [github repo](https://github.com/mmmsoup/tkst/tree/main/examples)