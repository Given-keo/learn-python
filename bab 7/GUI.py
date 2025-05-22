import tkinter as tk
from tkinter import messagebox

class Choices:
    def __init__(self): 
        pass

    def PilihanGame(self, GameChoice):
        games = {
            "1": "Mobile Legend",
            "2": "Free Fire",
            "3": "PUBG",
            "4": "Honor Of King"
        }
        return games.get(GameChoice, "Pilihan Tidak Tersedia")

    def PilihanPaket(self, PaketChoice):
        paket_choices = {
            "1": ('100 Diamond', 20000, 'Paket Ramah di Kantong'),
            "2": ('300 Diamond', 45000, 'Paket Level Menengah'),
            "3": ('500 Diamond', 50000, 'Paket Hemat!'),
            "4": ('900 Diamond', 75000, 'Paket Unggulan'),
            "5": ('1300 Diamond', 90000, 'Paket Hemat Pake Banget!!!')
        }
        return paket_choices.get(PaketChoice, (None, 0, 'Pilihan Tidak Tersedia'))

    def PaymentMethod(self, PembayaranChoice):
        payment_choice = {
            '1': 'Transfer Bank',
            '2': 'E- Wallet (Gopay, OVO)',
            '3': 'Pulsa',
            '4': 'Kartu Kredit'
        }
        return payment_choice.get(PembayaranChoice, 'Pilihan Tidak Tersedia')


class RiwayatPesanan:
    def __init__(self):  
        self.history = []

    def tambah_pesanan(self, game, paket, harga, metode_pembayaran):
        order = {
            'game': game,
            'paket': paket,
            'harga': harga,
            'metode_pembayaran': metode_pembayaran
        }
        self.history.append(order)

    def tampilkan_riwayat(self):
        return self.history


class TopUpApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Top Up Game")
        self.window.geometry('400x400')
        self.choices = Choices()
        self.riwayat_pesanan = RiwayatPesanan()

        self.create_widgets()

    def create_widgets(self):
        # Game Selection
        self.game_option = tk.Label(self.window,text='Menu Game',font=('Arial',14,'bold'))
        self.game_option.pack()

        self.frame_list = tk.Frame(self.window,bg='lightgrey',pady=18)
        self.frame_list.pack()

        self.frame_list_game = tk.Label(self.frame_list)
        self.frame_list_game.pack(side=tk.LEFT,padx=5)

        self.frame_list_paket = tk.Label(self.frame_list)
        self.frame_list_paket.pack(side=tk.LEFT,padx=5)


        # ini list game
        list_product_game = tk.Label(self.frame_list_game,text='Daftar Game :',font=('arial',12,'bold'))
        list_product_game.pack()

        list_pertama = tk.Label(self.frame_list_game,text='1. Mobile Legend')
        list_pertama.pack()
        list_kedua = tk.Label(self.frame_list_game,text='2. Free Fire')
        list_kedua.pack()
        list_ketiga = tk.Label(self.frame_list_game,text='3. PUBG')
        list_ketiga.pack()
        list_keempat = tk.Label(self.frame_list_game,text='4. Honor Of King')
        list_keempat.pack()

        # ini list paket
        list_paket = tk.Label(self.frame_list_paket,text='Daftar paket :',font=('arial',12,'bold'))
        list_paket.pack()

        list_pertama = tk.Label(self.frame_list_paket,text='1. Mobile Legend')
        list_pertama.pack()
        list_kedua = tk.Label(self.frame_list_paket,text='2. Free Fire')
        list_kedua.pack()
        list_ketiga = tk.Label(self.frame_list_paket,text='3. PUBG')
        list_ketiga.pack()
        list_keempat = tk.Label(self.frame_list_paket,text='4. Honor Of King')
        list_keempat.pack()


        self.game_label = tk.Label(self.window, text="Pilih Game (1-4):")
        self.game_label.pack()

        self.game_var = tk.StringVar()
        self.game_entry = tk.Entry(self.window, textvariable=self.game_var)
        self.game_entry.pack()

        # Package Selection
        self.paket_label = tk.Label(self.window, text="Pilih Paket (1-5):")
        self.paket_label.pack()

        self.paket_var = tk.StringVar()
        self.paket_entry = tk.Entry(self.window, textvariable=self.paket_var)
        self.paket_entry.pack()

        # Payment Method Selection
        self.payment_label = tk.Label(self.window, text="Pilih Metode Pembayaran (1-4):")
        self.payment_label.pack()

        self.payment_var = tk.StringVar()
        self.payment_entry = tk.Entry(self.window, textvariable=self.payment_var)
        self.payment_entry.pack()

        # ID Input
        self.id_label = tk.Label(self.window, text="Masukkan ID Game Anda:")
        self.id_label.pack()

        self.id_var = tk.StringVar()
        self.id_entry = tk.Entry(self.window, textvariable=self.id_var)
        self.id_entry.pack()

        # Submit Button
        self.submit_button = tk.Button(self.window, text="Submit", command=self.submit_order)
        self.submit_button.pack()

        # Show History Button
        self.history_button = tk.Button(self.window, text="Tampilkan Riwayat Pesanan", command=self.show_history)
        self.history_button.pack()

    def submit_order(self):
        game_choice = self.game_var.get()
        paket_choice = self.paket_var.get()
        payment_choice = self.payment_var.get()
        game = self.choices.PilihanGame(game_choice)
        paket, harga, deskripsi = self.choices.PilihanPaket(paket_choice)
        payment_method = self.choices.PaymentMethod(payment_choice)
        game_id = self.id_var.get()

        if game == "Pilihan Tidak Tersedia" or paket[0] is None or payment_method == "Pilihan Tidak Tersedia":
            messagebox.showerror("Error", "Pilihan tidak valid.")
            return

        self.riwayat_pesanan.tambah_pesanan(game, paket[0], harga, payment_method)
        messagebox.showinfo("Success", f"Pesanan berhasil ditambahkan:\nGame: {game}\nPaket: {paket[0]}\nHarga: Rp {harga}\nMetode Pembayaran: {payment_method}")

    def show_history(self):
        history = self.riwayat_pesanan.tampilkan_riwayat()
        if not history:
            messagebox.showinfo("Riwayat Pesanan", "Tidak ada riwayat pesanan.")
            return

        history_message = "Riwayat Pesanan:\n"
        for index, order in enumerate(history, start=1):
            history_message += (f"{index}. Game: {order['game']}, Paket: {order['paket']}, "
                                f"Harga: Rp {order['harga']}, Pembayaran: {order['metode_pembayaran']}\n")

        messagebox.showinfo("Riwayat Pesanan", history_message)


# Contoh penggunaan
root = tk.Tk()
main_app = TopUpApp(root)
root.mainloop()