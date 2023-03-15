import os
from colorama import Fore
from pytube import YouTube

print('''
\033[34m  __  __           _     \033[35m _____                      _                 _           \033[0m
\033[34m |  \/  |         (_)    \033[35m|  __ \                    | |               | |          \033[0m
\033[34m | \  / |_   _ ___ _  ___\033[35m| |  | | _____      ___ __ | | ___   __ _  __| | ___ _ __ \033[0m
\033[34m | |\/| | | | / __| |/ __\033[35m| |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|\033[0m
\033[34m | |  | | |_| \__ \ | (__\033[35m| |__| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   \033[0m
\033[34m |_|  |_|\__,_|___/_|\___\033[35m|_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   \033[0m
''')
print("                     ------CoderSigma------              ")

yt = YouTube(str(input(f"{Fore.GREEN}Enter URL of youtube video:  ")))
video = yt.streams.filter(only_audio=True).first()

print("Enter the destination address (leave blank to save in current directory or hit enter para di ka mahirapang hampaslupa ka!)")

destination = str(input(" ")) or '.'
out_file = video.download(output_path=destination)

base, ext = os.path.splitext(out_file)

new_file = base + '.mp3'
os.rename(out_file, new_file)

print(yt.title + " has been successfully downloaded. Mag Enjoy kang earthling ka!")
