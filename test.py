import customtkinter as ctk

app = ctk.CTk()
app.geometry("300x200")

selected_value = ctk.StringVar()  # متغیر برای نگه‌داشتن مقدار انتخاب شده

def show():
    global selected_value
    print(selected_value.get())

# کمبوباکس
combo = ctk.CTkComboBox(app, values=["Red", "Green", "Blue"], variable=selected_value)
combo.pack(pady=20)

# دکمه‌ای برای استفاده از مقدار انتخاب‌شده
btn = ctk.CTkButton(app, text="Show Selected", command=show)
btn.pack(pady=10)

app.mainloop()
