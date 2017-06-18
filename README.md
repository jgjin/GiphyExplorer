# Usage
Run GiphyExplorer.py through a Python interpreter and follow the prompts.

# Dependencies
## Python
[Download](https://www.python.org/downloads)

GiphyExplorer is tested with Python 2.7 but should work with Python 3.

## Requests
[Download](http://docs.python-requests.org/en/master/user/install)

GiphyExplorer uses the Python requests module to make requests to the Giphy API.

## Firefox (optional)
[Download](https://www.mozilla.org/en-US/firefox/new)

GiphyExplorer opens images in Firefox by default. You may change the browser by editing the line `self.controller = webbrowser.get("firefox")` in GiphyExplorer.py. See the [documentation](https://docs.python.org/2/library/webbrowser.html)  of the Python webbrowser module for a list of browsers.
