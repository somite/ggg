# -*- coding: utf-8 -*- 



from Tkinter import *
import Tkinter as tk
import sqlite3
import ttk
import tkinter.scrolledtext as tkst



root = tk.Tk()
root.title('永春動物醫院')
#设置窗口标题

class mainpage(object):
    def __init__(self, master=None):
        self.root = master 
        self.root.geometry('500x300+400+300')
        self.root.resizable(False, False)
#不允许改变窗口大小
     

#使用Treeview组件实现表格功能

        self.page = tk.Frame(self.root)

        self.page.place(x=0, y=10, width=480, height=280)
 #滚动条       
        self.scrollBar = tk.Scrollbar(self.page)

        self.scrollBar.pack(side=RIGHT, fill=Y)
        
  #Treeview组件，6列，显示表头，带垂直滚动条

        tree = ttk.Treeview(self.page,columns=('c1', 'c2', 'c3'),
        show="headings",yscrollcommand=self.scrollBar.set)

#设置每列宽度和对齐方式

        tree.column('c1', width=70, anchor='center')

        tree.column('c2', width=40, anchor='center')

        tree.column('c3', width=40, anchor='center')

       

#设置每列表头标题文本

        tree.heading('c1', text='姓名')

        tree.heading('c2', text='電話')

        tree.heading('c3', text='地址')

     

        tree.pack(side=LEFT, fill=Y)

#Treeview组件与垂直滚动条结合

        self.scrollBar.config(command=tree.yview)

#定义并绑定Treeview组件的鼠标单击事件

        def treeviewClick(event):
            self.secpage()

        tree.bind('<Button-1>', treeviewClick)



#插入演示数据
        hospital=sqlite3.connect('hospital.db')
        list=hospital.execute("SELECT name,phone,address from work;")
        
        index=0
        for i in list:

            tree.insert('', index, values=i)
            index += 1

#运行程序，启动事件循环     

       
        self.Button = tk.Button(self.page, text=u'跳頁',command=self.secpage) 
        self.Button.pack() 
        
        self.Button1 = tk.Button(self.page, text=u'新增',command=self.thirdpage) 
        self.Button1.pack() 
        
        self.Button2 = tk.Button(self.page, text=u'',command=self.secpage) 
        self.Button2.pack() 
        

    def secpage(self):
        self.page.destroy()
        secondpage(self.root)
        
    def thirdpage(self):
        self.page.destroy()
        thirdpage(self.root)
  
class secondpage(object):
    def __init__(self, master=None):
        self.root = master
        self.page = tk.Frame(self.root)
        self.page.pack()
        
        self.Button = tk.Button(self.page, text=u'主頁',command=self.mainpage) 
        self.Button.grid(column=0,row=0) 
    
        hospital=sqlite3.connect('hospital.db')
        list=hospital.execute("SELECT date, content from history;")
    
        self.editArea = tkst.ScrolledText(self.page, wrap= tk.WORD, width  = 20,height = 10)
        self.editArea.pack( expand=True)

        
        
    def mainpage(self):
        self.page.destroy()
        mainpage(self.root)  

class thirdpage(object):
    def __init__(self, master=None):
        self.root = master
        self.page = tk.Frame(self.root)
        self.page.pack()
        
        self.Button = tk.Button(self.page, text=u'主頁',command=self.mainpage) 
        self.Button.pack() 
        
        self.Button = tk.Button(self.page, text=u'新增',command=self.save) 
        self.Button.pack() 
    
        self.entry1=Entry(self.page)
        self.entry1.pack()

        self.entry2=Entry(self.page)
        self.entry2.pack()

        self.entry3=Entry(self.page)
        self.entry3.pack()
        
    def save(self):
        hospital=sqlite3.connect('hospital.db')
        
        name=self.entry1.get()
        phone=self.entry2.get()
        address=self.entry3.get()
        
        hospital.execute("INSERT INTO Work(name,phone,address) VALUES ('"+name+"','"+phone+"','"+address+"');")
        hospital.commit()
        hospital.close()

        
        
    def mainpage(self):
        self.page.destroy()
        mainpage(self.root)           
        
mainpage(root)
root.mainloop()     







#运行程序，启动事件循环