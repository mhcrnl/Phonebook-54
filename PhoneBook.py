#!usr/bin/python

from fltk import *
import pickle

def delbutcallback(wid):
    pos=brow.value()
    name=brow.text(pos)
    brow.remove(pos)
    d.pop(name) #any other way to remove sth from dictionary??
    textbox.value(str(len(d)))
    inp.value('')
    inp1.value('')
  
def browcallback(wid):
    pos=brow.value()
    name=brow.text(pos)
    inp.value(name)
    inp1.value(d[name])

def addbutcallback(wid): #to add things to the browser box and to the dictionary
    name=inp.value()
    telenumber=inp1.value()
    d[name]=telenumber
    textbox.value(str(len(d))) 
    inp.value('')
    inp1.value('')
    brow.clear()
    for contact in sorted(d):
        brow.add(contact)

def windowcallback(wid): #closes the window and pickles dictionary to data file
    f=file('phonebookcontacts.txt','w')
    pickle.dump(d,f)
    f.close()
    win.hide()
  
win=Fl_Window(100,200,600,600,'Phone Book')

win.begin()
brow=Fl_Hold_Browser(250,100,300,350,'Contacts')
inp=Fl_Input(50,100,150,30,'Name')
inp1=Fl_Input(50,150,150,30,'Tele')
textbox=Fl_Input(50,200,150,30,'Contacts')
addbut=Fl_Return_Button(50,250,70,25,'Add') #click or press enter
delbut=Fl_Button(50,300,70,25,'Delete') #delete the contact from the browser and data

win.end()

brow.align(FL_ALIGN_TOP)

d={}

try:
    f=open('phonebookcontacts.txt','r')
    d=pickle.load(f)
    for name in sorted(d):   
        brow.add(name)   
    f.close()
    textbox.value(str(len(d)))  
except:
    print 'This is your first time running the program or your database was deleted.'


win.callback(windowcallback)
addbut.callback(addbutcallback)
delbut.callback(delbutcallback)
brow.callback(browcallback)

win.show()
Fl.run()

