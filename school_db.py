from os.path import isfile
import pickle

class SchoolDB:
    def __init__(self, school_initializer):

        self.enrollments = {}
        self.file_name = r".\enroll.dat" #escape back slash
        self.school_initializer = school_initializer
        self.__initialize_data_files()
        self.load_data()

    def __initialize_data_files(self):

        if not isfile(self.file_name):
            self.enrollments = self.school_initializer.enrollments
            self.save_data()

    def load_data(self):

        try:

            if (isfile(self.file_name)):
                self.file = open(self.file_name, 'rb')
                self.enrollments = pickle.load(self.file)
                self.file.close()

        except IOError:
            print("Error saving file")

        finally:
            self.file.close()

    def save_data(self):

        self.file = open(self.file_name, 'wb')
        pickle.dump(self.enrollments, self.file)
        self.file.close()