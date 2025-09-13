import requests as req
import base64

def Invite_Code_Generate():
    url = "http://2million.htb/api/v1/invite/generate"
    try:
        r = req.post(url)
        code = r.json()['data']['code']
        decoded = base64.b64decode(code)
        print("The invite code: " + decoded.decode())
    except Exception as e:
        print("We couldn't fetch the data from the requested API: " + str(e))
