# automatic-album-cover-grabber
#### By Jesnine Erillo

Automatically grabs album covers from Spotify using Spotify API and saves them in a directory called album_covers.

To use this, you must get an `OAUTH_TOKEN` from spotify. This can be done [here](https://developer.spotify.com/console/get-current-user-saved-tracks/). 

**NOTE:** In the `get-saved-album-covers.py` file, I iterated through 100 different offsets (`OFFSET_RANGE = 100`), which causes the program to run longer, though it allows for you to find more album covers to save. Feel free to change this value.


## Usage:
1. Create a `secret.py` file containing your `OAUTH_TOKEN`
2. To save album covers, run: 
``` 
python3 get-saved-album-covers.py 
```

## Preview:
![Preview](preview.gif)
