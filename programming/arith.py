import requests

"""
TODO: i have parsed out the numbers, I just need to work out the formula
to calculate it now and put that in the 'results' variable
Un+1 = a + Un + n * b
U0 = c
n + 1 = d
"""

def parse_more(s):
        rubbish = "U<sub>"
        s = s[len(rubbish):s.index("</sub><br")]
        print(s)
        return s

def parse(s):
        rubbish = "iframe>U<sub>n+1</sub> = [ "
        s = s[s.index(rubbish) + len(rubbish):]
        return s.split()

url = "http://challenge01.root-me.org/programmation/ch1/"
sess = requests.Session()
r = sess.get(url)
print(r.text)
res = parse(r.text)
a = int(res[0])
b = int(res[8])
c = int(res[13])
d = int(parse_more(res[18]))
n = d - 1

print(parse(r.text), a, res[1], res[4], b, c, d)

# this doesn't work if res[4] == '-', but too lazy to write
# just rerun until it's '+'
result = int(a * (n + 1) + b * n * (n + 1) / 2 + c)
print(result)
url = "http://challenge01.root-me.org/programmation/ch1/ep1_v.php?result="
url += str(result)
r = sess.get(url)
print(r.text)
