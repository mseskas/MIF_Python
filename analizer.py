from statistics_types import FileStatistics
import os


# Analizer class that analizes directory/file and writes statistics
# to specified file in current work directory
class Analizer:

    __work_dir__ = None

    def __init__(self, path):
        if (os.path.exists(path) is not False):
            self.__work_dir__ = path
        else:
            print "Error no such directory exist."

# Analize all files in current work directory and write statistics
# to specified file
    def analize_dir(self, result_file_name):
        if (self.__work_dir__ is None):
            return False
        list_of_obj = os.listdir(self.__work_dir__)
        list_of_files = list()
        for obj in list_of_obj:
            # analize only files
            if (os.path.isfile(self.__work_dir__ + "/" + obj) is True):
                list_of_files.append(obj)

        list_of_statistics = list()
        for current in list_of_files:
            list_of_statistics.append(self.analize_single_file(current))

        total = self.total_statistics(list_of_statistics)
        self.write_statistics(total, list_of_statistics, result_file_name)
        return True

# Analize single file and return FileStatistics object as result
    def analize_single_file(self, name):
        if (self.__work_dir__ is None):
            return None
        curr_file = open(self.__work_dir__ + "/" + name, "r")
        content = curr_file.read()  # read file to the end
        array_char = list(content)
        dic_char = dict()
        for char in array_char:
            if (char.isalpha() is True):  # check only alphabet chars
                if (dic_char.get(char) is not None):
                    dic_char[char] = dic_char[char] + 1
                else:
                    dic_char[char] = 1

        array_char = None
        array_word = content.split()  # split to words
        dic_word = dict()
        for word in array_word:
            if (dic_word.get(word) is not None):
                dic_word[word] = dic_word[word] + 1
            else:
                dic_word[word] = 1

        statistics = FileStatistics(name)
        statistics.words_dic = dic_word
        statistics.chars_dic = dic_char
        return statistics

# Sums every FileStatistics element in list_of_statistics and
# return FileStatistics object as result
    def total_statistics(self, list_of_statistics):
        total = FileStatistics(".total")
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

# Write statistics to specified file
    def write_statistics(self, total, list_of_statistics, file_name):
        try:
            dest_file = open(file_name, "w")
        except Exception:
            print "Error : result can't be saved in : \"" + \
                  file_name + "\" file"
            return None
        # write total directory statistics
        dest_file.write("Directory \"" + self.__work_dir__ + "\" files'"
                        + " statistics :\n")
        if (len(total.chars_dic) == 0):  # if no data were processed
            dest_file.write("There is no statistics.")
            return None
        dest_file.write("List of words and times used :\n")
        for word in total.words_dic:
            dest_file.write("\t" + word + " - " + str(total.words_dic[word])
                            + "\n")
        dest_file.write("List of chars and times used :\n")
        for char in total.chars_dic:
            dest_file.write("\t" + char + " - " + str(total.chars_dic[char])
                            + "\n")
        # write each file's statistics
        for file_stat in list_of_statistics:
            dest_file.write("File \"" + file_stat.get_file_name()
                            + "\" statistics :\n")
            dest_file.write("List of words and times used in file:\n")
            for word in file_stat.words_dic:
                dest_file.write("\t" + word + " - "
                                + str(file_stat.words_dic[word]) + "\n")
            dest_file.write("List of chars and times used in file:\n")
            for char in file_stat.chars_dic:
                dest_file.write("\t" + char + " - "
                                + str(file_stat.chars_dic[char]) + "\n")
        dest_file.write("#End of file.")
