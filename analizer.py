from statistics_types import file_statistics
import os

def analize_dir(path):
    list_of_file = os.listdir(path)
    list_of_statistics = list()
    for item in list_of_file:
        list_of_statistics = analize_single_file(item)
    
    total = add_lists(list_of_statistics)
    write_statistics(total, list_of_statistics, "result.txt")


def analize_single_file(path):
    print "not implemented analize_single_file function"


def add_lists(list_of_lists):
    print "not implemented add_lists function"


def write_statistics(total, list_of_statistics, file_name):
    print "not implemented write_statistics function"
