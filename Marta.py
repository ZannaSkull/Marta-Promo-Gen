from pystyle import Colors, Colorate
from pypresence import Presence
import threading
import requests
import colorama
import random
import ctypes
import time
import os

PINK = "\033[95m"
RESET = "\033[0m"
BOLD = "\033[1m"

def GamingName(title):
    Yes = title.encode('cp1252')
    ctypes.windll.kernel32.SetConsoleTitleA(Yes)

def SettingsRPC():
    RPC = Presence(client_id="1171087300864786515")
    RPC.connect()
    RPC.update(
        state="Marta Promo Gen 🌹",
        details="im in love with her",
        large_image="martagen",
        large_text="Oh shit if i love her.."
    )
    return RPC

os.system("cls" if os.name == "nt" else "clear")

def Printitle():
    GamingTextw = r"""    
   __  ___         __         _____       
  /  |/  /__ _____/ /____ _  / ___/__ ___ 
 / /|_/ / _ `/ __/ __/ _ `/ / (_ / -_) _ \
/_/  /_/\_,_/_/  \__/\_,_/  \___/\__/_//_/

            Made by Hisako                                                    
    """.format()
        
    print(Colorate.Horizontal(Colors.purple_to_blue, GamingTextw, True)) 

GamingName("Marta Gen <3 ")    
Printitle()
RPC = SettingsRPC()
  
useproxiesor = input(Colorate.Horizontal(Colors.purple_to_blue, "Do you want to use proxies? (yes/no): ", 1))
howmany = int(input(Colorate.Horizontal(Colors.purple_to_blue, "Enter the number of threads: ", 1)))
    
class Counter:
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1
        return self.count

def pickproxy(file_path):
    with open(file_path, 'r') as file:
        proxies = [line.strip() for line in file.readlines()]
    return proxies

def dildogen():
    return ''.join(random.choice('0123456789abcdef') for _ in range(64))

def code(proxy, counter):
    headers = {
        'authority': 'api.discord.gx.games',
        'accept': '*/*',
        'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://www.opera.com',
        'referer': 'https://www.opera.com/',
        'sec-ch-ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/105.0.0.0 (Edition std-1)',
    }

    jsondata = {
        'partnerUserId': dildogen(),
    }

    with requests.Session() as session:
        response = session.post('https://api.discord.gx.games/v1/direct-fulfillment', headers=headers, json=jsondata, proxies=proxy)
        if response.status_code == 200:
            promo = f'discord.com/billing/partner-promotions/1180231712274387115/{response.json()["token"]}\n'
            count = counter.increment()
            print(colorama.Fore.GREEN + promo[:117] + ".. " + colorama.Fore.YELLOW + "Generated:" + colorama.Fore.RESET + f" [{count}]")
            with open('promo codes.txt', 'a') as f:
                f.write(promo)
        else:
            print(colorama.Fore.RED + "Rate-limit")
            time.sleep(300)

def worker(proxies, counter, useproxiesor):
    while True:
        if useproxiesor.lower() == 'yes':
            proxy = {
                'http': random.choice(proxies),
                'https': random.choice(proxies),
            }
        else:
            proxy = None

        try:
            code(proxy, counter)
        except:
            pass


proxies = pickproxy('proxies.txt') if useproxiesor.lower() == 'yes' else []

counter = Counter()
threads = [threading.Thread(target=worker, args=(proxies, counter, useproxiesor)) for _ in range(howmany)]
for t in threads:
    t.start()