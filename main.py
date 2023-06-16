import customtkinter

# Setting theme to dark and color theme to green
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme("green")

# Make a CTK App
app = customtkinter.CTk()
app.geometry('361x365+423+159')
app.title("Calculator")
app.resizable(False, False)


def calculate():
    calcul = output.get('0.0', 'end')
    resultant = eval(calcul)
    output.delete('0.0', 'end')
    output.insert('0.0', resultant)


# making a textbox to show the result
output = customtkinter.CTkTextbox(app, width=340, height=50, corner_radius=10, border_width=2,
                                  border_color='#6A5598', font=("Noto Sans", 50))
output.grid(row=0, column=0, columnspan=5, padx=5, pady=5)

# buttons
btn1 = customtkinter.CTkButton(app, text='1', command=lambda: output.insert('end', 1),
                               width=80, height=55, font=("Noto Sans", 30))
btn1.grid(row=1, column=0, padx=5, pady=5)

btn2 = customtkinter.CTkButton(app, text='2', command=lambda: output.insert('end', 2),
                               width=80, height=55, font=("Noto Sans", 30))
btn2.grid(row=1, column=1, padx=5, pady=5)

btn3 = customtkinter.CTkButton(app, text='3', command=lambda: output.insert('end', 3),
                               width=80, height=55, font=("Noto Sans", 30))
btn3.grid(row=1, column=2, padx=5, pady=5)

btn4 = customtkinter.CTkButton(app, text='4', command=lambda: output.insert('end', 4),
                               width=80, height=55, font=("Noto Sans", 30))
btn4.grid(row=2, column=0, padx=5, pady=5)

btn5 = customtkinter.CTkButton(app, text='5', command=lambda: output.insert('end', 5),
                               width=80, height=55, font=("Noto Sans", 30))
btn5.grid(row=2, column=1, padx=5, pady=5)

btn6 = customtkinter.CTkButton(app, text='6', command=lambda: output.insert('end', 6),
                               width=80, height=55, font=("Noto Sans", 30))
btn6.grid(row=2, column=2, padx=5, pady=5)

btn7 = customtkinter.CTkButton(app, text='7', command=lambda: output.insert('end', 7),
                               width=80, height=55, font=("Noto Sans", 30))
btn7.grid(row=3, column=0, padx=5, pady=5)

btn8 = customtkinter.CTkButton(app, text='8', command=lambda: output.insert('end', 8),
                               width=80, height=55, font=("Noto Sans", 30))
btn8.grid(row=3, column=1, padx=5, pady=5)

btn9 = customtkinter.CTkButton(app, text='9', command=lambda: output.insert('end', 9),
                               width=80, height=55, font=("Noto Sans", 30))
btn9.grid(row=3, column=2, padx=5, pady=5)

btn0 = customtkinter.CTkButton(app, text='0', command=lambda: output.insert('end', 0),
                               width=80, height=55, font=("Noto Sans", 30))
btn0.grid(row=4, column=0, padx=5, pady=5)

btn_del = customtkinter.CTkButton(app, text='C', command=lambda: output.delete('0.0', 'end'),
                                  width=80, height=55, font=("Noto Sans", 30))
btn_del.grid(row=4, column=1, padx=5, pady=5)

btn_calculate = customtkinter.CTkButton(app, text='=', command=calculate, width=80,
                                        height=55, font=("Noto Sans", 30))
btn_calculate.grid(row=4, column=2, padx=5, pady=5)

btn_sum = customtkinter.CTkButton(app, text='+', command=lambda: output.insert('end', '+'),
                                  width=80, height=55, font=("Noto Sans", 30))
btn_sum.grid(row=1, column=3, padx=5, pady=5)

btn_subtract = customtkinter.CTkButton(app, text='-', command=lambda: output.insert('end', '-'),
                                       width=80, height=55, font=("Noto Sans", 30))
btn_subtract.grid(row=2, column=3, padx=5, pady=5)

btn_multiplication = customtkinter.CTkButton(app, text='x', command=lambda: output.insert('end', '*'),
                                             width=80, height=55, font=("Noto Sans", 30))
btn_multiplication.grid(row=3, column=3, padx=5, pady=5)

btn_division = customtkinter.CTkButton(app, text='/', command=lambda: output.insert('end', '/'),
                                       width=80, height=55, font=("Noto Sans", 30))
btn_division.grid(row=4, column=3, padx=5, pady=5)

app.mainloop()
