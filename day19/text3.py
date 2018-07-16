"""

发送短信

Version: 0.1
Author: 骆昊
Date: 2018-03-23

"""

import urllib.parse
import http.client
import json

host = "106.ihuyi.com"
sms_send_uri = "/webservice/sms.php?method=Submit"

params = urllib.parse.urlencode({
    'account': '',
    'password': '',
    'content': '您的验证码是：147258。请不要把验证码泄露给其他人。',
    'mobile': '18281599458',
    'format': 'json'
})
print(params)
headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
conn = http.client.HTTPConnection(host, port=80, timeout=10)
conn.request('POST', sms_send_uri, params, headers)
response = conn.getresponse()
response_str = response.read()
jsonstr = response_str.decode('utf-8')
print(json.loads(jsonstr))
conn.close()
