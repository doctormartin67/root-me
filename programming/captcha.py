import requests
import base64
import pytesseract
from PIL import Image

def get_al(s):
        res = ""
        for c in s:
                if c.isalnum():
                        res += c
        return res

file = "captcha.png"

ses = requests.Session()
r = ses.get("http://challenge01.root-me.org/programmation/ch8/")
s = r.text
print(s)
start = "base64,"
end =  "/><br><br><form action"
code = s[s.index(start) + len(start):s.index(end)-2]
b = base64.b64decode(code)
f = open(file, "wb")
f.write(b)
a = pytesseract.image_to_string(Image.open(file))
print(a)

a = get_al(a)
print(a)

data = {"cametu": a.strip()}
r = ses.post("http://challenge01.root-me.org/programmation/ch8/", data=data)
print(r.text)
