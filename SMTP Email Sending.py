import smtplib as sm

ob = sm.SMTP('smtp.gmail.com', 587)
ob.ehlo()
ob.starttls()
ob.login('swapnanilmaity99@gmail.com' , "your_password_here")  # Replace with your actual password
subject = "Test Email"
message = "This is a test email sent from Python script."
message = "subject:{}"


#not complete
