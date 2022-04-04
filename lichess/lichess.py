import requests
from bs4 import BeautifulSoup


username = input("What is your lichess username(Note that it is case sensitive): ")

r = requests.get(f"https://lichess.org/@/{username}")

soup = BeautifulSoup(r.content , "html.parser")
ratings =soup.find_all("div", {"class":"side sub-ratings"})





from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep

if username == "":
    print("Please provide the username")
    print("Exiting.....")

else:
    class Loader:
        def __init__(self, desc="Loading...", end="Done!", timeout=0.1):
            """
            A loader-like context manager

            Args:
                desc (str, optional): The loader's description. Defaults to "Loading...".
                end (str, optional): Final print. Defaults to "Done!".
                timeout (float, optional): Sleep time between prints. Defaults to 0.1.
            """
            self.desc = desc
            self.end = end
            self.timeout = timeout

            self._thread = Thread(target=self._animate, daemon=True)
            self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
            self.done = False

        def start(self):
            self._thread.start()
            return self

        def _animate(self):
            for c in cycle(self.steps):
                if self.done:
                    break
                print(f"\r{self.desc} {c}", flush=True, end="")
                sleep(self.timeout)

        def __enter__(self):
            self.start()

        def stop(self):
            self.done = True
            cols = get_terminal_size((80, 20)).columns
            print("\r" + " " * cols, end="", flush=True)
            print(f"\r{self.end}", flush=True)

        def __exit__(self, exc_type, exc_value, tb):
            # handle exceptions with those variables ^
            self.stop()


    if __name__ == "__main__":
        with Loader("Finding your username..."):
            for i in range(10):
                sleep(0.25)

        loader = Loader("Loading your ratings...", "Found the data !", 0.05).start()
        for i in range(10):
            sleep(0.25)
        loader.stop()


    try:
        print("\n \n \n")
        print("Ultrabullet rating: " + "" +ratings[0].find_all("strong")[0].text)
    except:
        print("Ultrabullet ratings : None")
    try:
        print("Bullet rating: " + "" + ratings[0].find_all("strong")[1].text)
    except:
        print("Bullet rating : None")
    try:
        print("Rapid rating: " + "" + ratings[0].find_all("strong")[2].text)
    except:
        print("Rapid rating: None")
    try:
        print("Classical rating: " + "" + ratings[0].find_all("strong")[3].text)
    except:
        print("Classical Rating: None")
    try:
        print("Correspondence rating: " + "" + ratings[0].find_all("strong")[4].text)
    except:
        print("Classical Rating: None")
    try:
        print("Crazyhouse rating: " + "" + ratings[0].find_all("strong")[5].text)
    except:
        print("Crazyhouse Rating: None")
    try:
        print("Chess960 rating: " + "" + ratings[0].find_all("strong")[6].text)
    except:
        print("Chess960 rating: None")
    try:
        print("King of the hill rating: " + "" + ratings[0].find_all("strong")[7].text)
    except:
        print("King of the hill rating: None")
    try:
        print("Three check rating: " + "" + ratings[0].find_all("strong")[8].text)
    except:
        print("Three check rating: None")
    try:
        print("Antichess rating: " + "" + ratings[0].find_all("strong")[9].text)
    except:
        print("Antichess rating: None")
    try:
        print("Atomic rating: " + "" + ratings[0].find_all("strong")[10].text)
    except:
        print("Atomic rating: None")
    try:
        print("Horde rating: " + "" + ratings[0].find_all("strong")[11].text)
    except:
        print("Horde rating: None")
    try:
        print("Racing Kings rating: " + "" + ratings[0].find_all("strong")[12].text)
    except:
        print("Racing Kings rating: None")
    try:
        print("Puzzles rating: " + "" + ratings[0].find_all("strong")[13].text)
    except:
        print("Puzzle Kings rating: None")
    try:
        print("Puzzle storm rating: " + "" + ratings[0].find_all("strong")[14].text)
    except:
        print("Puzzles Kings rating: None")
    try:
        print("Puzzle racer rating: " + "" + ratings[0].find_all("strong")[15].text)
    except:
        print("Puzzle racer rating: None")
    try:
        print("Puzzle streak rating: " + "" + ratings[0].find_all("strong")[16].text)
    except:
        print("Puzzle streak rating: None")
