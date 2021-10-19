import requests
import smtplib 
import time
#python stock price notifier bot pseudocode

api_key = 'stonks'
password= 'stonkes' 

def send_mail(password):
  server = 
('smtp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.login('pythonstocktracker21sai@gmail.com',password)
  subject= 'test'
  body = 'price down'

  msg= f'subject: {subject} {body}'

  server.sendmail(
  'pythonstocktracker21sai@gmail.com',
  'pythonstocktracker21sai@gmail.com',
  msg
  )
  print('email is sent')
  server.quit()


def price_tracker(api_key,password):
  prices = requests.get(f'https://financialmodelingprep.com/api/v3/quote/AAPL?apikey={api_key}').json()
  stockPrice = prices[0]['price']
  print(stockPrice)
  if stockPrice < 140:
    send_mail(password)
 
#run evrey 10 minutes
while(True):
  price_tracker(api_key,password)
  time.sleep(600)