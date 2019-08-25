import requests
from bs4 import BeautifulSoup


#login to GitHub using Request library
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}

login_data = {
'commit':	'Sign+in',
'utf8':	'✓',
'login':	'XXXXXXXXXXXXXXXX',
'password':	'XXXXXXXXXXXXXXXX',
'webauthn-support':	'supported',
'required_field_638e':'',
}

with requests.Session() as s:
    url = "https://github.com/session"
    r = s.get(url,headers=headers)
    soup = BeautifulSoup(r.text,'html.parser')
    login_data['authenticity_token'] = soup.find(attrs={'name':'authenticity_token'})['value']
    login_data['timestamp'] = soup.find(attrs={'name':'timestamp'})['value']
    login_data['timestamp_secret'] = soup.find(attrs={'name':'timestamp_secret'})['value']
    
    r = s.post(url,headers=headers,data=login_data)
    print(r.text)
    
