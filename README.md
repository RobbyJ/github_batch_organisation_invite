# github_batch_organisation_invite
Enable you to invite several users to your organisation using a file containing the emails of each user to be invited, one per line.
This meets with GitHub rate limiting requirements detailed here: https://developer.github.com/v3/#rate-limiting

To run this script, you will need:
- Python 3.x installed to run this script.
- Your organisation name as defined in the URL, e.g. BredaUniversity if your GitHub URL is https://github.com/BredaUniversity
- Your GitHub username.
- A personal OAuth token (please keep private and secure). How you create this is found here: https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/creating-a-personal-access-token
- A file containing only a single valid email per line that are to be each invited to your GitHub organisation.

Command line format (where python is available and is version 3.x):
python github_batchadd.py -o <your_organistionname> -u <github_username> -t <github_personal_token> -f <list_of_emails_input_file>

Example, where the list of emails to invite to the organisation is in a text file called emails.txt (one email per line), and I have used my username and organsiation (and a pretend personal OAuth token):
python github_batchadd.py -o BredaUniversity -u RobbyJ -t PREtendTOKENcode -f emails.txt
