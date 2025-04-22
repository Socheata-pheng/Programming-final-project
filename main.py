from tkinter import *
from tkinter import ttk

class libraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")
        # self.root.config(bg="#f0f0f0")

        lbltitle = Label(self.root, text= "Library Management System", bg="blue", fg="green",bd=20, relief= RIDGE, font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd = 12, relief = RIDGE, padx= 20, bg = "powder blue")
        frame.place(x = 0 , y = 130, width= 1530, height= 400)

        # ================================DataFrameLeft==========================================
        DataFrameLeft=LabelFrame(frame, text="Library Membership Information", bg="powder blue", fg = "green", bd = 12, relief = RIDGE, font=("times new roman", 12, "bold"))
        DataFrameLeft.place(x=0, y = 5, width = 760, height = 350)

        lblMember = Label(DataFrameLeft,text="Member Type", bg = "powder blue",font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblMember.grid(row = 0,column=0, sticky=W )

        comMember = ttk.Combobox(DataFrameLeft,font=("times new roman", 12, "bold"),width = 27)
        comMember['values'] = ("Admin Staff", "Student", "Lecturer")
        comMember.grid(row=0, column=1)

        lblPRN_No = Label(DataFrameLeft,text="PRN No", bg = "powder blue",font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblPRN_No.grid(row = 1,column=0, sticky=W )
        txtPRN_NO=Entry(DataFrameLeft, font=("times new roman", 12, "bold") ,width= 29)
        txtPRN_NO.grid(row=1, column=1)

        lblTitle = Label(DataFrameLeft, font=("times new roman", 12, "bold"),text = "ID No:", padx=2, pady= 4, bg = "powder blue")
        lblTitle.grid(row=2, column=0, sticky=W)
        txtTitle = Entry(DataFrameLeft,font=("times new roman", 12, "bold"), width=29)
        txtTitle.grid(row=2, column=1)

        lblFirstName=Label(DataFrameLeft, font=("times new roman", 12, "bold"), text="FirstName", padx=2, pady=6,bg="powder blue")
        lblFirstName.grid(row=3, column = 0, sticky=W)
        txtFirstName= Entry(DataFrameLeft, width=29, font=("times new roman", 12, "bold"))
        txtFirstName.grid(row=3, column=1)

        lblLastName=Label(DataFrameLeft, font=("times new roman", 12, "bold"), text="LastName", padx=2, pady=6,bg="powder blue")
        lblLastName.grid(row=4, column=0, sticky=W)
        txtLastName= Entry(DataFrameLeft, width=29, font=("times new roman", 12, "bold"))
        txtLastName.grid(row=4, column=1)

        lblAddress=Label(DataFrameLeft, text="Address", padx=2, pady=6, bg="powder blue",font=("times new roman", 12, "bold"))
        lblAddress.grid(row=5, column=0, sticky=W)
        txtAddress = Entry(DataFrameLeft,font=("times new roman", 12, "bold"),width=29)
        txtAddress.grid(row=5, column=1)

        lblMobile = Label(DataFrameLeft, font=("times new roman", 12, "bold"), text= "Mobile Number", padx= 2, bg= "powder blue")
        lblMobile.grid(row=6, column=0, sticky=W)
        txtMobile = Entry(DataFrameLeft, font=("times new roman", 12, "bold"), width=29)
        txtMobile.grid(row=6, column=1)   

        lblBookID = Label(DataFrameLeft, font=("times new roman", 12, "bold"), text= "Book ID", padx= 2, bg= "powder blue")
        lblBookID.grid(row=7, column=0, sticky=W)
        txtBookID = Entry(DataFrameLeft, font=("times new roman", 12, "bold"), width=29)
        txtBookID.grid(row=7, column=1)     

        lblBookTitle = Label(DataFrameLeft, text="Book Title", padx=2, pady=6, bg="powder blue", font=("times new roman", 12, "bold"))
        lblBookTitle.grid(row=8, column=0, sticky=W)
        txtBookTitle= Entry(DataFrameLeft, font=("times new roman", 12, "bold"), width=29)
        txtBookTitle.grid(row=8, column=1)

        lblAuthur = Label(DataFrameLeft, font=("times new roman", 12, "bold"), text="Author", padx=2, pady=6, bg="powder blue")
        lblAuthur.grid(row=0, column =2, sticky=W)
        txtAuthur=Entry(DataFrameLeft,font=("times new roman", 12, "bold"), width=29)
        txtAuthur.grid(row=0, column=3)

        lblBorrowDate = Label(DataFrameLeft, font=("times new roman", 12, "bold"), text="Borrow Date", padx=2, pady=6, bg="powder blue")
        lblBorrowDate.grid(row=1, column=2, sticky=W)
        txtBorrowDate=Entry(DataFrameLeft,font=("times new roman", 12, "bold"), width=29)
        txtBorrowDate.grid(row=1, column=3)

        lblDueDate = Label(DataFrameLeft, font=("times new roman", 12, "bold"), padx=2, pady=6, text="Due Date", bg="powder blue")
        lblDueDate.grid(row=2, column=2, sticky=W)
        txtDueDate=Entry(DataFrameLeft, font=("times new roman", 12, "bold"), width=29)
        txtDueDate.grid(row=2, column=3)

        lblLateReturnFIne= Label(DataFrameLeft, font=("times new roman", 12, "bold"), text="Late Return Fine", padx=2, pady=6, bg="powder blue")
        lblLateReturnFIne.grid(row=3, column=2, sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft, font=("times new roman", 12, "bold"), width=29)
        txtLateReturnFine.grid(row=3, column=3)

        lblDateOverDue= Label(DataFrameLeft, font=("times new roman", 12, "bold"), text="Date Overdue", padx=2, pady=6, bg="powder blue")
        lblDateOverDue.grid(row=4, column=2, sticky=W)
        txtDateOverDue=Entry(DataFrameLeft, font=("times new roman", 12, "bold"), width=29)
        txtDateOverDue.grid(row=4, column=3)

        lblBookStatus = Label(DataFrameLeft, font=("times new roman", 12, "bold"), text="Books condition", padx=2, pady=6, bg="powder blue")
        lblBookStatus.grid(row=5, column=2, sticky=W)
        comBookStatus = ttk.Combobox(DataFrameLeft,font=("times new roman", 12, "bold"),width = 27)
        comBookStatus['values'] = ("Old", "Neutral", "New")
        comBookStatus.grid(row=5, column=3)

        lblPrice=Label(DataFrameLeft,font=("times new roman", 12, "bold"),text="Price:", padx=2, pady=6,bg="powder blue")
        lblPrice.grid(row=6, column=2, sticky=W)
        txtPrice=Entry(DataFrameLeft, font=("times new roman", 12, "bold"), width=29)
        txtPrice.grid(row=6, column=3)



        # ==================================DataFrameRight===============================================
        DataFrameRight=LabelFrame(frame, text="Books Detail", bg="powder blue", fg = "green", bd = 12, relief = RIDGE, font=("times new roman", 12, "bold"))
        DataFrameRight.place(x=780, y = 4, width = 440, height = 350)

        self.txtBox=Text(DataFrameRight,font=("times new roman", 12, "bold"), width=32, height=16, padx=2, pady=6)
        self.txtBox.grid(row=0, column=2)

        listScrollbar= Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0, column=1, sticky='ns')


        listBooks = ["To Kill a Mockingbird","1984",
        "Pride and Prejudice",
        "The Great Gatsby",
        "Moby-Dick",
        "The Catcher in the Rye",
        "The Lord of the Rings",
        "Harry Potter and the Sorcerer's Stone",
        "The Hobbit",
        "Brave New World",
        "The Chronicles of Narnia",
        "Animal Farm",
        "Jane Eyre",
        "Wuthering Heights",
        "Fahrenheit 451",
        "The Alchemist",
        "Crime and Punishment",
        "The Picture of Dorian Gray",
        "The Da Vinci Code",
        "Les Misérables"
    ]
        listBox = Listbox(DataFrameRight, font=("times new roman", 12, "bold"), width= 16, height=16)
        listBox.grid(row=0, column=0, padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END, item)


        # ================================Buttin Frame===================================
        frameButton = Frame(self.root, bd = 12, relief = RIDGE, padx= 20, bg = "powder blue")
        frameButton.place(x = 0 , y = 500, width= 1530, height= 70)
        
        # ==================================Information button===============================
        frameDetail = Frame(self.root, bd = 12, relief = RIDGE, padx= 20, bg = "powder blue")
        frameDetail.place(x = 0 , y = 580, width= 1530, height= 195)

if __name__ == "__main__":
    root = Tk()
    obj = libraryManagementSystem(root)
    root.mainloop()