import qrcode

link=input('Please Enter the link here -> ')
qr=qrcode.make(link)
name=(input('save as -> '))
qr.save(name+'.jpeg')
print('Qrcode is generated')
