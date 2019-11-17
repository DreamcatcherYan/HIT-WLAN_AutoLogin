#user = '$USERNAME$'
#password = '$PASSWORD$'


#import requests
#import urllib
#import os
#import subprocess

#''' Check if connected to HIT-WLAN.  Only works on Mac OS.  '''
#process =
#subprocess.Popen(['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport','-I'],
#stdout=subprocess.PIPE)
#out, err = process.communicate()
#process.wait()
#out = str(out)
#if not 'HIT-WLAN' in out:
#	print("You have not connected to HIT-WLAN.")
#	os._exit(0)

#''' Check if logged in.  '''
#response = requests.get("http://202.118.253.94:8080")
#if not response.ok:
#	print("Error:", response.status_code)
#	os._exit(0)
#if 'success' in response.url:
#	print("You have already logged in.")
#	os._exit(0)

#''' Get url paraments.  '''
#print("Get http://123.123.123.123...")
#response = requests.get("http://123.123.123.123")
#if not response.ok:
#	print("Error:", response.status_code)
#	os._exit(0)
#else:
#	print("Attempt to login...")

#headers = {
#	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#	'Referer':
#	response.text.strip().lstrip("<script>top.self.location.href='").rstrip("'</script>"),
#	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6)
#	AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
#}
#url = "http://202.118.253.94:8080/eportal/InterFace.do?method=login"
#prefix =
#"<script>top.self.location.href='http://202.118.253.94:8080/eportal/index.jsp?"
#suffix = "'</script>"
#paraments =
#urllib.parse.quote(response.text.strip().lstrip(prefix).rstrip(suffix))
#paraments = urllib.parse.quote(paraments)
#form_data = "userId=" + user + "&password=" + password +
#"&service=&queryString=" + \
#			paraments +
#			"&operatorPwd=&operatorUserId=&validcode=&passwordEncrypt=false"
#response = requests.post(url, data=form_data, headers=headers)
#response.encoding = 'utf-8'

#if not response.ok:
#	print("Error:", response.status_code)
#	os._exit(0)

#if response.json()['result'] == "success":
#	print("Login succeeded.")
#else:
#	print("Login failed:", response.json()['message'])


#import requests
#from bs4 import BeautifulSoup

##url="http://202.118.253.94:8080"
#url = 'http://pythonscraping.com/pages/files/processing.php'
#data = {'firstname':'guan','lastname':'ji'}

#response = requests.post(url=url,data=data)

#response.encoding = response.apparent_encoding
#print(response.text)


#import requests

#url = 'http://pythonscraping.com/pages/cookies/welcome.php'

#payload = {'username':'guan','password':'password'}
#response = requests.post(url,data=payload)
#print(response.cookies.get_dict())

#response =
#requests.get('http://pythonscraping.com/pages/cookies/profile.php',cookies=response.cookies)
#print(response.text)



#import requests

#session = requests.Session()
#payload = {'username':'hahaha','password':'password'}
#r =
#session.post('http://pythonscraping.com/pages/cookies/welcome.php',data=payload)
#print(r.cookies.get_dict())

#r = session.get('http://pythonscraping.com/pages/cookies/profile.php')
#print(r.text)



#import requests

#data = {'userId':'1190200703',
#      'password':'142733242',
#      'queryString':'wlanuserip%3Dc383744909badeed5a365180a39e425d%26wlanacname%3D863c3efef25205fce5c019f4f164e5e0%26ssid%3D%26nasip%3De6e93de2becd39306d64af70461885e8%26snmpagentip%3D%26mac%3D22788239ebd744465ed70b3f9e3aa578%26t%3Dwireless-v2%26url%3D1af7de55847f1c8549f5ec14818707e848cc09cec606ed94%26apmac%3D%26nasid%3D863c3efef25205fce5c019f4f164e5e0%26vid%3Dd6d481a32967de9e%26port%3D9ac18bd93d581e1e%26nasportid%3Db0d2988f370208b6dfc731b936a033761ccde265e602e502b3d83184d0638aaeb9548f7636ce179b',
#      'passwordEncrypt':'false'
#      }

#headers = {'Accept':'*/*',
#         'Accept-Encodin':'gzip, deflate',
#         'Accept-Language':'zh-CN,zh;q=0.9',
#         'Connection': 'keep-alive',
#         'Content-Length': '649',
#         'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
#         'Cookie':'EPORTAL_COOKIE_USERNAME=1190200703;
#         EPORTAL_COOKIE_PASSWORD=142733242; EPORTAL_COOKIE_SERVER=;
#         EPORTAL_COOKIE_SERVER_NAME=%E8%AF%B7%E9%80%89%E6%8B%A9%E6%9C%8D%E5%8A%A1;
#         EPORTAL_COOKIE_OPERATORPWD=; EPORTAL_COOKIE_DOMAIN=;
#         EPORTAL_COOKIE_SAVEPASSWORD=true; EPORTAL_AUTO_LAND=;
#         EPORTAL_USER_GROUP=%E5%AD%A6%E7%94%9F%E7%94%A8%E6%88%B7%E7%BB%84;
#         JSESSIONID=A8E7223E9DA826C2A0AD1BC9C71903A3',
#         'Host':'202.118.253.94:8080',
#         'Origin':'http://202.118.253.94:8080',
#         'Referer':'http://202.118.253.94:8080/eportal/index.jsp?wlanuserip=c383744909badeed5a365180a39e425d&wlanacname=863c3efef25205fce5c019f4f164e5e0&ssid=&nasip=e6e93de2becd39306d64af70461885e8&snmpagentip=&mac=22788239ebd744465ed70b3f9e3aa578&t=wireless-v2&url=1af7de55847f1c8549f5ec14818707e848cc09cec606ed94&apmac=&nasid=863c3efef25205fce5c019f4f164e5e0&vid=d6d481a32967de9e&port=9ac18bd93d581e1e&nasportid=b0d2988f370208b6dfc731b936a033761ccde265e602e502b3d83184d0638aaeb9548f7636ce179b',
#         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)
#         AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97
#         Safari/537.36'
#         }

#url = 'http://202.118.253.94:8080/eportal/InterFace.do?method=login'


#r = requests.post(url,data=data,headers=headers)
#r.encoding = r.apparent_encoding
#print(r.text)

import urllib
import requests
from sys import exit

user='1190200703'
password='142733242'

''' Get url paraments.  '''
print("Get http://123.123.123.123...")
response = requests.get("http://123.123.123.123")
if not response.ok:
	print("Error:", response.status_code)
	os._exit(0)
else:
	print("Attempt to login...")

headers = {
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'Referer':response.text.strip().lstrip("<script>top.self.location.href='").rstrip("'</script>"),
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
}
url = "http://202.118.253.94:8080/eportal/InterFace.do?method=login"
prefix = "<script>top.self.location.href='http://202.118.253.94:8080/eportal/index.jsp?"
suffix = "'</script>"
paraments = urllib.parse.quote(response.text.strip().lstrip(prefix).rstrip(suffix))
paraments = urllib.parse.quote(paraments)
form_data = "userId=" + user + "&password=" + password + "&service=&queryString=" + paraments + "&operatorPwd=&operatorUserId=&validcode=&passwordEncrypt=false"
response = requests.post(url, data=form_data, headers=headers)
response.encoding = 'utf-8'

if not response.ok:
	print("Error:", response.status_code)
	os._exit(0)

if response.json()['result'] == "success":
	print("Login succeeded.")
else:
	print("Login failed:", response.json()['message'])
