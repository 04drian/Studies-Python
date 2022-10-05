
import pyqrcode

# String representada pelo QR code

s = "https://github.com/04drian"

# Gerador QR code

url = pyqrcode.create(s)

# Criar e salva o arquivo

url.svg("MeuGithub.svg", scale=8)