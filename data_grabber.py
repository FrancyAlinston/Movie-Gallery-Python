import json
import urllib.request


def fetch_info(title):
    try:
        # Parsing url
        api = 'http://www.omdbapi.com/?t=' + title.replace(' ', '+') + '&y=&plot=full&r=json'

        # Graping data from the api
        connection = urllib.request.urlopen(api)
        output = connection.read().decode('utf-8')
        connection.close()

        # Creating dictionary using json object
        data = json.loads(output)
        return data

    except urllib.request.URLError as no_internet:
        return no_internet
