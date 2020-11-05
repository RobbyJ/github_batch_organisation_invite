# An OAuth access token is needed, see: https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/creating-a-personal-access-token
# Rate limit is 500 per day or 50 if you do not meet certain requirements.
# For more informations see: https://docs.github.com/en/free-pro-team@latest/rest/reference/orgs#set-organization-membership-for-a-user
import requests
import time
import sys
import getopt

examplecommandline = 'Expecting 4 arguments:   github_batchadd.py -o <your_organistionname> -u <github_username> -t <github_personal_token> -f <list_of_emails_input_file>'

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
invitecount = 0
for email in content:
    if (email!=""):
        r = requests.post('https://api.github.com/orgs/' + org + '/invitations', headers=h, json={"email":email}, auth = (username, token))
        time.sleep(1)
        print(r.status_code, r.reason)
        print(r.text)
        if (r.status_code!=201):
            print("Error occurred. " + str(invitecount) + " have been invited. See error information above.")
            sys.exit(4)
        invitecount+=1
print("Finished. " + str(invitecount) + " has been invited.")
