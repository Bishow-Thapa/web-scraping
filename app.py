import requests, bs4, smtplib

# Scrap part
nrb = requests.get('https://nrb.org.np/fxmexchangerate.php')

soup = bs4.BeautifulSoup(nrb.text, 'html.parser')

# It pretitfy the html in Beautiful Text
soup.prettify()

elem = soup.findAll("tr", {"bordercolor": "#FFFFFF"})

# Tag Obj
tagObj = elem[2]

# getText() methods returns only the text from the tags
sVariable = tagObj.getText()

# newV variable split the variable in lists data type
newV = sVariable.split()

# Currency Name
name = newV[0] + ' ' + newV[1]

# poundInBuying = newV[4]
buying = newV[len(newV) - 2]

# poundInSelling = newV[5]
selling = newV[len(newV) - 1]


# tagObj variable contains the values of uk pound foreign exchange rate

# SendMail part
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()

# Now, call the login() method and pass your username and password as arguments
smtpObj.login('yourgmail.com', 'yourgmailpasswd')

#emailID = ['receiver11@gmail.com', 'receiver22@gmail.com',
#'receiver33@gmail.com', 'receiver44@gmail.com']

smtpObj.sendmail('yourgmail.com', 'receivergmail.com', 'Subject:' + name +' \n' 
+'Buying/Rs ' + str(buying) + 
'\n' + 'Selling/Rs ' + str(selling))

# After sending your email close the SMTP server by calling the quit() method
smtpObj.quit()
