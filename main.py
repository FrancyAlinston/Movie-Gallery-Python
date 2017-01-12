import movies
import building_html_page
from data_grabber import fetch_info
from files_grabber import get_file_name_list
import webbrowser

from stop_watch import StopWatch

movies_list = []
missing = []
path = '/Volumes/Macintosh HD 2/MyBackUpMovies/'
include_youtube_trailer = True


def gathering_list_files_information():
    print('Collecting Files Movie Names...')
    file_name_list = get_file_name_list(path)
    for each_name in file_name_list[0]:
        each_name_string = str(each_name).split('|')[0]

        movie = fetch_info(each_name_string)  # dict
        if movie.get('Response') == 'True':
            movie_object = movies.Movies(**movie)
            movies_list.append(movie_object)
        else:
            missing.append(movie)
    print('Done')
    print('Total: ' + str(movies_list.__len__()) + ' Movie')
    print(' ')


def build_html_page():
    print('Generating the Web-Page HTML...')
    print('May take long time (some minutes), depends on the number of files & youtube trailer if enabled')
    #two = StopWatch()
    #two.start()
    building_html_page.create_movies_page(movies_list)
    #two.end()
    print('Done')
    print(' ')


def open_html_page_in_browser():
    print('Opening the Web-Page HTML in the browser...')
    webbrowser.open("on_the_fly.html")
    print('Done')
    print(' ')


def main():
    gathering_list_files_information()
    build_html_page()
    open_html_page_in_browser()


if __name__ == '__main__':
    main()
