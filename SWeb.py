#! python3
# SWeb.py is smart search web from the terminal

import requests
import sys
import webbrowser

if len(sys.argv) > 1:
    site = sys.argv[1]
    user = sys.argv[2]
else:
    print("python3 SWeb.py [sitenmae] [username]")
    sys.exit()
webbrowser.open('https://www.' + site + '.com/' +  user + '/')


