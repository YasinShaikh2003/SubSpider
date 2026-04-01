from colorama import Fore, Style

def banner():

    print(Fore.GREEN + r"""
   _____       _     _____       _     _           
  / ____|     | |   / ____|     (_)   | |          
 | (___  _   _| |__| (___  _ __  _  __| | ___ _ __ 
  \___ \| | | | '_ \\___ \| '_ \| |/ _` |/ _ \ '__|
  ____) | |_| | |_) |___) | |_) | | (_| |  __/ |   
 |_____/ \__,_|_.__/_____/| .__/|_|\__,_|\___|_|   
                          | |                      
                          |_|                      

        SubSpider - Subdomain Discovery Tool
    """ + Style.RESET_ALL)


def save_results(results, filename):

    with open(filename, "w") as f:
        for sub, ip in results:
            f.write(f"{sub} -> {ip}\n")