# Automatic Album Cover Grabber
#### By Jesnine Erillo

Automatically grabs album covers from Spotify using Spotify API and saves them in a directory called album_covers.

**NOTE:** In the `get-saved-album-covers.py` file, I iterated through 100 different offsets (`OFFSET_RANGE = 100`), which causes the program to run longer, though it allows for you to find more album covers to save. Feel free to change this value.

## Inspiration
I was planning on decorating my room by getting my favorite album covers printed, but it was really tedious to go through which albums I wanted to look for and actually save images of them. So I decided to automate it!

## Usage:
1. To use this, you must get an `OAuth token` from spotify. This can be done [here](https://developer.spotify.com/console/get-current-user-saved-tracks/). 
2. To save album covers, run: 
``` 
python3 get-saved-album-covers.py 
```
3. Enter your `OAuth token` when prompted, which will automatically start downloading your files.

## If you are getting a 'SSL: CERTIFICATE_VERIFY_FAILED' error:
To fix the error, try double clicking on 'Install Certificates.command' in your Python folder.

## Preview:
![Preview](preview.gif)
