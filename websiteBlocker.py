import tkinter as tk
from tkinter import ttk
import time
from datetime import datetime as dt


def func():

    if dateA < dt.now() < dateB:
        global secondFlag
        secondFlag = True
        aLable.configure(text='Working hours')

        cLable.configure(text='Time Now: ' + str(dt.now()))
        with open(hostsPath, 'r+') as file:
            content = file.read()
            for website in web_sites_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + ' ' + website + '\n')
    else:
        secondFlag = False


def stop():
    global globalFlag

   

    for site in web_sites_list:

        with open(hostsPath, 'r+') as file:
            content = file.readlines()
            file.seek(0)

            for line in content:

                if site not in line.strip('\n'):
                    file.write(line)

                    # print line

            file.truncate()
            file.close()

    globalFlag = False


if __name__ == '__main__':
    hostsPath = r"/etc/hosts"
    redirect = '127.0.0.1'
    globalFlag = True
    secondFlag = False
    web_sites_list = []

    f = open('demofile.txt', 'r')
    Lines = f.readlines()
    f.close()

    

    for i in range(len(Lines)):
        if i > 1:
            web_sites_list.append(Lines[i].strip('\n'))

    

    dateA = dt.strptime(str(dt.now()).split(' ')[0] + ' '
                        + Lines[0].strip('\n'), '%Y-%m-%d %H:%M')
    dateB = dt.strptime(str(dt.now()).split(' ')[0] + ' '
                        + Lines[1].strip('\n'), '%Y-%m-%d %H:%M')

    window = tk.Tk()
    window.geometry('450x160')
    window.title('TITLE')

    aLable = ttk.Label(window, text='Nothing')
    aLable.grid(column=0, row=0, padx=60, pady=4)

    bLable = ttk.Label(window, text='Working hours: ' + str(dateA)
                       + ' - ' + str(dateB))
    bLable.grid(column=0, row=1, padx=8, pady=4)

    cLable = ttk.Label(window, text='Time Now: ' + str(dt.now()))
    cLable.grid(column=0, row=2, padx=8, pady=4)

    actionA = ttk.Button(window, text='Start', command=func)
    actionA.grid(column=0, row=3, padx=8, pady=4)

    actionB = ttk.Button(window, text='Stop', command=stop)
    actionB.grid(column=0, row=4, padx=8, pady=4)

    while globalFlag:
    	if secondFlag:
    	    func()
    	window.update_idletasks()
    	window.update()

