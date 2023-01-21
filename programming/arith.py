import requests

"""
TODO: i have parsed out the numbers, I just need to work out the formula
to calculate it now and put that in the 'results' variable
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
res = parse(r.text)
print(parse(r.text), res[0], res[1], res[4], res[8], res[13],
parse_more(res[18]))

result = 0
url = "http://challenge01.root-me.org/programmation/ch1/ep1_v.php?result="
url += str(result)
r = sess.get(url)
print(r.text)
