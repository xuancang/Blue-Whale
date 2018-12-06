import re
import requests
while 1:
   	ss=requests.session()
   	a=ss.get('http://10.112.169.84/domjudge')
   	print(a.text)
   	coo=ss.cookies
   	#print(coo)
   	ss.cookies.update(coo)
   	print(a.text)

