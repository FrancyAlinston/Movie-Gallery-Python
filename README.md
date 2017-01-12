# Movie-Gallery-Python
Python script to generate locally Web-Page, as a gallery for your movie folder.

* Written by [Mohammad Laif](https://twitter.com/mohammadlaif), [Droid Programming](droidprogramming.com).
* Licensed under The [MIT License](../master/LICENSE).


## Version
* 1


## Updates
* You are in your own!
I don't have time to Python, Android Development got me.
I made this repository while I was learning python. Pardon me if you see rusty code :).


## Requirement
* Python 3.5+


## Install
* Not yet, but you can clone/downloaded and use it.
* git clone https://github.com/mzdhr/Movie-Gallery-Python.git


## Usage
1. Edit main.py, change **path** string with your movies folder path, in line ~11.
```
path = '/Volumes/Macintosh HD 2/MyBackUpMovies/'
```
2. From the terminal write:
```
python3 main.py
```


## Outputs
* movie_gallery_python.html, located in the same movies folder.


## Examples
![Movie Gallery Python](../master/img/movie_gallery_python01.png "Terminal Weather")
![Movie Gallery Python](../master/img/movie_gallery_python02.png "Terminal Weather")
![Movie Gallery Python](../master/img/movie_gallery_python03.png "Terminal Weather")


## Notes
* The generated html page will be in the same movies folder, that you specified.
* Movies ordered by Date Modified.
* To disable youtube trailers (because it slow the process), set **include_youtube_trailer** in **main.py** to False, by default its:
```
include_youtube_trailer = True
```
* Tried only in Mac OS.


## Modules
* main.py
Main script.

* building_html_page.py
Script to generate html pages.

* data_grabber.py
Used to grap movie information from [OMDAPI](http://www.omdbapi.com)
Another Implement in this repository [MovieInfo](https://github.com/mzdhr/movieinfo)

* files_grabber.py
Used to collect files/directories inside a folder path.

* movies.py
A simple class to create movie objects.

* stop_watch.py
Basic stopwatch class (used in debugging) to calculate time for code to complete in Python 3.5.
(StopWatch Repository)[https://github.com/mzdhr/stopwatch]

* youtube_search.py
Simple script to get youtube video IDs, manually (without youtube API).


## To Do:
- [ ] need to use cached list, to not generate whats already generated.
- [ ] fix duplicated movies bug.
- [ ] if movie reproduce, it will bring info for the old one.
- [ ] setup.py.
- [ ] refactor.
- [ ] refactor.
- [ ] refactor.
- [ ] refactor.
- [ ] refactor.
