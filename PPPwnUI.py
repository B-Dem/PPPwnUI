import tkinter as tk
from tkinter import messagebox, filedialog
import psutil
import subprocess
import os
import sys

def get_network_interface_names():
    interfaces = psutil.net_if_addrs()
    return interfaces.keys()

class App:
    def __init__(self, master):

        self.master = master
        master.title("PPPwnUI v2.01 By Memz")

        # taille de la fenêtre
        master.geometry("400x380")
        # master.eval('tk::PlaceWindow . center')

        #Set the resizable property False
        master.resizable(False, False)

        # logo d'application
        master.iconbitmap("media/logo.ico")

        self.menu = tk.Menu(master)
        master.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Exit", command=master.quit)

        self.exploit_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="PPPwn", menu=self.exploit_menu)
        self.exploit_menu.add_command(label="  Start PPPwn > ", command=self.start_pppwn)

        self.help_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="About", command=self.about)
        
        # Menu déroulant pour les interfaces réseau
        self.interface_var = tk.StringVar(master)
        self.interface_var.set("Select an interface :") # .set("Ethernet") Réseau pré-sélectionné
        self.interface_menu = tk.OptionMenu(master, self.interface_var, *get_network_interface_names())
        self.interface_menu.pack()

        # Conteneur pour les colonnes des firmwares
        self.firmware_label = tk.Label(master, text="Choose your Firmware:")
        self.firmware_label.pack()
        self.columns_container = tk.Frame(master)
        self.columns_container.pack()

        # Firmwares avec noms des versions
        firmware_versions = ["7.50", "7.51", "7.55", "8.00", "8.01", "8.03", "8.50", "8.52", "Custom", "9.00", "9.03", "9.04", "9.50", "9.51", "9.60", "10.00", "10.01", "10.50", "10.70", "10.71", "11.00"]

        self.firmware_var = tk.StringVar(master)
        self.firmware_var.set("11.00")  # Firmware pré-sélectionné

        # Création boutons radio pour chaque firmware dans les colonnes gauche & droite
        self.left_column = tk.Frame(self.columns_container)
        self.left_column.pack(side=tk.LEFT)

        self.middle_column = tk.Frame(self.columns_container)
        self.middle_column.pack(side=tk.LEFT)

        self.right_column = tk.Frame(self.columns_container)
        self.right_column.pack(side=tk.RIGHT)

        column_counter = 0

        for firmware in firmware_versions:
            radio_button = tk.Radiobutton(self.left_column if column_counter % 3 == 0 else self.middle_column if column_counter % 3 == 1 else self.right_column, text=firmware, variable=self.firmware_var, value=firmware, command=self.show_payload_options)
            radio_button.pack(anchor=tk.W)
            column_counter += 1

        # Sélection payloads
        self.payload_frame = tk.Frame(master)

        self.payload_label = tk.Label(self.payload_frame, text="Select Payloads:")
        self.payload_label.pack()

        self.payload_var = tk.StringVar(master)

        self.custom_payloads_frame = tk.Frame(master)

        self.stage1_label = tk.Label(self.custom_payloads_frame, text="Custom Stage 1:")
        self.stage1_label.grid(row=0, column=0)

        self.stage1_path = tk.StringVar()
        self.stage1_entry = tk.Entry(self.custom_payloads_frame, textvariable=self.stage1_path, width=30)
        self.stage1_entry.grid(row=0, column=1)

        self.stage1_browse_button = tk.Button(self.custom_payloads_frame, text="Browse", command=self.select_stage1_file)
        self.stage1_browse_button.grid(row=0, column=2, padx=5)

        self.stage2_label = tk.Label(self.custom_payloads_frame, text="Custom Stage 2:")
        self.stage2_label.grid(row=1, column=0)

        self.stage2_path = tk.StringVar()
        self.stage2_entry = tk.Entry(self.custom_payloads_frame, textvariable=self.stage2_path, width=30)
        self.stage2_entry.grid(row=1, column=1)

        self.stage2_browse_button = tk.Button(self.custom_payloads_frame, text="Browse", command=self.select_stage2_file)
        self.stage2_browse_button.grid(row=1, column=2, padx=5)

        # Start PPPwn
        self.start_button = tk.Button(master, text="  Start PPPwn > ", bg='white',fg='blue', font = ('Sans','10','bold'), command=self.start_pppwn)
        self.start_button.pack(side=tk.BOTTOM, pady=10)

    def show_payload_options(self):
        if self.firmware_var.get() == "Custom":
            self.payload_frame.pack()
            self.custom_payloads_frame.pack()
        else:
            self.payload_frame.pack_forget()
            self.custom_payloads_frame.pack_forget()

    def select_stage1_file(self):
        stage1_file = filedialog.askopenfilename()
        self.stage1_path.set(stage1_file)

    def select_stage2_file(self):
        stage2_file = filedialog.askopenfilename()
        self.stage2_path.set(stage2_file)

    def start_pppwn(self):
        interface = self.interface_var.get()
        firmware = self.firmware_var.get()

        stage1_path = self.stage1_path.get()
        stage2_path = self.stage2_path.get()

        if interface == "Select an interface :":
            messagebox.showerror("Error", "Select a network interface")
            return

        if firmware == "Custom":
            command = f'python PPPwn/pppwn.py --interface="{interface}" --stage1="{stage1_path}" --stage2="{stage2_path}"'
        else:
            firmware_value = firmware.replace(".", "")
            if firmware_value.isdigit():
                command = f'python PPPwn/pppwn{firmware_value}.py --interface="{interface}" --fw={firmware_value}'
            else:
                messagebox.showerror("Error", "Invalid firmware selection")
                return

        try:
            subprocess.Popen(command, shell=True)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def about(self):
        messagebox.showinfo("About", "PPPwnUI v2.0\nThis app was developed by Memz to make PPPwn easier to use.")

if sys.platform == "linux" and not os.geteuid() == 0:
    print("You must run this program as administrator.")
    sys.exit(1)

root = tk.Tk()
app = App(root)
root.mainloop()