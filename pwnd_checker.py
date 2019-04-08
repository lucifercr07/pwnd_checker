import click
import requests
import json

url = 'https://haveibeenpwned.com/api/'
api_version = '2'
headers = {'api-version':api_version}

@click.command()
@click.option('--pwnd_account', default=None, help='Checks if account has been breached')
@click.option('--passwd', default=None, help='Checks if password has been breached')

def main(pwnd_account, passwd):
	if pwnd_account:
		breached_account(pwnd_account)
	else:
		click.secho('Usage: passwd_checker.py --help', fg="red", bold=True)

def breached_account(pwnd_account):
	try:
		response = requests.get(url + 'breachedaccount/'+ pwnd_account, headers = headers)
		if response.status_code == requests.codes.not_found:
			print "Congrats!! Your account hasn't been breached yet."
			return 0

		print "Account has been breached at following domains: \n"
		json_response = json.loads(response.text)
		for response in json_response:
			print "1. Website Name: {0}".format(response['Name'])
			print "2. Domain: {0}".format(response['Domain'])
			print "3. Breach date: {0}\n".format(response['BreachDate'])
	except Exception as e:
		click.secho(str(e), fg="red", bold=True)

if __name__ == '__main__':
	main()