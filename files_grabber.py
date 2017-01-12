import os
from guessit import guessit
path = 'ShouldBeUsedFromMainPy'


def extract_title_from_file_name(file_name: str) -> str:
    file = guessit(file_name)
    title_with_format = file.get('title') + '|' + str(file.get('format'))
    return title_with_format


def get_file_name_list(directory_path: str)-> list:
    files_list = []
    files_path = []

    os.chdir(directory_path)
    files = (os.listdir(directory_path))

    # order item by Date Modified
    files = sorted(files, key=lambda item: os.path.getmtime(item))

    for file in files:
        file_path = path + file
        file_title = extract_title_from_file_name(file)
        if file_title not in files_list:
            files_list.insert(0, file_title)
            files_path.insert(0, file_path)

    return files_list, files_path


def dump_list_in_txt():
    with open('movie_list.txt', 'w') as text:
        for item in get_file_name_list(path):
            text.write(item + '\n')
