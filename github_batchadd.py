# An OAuth access token is needed, see: https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/creating-a-personal-access-token
import requests
import time
import sys
import getopt

# Avoid rate limit cap (5000 per hour)
# 60 minutes * 60 seconds / 5000 rate limit = 0.72 seconds for each transaction
ratelimitdelay = 1
examplecommandline = 'Expecting 4 arguments:   github_batchadd.py -o <your_organistionname> -u <github_username> -t <github_personal_token> -f <list_of_emails_input_file>'

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

if (len(sys.argv)!=9):
    print(examplecommandline)
    sys.exit(2)

org = ''
username = ''
token = ''
inputfile = ''

try:
    opts, args = getopt.getopt(sys.argv[1:],"ho:u:t:f:",["organisation=","username=","token=","listofemailsfile="])
except getopt.GetoptError:
    print(examplecommandline)
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print(examplecommandline)
        sys.exit(0)
    elif opt in ("-o", "--iorganisation"):
        org = arg
    elif opt in ("-u", "--iusername"):
        username = arg
    elif opt in ("-t", "--itoken"):
        token = arg
    elif opt in ("-f", "--ifile"):
        inputfile = arg
h = {
    'Content-type': 'application/json',
    'Accept' : 'application/vnd.github.v3+json'
}

try:
    with open(inputfile) as f:
        content = f.readlines()
except:
    print('File could not be opened.')
    sys.exit(3)

content = [line.strip() for line in content]
for email in content:
    if (email!=""):
        r = requests.post('https://api.github.com/orgs/' + org + '/invitations', headers=h, json={"email":email}, auth = (username, token))
        time.sleep(ratelimitdelay)
        print(r.status_code, r.reason)
        print(r.text)
        if (r.status_code!=201):
            sys.exit(4)
