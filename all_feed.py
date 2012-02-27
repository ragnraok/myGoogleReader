from urllib import urlencode
from urllib2 import urlopen, Request
import json
import shelve

LOGIN_URL = 'https://www.google.com/accounts/ClientLogin'
EMAIL = ''
PASSWORD = ''

AUTH_FILE_NAME = 'auth'
SID_FILE_NAME = 'sid'
USER_INFO_FILE_NAME = 'user_info'

user_info = {}

def login(email, password):
    global EMAIL
    global PASSWORD
    global user_info

    auth_file = shelve.open(AUTH_FILE_NAME)
    sid_file = shelve.open(SID_FILE_NAME)

    if 'auth' in auth_file.keys() and 'sid' in sid_file.keys():
        auth = auth_file['auth']
        auth_file.close()
        
        sid = sid_file['sid']
        sid_file.close()

        user_info = {'auth' : auth, 'sid' : sid}

    else:
        EMAIL = email
        PASSWORD = password
    
        request = Request(LOGIN_URL,
                          data = urlencode({
                              'service' : 'reader',
                              'Email' : email,
                              'Passwd' : password,
                              'source' : 'ragnarok'
                              }))
        f = urlopen(request)
        
        print 'login url has connected'

        lines = f.read().split()
        auth = lines[2][5:]
    
        auth_file['auth'] = auth
        auth_file.close()

        sid = lines[0][4:]
        sid_file['sid'] = sid
        sid_file.close()

        user_info = {'auth' : auth, 'sid' : sid}
    return user_info

def get_auth():
        auth_file = shelve.open(AUTH_FILE_NAME)
        if 'auth' in auth_file.keys():
                auth = auth_file['auth']
                auth_file.close()
                return auth
        else:
                return None

def get_sid():
        sid_file = shelve.open(SID_FILE_NAME)

        if 'sid' in sid_file.keys():
                sid = sid_file['sid']
                sid_file.close()
                return sid
        else:
                return None

def logout():
        auth_file = shelve.open(AUTH_FILE_NAME)
        sid_file = shelve.open(SID_FILE_NAME)

        if 'auth' in auth_file.keys():
                del auth_file['auth']

        if 'sid' in sid_file.keys():
                del sid_file['sid']

        auth_file.close()
        sid_file.close()

def get_sub_json():
    auth = get_auth()

    if auth:
            headers = {'Authorization': 'GoogleLogin auth=' + auth}

            request = Request('https://www.google.com/reader/api/0/subscription/list?output=json', headers=headers)
            f = urlopen(request)

            return f.read()
    else:
            return None

"""
    return all feed address and title
    title : address
"""
def get_all_feed():
    feed_json = get_sub_json()
    
    if feed_json:

        feed_data = json.loads(feed_json)

        sub = feed_data["subscriptions"]

        feed = {}

        for f in sub:
            link = (f["id"])
            link = link[5:]
            feed[f["title"]] = link

        return feed
    else:
            return None

def sub_a_feed(feed_address):
        auth = get_auth()
        sid = get_sid()

        if auth and sid:
                headers = {'Authorization' : 'GoogleLogin auth=' + auth,
                           'Cookie' : 'SID=' + sid}
                request = Request('https://www.google.com/reader/api/0/token',
                                  headers = headers)
                f1 = urlopen(request)
                token = f1.read()
                f1.close()

                if token:
                        sub_request = Request('https://www.google.com/reader/api/0/subscripiton/quickadd',
                                                 data = urlencode({
                                                         'quickadd' : feed_address,
                                                         'T' : token
                                                  }), headers = headers)
                        f2 = urlopen(sub_request)
                        result = f2.read()
                        
                        json_result = json.loads(result)

                        if json_result["numResults"] != 0:
                                return True
                        else:
                                return False
        else:
                return False


"""
    test this module
"""
if __name__ == '__main__':

    login('okone1288@gmail.com', '13726137977')
    auth = get_auth()

    print auth + '\n'
    
    json_str = get_sub_json()

    print json_str + '\n'

    feed = get_all_feed()
    
    print feed

    input('end')




        
