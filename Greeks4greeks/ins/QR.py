import pyqrcode
import png 
from pyqrcode import QRCode

s = "Python.hub"
url = pyqrcode.created(s)
url.svg("myqr.svg", scale = 8)
url.png('myqr.png', scale = 6)