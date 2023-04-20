import qrcode as qr 
img= qr.make("https://www.wscubetech.com/")
img.save("wscube_web.png")