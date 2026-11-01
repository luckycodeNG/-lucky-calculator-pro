import tkinter as tk

root = tk.Tk()
root.title("Lucky Calculator Pro - Udi, Enugu")
root.geometry("320x450")
root.config(bg="#1a1a1a")

entry = tk.Entry(root, font=("Arial", 24), justify="right")
entry.pack(fill="both", padx=10, pady=10, ipady=20)

def click(k): entry.insert(tk.END, k)
def clear(): entry.delete(0, tk.END)
def calc():
    try:
        exp = entry.get()
        res = eval(exp)
        entry.delete(0, tk.END)
        entry.insert(0, str(res))
        with open("lucky_history.txt", "a") as f:
            f.write(f"{exp} = {res}\n")
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

buttons = [["7","8","9","/"],["4","5","6","*"],["1","2","3","-"],["0",".","%","+"],["C","="]]

for row in buttons:
    fr = tk.Frame(root, bg="#1a1a1a")
    fr.pack(expand=True, fill="both")
    for ch in row:
        if ch=="C": b=tk.Button(fr,text=ch,bg="red",fg="white",font=("Arial",18),command=clear)
        elif ch=="=": b=tk.Button(fr,text=ch,bg="green",fg="white",font=("Arial",18),command=calc)
        else: b=tk.Button(fr,text=ch,font=("Arial",18),command=lambda c=ch: click(c))
        b.pack(side="left",expand=True,fill="both",padx=2,pady=2)

root.mainloop()
