from FileManager import read_file
from YoutubeFile import download_file

your_file = "files/test.txt"
path_to_storage = "~/Music/"

tracks = read_file(your_file)
download_file(tracks, path_to_storage)


