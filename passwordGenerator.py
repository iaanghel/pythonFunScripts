import random


def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

def passWord():
	Letter1=chr(random.randint(65,90)) #Uppercase
	Letter2=chr(random.randint(65,90)) #Uppercase
	Letter3=chr(random.randint(65,90)) #Uppercase
	Letter4=chr(random.randint(97,122)) #lowerCase
	Letter5=chr(random.randint(97,122)) #lowerCase
	Letter6=chr(random.randint(97,122)) #lowerCase
	Letter7=chr(random.randint(33,47)) #SpecialChar
	Letter8=chr(random.randint(33,47)) #SpecialChar
	Letter9=chr(random.randint(48,57)) #Digits
	Letter10=chr(random.randint(48,57)) #Digits
	Letter11=chr(random.randint(48,57)) #Digits

	password = Letter1 + Letter2 +Letter3 + Letter4+ Letter5 +Letter6 + Letter7 + Letter8 +Letter9 + Letter10+Letter11 
	password = shuffle(password)
	userName = raw_input("UserName :")
	file = open("Passwords.txt","a")
	file.write(userName + "		"+ password+"\n" )	
	file.close()
	
	response = raw_input("Want to get another password?(y/n)")
	if response== 'y' or response =='Y':
		passWord()
	else:
		return
		

if __name__ == "__main__":
    passWord()	
	


