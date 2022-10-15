#生成二维码
import qrcode
def url(url):
    global img
    img = qrcode.make(url)
def 保存路径(path):
    with open(path+'\\test.png', 'wb') as f:
        img.save(f)
