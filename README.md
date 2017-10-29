* You will need the [requests](http://docs.python-requests.org/en/master/) library, if you don't have it
* To authenticate for the api
  1. [Create a personal access token](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/)
  2. Add the token as an environment variable to your bash profile:
  `export GHAPIAUTH=ABCDEFGTOKENVALUE`
* The output is (invalid) html. I just direct the output into a file and open that in a browser `python client.py > output.html`
* To run the script for the commits endpoint to search for the keyword "removed password"
	python client.py -e=commits -q="removed password" > output.html
* To run the script for the code endpoint to search for pom.xml file containing the keyword apache
    python client.py -e=code -q="apache+filename:pom.xml" > output.html
