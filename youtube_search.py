import urllib.request
import urllib.parse
import re
import main

# Credit:
# www.codeproject.com/Articles/873060/Python-Search-Youtube-for-Video
# Rather than using Google api


def get_youtube_trailer(title):
    title += ' trailer'
    query_string = urllib.parse.urlencode({"search_query" : title})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    return "http://www.youtube.com/watch?v=" + search_results[0]


def get_youtube_id_trailer(title):
    if main.include_youtube_trailer:
        title += ' trailer'
        query_string = urllib.parse.urlencode({"search_query" : title})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        return search_results[0]
    else:
        return 0
