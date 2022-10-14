import requests as req
def 生成验证码数字(s):
    global r
    r=req.get("https://api.xyfish.cn/api/verifycode_api/api.php?code="+s)
def 保存路径(path):
    with open(path+"\png.png","wb")as f:
        f.write(r.content)
