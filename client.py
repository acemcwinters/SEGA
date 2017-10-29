import os
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-e', '--endpoint')
parser.add_argument('-q', '--query')
args = parser.parse_args()
#print(args.endpoint)

auth_token = os.environ['GHAPIAUTH']
headers = {'Authorization' : 'token ' + auth_token, 'Accept' : 'application/vnd.github.cloak-preview'}
#           'Accept' : 'application/vnd.github.v3.text-match+json

url = 'https://api.github.com/search/' + args.endpoint

#payload = {'q' : 'Removed password'}
payload = {'q' : args.query}


r = requests.get(url, headers=headers, params=payload)

if args.endpoint=='commits':
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
elif args.endpoint=='code':
    for o in r.json()['items']:
	    print('<p>')	
	    url = o['html_url']    
	    print('<a href=\'{0}\'>{0}</a>)'.format(url))
	    print('</p>')
print(r.json())

