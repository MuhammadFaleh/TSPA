from tkinter import *
from tkinter import ttk
from tkinter import filedialog
value = 0
result = []
final_result = []
def Absorption(TPSA):
    a =109.0
    b = 0.345
    bTPSA = b * TPSA
    result = a - bTPSA
    return result

def add():
    global value
    global result
    global final_result
    value = e1.get()
    result = '%'+str(round(Absorption(float(value)), 6))
    tree1.insert("", index='end', values=(value, result))


def save_info():
    file = open("data.txt", "w")
    for row_id in tree1.get_children():
        row = tree1.item(row_id)['values']
        file.write(str(row))
    file.close()

root = Tk()
root.title('reading club app')
root.geometry('500x350')
root.resizable(False, False)
tree1 = ttk.Treeview(root)
tree1['columns'] = ("TSPA", "result")
tree1.heading("TSPA", text="TSPA", anchor=W)
tree1.heading("result", text="result", anchor=CENTER)
tree1.column("#0", width=0, stretch=NO)
e1 = ttk.Entry(root)
ttk.Label(root, text="TPSA").place(relx=0.1, rely=0.80, anchor=CENTER)
e1.place(relx=0.3, rely=0.8, anchor=CENTER)
new_newvalue = []
button1 = Button(root, text="add", command=add)
button1.place(relx=0.3, rely=0.87, anchor=CENTER)
button1 = Button(root, text="save", command=save_info)
button1.place(relx=0.5, rely=0.8, anchor=CENTER)
tree1.place(relx=0.4, rely=0.4, anchor=CENTER)
root.mainloop()


