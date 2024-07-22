import qrcode as qr

img=qr.make('https://www.youtube.com/watch?v=hQdqL6RD42Q')

img.save('my_qr_link.jpg')

print('created')