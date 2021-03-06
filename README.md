# github_batch_organisation_invite
Enable you to invite several users to your organisation using a file containing the emails of each user to be invited, one per line.
Rate limit is 500 per day or 50 if you do not meet certain requirements.
For more informations see: https://docs.github.com/en/free-pro-team@latest/rest/reference/orgs#set-organization-membership-for-a-user

Another option, if using GitHub Classroom, is where you invite using an assignment link or add multiple users at once through the rooster creation. With the assignment you can automatically create associated repositories and create teams if you want. See: https://classroom.github.com/help/creating-an-individual-assignment https://classroom.github.com/help/create-group-assignments and https://classroom.github.com/help/import-roster-from-lms

To run this script, you will need:
- Python 3.x installed (tested with 3.8).
- Your organisation name as defined in the URL, e.g. BredaUniversity if your GitHub URL is https://github.com/BredaUniversity
- Your GitHub username.
- A personal OAuth token (please keep private and secure). How you create this is found here: https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/creating-a-personal-access-token
- A file containing only a single valid email per line that are to be each invited to your GitHub organisation.

Command line format (where python is available and is version 3.x):

python github_batchadd.py -o <your_organistionname> -u <github_username> -t <github_personal_token> -f <list_of_emails_input_file>

Example, where the list of emails to invite to the organisation is in a text file called emails.txt (one email per line), and I have used my username and organsiation (and a pretend personal OAuth token):

python github_batchadd.py -o BredaUniversity -u RobbyJ -t PREtendTOKENcode -f emails.txt
