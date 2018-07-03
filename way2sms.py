import requests
import keys
from urllib import parse

def send_msg(msg, receivers_num=keys.receiver_num):
    URL = 'http://www.way2sms.com/content/index.html/Login1.action'

    payload = {
        'username': keys.username,
        'password': keys.password
    }

    iam_not_a_bot_header = {
        'User-Agent': 'User-Agent, Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120'   
    }

    try:
        with requests.Session() as s:
            # s.headers.update()
            way2sms_page = s.post(URL, data=payload, headers = iam_not_a_bot_header)
            token = dict(parse.parse_qs(parse.urlsplit(way2sms_page.url).query))
            msg_payload = {
                'ssaction': 'ss',
                'Token': token['Token'][0],
                'mobile': receivers_num,
                'message': msg,
                'msgLen': '136'
            }
            s.post('http://www.way2sms.com/smstoss.action?', 
                data=msg_payload, 
                headers={'Referer': 'http://www.way2sms.com/sendSMS?Token=' + token['Token'][0]}
            )
            print('Done')
    except Exception as ex:
        print('Error: ' + str(ex))