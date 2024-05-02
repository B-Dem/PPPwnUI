import tkinter as tk
from tkinter import messagebox, scrolledtext
import psutil
import subprocess

def get_network_interface_names():
    interfaces = psutil.net_if_addrs()
    return interfaces.keys()

class App:
    def __init__(self, master):
        self.master = master
        master.title("PPwnUI v1.1 By Memz")

        # Définir la taille de la fenêtre
        master.geometry("450x450")

        # Ajouter un logo d'application
        master.iconbitmap("media/sighya.ico")

        self.menu = tk.Menu(master)
        master.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Menu", menu=self.file_menu)
        self.file_menu.add_command(label="Leave App", command=master.quit)

        self.exploit_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="PPPwn", menu=self.exploit_menu)
        self.exploit_menu.add_command(label="Start PPPwn", command=self.start_pppwn)

        self.help_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="More", menu=self.help_menu)
        self.help_menu.add_command(label="About", command=self.about)
        
        self.label = tk.Label(master, text="Select an interface :")
        self.label.pack()

        # Menu déroulant pour les interfaces réseau
        self.interface_var = tk.StringVar(master)
        self.interface_var.set("Select an interface :")
        self.interface_menu = tk.OptionMenu(master, self.interface_var, *get_network_interface_names())
        self.interface_menu.pack()

        # Ajouter les firmwares
        self.firmware_var = tk.StringVar(master)
        self.firmware_var.set("900")  # Firmware pré-sélectionné
        self.firmware_label = tk.Label(master, text="Choose your Firmware:")
        self.firmware_label.pack()
        self.firmware_radio_900 = tk.Radiobutton(master, text="9.00", variable=self.firmware_var, value="900")
        self.firmware_radio_903 = tk.Radiobutton(master, text="9.03", variable=self.firmware_var, value="903")
        self.firmware_radio_904 = tk.Radiobutton(master, text="9.04", variable=self.firmware_var, value="904")
        self.firmware_radio_1100 = tk.Radiobutton(master, text="11.00", variable=self.firmware_var, value="1100")
        self.firmware_radio_1000 = tk.Radiobutton(master, text="10.00", variable=self.firmware_var, value="1000")
        self.firmware_radio_1001 = tk.Radiobutton(master, text="10.01", variable=self.firmware_var, value="1001")
        self.firmware_radio_900.pack()
        self.firmware_radio_903.pack()
        self.firmware_radio_904.pack()
        self.firmware_radio_1000.pack()
        self.firmware_radio_1001.pack()
        self.firmware_radio_1100.pack()

        # Bouton Start PPPwn
        self.start_button = tk.Button(master, text="Start PPPwn", command=self.start_pppwn)
        self.start_button.pack(side=tk.BOTTOM, pady=10)

    def start_pppwn(self):
        interface = self.interface_var.get()
        firmware = self.firmware_var.get()

        if firmware == "900":
            command = f'python pppwn900.py --interface="{interface}" --fw=900'
        elif firmware == "1100":
            command = f'python pppwn1100.py --interface="{interface}" --fw=1100'
        elif firmware == "903":
            command = f'python pppwn903.py --interface="{interface}" --fw=903'
        elif firmware == "904":
            command = f'python pppwn904.py --interface="{interface}" --fw=904'
        elif firmware == "1000":
            command = f'python pppwn1000.py --interface="{interface}" --fw=1000'
        elif firmware == "1001":
            command = f'python pppwn1001.py --interface="{interface}" --fw=1001'
        else:
            messagebox.showerror("Error", "Invalid firmware selection")
            return

        try:
            subprocess.Popen(command, shell=True)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def about(self):
        messagebox.showinfo("About", "PPPwnUI v1.1\nThis app was developped by Memz for Sighya to make PPPwn easier to use.")

root = tk.Tk()
app = App(root)
root.mainloop()
