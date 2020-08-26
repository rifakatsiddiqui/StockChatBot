import requests
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from twilio.rest import Client


def get_date(url): 
	
	
	data = requests.get(url) 

	
	soup1 = soup(data.text, 'html.parser') 

	 
	datelive = soup1.find("p", class_ = "updateTime").text
	
	
	return datelive

def get_nifty(url): 
	
	
	data = requests.get(url) 

	
	soup2 = soup(data.text, 'html.parser') 

	 
	niftylive = soup2.find("div", id = "ltp").text
	
	
	return niftylive


    
    



    




    
if __name__ == "__main__":
        url = "https://economictimes.indiatimes.com/indices/nifty_50_companies"
        

        
        livedate1 = get_date(url)
        nifty1 = "Nifty 50 : " + get_nifty(url)
            

        

        account_sid = 'AC7ab028a6b846bd0d86f555dbac71fe15'
        auth_token = '61b5dde7a7a08fc3ecc1720da590ec02'
        client = Client(account_sid, auth_token)
        message = client.messages.create(
                                      body=livedate1 + nifty1,
                                      from_='whatsapp:+14155238886',
                                      to='whatsapp:+917771972256'
                          )
        

        
        print(message.sid)                              
                                      


       
       
