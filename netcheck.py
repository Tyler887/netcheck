import requests
from art import *
from colorama import *
import os
os.system("cls" if os.name=="nt" else "clear")
tprint("Network\n      ?     Checker")
print(f"{Fore.RED}+{Style.RESET_ALL} Got a problem? {Fore.GREEN}Check your network{Style.RESET_ALL}! {Fore.RED}+{Style.RESET_ALL}\n")
site = input("Enter site to connect to: ")
if site == "":
    site = "http://example.org"
try:
      r = requests.head(site)
      http = str(r.status_code)
      if not http.startswith("2") and not http.startswith("3"): # 2XX is OK, 3XX is redirect. Other codes are ERRORs. Also prints google-like message.
        print(Fore.RED + "(" + http + ". That's an error.)")
        print("No connection. Detected HTTP code " + http + " " + responses[r.status_code] + "." + Style.RESET_ALL)
        input("Press Enter to exit... ")
        exit()
except requests.ConnectionError:
      print(Fore.RED + "No connection. Could not establish a working connection to your requested site.\nIt could be that the site is down. There's no server admin for example sites; if the hostname does not begin with\n'example.', contact the server administrator." + Style.RESET_ALL)
      input("Press Enter to exit... ")
      exit()
except TimeoutError:
      print(Fore.RED + "No connection. Connection has timed out." + Style.RESET_ALL)
      input("Press Enter to exit... ")
      exit()
except KeyboardInterrupt:
  raise KeyboardInterrupt("Cancelled via keyboard")
else:
      print("Your connection works properly.")
      input("Press Enter to Exit... ")