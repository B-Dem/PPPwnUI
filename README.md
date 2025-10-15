# PPPwnUI
PPPwnUI is a Python/TK GUI for installing the GoldHen homebrew tool for the PS4 [PPPwn](https://github.com/TheOfficialFloW/PPPwn/) created by [TheFlow](https://github.com/TheOfficialFloW/).

goldhen enables you to install homebrew PS4 software onto the PS4's hard drive and copy files to and from it via FTP amongst other handy features.

## Hardware requirements

PPPwn UI requires an ethernet port and cable to connect your computer to the PS4.

You must be running PS4 firmware v11.00. Unfortunately this exploit does not curently work under later firmware revisions.


## Installation :

- Clone the repository:

```sh
git clone https://github.com/B-Dem/PPPwnUI
```

- Install the requirements:

Under Debian and Ubuntu based Linux distros run:

```sh
sudo apt install python3-scapy python3-tk
```

## Network configuration

Your ethernet port must be configured to use the **shared to other computers** method before you run PPPwnUI.

You can configure this under Linux using the NetworkManager GUI by opening your wired connection's settings window, switch to the **IPv4 settings** tab then click the **Method** drop down menu and change the **Method** confguration option to use **shared to other computers**.

## Copy goldhen.bin to a USB disk

On your computer:

- Copy `goldhen.bin` from the **USB Drive (GoldHEN_vX.XXX)** directory of this repo to the root directory of an exfat/fat32 USB and insert it into your PS4.

Note that you are only required to have the USB disk storing **goldhen.bin** inserted into your PS4 on the frst time that you successfully run PPPwnUI. **goldhen.bin** is copied onto your PS4 hard drive after being run once so that subsequent uses of PPPwnUI will work without a USB disk.

## Running PPPwnUI

- Launch the app by cd'ing into the repo's directory then run:

  **Windows :**
  
  ```PPPwnUI.bat```

  **Linux :**

  ```sh
  sudo python3 PPPwnUI.py
  ```

**PPPwnUI must be run either using sudo or as the root user**

- Select your Interface using the drop-down menu. Under Linux this will usually be eth0.

- Choose Between the Exploit Version you want to use ([PPPwn Python](https://github.com/TheOfficialFloW/PPPwn), [PPPwn_Go](https://github.com/BestPig/PPPwn_go))

- Choose your Payload Between :

- **PPPwn** : (Available for : 7.00, 7.01, 7.02, 7.50, 7.51, 7.55, 8.00, 8.01, 8.03, 8.50, 8.52, 9.00, 9.03, 9.04, 9.50, 9.51, 9.60, 10.00, 10.01, 10.50, 10.70, 10.71 & 11.00)

- **PPPwn Goldhen** Payloads : (Available for : 9.00, 9.60, 10.00, 10.01 & 11.00)

- **VTX HEN** : (Available for : 7.55, 8.00, 8.03, 8.50, 8.52, 9.00, 9.03, 9.04, 10.00, 10.01 10.50, 10.70, 10.71 & 11.00)

- **PPPwn Linux Payloads** : (Available for : 11.00) 

- **Custom Payloads** : (Your own custom Payloads)
 

- Then click on **Start PPPwn** to start the Exploit.


## Connecting to PPPwn from your PS4

After configuring your ethernet interface, copying goldhen.bin onto USB, connecting an ethernet cable to your PS4 and starting PPPwn you do the following on your PS4:

- Go to **Settings**` and then **Network**
- Select **Set Up Internet connection** and choose **Use a LAN Cable**
- Choose **Custom setup** and choose **PPPoE** for **IP Address Settings**
- Enter anything for **PPPoE User ID** and **PPPoE Pasword**
- Choose **Automatic** for **DNS Settings** and **MTU Settings**
- Choose **Do Not Use** for **Proxy Server**
- Click **Test Internet Connection** to connect to PPwnUI

If the exploit fails or the PS4 crashes, you can skip the internet setup and simply click on `Test Internet Connection`. If the script fail or is stuck waiting for a request/response, abort it and run it again on your computer, and then click on `Test Internet Connection` on your PS4.


## Example run : 

```sh
[+] PPPwn - PlayStation 4 PPPoE RCE by theflow
[+] args: interface=enp0s3 fw=1100 stage1=stage1/stage1.bin stage2=stage2/stage2.bin
[+] Using PPPwnUI By Memz !

[+] STAGE 0: Initialization
[*] Waiting for PADI...
[+] pppoe_softc: 0xffffabd634beba00
[+] Target MAC: xx:xx:xx:xx:xx:xx
[+] Source MAC: 07:ba:be:34:d6:ab
[+] AC cookie length: 0x4e0
[*] Sending PADO...
[*] Waiting for PADR...
[*] Sending PADS...
[*] Waiting for LCP configure request...
[*] Sending LCP configure ACK...
[*] Sending LCP configure request...
[*] Waiting for LCP configure ACK...
[*] Waiting for IPCP configure request...
[*] Sending IPCP configure NAK...
[*] Waiting for IPCP configure request...
[*] Sending IPCP configure ACK...
[*] Sending IPCP configure request...
[*] Waiting for IPCP configure ACK...
[*] Waiting for interface to be ready...
[+] Target IPv6: fe80::2d9:d1ff:febc:83e4
[+] Heap grooming...done

[+] STAGE 1: Memory corruption
[+] Pinning to CPU 0...done
[*] Sending malicious LCP configure request...
[*] Waiting for LCP configure request...
[*] Sending LCP configure ACK...
[*] Sending LCP configure request...
[*] Waiting for LCP configure ACK...
[*] Waiting for IPCP configure request...
[*] Sending IPCP configure NAK...
[*] Waiting for IPCP configure request...
[*] Sending IPCP configure ACK...
[*] Sending IPCP configure request...
[*] Waiting for IPCP configure ACK...
[+] Scanning for corrupted object...found fe80::0fdf:4141:4141:4141

[+] STAGE 2: KASLR defeat
[*] Defeating KASLR...
[+] pppoe_softc_list: 0xffffffff884de578
[+] kaslr_offset: 0x3ffc000

[+] STAGE 3: Remote code execution
[*] Sending LCP terminate request...
[*] Waiting for PADI...
[+] pppoe_softc: 0xffffabd634beba00
[+] Target MAC: xx:xx:xx:xx:xx:xx
[+] Source MAC: 97:df:ea:86:ff:ff
[+] AC cookie length: 0x511
[*] Sending PADO...
[*] Waiting for PADR...
[*] Sending PADS...
[*] Triggering code execution...
[*] Waiting for stage1 to resume...
[*] Sending PADT...
[*] Waiting for PADI...
[+] pppoe_softc: 0xffffabd634be9200
[+] Target MAC: xx:xx:xx:xx:xx:xx
[+] AC cookie length: 0x0
[*] Sending PADO...
[*] Waiting for PADR...
[*] Sending PADS...
[*] Waiting for LCP configure request...
[*] Sending LCP configure ACK...
[*] Sending LCP configure request...
[*] Waiting for LCP configure ACK...
[*] Waiting for IPCP configure request...
[*] Sending IPCP configure NAK...
[*] Waiting for IPCP configure request...
[*] Sending IPCP configure ACK...
[*] Sending IPCP configure request...
[*] Waiting for IPCP configure ACK...

[+] STAGE 4: Arbitrary payload execution
[*] Sending stage2 payload...
[+] Done!
```

## Installing PS4 .pkg files

Its possible to install pkg files via USB disk but its usually faster and easier to copy pkg files onto your PS4 using a FTP program such as [FileZilla.](https://filezilla-project.org/)

Copy your .pkg files into the **/data/pkg** directory on your PS4. To install them use the **Package Installer** option within the **Debug Settings** menu of the **Goldhen** app on the home screen.

For more detailed instructions see [this guide.](https://consolemods.org/wiki/PS4:How_to_Install_PKG_Files)

## To do : 

- Rebuild PPPwn_CPP to use Interface Name and not ID  
- Auto Updater

This Program was originally made with ❤️ by [Memz](https://github.com/B-Dem) for [Sighya](https://sighya.fr).

If you find this program helpful please star the repo and open an issue if you find any bugs.
