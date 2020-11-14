import sys
import os
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style

stack = list()
args = sys.argv

dir_for_files = args[1]

try:
    os.mkdir(dir_for_files)
except FileExistsError:
    print(f"Directory {dir_for_files} is already exists!")


def check_url(url_string):
    if "." in url_string:
        return True
    else:
        return False


def main():
    while True:
        url = input()
        if url == "exit":
            break
        elif url == "back" and len(stack) != 1:
            stack.pop()
            print(stack.pop())
        elif check_url(url):
            text = ""
            r = requests.get("http://" + url)
            soup = BeautifulSoup(r.content, 'html.parser')
            all_tags = soup.find_all(["div", "p", "a", "h1", "h2", "h3", "h4", "h5", "h6", "ul", "ol", "li"])
            with open(dir_for_files + "/" + url.split(".")[0], "w", encoding="utf-8") as f:
                for tag in all_tags:
                    if tag.string:
                        if tag.name == "a":
                            print(Fore.BLUE + tag.string)
                            print(Fore.BLUE + tag.string, file=f, flush=True)
                            text = text + Fore.BLUE + tag.string + "\n"
                        else:
                            print(Style.RESET_ALL + tag.string)
                            print(Style.RESET_ALL + tag.string, file=f, flush=True)
                            text = text + Style.RESET_ALL + tag.string + "\n"

            stack.append(text)

        else:
            print("error!")


if __name__ == "__main__":
    main()
