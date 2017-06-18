import requests
import json

class GiphyGenerator:
    def __init__(self, query = "banana"):
        """Initialize query"""
        self.query = query

    def generate(self):
        """Run GiphyGenerator"""
        with open(self.query + ".txt", "w") as txt:
            images = self.search(offset = 0)
            for image in images["data"]:
                txt.write(image["images"]["original"]["url"] + "\n")
            nextIndex = 100
            totalCount = images["pagination"]["total_count"]
            print ("Collected \"" + self.query + "\" images " + \
                "number 0-" + str(min(nextIndex, totalCount)) + \
                " of " + str(totalCount))
            while nextIndex < totalCount:
                images = self.search(offset = nextIndex)
                for image in images["data"]:
                    txt.write(image["images"]["original"]["url"] + "\n")
                print ("Collected \"" + self.query + "\" images " + \
                    "number " + str(nextIndex) + "-" + \
                    str(min(nextIndex + 100, totalCount)) + \
                    " of " + str(totalCount))
                nextIndex += 100
        print ("Finished performing query \"" + self.query + "\"")

    def search(self, offset = 0):
        """Retrieve JSON of up to 100 images from Giphy API
        starting from index offset"""
        url = "http://api.giphy.com/v1/gifs/search"
        url += "?q=" + self.query.replace(" ", "+")
        url += "&limit=100"
        url += "&offset=" + str(offset)
        url += "&api_key=dc6zaTOxFJmzC" # uses public key
        request = requests.get(url)
        return json.loads(request.text)
