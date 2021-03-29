from datetime import datetime
startTime = datetime.now()
import telebot

bit=''
bit=input('''FILE ----- f
MESSAGE -----  m

''')
	  
 
	     
t0ken  = <apiToken>

    
try:	     
    b0t = telebot.TeleBot(t0ken)	 
    chat_id = <chat id>
         
    if bit=='f':	     
        fisier = input("Name of File:      ")
        doc = open(fisier, 'rb')
        b0t.send_document(chat_id, doc, timeout=60000)
    if bit =='m':
        message = input("MESSAGE:     ") 
        b0t.send_message(chat_id, message)
 
except Exception as e:
    print(e)
    pass

if bit!='f' and bit!='m':
    print ("Preesd o wrong key!!!")



input("\nEnd of program     "+str(datetime.now()-startTime)+"\n"+"Press ENTER!!!") 



