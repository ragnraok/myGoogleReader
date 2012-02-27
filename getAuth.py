from urllib import urlencode
from urllib2 import urlopen, Request

LOGIN_URL = 'https://www.google.com/accounts/ClientLogin'
EMAIL = 'okone1288@gmail.com'
PASSWORD = '13726137977'

request = Request(LOGIN_URL, data = urlencode({
    'service': 'reader',
    'Email': EMAIL,
    'Passwd': PASSWORD,
    'source': 'scroll',
}))

f = urlopen(request)

lines = f.read().split()
auth = lines[2][5:]

print auth
