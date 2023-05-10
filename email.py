#take email address from user 
email = input('Ingrese su mail: ').strip()

#Slice and store username 
username = email[:email.index('@')]

#slice and store domain name 
domain = email[email.index('@')+1:]

#Verifica de donde es el dominio 
email_domains = {
    "gmail.com": "Google",
    "hubspot.com": "HubSpot",
    "protonmail.com": "ProtonMail",
    "icloud.com": "iCloud Mail",
    "zoho.com": "Zoho Mail",
    "outlook.com": "Outlook",
    "mailbox.org": "Mailbox.org"
}

if domain in email_domains:
    print(f"Esta dirección de correo electrónico pertenece a {email_domains[domain]}.")

#format message 
output = "Su nombres es  '{} Y su dominio es  '{} ".format(username,domain)

#display output message 
print(output)

