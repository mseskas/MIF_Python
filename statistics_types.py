# class that holds file's statistics
class file_statistics:
    __file_name__ = ""
    words_dic = None
    char_dic = None

    def __init__(self, name):
        self.__file_name__ = name

    def get_file_name(self):
        return self.__file_name__
