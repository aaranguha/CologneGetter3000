import smtplib

# Define the email addresses of sender and recipient
sender_email = "aaranguhaca@gmail.com"

# Read in company names and email addresses from a file
with open('company_email_list.txt', 'r') as f:
    company_email_list = [line.strip().split(',') for line in f]

# Loop through each company and send an email
for company, email in company_email_list:
    # Create a message object
    message = f"""Subject: Request for Cologne Tester

Dear {company},

As a passionate cologne enthusiast, I am always on the lookout for new fragrances to add to my collection. I came across your company and was immediately intrigued by the unique scents you offer. I would love the opportunity to try out a free cologne tester from your company, as I believe your fragrances would be the perfect addition to my collection. Your products have received rave reviews and I would be honored to experience them for myself.

I greatly appreciate your time and consideration in this matter. Thank you in advance for your generosity.

Best regards,
Aaran"""

    # Connect to the email server
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()

        # Login to the email account
        smtp.login(sender_email, 'hiyulumnuelzifdo')

        # Send the message
        smtp.sendmail(sender_email, email, message.encode('utf-8'))

        print(f"Email sent to {company} ({email})")

print("All emails sent!")