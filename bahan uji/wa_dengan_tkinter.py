import tkinter as tk
from tkinter import messagebox, simpledialog

class Login:
    def __init__(self, windows):
        self.windows = windows
        self.windows.geometry('380x350')
        self.windows.title('Whatsapp Login')
        
        self.label_produk = tk.Label(windows, text='WHATSSAPP LOGIN', font=('Arial', 14, 'bold'), fg='green', pady=20)
        self.label_produk.pack()

        self.label_nama = tk.Label(windows, text='Nama:', pady=10, font=('Arial', 10))
        self.label_nama.pack()

        self.input_nama = tk.Entry(windows, width=25, font=('Arial', 12))
        self.input_nama.pack()

        self.label_password = tk.Label(windows, text='Password:', pady=10, font=('Arial', 10))
        self.label_password.pack()

        self.input_password = tk.Entry(windows, show='*', width=25, font=('Arial', 12))
        self.input_password.pack()

        self.tombol_login = tk.Button(windows, text='Login', command=self.check_login, width=15, bg='green', fg='white', font=('Arial', 11, 'bold'))
        self.tombol_login.pack(pady=25)

    def check_login(self):
        nama = self.input_nama.get()
        password = self.input_password.get()

        if nama == 'fajar' and password == '456':
            messagebox.showinfo('Login Berhasil', f'Selamat datang {nama}!')
            self.windows.withdraw()  # Hide the login window
            username = 'given'
            Chat(username)  # Pass the username to Chat
        elif nama == 'given' and password == '123':
            messagebox.showinfo('Login Berhasil', f'Selamat datang {nama}!')
            self.windows.withdraw()  # Hide the login window
            username = 'fajar'
            Chat(username)  # Pass the username to Chat
        else:
            messagebox.showerror('Login Gagal', 'Username atau password salah.')

class Message:
    def __init__(self, content):
        self.content = content

class Chat:
    def __init__(self, user):
        self.user = user
        self.messages = []
        self.windows = tk.Toplevel()  # Create a new window for chat
        self.windows.geometry('380x400')
        self.windows.title('Aplikasi Whatssapp Utama')

        # Scrollable Text Area for Messages
        self.text_area = tk.Text(self.windows, height=10, width=50, state='disabled')
        self.text_area.pack(pady=10)

        self.scrollbar = tk.Scrollbar(self.windows, command=self.text_area.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.text_area.config(yscrollcommand=self.scrollbar.set)

        self.label_kirim = tk.Label(self.windows, text='Kirim Pesan:', fg='green', font=('Arial', 14, 'bold'), pady=20)
        self.label_kirim.pack()

        self.input_pesan = tk.Entry(self.windows, width=50)
        self.input_pesan.pack()

        self.frame_tombol = tk.Frame(self.windows)
        self.frame_tombol.pack(pady=20)

        self.frame_tombol2 = tk.Frame(self.windows)
        self.frame_tombol2.pack(pady=1)

        self.tombol_kirim = tk.Button(self.frame_tombol, text='Kirim Pesan', command=self.send_message, bg='green', fg='white', font=('Arial', 11, 'bold'))
        self.tombol_kirim.pack(side=tk.LEFT, padx=5)

        self.tombol_tampilkan = tk.Button(self.frame_tombol, text='Tampilkan Pesan', command=self.show_messages_popup, bg='blue', fg='white', font=('Arial', 11, 'bold'))
        self.tombol_tampilkan.pack(side=tk.LEFT, padx=5)

        self.tombol_edit = tk.Button(self.frame_tombol, text='Edit Pesan', command=self.edit_message, bg='orange', fg='white', font=('Arial', 11, 'bold'))
        self.tombol_edit.pack(side=tk.LEFT, padx=5)

        self.tombol_hapus = tk.Button(self.frame_tombol2, text='Hapus Pesan', command=self.delete_message, bg='red', fg='white', font=('Arial', 11, 'bold'))
        self.tombol_hapus.pack(side=tk.LEFT, padx=5)

        self.tombol_keluar = tk.Button(self.frame_tombol2, text='Keluar', command=self.windows.quit, bg='red', fg='white', font=('Arial', 11, 'bold'))
        self.tombol_keluar.pack(side=tk.LEFT, padx=5)

    def send_message(self):
        message_content = self.input_pesan.get()
        if message_content:
            message = Message(message_content)
            self.add_message(message)
            self.input_pesan.delete(0, tk.END)  
            self.display_messages()  
        else:
            messagebox.showwarning("Peringatan", "Pesan tidak boleh kosong!")

    def add_message(self, message):
        self.messages.append(message)
        messagebox.showinfo('Berhasil mengirim', f'Pesan sudah terkirim {self.user}')

    def display_messages(self):
        self.text_area.config(state='normal')  
        self.text_area.delete(1.0, tk.END)  
        all_messages = self.get_all_messages()
        for index, msg in enumerate(all_messages):
            self.text_area.insert(tk.END, f"{index + 1}. You: {msg}\n")
        self.text_area.config(state='disabled')

    def get_all_messages(self):
        return [msg.content for msg in self.messages]

    def show_messages_popup(self):
        all_messages = self.get_all_messages()
        if not all_messages:
            messagebox.showinfo("Informasi", "Tidak ada pesan untuk ditampilkan.")
        else:
            message_list = "\n".join(f"{index + 1}. You: {msg}" for index, msg in enumerate(all_messages))
            messagebox.showinfo("Daftar Pesan", message_list)

    def edit_message(self):
        all_messages = self.get_all_messages()
        if not all_messages:
            messagebox.showinfo("Informasi", "Tidak ada pesan untuk diedit.")
            return
        index = simpledialog.askinteger("Edit Pesan", "Masukkan nomor pesan yang ingin diedit (1 untuk pesan pertama):", minvalue=1, maxvalue=len(all_messages))
        if index is not None and 1 <= index <= len(all_messages):
            new_message = simpledialog.askstring("Edit Pesan", "Masukkan pesan baru:", initialvalue=all_messages[index - 1])
            if new_message is not None:
                self.messages[index - 1].content = new_message
                self.display_messages()  
        else:
            messagebox.showerror("Error", "Nomor pesan tidak valid.")

    def delete_message(self):
        all_messages = self.get_all_messages()
        if not all_messages:
            messagebox.showinfo("Informasi", "Tidak ada pesan untuk dihapus.")
            return
        index = simpledialog.askinteger("Hapus Pesan", "Masukkan nomor pesan yang ingin dihapus (1 untuk pesan pertama):", minvalue=1, maxvalue=len(all_messages))
        if index is not None and 1 <= index <= len(all_messages):
            self.messages.pop(index - 1)
            self.display_messages()  
        else:
            messagebox.showerror("Error", "Nomor pesan tidak valid.")

root = tk.Tk()
app = Login(root)
root.mainloop()