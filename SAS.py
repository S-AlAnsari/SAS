import os
import subprocess
import sys
import PySimpleGUI as sg
from subprocess import Popen
def popUp(account):
    if(account == 'first'):
        # Add a touch of color
        # All the stuff inside your window.
        layout = [  [sg.Text('First account')],
                    [sg.Text('Username'), sg.InputText(size=(10,30))],
                    [sg.Button('Ok'), sg.Button('Cancel')] ]

        # Create the Window
        window = sg.Window('SAS', layout)
        # Event Loop to process "events" and get the "values" of the inputs
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
                break
            saveUsername('first',values[0])
            createBatch('first')
            window.close()
    else:
        # Add a touch of color
        # All the stuff inside your window.
        layout = [  [sg.Text('Second account')],
                    [sg.Text('Username'), sg.InputText(size=(10,30))],
                    [sg.Button('Ok'), sg.Button('Cancel')] ]

        # Create the Window
        window = sg.Window('SAS', layout,size=(200,100))
        # Event Loop to process "events" and get the "values" of the inputs
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
                break
            saveUsername('second',values[0])
            createBatch('second')
            window.close()

def saveUsername(account,username):
    if(account == 'first'):
        f = open("first account.dat", "w")
        f.write(username)
        f.close()
    else:
        f = open("second account.dat", "w")
        f.write(username)
        f.close
    
def createBatch(account):
    if(account == 'first'):
        reader = open("first account.dat",'r')
        username = reader.readline()
        f = open("first account.bat","w")
        reader.close()
        f.write('@echo off\ntaskkill.exe /F /IM steam.exe\n')
        f.write('reg add "HKCU\Software\Valve\Steam" /v AutoLoginUser /t REG_SZ /d '+username+' /f')
        f.write('\nreg add "HKCU\Software\Valve\Steam" /v RememberPassword /t REG_DWORD /d 1 /f\nstart steam://open/main\nexit')
        f.close()
    elif(account == 'second'):
        reader = open("second account.dat",'r')
        username = reader.readline()
        reader.close()
        f = open("second account.bat","w")
        f.write('@echo off\ntaskkill.exe /F /IM steam.exe\n')
        f.write('reg add "HKCU\Software\Valve\Steam" /v AutoLoginUser /t REG_SZ /d '+username+' /f')
        f.write('\nreg add "HKCU\Software\Valve\Steam" /v RememberPassword /t REG_DWORD /d 1 /f\nstart steam://open/main\nexit')
        f.close()
cwd = os.getcwd()
if(os.path.isfile(cwd+'/first account.dat') and os.path.isfile(cwd+'/second account.dat')):
    reader = open("first account.dat",'r')
    firstUsername = reader.readline()
    reader = open("second account.dat",'r')
    secondUsername = reader.readline()
    layout=[ [sg.Button(firstUsername),
            sg.Text(''),sg.Button('Edit')],
            [sg.Button(secondUsername),
            sg.Text(''),sg.Button('Edit')],[sg.Button('Exit')]]
    sg.theme('Dark Teal 9')
    window = sg.Window('SAS',layout,size=(200,100))
    while True:             
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event in('Edit'):
            popUp('first')
        elif event in(firstUsername):
            
            subprocess.call([cwd+"/first account.bat"], shell=False)
            # p = Popen()
            # stdout, stderr = p.communicate()
        elif event in(secondUsername):
            subprocess.call([cwd+"/second account.bat"], shell=False)
            # p = Popen("/first account.bat", cwd=cwd2)
            # stdout, stderr = p.communicate()
        elif event in('Second Account'):
            subprocess.call([cwd+"/second account.bat"], shell=False)
            # p = Popen("/first account.bat", cwd=cwd2)
            # stdout, stderr = p.communicate()+
        else:
            popUp('second')

    window.close()
else:
    layout=[ [sg.Button('First Account     '),
            sg.Text(''),sg.Button('Edit')],
            [sg.Button('Second Account'),
            sg.Text(''),sg.Button('Edit')],[sg.Button('Exit')]]
    sg.theme('Dark Teal 9')
    window = sg.Window('SAS',layout)
    while True:             
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event in('Edit'):
            popUp('first')
        elif event in('First Account     '):
            
            subprocess.call([cwd+"/first account.bat"], shell=False)
            # p = Popen()
            # stdout, stderr = p.communicate()
        elif event in('Second Account'):
            subprocess.call([cwd+"/second account.bat"], shell=False)
            # p = Popen("/first account.bat", cwd=cwd2)
            # stdout, stderr = p.communicate()+
        else:
            popUp('second')

    window.close()


