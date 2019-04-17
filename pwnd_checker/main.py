import click
import requests
import json
import time

from breached_passwd import BreachedPassword

url = 'https://haveibeenpwned.com/api/'
api_version = '2'
headers = {'api-version':api_version,
           'user-agent':'pwnd_checker'}

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
      #TODO: Fix Description printing
      print "2. Breach details: {0}\n".format(json_response['Description'])
      if json_response['IsSensitive']:
         print "3. Breach is sensitive. Please change your email if associated with this domain."
   except Exception as e:
      click.secho(str(e), fg="red", bold=True)

def breached_account(pwnd_account):
   try:
      response_json = get_response('breachedaccount/'+ pwnd_account, headers)
      if response_json is None:
         click.secho("Congrats!! Your account hasn't been breached yet.", fg='green', bold=True)
         return 0

      print "Account has been breached at following domains: \n"
      json_response = json.loads(response_json.text)
      for response in json_response:
         print "1. Website Name: {0}".format(response['Name'])
         print "2. Domain: {0}".format(response['Domain'])
         print "3. Breach date: {0}\n".format(response['BreachDate'])
   except Exception as e:
      click.secho(str(e), fg="red", bold=True)

#class to handle optional args like: passwd
class CommandWithOptionalPassword(click.Command):
   def parse_args(self, ctx, args):
      for i, a in enumerate(args):
         if args[i] == '--passwd':
            try:
               passwd = args[i + 1] if not args[i + 1].startswith('--') else None
            except IndexError:
               passwd = None
            if not passwd:
               passwd = click.prompt('Password', hide_input=True)
               args.insert(i + 1, passwd)
      return super(CommandWithOptionalPassword, self).parse_args(ctx, args)

@click.command(cls=CommandWithOptionalPassword)
@click.option('--pwnd_account', default=None, help='Checks if account has been breached')
@click.option('--pwnd_website', default=None, help='Checks if domain has been breached, e.g: adobe')
@click.option('--passwd', help='Checks if password has been breached(will prompt if not supplied)')

def main(pwnd_account, pwnd_website, passwd):
   if pwnd_account:
      breached_account(pwnd_account)
   elif pwnd_website:
      breached_domain(pwnd_website)
   elif passwd:
      #TODO: make passwd input as hidden
      breached_pass = BreachedPassword(headers)
      passwd_breach_count = breached_pass.check_passwd_breach(passwd)
      if passwd_breach_count != 0:
         sad_emoji = '\U0001F61E'
         click.secho("OOPS!! Looks like your password has been breached", fg="red", bold=True)
         click.secho("Times it appeared in the breach dataset: {0}".format(passwd_breach_count),
                     fg="red", bold=True)
         print sad_emoji.decode('unicode-escape')
         #TODO: integrate with domain, i.e if email leaked dataset open email in browser with
         #suggested pass and make the below part mandatory
         if click.confirm('Do you want new password suggestion?'):
            click.secho('Getting you new pass...', fg='green', bold=True)
            time.sleep(1)
            click.secho('Please use this secure pass: {0}'.format(breached_pass.get_new_passwd()),
                        fg='green', bold=True)
         else:
            click.secho('Please change your password ASAP.', fg='red', bold=True)    
      else:
         #TODO: Add current pass strength check and provide suggestions based on that.
         click.secho('Congrats!! Your passwords not been breached.', fg='green', bold=True)
   else:
      click.secho('Usage: passwd_checker.py --help', fg="red", bold=True)

if __name__ == '__main__':
   main()
