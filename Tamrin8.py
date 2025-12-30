import tkinter as tk
from tkinter import messagebox

def calculate_share():
    try:
        bill_total = float(entry_bill.get())
        people = int(entry_people.get())

        if people <= 0:
            raise ValueError("تعداد نفرات باید بیشتر از صفر باشد")

        share = bill_total / people
        messagebox.showinfo(
            "نتیجه",
            f"سهم هر نفر: {share:.0f} تومان"
        )

    except ValueError:
        messagebox.showwarning(
            "خطا",
            "لطفاً مبلغ و تعداد نفرات را به صورت عددی و صحیح وارد کنید."
        )

# ساخت پنجره اصلی
root = tk.Tk()
root.title("محاسبه سهم هر نفر")
root.geometry("300x200")

# برچسب و ورودی مبلغ کل
label_bill = tk.Label(root, text="مبلغ کل صورتحساب:")
label_bill.pack(pady=5)

entry_bill = tk.Entry(root)
entry_bill.pack(pady=5)

# برچسب و ورودی تعداد نفرات
label_people = tk.Label(root, text="تعداد نفرات:")
label_people.pack(pady=5)

entry_people = tk.Entry(root)
entry_people.pack(pady=5)

# دکمه محاسبه
btn_calculate = tk.Button(
    root,
    text="محاسبه سهم هر نفر",
    command=calculate_share
)
btn_calculate.pack(pady=15)

# اجرای برنامه
root.mainloop()
