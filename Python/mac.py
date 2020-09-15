import subprocess
newmac=raw_input("Enter new MAC Address: ")

subprocess.call(["ifconfig","wlan0","down"])
subprocess.call(["ifconfig", "wlan0", "hw", "ether",newmac])
subprocess.call(["ifconfig","wlan0","up"])
