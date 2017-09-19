import requests
import json

# Gets 'hot' submissions from showerthoughts reddit using the Requests package

# Ask user for count
inputNumThoughts = input("Number of thoughts (1-100): ")

try:
    int(inputNumThoughts)
except ValueError:
    print("Invalid number: {}".format(inputNumThoughts))
    exit(1)

numThoughts = int(inputNumThoughts)
numThoughts = max(1, min(100, numThoughts))

# Get listings from http request
r = requests.get('https://www.reddit.com/r/showerthoughts/hot.json?limit={}'.format(numThoughts), headers = {'User-agent': 'showerbotpyscript 1.0'})

if r.status_code != 200:
    print('Warning: HTTP Status code {}', r.status_code)

data = json.loads(r.text)

# Print listings
for i in range(0, numThoughts):
    print(str(i+1) + '. ' + data["data"]["children"][i]["data"]["title"])
