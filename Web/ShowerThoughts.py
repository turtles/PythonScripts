import requests
import json

# Gets 5 'hot' submissions from showerthoughts reddit using the Requests package

numThoughts = 10

r = requests.get('https://www.reddit.com/r/showerthoughts/hot.json?limit={}'.format(numThoughts), headers = {'User-agent': 'showerbotpyscript 1.0'})

if r.status_code != 200:
    print('Warning: HTTP Status code {}', r.status_code)

data = json.loads(r.text)

for i in range(0, numThoughts):
    print(str(i+1) + '. ' + data["data"]["children"][i]["data"]["title"])
