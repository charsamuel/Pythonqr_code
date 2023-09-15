import segno

qrcode = segno.make_qr("Hello, World")
qrcode.save(
  "basic_qrcode.png",
  scale = 5,
  border = 10,
  light = "lightpink",
  data_dark = "black",
  )


