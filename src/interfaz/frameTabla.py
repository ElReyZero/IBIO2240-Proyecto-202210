from tkinter import ttk, Frame, NO, CENTER

def frameTabla(ventana):
    # Crear el frame con la tabla
    frameTabla = Frame(ventana, width=600, height=600)
    frameTabla.place(x=650, y=470)
    
    style = ttk.Style()

    style.theme_use('default')

    style.configure("Treeview", rowheight=25)
    
    tabla = ttk.Treeview(frameTabla)
    tabla['columns'] = ('inicial', 'final', 'estimulacion')
    
    tabla.column("#0", width=0, stretch=NO)
    tabla.column("inicial", anchor=CENTER, width=160)
    tabla.column("final", anchor=CENTER, width=160)
    tabla.column("estimulacion", anchor=CENTER, width=160)

    tabla.heading("#0", text="", anchor=CENTER)
    tabla.heading("inicial", text="T inicial (ms)", anchor=CENTER)
    tabla.heading("final", text="T final (ms)", anchor=CENTER)
    tabla.heading("estimulacion", text="Estimulación (mA)", anchor=CENTER)

    data = [["", "", ""], 
            ["", "", ""], 
            ["", "", ""]]

    tabla.tag_configure('oddrow', background='#f0f0f0')
    tabla.tag_configure('evenrow', background='#e1e1e1')

    global count
    count = 0
    for record in data:
        if count % 2 == 0:
            tabla.insert(parent="", index="end", iid=count, text="", values=(record[0], record[1], record[2]), tags=('evenrow',))

        else:
            tabla.insert(parent="", index="end", iid=count, text="", values=(record[0], record[1], record[2]), tags=('oddrow',))
        
        count += 1

    tabla.place(x=60, y=0)
    tabla.config(height=len(data))