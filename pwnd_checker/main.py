import click
import requests
import json

from breached_passwd import BreachedPassword

url = 'https://haveibeenpwned.com/api/'
api_version = '2'
headers = {'api-version':api_version}

def get_response(api, headers):
	response = requests.get(url + api, headers = headers)
	if response.status_code == requests.codes.not_found:
		return None

	return response

def breached_domain(pwnd_website):
	try:
		response_json = get_response('breach/'+ pwnd_website, headers)
		if response_json is None:
			print "{0} website hasn't been breached yet.".format(pwnd_website)
			return 0

		print "{0} has been breached. Details are following: \n".format(pwnd_website)
		json_response = json.loads(response_json.text)
		print "1. Breach date: {0}".format(json_response['BreachDate'])
		print "2. Breach details: {0}\n".format(json_response['Description'])
		if json_response['IsSensitive']:
			print "3. Breach is sensitive. Please change your email if associated with this domain."
	except Exception as e:
		click.secho(str(e), fg="red", bold=True)

def breached_account(pwnd_account):
	try:
		response_json = get_response('breachedaccount/'+ pwnd_account, headers)
		if response_json is None:
			print "Congrats!! Your account hasn't been breached yet."
			return 0

		print "Account has been breached at following domains: \n"
		json_response = json.loads(response_json.text)
		for response in json_response:
			print "1. Website Name: {0}".format(response['Name'])
			print "2. Domain: {0}".format(response['Domain'])
			print "3. Breach date: {0}\n".format(response['BreachDate'])
	except Exception as e:
		click.secho(str(e), fg="red", bold=True)

@click.command()
@click.option('--pwnd_account', default=None, help='Checks if account has been breached')
@click.option('--pwnd_website', default=None, help='Checks if domain has been breached,e.g: adobe')
@click.option('--passwd', default=None, help='Checks if password has been breached')

def main(pwnd_account, pwnd_website, passwd):
	if pwnd_account:
		breached_account(pwnd_account)
	elif pwnd_website:
		breached_domain(pwnd_website)
	elif passwd:
		breached_pass_object = BreachedPassword(url, headers)	
	else:
		click.secho('Usage: passwd_checker.py --help', fg="red", bold=True)

if __name__ == '__main__':
	main()