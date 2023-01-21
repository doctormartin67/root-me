import base64
from Crypto.Cipher import AES
passwd = """
76492d1116743f0423413b16050a5345MgB8AEkAMQBwAEwAbgBoAHgARwBXAHkAMgB3AGcAdwB3AHQARQBqAEEARQBPAEEAPQA9AHwAMgAyAGMANQA1ADIANwBiADEANQA4ADIANwAwAGIANAA2ADIAMQBlADAANwA3ADIAYgBkADYANgAyADUAYwAyAGMAYQBhAGUAMAA5ADUAMAA2ADUAYQBjADIAMQAzADIAMgA1AGYANgBkAGYAYgAxAGMAMgAwADUANQBkADIAMgA0AGQAYgBmADYAMQA4AGQAZgBkAGQAMwAwADUANAA4AGYAMAAyADgAZAAwADEAMgBmAGEAZQBmADgANAAyADkA"""
passwd = passwd.strip()

key = "3 4 2 3 56 34 254 222 1 1 2 23 42 54 33 233 1 34 2 7 6 5 35 43"

key = key.split(" ")

for i in range(0, len(key)):
        key[i] = int(key[i])

b = base64.b64decode(passwd)

print(b, len(b), len(passwd))

aes = AES.new(bytes(key), AES.MODE_CBC)
print(aes.decrypt(bytes(passwd[:16], "utf-8")))
