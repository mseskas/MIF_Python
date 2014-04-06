from statistics_types import file_statistics
import os


def analize_dir(path):
    list_of_obj = os.listdir(path)
    list_of_files = list()
    for obj in list_of_files:
        if (os.path.isfile(obj) is True):
            list_of_files.append(obj)

    list_of_statistics = list()
    for item in list_of_files:
        list_of_statistics.append(analize_single_file(path, item))

    total = total_statistics(list_of_statistics)
    write_statistics(total, list_of_statistics, "result.txt")


def analize_single_file(path, name):
    curr_file = open(path + "/" + name, "r")
    content = curr_file.read()
    array_char = list(content)
    dic_char = dict()
    for char in array_char:
        if (dic_char.get(char) is not None):
            dic_char[char] = dic_char[char] + 1
        else:
            dic_char[char] = 1

    array_char = None
    array_word = content.split()  # split to word including newLine
    dic_word = dict()
    for word in array_word:
        if (dic_word.get(word) is not None):
            dic_word[word] = dic_word[word] + 1
        else:
            dic_word[word] = 1

    statistics = file_statistics(name)
    statistics.words_dic = dic_word
    statistics.char_dic = dic_char
    return statistics


def total_statistics(list_of_lists):
    print "not implemented add_lists function"


def write_statistics(total, list_of_statistics, file_name):
    # list().sort()
    print "not implemented write_statistics function"
