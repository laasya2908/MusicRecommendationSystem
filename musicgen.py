from tkinter import *
import mysql.connector
import webbrowser
import random
import cv2
import time

mydb=mysql.connector.connect(host='localhost',user='root',passwd='root')#password depending on the user pc
mc=mydb.cursor()
mc.execute("use dbms")

#https://youtube.com/playlist?list=PL9bw4S5ePsEF-J_tIORZ6xE_OXkGuKjjY
#https://youtube.com/playlist?list=PLB00151086C9310A0
#https://youtube.com/playlist?list=PL9bw4S5ePsEG1Ovrxj9o2RLx43ALFoFyU
#https://youtube.com/playlist?list=PLCWmS9uzEfpUsYKnghK8VUo5o4Fogm3u8
def Hindi():
    try:
        if final=="happy" or final=="neutral":
            mc.execute("use dbms")
            mc.execute("select link from Hplaylist where lang='hindi';")
            op=mc.fetchall() #op= type "list", and the elements are of type "tuple":[('https://',),('https:',)]
            res=random.randint(0,len(op)) #ex: res=3
            myLink.set(op[res]) #myText= op[3]
            x=str(op[res]) # "('https://youtube.com/playlist?list=PLB00151086C9310A0',)"
            y=len(x)
            webbrowser.open(x[2:y-3]) #https-----.com. 
        if final=="sad":
            mc.execute("use dbms")
            mc.execute("select link from Splaylist where lang='hindi';")
            op=mc.fetchall() #op= type "list", and the elements are of type "tuple":[('https://',),('https:',)]
            res=random.randint(0,len(op)) #ex: res=3
            myLink.set(op[res]) #myText= op[3]
            x=str(op[res]) # "('https://youtube.com/playlist?list=PLB00151086C9310A0',)"
            y=len(x)
            webbrowser.open(x[2:y-3]) #https-----.com. 
    except:
        print("Error encountered!")

def English():
    try:
        if final=="happy" or final=="neutral":
            mc.execute("use dbms")
            mc.execute("select link from Hplaylist where lang='english';")
            op2=mc.fetchall()
            res2=random.randint(0,len(op2))
            myLink.set(op2[res2])
            z=str(op2[res2])
            w=len(z)
            webbrowser.open(z[2:w-3])
        if final=="sad":
            mc.execute("use dbms")
            mc.execute("select link from Splaylist where lang='english';")
            op2=mc.fetchall()
            res2=random.randint(0,len(op2))
            myLink.set(op2[res2])
            z=str(op2[res2])
            w=len(z)
            webbrowser.open(z[2:w-3])
    except:
        print("Error encountered!")


def Camera():
    import cv2

    cam = cv2.VideoCapture(0)

    cv2.namedWindow("camera")
    
    img_counter = 0

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("camera", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
    cam.release()
    cv2.destroyAllWindows()
    
    emotion()


def emotion():
    import matplotlib.pyplot as plt
    from deepface import DeepFace
    # read image
    import os
    import glob

    ts = 0
    found = None
    for file_name in glob.glob("C:/Users/varun/Documents/python practice/EMOTICA/*"): #subject to your path where musicgen.py is saved
        fts = os.path.getmtime(file_name)
        if fts > ts:
            ts = fts
            found = file_name

    print(found)
    img = cv2.imread(found)
    try:
        # call imshow() using plt object 
        plt.imshow(img[:,:,::-1])
  
        # display that image
        plt.show()
  
        # storing the result
        result = DeepFace.analyze(img,actions=['emotion'],enforce_detection=False)
        '''res = DeepFace.analyze(img,actions=['age'])'''
        global final
        final = result[0]['dominant_emotion']
        # print result
        '''print(result)
        print("the dominant emotion: ",result['dominant_emotion'])
        print("the approximate age of the person: ",res['age'])'''
        emo=StringVar()
        Label(root, text='The dominant emotion: ',font=('Helveticabold',15)).grid(row=8, sticky=W)
        text=Label(root, text="", textvariable=emo, font=('Helveticabold',15),fg="purple",cursor="hand2").grid(row=9,column=0, sticky=W)
        emo.set(final)

        Label(root, text='Select your language:',font=('Helveticabold',13)).grid(row=11,sticky=W)
        b2 = Button(root, text="English",font=('Helveticabold',15),relief=RAISED, command=English)
        b2.grid(row=12, column=0,columnspan=2, rowspan=1,sticky=W+E+N+S, padx=4, pady=4)
        b3 = Button(root, text="Hindi",font=('Helveticabold',15),relief=RAISED, command=Hindi)
        b3.grid(row=13, column=0,columnspan=2, rowspan=1,sticky=W+E+N+S, padx=4, pady=4)
    except:
        Label(root, text='See you later!!',font=('Helveticabold',15)).grid(row=15,sticky=W)
        time.sleep(4)
        root.destroy()
        
root = Tk()
root.title("Emotica - The Song Generator")
root.iconbitmap("C:/Users/varun/Documents/python practice/EMOTICA/img.ico") #subject to your path where the img.ico is saved -> in the same folder as musicgen.py
root.geometry("400x400")

Label(root, text='''Welcome to Emotica!''',font=('Helveticabold',15)).grid(row=0, sticky=W)
Label(root, text='''We will click your picture and find your emotion,
    then recommend you a song!
    Press SPACEBAR to click a photo, and ESC to exit the camera!''',font=('Helveticabold',13)).grid(row=3, sticky=W)
Label(root, text='''Click OK to open camera!''',font=('Helveticabold,8)')).grid(row=4, column=0, sticky=W)
b1 = Button(root, text="OK!",font=('Helveticabold',15),relief=RAISED, command=Camera)
b1.grid(row=5, column=0,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=4, pady=4)
myLink=StringVar()
link=Label(root, text="", textvariable=myLink, font=('Helveticabold',15),fg="purple",cursor="hand2").grid(row=14,column=0, sticky=W)

mainloop()
