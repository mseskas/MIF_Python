# class that contains file's statistics
class FileStatistics:
    __file_name__ = ""
    words_dic = None  # words dictionary
    chars_dic = None  # chars dictionary

    def __init__(self, name):
        self.__file_name__ = name

    def get_file_name(self):
        return self.__file_name__
