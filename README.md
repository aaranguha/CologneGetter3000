#CologneGetter3000
The CologneGetter3000 is a Python script that sends an email to a list of companies requesting a free cologne tester. This script uses the smtplib library to connect to the email server and send the message.

Prerequisites
Python 3.x
An email account with SMTP access (e.g. Gmail)
How to Use
Clone this repository or download the colognegetter3000.py file.

Create a file named company_email_list.txt in the same directory as the script.

In the company_email_list.txt file, add each company name and email address on a new line separated by a comma. For example:

graphql
Copy code
Company A, company_a@example.com
Company B, company_b@example.com
Company C, company_c@example.com
Open the colognegetter3000.py file and replace the sender_email variable with your own email address.

Replace the password in smtp.login(sender_email, 'hiyulumnuelzifdo') with your own email account password or use environment variables for storing the sensitive information.

Save and close the file.

Open the terminal and navigate to the directory where the script is saved.

Run the script using the command python colognegetter3000.py.

The script will loop through each company in the company_email_list.txt file and send an email requesting a free cologne tester.

Once all emails have been sent, the script will print "All emails sent!".

Notes
This script uses the starttls() method to establish a secure connection to the email server before login and sending the message.
The message body is formatted using f-strings to personalize the email with each company's name.
It is recommended to use a disposable email address when sending these types of emails to avoid spamming your personal or professional email account.

P.S.:

If anyone finds a list of emails for Cologne Companies, please reach out!