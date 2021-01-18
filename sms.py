import requests

url = "https://www.fast2sms.com/dev/bulk"
a = "hello, this is tesing"
payload = "sender_id=FSTSMS&message="+a+"&language=english&route=p&numbers=7600230727"


#api = O9jTZgx3pDaXEo1eHl8Pyk7YmLvFGMNrIqBQs0SbUWhzut6d2ncR9FaINPyV1mEAr86TL4eGlQi3UfnD

headers = {
'authorization': "O9jTZgx3pDaXEo1eHl8Pyk7YmLvFGMNrIqBQs0SbUWhzut6d2ncR9FaINPyV1mEAr86TL4eGlQi3UfnD",
'Content-Type': "application/x-www-form-urlencoded",
'Cache-Control': "no-cache",
}

response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)




