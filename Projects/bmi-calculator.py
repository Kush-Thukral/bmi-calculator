import tkinter as tk

def calculate():
    try :
        weight = float(entry_weight.get())
        height= float(entry_height.get())
        bmi = weight / height ** 2
        if bmi < 18.5 :
            category = "underweight"
        elif bmi >= 18.5 and bmi < 25 :
            category = "normal"
        elif bmi >= 25 and bmi < 30 :
            category = "overweight"
        else :
            category = "obese"
        label_result.config(text=f"Your BMI is {bmi:.2f}. {category} ", fg="blue")
        label_result.pack()
    except :
                label_result.config(text="Enter Valid Values", fg="red")
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x250")
tk.Label(root, text="Weight (kg):").pack()
entry_weight = tk.Entry(root)
entry_weight.pack()
tk.Label(root, text="Height (m):").pack()
entry_height = tk.Entry(root)
entry_height.pack()
tk.Button(root, text="Calculate BMI", command=calculate).pack()
label_result = tk.Label(root, text="Enter your weight and height above")
label_result.pack()
root.mainloop()