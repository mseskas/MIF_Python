from statistics_types import file_statistics
import os


class analizer:

    __work_dir__ = None

    def __init__(self, path):
        self.__work_dir__ = path

    def analize_dir(self):
        list_of_obj = os.listdir(self.__work_dir__)
        list_of_files = list()
        for obj in list_of_files:
            if (os.path.isfile(obj) is True):
                list_of_files.append(obj)

        list_of_statistics = list()
        for item in list_of_files:
            list_of_statistics.append(self.analize_single_file(item))

        total = self.total_statistics(list_of_statistics)
        self.write_statistics(total, list_of_statistics, "result.txt")

    def analize_single_file(self, name):
        curr_file = open(self.__work_dir__ + "/" + name, "r")
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
        statistics.chars_dic = dic_char
        return statistics

    def total_statistics(self, list_of_statistics):
        total = file_statistics("!Total")
        total_words = dict()
        total_chars = dict()
        for stat in list_of_statistics:
            for word in stat.words_dic:
                if (total_words.get(word) is not None):
                    total_words[word] = total_words[word] + \
                        stat.words_dic[word]
                else:
                    total_words[word] = stat.words_dic[word]

            for char in stat.chars_dic:
                if (total_chars.get(char) is not None):
                    total_chars[char] = total_chars[char] + \
                        stat.chars_dic[char]
                else:
                    total_chars[char] = stat.chars_dic[char]

        total.words_dic = total_words
        total.chars_dic = total_chars
        return total

    def write_statistics(self, total, list_of_statistics, file_name):
        try:
            dest_file = open(file_name, "w")
        except Exception:
            print "Error : result can't be saved in : \"" + \
                  file_name + "\" file"
            quit()
        # list().sort()
        if (len(total) == 0):
            dest_file.write("Directory \"" + self.__work_dir__ + "\" files'"
                            + " statistics :\n")
