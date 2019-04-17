# pwnd_checker
This application allows you to check if your account has been breached and credentials are publicly accessible. Also checks if your password has been breached, and suggests strong passwords in that case.

# Installation via pip:
`pip install pwnd-checker`
# Installation via github:
1. Clone the github project.
2. `cd pwnd_checker`
2. Run `python setup.py install`
# pwnd_checker usage:
```sh
root@ubuntu:/home/github/passwd_checker# pwnd_checker --help
Usage: pwnd_checker [OPTIONS]

Options:
  --pwnd_account TEXT  Checks if account has been breached
  --pwnd_website TEXT  Checks if domain has been breached, e.g: adobe
  --passwd TEXT        Checks if password has been breached(will prompt if not
                       supplied)
  --help               Show this message and exit.
```

**P.S: Thanks to [Troy Hunt](https://www.troyhunt.com/) for [pwned apis](https://haveibeenpwned.com/API/v2) this application leverages these apis.**
