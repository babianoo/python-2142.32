import qrcode

url = "https://ifconfig.me"
img = qrcode.make(url)
img.save('qrcode.png')