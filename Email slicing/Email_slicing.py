import smtplib

username = ''
password = ''

sent_from = username
n = int(input('Enter the number of recipents\n'))
to = []
for _ in range(n):
    ele = input()
    to.append(ele)

subject = input('Enter the subject\n')
body  = input('Enter the body\n')

email_txt = """\
    From:%s
    To:%s
    Subject:%s

    %s    
    """%(sent_from, ",".join(to), subject, body)

# try:
#     smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#     smtp_server.ehlo()
#     smtp_server.login(username, password)
#     smtp_server.sendmail(sent_from, to, email_txt)
#     smtp_server.close()
#     print ("Email sent successfully!")
# except Exception as ex:
#     print ("Something went wrong….",ex)
try: 
    #Create your SMTP session 
    smtp = smtplib.SMTP('smtp.gmail.com', 587) 

   #Use TLS to add security 
    smtp.starttls() 

    #User Authentication 
    smtp.login(username, password)
    
    #Defining The Message 
    message = message = 'Subject: {}\n\n{}'.format(subject, body)

    
    #Sending the Email
    smtp.sendmail(username, ",".join(to), message) 

    #Terminating the session 
    smtp.quit() 
    print ("Email sent successfully!") 

except Exception as ex: 
    print("Something went wrong....", ex) 
