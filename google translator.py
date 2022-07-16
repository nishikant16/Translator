#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
from tkinter import ttk
from googletrans import Translator,LANGUAGES


def conversion(text="type",src="English",dest="Hindi"):
    text1=text
    src1=src
    dest1=dest
    trans=Translator()
    t1=trans.translate(text,src=src1,dest=dest1)
    return t1.text
    
def data():
    s=combo_source.get()
    d=combo_destination.get()
    msg=Source_Text.get(1.0,END)
    textget=conversion(text=msg,src=s,dest=d)
    Destination_text.delete(1.0,END)
    Destination_text.insert(END,textget)








root=Tk()
root.title("Translator")
root.config(bg="Cyan")

label1=Label(root,text="Google Translator",font=('Times New Roman',20,'bold'),bg='Cyan')     # for 1st label
label1.place(x=500,y=40,height=50,width=300)
label2=Label(root,text='Source Text',font=('Times New Roman',15,'bold'),bg='Cyan')
label2.place(x=600,y=100)

frame=Frame(root).pack(side=BOTTOM)
Source_Text=Text(frame,font=('Times New Roman',20,'bold'),wrap=WORD)                        # text for input
Source_Text.place(frame,x=470,y=150,height=150,width=400)

list_text =list(LANGUAGES.values())

combo_source=ttk.Combobox(frame,value=list_text)
combo_source.place(x=520,y=320,height=30,width=60)
combo_source.set("English")

Button_1=Button(frame,text='Translate',relief=RAISED,command=data)
Button_1.place(x=620,y=320,height=30,width=60)

combo_destination=ttk.Combobox(frame,value=list_text)
combo_destination.place(x=720,y=320,height=28,width=60)
combo_destination.set('Select Language')


label3=Label(root,text='Destination Text',font=('Times New Roman',15,'bold'),bg='Cyan')
label3.place(x=600,y=380)

Destination_text=Text(frame,font=('Times New Roman',20,'bold'),wrap=WORD)
Destination_text.place(frame,x=470,y=430,height=150,width=400)


root.mainloop()


# In[ ]:




