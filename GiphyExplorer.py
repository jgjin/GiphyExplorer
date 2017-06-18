from os.path import isfile
from GiphyGenerator import GiphyGenerator
import time
import webbrowser

class GiphyExplorer:
    def __init__(self, timed = False, period = 60):
        """Initialize query, mode, and period"""
        self.query = raw_input("Enter query: ")
        while self.query.strip() == "":
            self.query = raw_input("Please enter a valid query: ")
        self.timed = timed
        self.period = period

    def explore(self):
        """Run GiphyExplorer"""
        self.initialize()
        self.readBookmark()
        self.viewImages()

    def initialize(self):
        """Perform query if necessary,
        then read results,
        then get web browser controller"""
        if not isfile(self.query + ".txt"):
            print ("Query \"" + self.query + \
                   "\" has not been performed, performing query")
            generator = GiphyGenerator(self.query)
            generator.generate()
        with open(self.query + ".txt", "r") as results:
            self.lines = results.readlines()
        self.controller = webbrowser.get("chromium-browser")

    def readBookmark(self):
        """Read or create bookmark,
        then report bookmark,
        then receive starting image number from user input"""
        bookmarkVal = 0
        self.bookmarkName = "bookmark_" + self.query
        if self.timed:
            self.bookmarkName += "_timed.txt"
        else:
            self.bookmarkName += "_user.txt"
        try:
            with open(self.bookmarkName, "r") as bookmark:
                bookmarkVal = int(bookmark.read())
        except IOError:
            with open(self.bookmarkName, "w") as bookmark:
                bookmark.write("0")
        print ("Last recorded first unviewed image number: " + str(bookmarkVal))
        self.imageNumber = input("Enter image number to view: ")
        while not (isinstance(self.imageNumber, int) and self.imageNumber > -1):
            self.imageNumber = input(
                "Please enter a nonnegative image number: ")

    def viewImages(self):
        """View images one at a time in either timed or user response mode"""
        while self.imageNumber < len(self.lines):
            self.viewImage()
            self.imageNumber += 1
            self.recordBookmark()
            if self.timed:
                response = raw_input("[w]ait for " + str(self.period) + "s/[n]ext image: ")
                while response != "w" and response != "n":
                    response = raw_input("Please enter \"w\" or \"n\": ")
                if response == "w":
                    time.sleep(self.period)
            else:
                response = raw_input("Continue? (y/n): ")
                while response != "y" and response != "n":
                    response = raw_input("Please enter \"y\" or \"n\": ")
                if response == "n":
                    break

    def viewImage(self):
        """View image with image number self.imageNumber"""
        print ("Viewing image number " + str(self.imageNumber))
        url = self.lines[self.imageNumber]
        self.controller.open(url)

    def recordBookmark(self):
        """Record last unviewed image image number"""
        with open(self.bookmarkName, "w") as bookmark:
            if self.imageNumber >= len(self.lines):
                print ("All images viewed, setting bookmark to 0")
                bookmark.write("0")
            else:
                bookmark.write(str(self.imageNumber))

if __name__ == "__main__":
    period = input(
        "Enter period (-1 to use user response mode instead of timed mode): ")
    while not (isinstance(period, int) and (period > 0 or period == -1)):
        period = input(
            "Please enter a positive integer or -1 to use user response mode: ")
    explorer = GiphyExplorer(timed = (period != -1), period = period)
    explorer.explore()
