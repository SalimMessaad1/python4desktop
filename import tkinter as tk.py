# By Salim 
# never care 
# just skip  
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import qrcode

root = tk.Tk()
root.title("Just Prototype")
root.geometry("700x500")

window_width = 700
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# background color
root.config(bg="#f7f7f7")

qr_image = None
qr_label = None
url_entry = None 

# Function to handle menu item clicks
def home():
    content_label.config(text="Welcome to Home", fg="#34495e")
    info_label.config(text="This is the Home page.", fg="#34495e")
    if qr_label:
        qr_label.pack_forget()  # Hide QR code when switching back to Home

def open_file():
    messagebox.showinfo("File", "Opening File...")

def about_us():
    content_label.config(text="About Us", fg="#34495e")
    info_label.config(text="This app was developed by Salim Messaad, a modern software solution.", fg="#34495e")
    if qr_label:
        qr_label.pack_forget()  

# generate QR code 
def generate_qr_code(url):
    global qr_image, qr_label

    try:
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        qr_img = qr.make_image(fill='black', back_color='white')

        qr_photo = ImageTk.PhotoImage(qr_img.resize((150, 150), Image.LANCZOS)) 

        # Display the QR code image
        if qr_label:
            qr_label.pack_forget() 
        qr_label = tk.Label(right_frame, image=qr_photo, bg="#ecf0f1")
        qr_label.image = qr_photo 
        qr_label.pack(pady=10)

        url_entry.delete(0, tk.END)

    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate QR code: {e}")

def show_developer_info():
    content_label.config(text="Developer Info", fg="#34495e")
    
    info_label.config(text="https://www.linkedin.com/in/salim-messaad-3364b5273/", fg="#34495e")

    entry_label = tk.Label(right_frame, text="", bg="#ecf0f1", font=("Arial", 12), fg="#34495e")
    entry_label.pack(pady=5)

    global url_entry 
    url_entry = tk.Entry(right_frame, width=40)
    url_entry.pack(pady=5)

    generate_button = tk.Button(right_frame, text="Generate QR Code", command=lambda: generate_qr_code(url_entry.get()))
    generate_button.pack(pady=10)

menu_bar = tk.Menu(root)

home_menu = tk.Menu(menu_bar, tearoff=0)
home_menu.add_command(label="Home", command=home)
menu_bar.add_cascade(label="Home", menu=home_menu)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=lambda: messagebox.showinfo("Save", "File Saved"))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

about_menu = tk.Menu(menu_bar, tearoff=0)
about_menu.add_command(label="About Us", command=about_us)
menu_bar.add_cascade(label="About Us", menu=about_menu)

root.config(menu=menu_bar)

sidebar_frame = tk.Frame(root, bg="#34495e", bd=0)  
sidebar_frame.pack(side="left", fill="y", padx=0, pady=0)

def on_enter(e):
    e.widget['bg'] = '#1abc9c' 

def on_leave(e):
    e.widget['bg'] = '#16a085' 

button_texts = ["Dashboard", "Settings", "Reports", "Help", "Info About Developer", "Exit"]
buttons = []
for text in button_texts:
    button = tk.Button(sidebar_frame, text=text, bg='#16a085', fg="white", relief="flat", font=("Arial", 12), padx=20, pady=20, anchor='w')
    button.pack(fill="x", pady=1) 
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)
    buttons.append(button)

# buttons
buttons[0].config(command=lambda: messagebox.showinfo("Dashboard", "Welcome to the Dashboard"))
buttons[1].config(command=lambda: messagebox.showinfo("Settings", "Settings Window"))
buttons[2].config(command=lambda: messagebox.showinfo("Reports", "Report Section"))
buttons[3].config(command=lambda: messagebox.showinfo("Help", "Help Section"))
buttons[4].config(command=show_developer_info)  
buttons[5].config(command=root.quit) 

right_frame = tk.Frame(root, bg="#ecf0f1", bd=0, relief="flat")  # Light background for contrast
right_frame.pack(expand=True, fill="both", padx=20, pady=20)

content_label = tk.Label(right_frame, text="Welcome to the Application", bg="#ecf0f1", font=("Arial", 18, "bold"), fg="#34495e")
content_label.pack(pady=40)

info_label = tk.Label(right_frame, text="this is prototype and my try to develop and desktop app using python and make modern GUI app with professional design from Zero.", bg="#ecf0f1", font=("Arial", 12), fg="#34495e", wraplength=400, justify="left")
info_label.pack(pady=10)

footer_label = tk.Label(root, text="Developed by Salim Messaad", bg="#f7f7f7", fg="#7f8c8d", font=("Arial", 10, "italic"))
footer_label.pack(side="bottom", pady=10)

# the end thank god 
root.mainloop()
