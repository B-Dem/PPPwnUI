import tkinter as tk
from tkinter import messagebox, filedialog
import psutil
import subprocess
import os
import sys

CUSTOM = "Custom"
GOLDHEN_900 = "Goldhen for 9.00"
GOLDHEN_1000 = "Goldhen for 10.00"
GOLDHEN_1001 = "Goldhen for 10.01"
GOLDHEN_1100 = "Goldhen for 11.00"

VTX_903  = "VTX HEN for 9.03"
VTX_1050 = "VTX HEN for 10.50"
VTX_1070 = "VTX HEN for 10.70"

LINUX_1GB = "Linux 1GB 11.00"
LINUX_2GB = "Linux 2GB 11.00"
LINUX_3GB = "Linux 3GB 11.00"
LINUX_4GB = "Linux 4GB 11.00"


def get_network_interface_names():
    interfaces = psutil.net_if_addrs()
    return interfaces.keys()

class App:
    def __init__(self, master):
        self.master = master
        master.title("PPPwnUI v3.1 by Memz")

        # taille de la fenêtre
        master.geometry("420x400")
        #master.eval('tk::PlaceWindow . center')

        # Set the resizable property False
        master.resizable(False, False)

        # logo d'application
        if sys.platform == "linux":
            pass
        else :
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
        if sys.platform == "linux":
            self.interface_var.set("Select an interface :") # Réseau pré-sélectionné
        else:
            self.interface_var.set("Ethernet") # .set("Select an interface :") # Réseau pré-sélectionné
        self.interface_menu = tk.OptionMenu(master, self.interface_var, *get_network_interface_names())
        self.interface_menu.pack()

        # Frame pour les boutons radio "PPPwn" et "PPPwn Goldhen"
        self.radio_frame = tk.Frame(master)
        self.radio_frame.pack()

        # Variables pour les boutons radio PPPwn et PPPwn Goldhen
        self.radio_var = tk.StringVar(master, value="PPPwn Goldhen")

        # Création des boutons radio pour PPPwn et PPPwn Goldhen
        self.pppwn_radio_button = tk.Radiobutton(self.radio_frame, text="PPPwn", variable=self.radio_var, value="PPPwn", command=self.update_firmware_options)
        self.pppwn_radio_button.pack(side=tk.LEFT, padx=5)

        self.goldhen_radio_button = tk.Radiobutton(self.radio_frame, text="PPPwn Goldhen", variable=self.radio_var, value="PPPwn Goldhen", command=self.update_firmware_options)
        self.goldhen_radio_button.pack(side=tk.LEFT, padx=5)

        self.hen_radio_button = tk.Radiobutton(self.radio_frame, text="HEN", variable=self.radio_var, value="HEN", command=self.update_firmware_options)
        self.hen_radio_button.pack(side=tk.LEFT, padx=5)

        self.linux_radio_button = tk.Radiobutton(self.radio_frame, text="Linux", variable=self.radio_var, value="Linux", command=self.update_firmware_options)
        self.linux_radio_button.pack(side=tk.LEFT, padx=5)

        self.custom_radio_button = tk.Radiobutton(self.radio_frame, text=CUSTOM, variable=self.radio_var, value=CUSTOM, command=self.update_firmware_options)
        self.custom_radio_button.pack(side=tk.LEFT, padx=5)

        # Frame pour les versions d'exploit
        self.exploit_frame = tk.Frame(master)
        self.exploit_frame.pack(pady=10)

        # Variable pour les versions d'exploit
        self.exploit_var = tk.StringVar(master, value="PPPwn Python")

        # Création des boutons radio pour les versions d'exploit
        self.pppwn_python_radio_button = tk.Radiobutton(self.exploit_frame, text="PPPwn Python", variable=self.exploit_var, value="PPPwn Python")
        self.pppwn_python_radio_button.pack(side=tk.LEFT, padx=5)

        # self.pppwn_cpp_radio_button = tk.Radiobutton(self.exploit_frame, text="PPPwn C++", variable=self.exploit_var, value="PPPwn C++")
        # self.pppwn_cpp_radio_button.pack(side=tk.LEFT, padx=5)

        self.pppwn_go_radio_button = tk.Radiobutton(self.exploit_frame, text="PPPwn_GO", variable=self.exploit_var, value="PPPwn_GO")
        self.pppwn_go_radio_button.pack(side=tk.LEFT, padx=5)

        # Conteneur pour les colonnes des firmwares
        self.firmware_label = tk.Label(master, text="Choose your Payload:")
        self.firmware_label.pack()
        self.columns_container = tk.Frame(master)
        self.columns_container.pack()

        self.selected_fw1 = "11.00"
        self.selected_fw2 = GOLDHEN_1100
        self.selected_fw3 = VTX_1070

        # Firmwares avec noms des versions
        self.firmware_var = tk.StringVar(master)
        self.firmware_var.set(self.selected_fw1)  # Firmware pré-sélectionné

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
        self.start_button.focus()

        self.update_firmware_options()  # Mettre à jour les options de firmware initiales

    def update_firmware_options(self):
        # Supprimer les boutons radio actuels
        for widget in self.columns_container.winfo_children():
            widget.destroy()

        # Mettre à jour les options de firmware en fonction de la sélection de l'utilisateur
        firmware_versions = self.get_firmware_options()

        if self.firmware_var.get() == GOLDHEN_900:
            self.selected_fw2 = self.firmware_var.get()
        elif self.firmware_var.get() == GOLDHEN_1000:
            self.selected_fw2 = self.firmware_var.get()
        elif self.firmware_var.get() == GOLDHEN_1001:
            self.selected_fw2 = self.firmware_var.get()
        elif self.firmware_var.get() == GOLDHEN_1100:
            self.selected_fw2 = self.firmware_var.get()
        elif self.firmware_var.get() != CUSTOM:
            self.selected_fw1 = self.firmware_var.get()

        # Créer les colonnes des boutons radio avec les nouvelles options de firmware
        if self.radio_var.get() == CUSTOM:
            num_columns = 2
            self.firmware_var.set(CUSTOM)
            self.custom_payloads_frame.pack()
        elif self.radio_var.get() == "HEN":
            num_columns = 1
            self.firmware_var.set(VTX_1070)
        elif self.radio_var.get() == "Linux":
            num_columns = 1
            self.firmware_var.set(LINUX_1GB)
        else:
            self.custom_payloads_frame.pack_forget()
            if self.radio_var.get() == "PPPwn":
                num_columns = 3
                self.firmware_var.set(self.selected_fw1)
            else:
                num_columns = 1
                self.firmware_var.set(self.selected_fw2)

        column_widgets = []
        for firmware in firmware_versions:
            radio_button = tk.Radiobutton(self.columns_container, text=firmware, variable=self.firmware_var, value=firmware, command=self.show_payload_options)
            column_widgets.append(radio_button)

        for i, widget in enumerate(column_widgets):
            column_index = i % num_columns
            row_index = i // num_columns
            widget.grid(row=row_index, column=column_index, sticky="w")

        self.show_payload_options

    def get_firmware_options(self):
        if self.radio_var.get() == "PPPwn":
            # Options de firmware pour PPPwn
            return ["7.00", "7.01", "7.02", "7.50", "7.51", "7.55",
                    "8.00", "8.01", "8.03", "8.50", "8.52",
                    "9.00", "9.03", "9.04", "9.50", "9.51", "9.60",
                    "10.00", "10.01", "10.50", "10.70", "10.71", "11.00"]
        elif self.radio_var.get() == "PPPwn Goldhen":
            # Options de firmware pour PPPwn Goldhen
            return [GOLDHEN_900, GOLDHEN_1000, GOLDHEN_1001, GOLDHEN_1100]
        elif self.radio_var.get() == "HEN":
            return [VTX_903, VTX_1050, VTX_1070]
        elif self.radio_var.get() == "Linux":
            return [LINUX_1GB, LINUX_2GB, LINUX_3GB, LINUX_4GB]
        elif self.radio_var.get() == CUSTOM:
            # Options de firmware pour PPPwn Goldhen
            return [CUSTOM]

    def show_payload_options(self):
        if self.firmware_var.get() == CUSTOM:
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
        exploit_version = self.exploit_var.get()

        stage1_path = self.stage1_path.get()
        stage2_path = self.stage2_path.get()

        if interface == "Select an interface :":
            messagebox.showerror("Error", "Select a network interface")
            return

        if firmware == CUSTOM:
            firmware_value = self.selected_fw1.replace(".", "")
            if not os.path.isfile(stage1_path):
                messagebox.showerror("Error", "Stage1 does not exist")
                return
            if not os.path.isfile(stage2_path):
                messagebox.showerror("Error", "Stage2 does not exist")
                return
            if sys.platform == "linux":
                command = f'python3 PPPwn/pppwn.py --interface="{interface}" --stage1="{stage1_path}" --stage2="{stage2_path}"'
            else:
                command = f'python PPPwn/pppwn.py --interface="{interface}" --stage1="{stage1_path}" --stage2="{stage2_path}"'
        elif firmware.find("Goldhen for ") != -1:
            firmware_value = firmware.replace("Goldhen for ","").replace(".", "")
            if exploit_version == "PPPwn Python":
                if sys.platform == "linux":
                    command = f'python3 PPPwn/pppwn.py --interface="{interface}" --stage1="PPPwn/goldhen/{firmware_value}/stage1.bin" --stage2="PPPwn/goldhen/{firmware_value}/stage2.bin"'
                else:
                    command = f'python PPPwn/pppwn.py --interface="{interface}" --stage1="PPPwn/goldhen/{firmware_value}/stage1.bin" --stage2="PPPwn/goldhen/{firmware_value}/stage2.bin"'
            elif exploit_version == "PPPwn C++":
                if sys.platform == "linux":
                    command = f'./PPPwn/pppwn_cpp --interface="{interface}" --stage1="PPPwn/goldhen/{firmware_value}/stage1.bin" --stage2="PPPwn/goldhen/{firmware_value}/stage2.bin"'
                else:
                    command = f'PPPwn\\pppwn_cpp.exe --interface="{interface}" --stage1="PPPwn/goldhen/{firmware_value}/stage1.bin" --stage2="PPPwn/goldhen/{firmware_value}/stage2.bin"'
            elif exploit_version == "PPPwn_GO":
                if sys.platform == "linux":
                    command = f'./PPPwn/pppwn_go --stage1="PPPwn/goldhen/{firmware_value}/stage1.bin" --stage2="PPPwn/goldhen/{firmware_value}/stage2.bin"'
                else:
                    command = f'PPPwn\\pppwn_go.exe --interface="{interface}" --stage1="PPPwn/goldhen/{firmware_value}/stage1.bin" --stage2="PPPwn/goldhen/{firmware_value}/stage2.bin"'
        elif firmware.find("VTX HEN for ") != -1:
            firmware_value = firmware.replace("VTX HEN for ","").replace(".", "")
            if exploit_version == "PPPwn Python":
                if sys.platform == "linux":
                    command = f'python3 PPPwn/pppwn.py --interface="{interface}" --stage1="PPPwn/hen/{firmware_value}/stage1.bin" --stage2="PPPwn/hen/{firmware_value}/stage2.bin"'
                else:
                    command = f'python PPPwn/pppwn.py --interface="{interface}" --stage1="PPPwn/hen/{firmware_value}/stage1.bin" --stage2="PPPwn/hen/{firmware_value}/stage2.bin"'
            elif exploit_version == "PPPwn C++":
                if sys.platform == "linux":
                    command = f'./PPPwn/pppwn_cpp --interface="{interface}" --stage1="PPPwn/hen/{firmware_value}/stage1.bin" --stage2="PPPwn/hen/{firmware_value}/stage2.bin"'
                else:
                    command = f'PPPwn\\pppwn_cpp.exe --interface="{interface}" --stage1="PPPwn/hen/{firmware_value}/stage1.bin" --stage2="PPPwn/hen/{firmware_value}/stage2.bin"'
            elif exploit_version == "PPPwn_GO":
                if sys.platform == "linux":
                    command = f'./PPPwn/pppwn_go --fw={firmware_value} --stage1="PPPwn/hen/{firmware_value}/stage1.bin" --stage2="PPPwn/hen/{firmware_value}/stage2.bin"'
                else:
                    command = f'PPPwn\\pppwn_go.exe --fw={firmware_value} --stage1="PPPwn/hen/{firmware_value}/stage1.bin" --stage2="PPPwn/hen/{firmware_value}/stage2.bin"'
        elif firmware.find("Linux") != -1:
            firmware_value = firmware.replace("Linux ", "").replace("GB", "gb").replace(" 11.00", "")
            stage2_file = f'PPPwn/linux/stage2-1100-{firmware_value}.bin'
            if exploit_version == "PPPwn Python":
                if sys.platform == "linux":
                    command = f'python3 PPPwn/pppwn.py --interface="{interface}" --stage1="PPPwn/linux/stage1-1100.bin" --stage2="{stage2_file}"'
                else:
                    command = f'python PPPwn/pppwn.py --interface="{interface}" --stage1="PPPwn/linux/stage1-1100.bin" --stage2="{stage2_file}"'
            elif exploit_version == "PPPwn C++":
                if sys.platform == "linux":
                    command = f'./PPPwn/pppwn_cpp --i "{interface}" --stage1="PPPwn/linux/stage1-1100.bin" --stage2="{stage2_file}"'
                else:
                    command = f'PPPwn\\pppwn_cpp.exe --i={interface} --stage1="PPPwn/linux/stage1-1100.bin" --stage2="{stage2_file}"'
            elif exploit_version == "PPPwn_GO":
                if sys.platform == "linux":
                    command = f'./PPPwn/pppwn_go --interface="{interface}" --stage1="PPPwn/linux/stage1-1100.bin" --stage2="{stage2_file}"'
                else:
                    command = f'PPPwn\\pppwn_go.exe --fw=1100 --stage1="PPPwn/linux/stage1-1100.bin" --stage2="{stage2_file}"'
        else: 
            firmware_value = firmware.replace(".", "")
            if firmware_value.isdigit():
                if exploit_version == "PPPwn Python":
                    if sys.platform == "linux":
                        command = f'python3 PPPwn/pppwn.py --interface="{interface}" --fw="{firmware_value}" --stage1="PPPwn/stage1/{firmware_value}/stage1.bin" --stage2="PPPwn/stage2/{firmware_value}/stage2.bin"'
                    else:
                        command = f'python PPPwn/pppwn.py --interface="{interface}" --fw="{firmware_value}" --stage1="PPPwn/stage1/{firmware_value}/stage1.bin" --stage2="PPPwn/stage2/{firmware_value}/stage2.bin"'
                elif exploit_version == "PPPwn C++":
                    if sys.platform == "linux":
                        command = f'./PPPwn/pppwn_cpp --interface="{interface}" --fw="{firmware_value}"'
                    else:
                        command = f'PPPwn\\pppwn_cpp.exe --interface="{interface}" --fw="{firmware_value}"'
                elif exploit_version == "PPPwn_GO":
                    if sys.platform == "linux":
                        command = f'./PPPwn/pppwn_go --interface="{interface}" --fw="{firmware_value}"'
                    else:
                        command = f'PPPwn\\pppwn_go.exe --interface="{interface}" --fw="{firmware_value}"'
            else:
                messagebox.showerror("Error", "Invalid firmware selection")
                return

        try:
            subprocess.Popen(command, shell=True)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"An error occurred: {e}")



    def about(self):
        messagebox.showinfo("About", "PPPwnUI v3.1\n\nDeveloped by Memz")

if sys.platform == "linux" and not os.geteuid() == 0:
    print("You must run this program as administrator.")
    sys.exit(1)

root = tk.Tk()
app = App(root)
root.mainloop()