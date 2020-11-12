from os import system as execute
from os import path
from colorama import Fore as c

def download_file(tracks, storage):
    original_path = storage
    for track in tracks:
        if track[0] == "#":
            track = track.replace("#", "")
            comment_text = f"[{c.MAGENTA}#{c.WHITE}] ~> {c.MAGENTA}{track}{c.WHITE}"
            print(comment_text)
        elif track[0] == "[":
            track = track.replace("[", "")
            track = track.replace("]", "")
            playlist_text = f"[{c.YELLOW}*{c.WHITE}] >>> {c.YELLOW}{track}{c.WHITE}"
            storage = original_path + track
            print(playlist_text)
            if path.exists(storage) is False:
                execute(f"mkdir {storage}")
        else:
            download_track = f"[{c.GREEN}+{c.WHITE}] Downloading: {c.GREEN}{track}{c.WHITE}"
            command = f"cd {storage} && youtube-dl -qx --audio-format mp3 {track}"
            execute(command)


