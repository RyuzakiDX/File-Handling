from tkinter import*

root = Tk()
root.geometry("500x500")
root.title("File handler")

def edit_file():
    global root2
    root2 = Tk()
    root2.geometry("600x500")
    
    def save():
        if e1.get() == "":
            def dele():
                l5.destroy()
                btn_ok.destroy()

            l5 = Label(root2, text="Please Enter file name", fg="red")
            l5.place(x= 20 , y = 120)

            btn_ok = Button(root2, text = "OK", command=dele, fg = "red")
            btn_ok.place(x = 170 , y = 118)
        else:
            btn_save.destroy()    

        
        def app():
            l6 = Label(root2, text = "Your file is save")
            l6.pack()
            f.write(e2.get()+ "\t" + e3.get() + "\t" + e4.get() + "\n")            
            f.close()
        
        f = open(e1.get(), 'a')
            
        root2.title(e1.get())
        l2 = Label(root2 , text = "Enter student name :" )
        l2.place(x = 20 , y = 100)

        e2 = Entry(root2, width=30)
        e2.place(x = 160 , y = 100)

        l3 = Label(root2 , text = "Enter student Admision no. :" )
        l3.place(x = 20 , y = 150)

        e3 = Entry(root2, width=20)
        e3.place(x = 190 , y = 150)
        
        l4 = Label(root2 , text = "Enter student marks :" )
        l4.place(x = 20 , y = 200)

        e4 = Entry(root2, width=20)
        e4.place(x = 160 , y = 200)

        save_btn = Button(root2, text = "SAVE", fg = "green",command=app )
        save_btn.place(x = 300 , y = 250)
       
            
    l1 = Label(root2, text="Enter file name with extension:>>")
    l1.place(x = 10 , y = 20)

    e1 = Entry(root2, width= 20 )
    e1.place(x = 220 , y = 20)
    
    btn_save = Button(
        root2,
        text = "Edit",
        command=save 
    )
    btn_save.place(x = 430 , y = 19)

    root2.mainloop()


def newfile():
    global root1
    root1 = Tk()
    root1.geometry("600x500")
    
    def save():
        if e1.get() == "":
            def dele():
                l5.destroy()
                btn_ok.destroy()

            l5 = Label(root1, text="Please Enter file name", fg="red")
            l5.place(x= 20 , y = 120)

            btn_ok = Button(root1, text = "OK", command=dele, fg = "red")
            btn_ok.place(x = 170 , y = 118)
        else:
            btn_save.destroy()    

        
        def app():
            l6 = Label(root1, text = "Your file is save")
            l6.pack()
            f.write("\n"+'\n'+e2.get()+ "\t" + e3.get() + "\t" + e4.get() + "\n")            
            f.close()
        
        f = open(e1.get(), 'a+')
        f.write("Name" + "\t" + "Adm No." + "\t"+ "Roll No.")
            
        root1.title(e1.get())
        l2 = Label(root1 , text = "Enter student name :" )
        l2.place(x = 20 , y = 100)

        e2 = Entry(root1, width=30)
        e2.place(x = 160 , y = 100)

        l3 = Label(root1 , text = "Enter student Admision no. :" )
        l3.place(x = 20 , y = 150)

        e3 = Entry(root1, width=20)
        e3.place(x = 190 , y = 150)
        
        l4 = Label(root1 , text = "Enter student marks :" )
        l4.place(x = 20 , y = 200)

        e4 = Entry(root1, width=20)
        e4.place(x = 160 , y = 200)

        save_btn = Button(root1, text = "SAVE", fg = "green",command=app )
        save_btn.place(x = 300 , y = 250)
       
            
    l1 = Label(root1, text="Enter file name with extension:>>")
    l1.place(x = 10 , y = 20)

    e1 = Entry(root1, width= 20 )
    e1.place(x = 220 , y = 20)
    
    btn_save = Button(
        root1,
        text = "Create",
        command=save 
    )
    btn_save.place(x = 430 , y = 19)

    root1.mainloop()

l_File = Label(
    root,
    text = "File Handler",
    fg = 'cyan',
    font= "lucida 29 bold"
)
l_File.place(x= 200 , y = 20 )

def exit():
    root.destroy()
    try:
        root1.destroy()
        root2.destroy()
    except:
        pass    
        
newfile_btn = Button(root, text = "New file", padx= 10 , pady=10, command= newfile )
newfile_btn.place(x= 129 , y = 100)

oldfile_btn = Button(root, text = "Edit File", padx= 10 , pady=10 , command= edit_file)
oldfile_btn.place(x= 299 , y = 100)

end_btn = Button(root, text = "Exit", command= exit)
end_btn.place(x = 400 , y = 400)




root.mainloop()