import os
import requests

auth_token = os.environ['GHAPIAUTH']
headers = {'Authorization' : 'token ' + auth_token, 'Accept' : 'application/vnd.github.cloak-preview'}
#           'Accept' : 'application/vnd.github.v3.text-match+json

url = 'https://api.github.com/search/commits'

payload = {'q' : 'Removed password'}


r = requests.get(url, headers=headers, params=payload)

for o in r.json()['items']:
    print('<p>')
    date = o['commit']['committer']['date']
    message = o['commit']['message']
#    patch = o['files']['patch']
    url = o['html_url']
    print(date)
    print(message)
 #   print(patch)
    print('<a href=\'{0}\'>{0}</a>)'.format(url))
    print('</p>')
#print(r.json())

