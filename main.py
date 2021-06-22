import pyqrcode
import png
from pyqrcode import QRCode
# string which represents the QR  code
s = "hello world"
url = pyqrcode.create(s)
url.svg("my qr.svg", scale=8)
url.png("my qr.png", scale=6)
