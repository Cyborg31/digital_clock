from time import strftime
from tkinter import Label, Tk

# ======= Configuring window =========
window = Tk()
window.title("Digital Clock")
window.geometry("200x80")
window.configure(bg="white")  # =======Background of the clock=====
window.resizable(True, True)

clock_label = Label(
    window, bg="black", fg="white", font=("Arial", 30, "bold"), relief="flat"
)
clock_label.pack(anchor="center")

def update_label():
    """
    This function will update the clock

    every 80 milliseconds
    """
    current_time = strftime("%I: %M: %S\n %d-%m-%Y ")
    clock_label.configure(text=current_time)
    clock_label.after(80, update_label)

update_label()
window.mainloop()

# ==============The end by github.com/kalebu ==========
