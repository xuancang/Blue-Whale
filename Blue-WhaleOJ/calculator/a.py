import re
import requests
ss=requests.session()
a=ss.get('http://123.207.149.64:23331/calculator/')
print(a.text)
coo=ss.cookies
#print(coo)
ss.cookies.update(coo)
print(ss.cookies.get_dict())
pattern = re.compile(r'\d+')
#print (a.text)
#b= re.findall(r"/d{7} \s \\+ \s /d{6} \s \\* \s /d{5} \s \\- \s /d{5}",a.text)
b= re.findall(r'\d+',a.text)
s=int(b[8])+int(b[9])*int(b[10])-int(b[11])
#a=ss.get('http://123.207.149.64:23331/calculator/',data=str(s),cookies=coo)
a=ss.get('http://123.207.149.64:23331/calculator/?answer='+str(s),cookies=coo)
print(a.text)

