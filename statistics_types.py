# class that holds file's statistics
class file_statistics:
   __file_name = ""
   words_list = None
   symbols_list = None

   def __init__(self, name):
       self.__file_name = name
