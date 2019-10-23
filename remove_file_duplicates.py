import os
import hashlib
import sys

"""This script eliminates duplicate files in the given directory path
Also works as module"""

def eliminate_file_duplicates(directory_path):
    files_with_hashvalue = {}
    file_duplicates = []
    files = os.listdir(directory_path)
    for file in files:
        file_path = os.path.join(directory_path, file)
        if os.path.isfile(file_path):

            # For every file compute hash value
            with open(file_path, 'rb') as file_object:
                hash = hashlib.sha1()
                data = file_object.read()
                hash.update(data)
                file_hashvalue = hash.digest()

                #Files having same hash value move into file_duplicates list
                if files_with_hashvalue.__contains__(file_hashvalue):
                    file_duplicates.append(file_path)

                #Add unique files into dictionary with hash_value as key and path as value
                else:
                    files_with_hashvalue[file_hashvalue] = file_path

    #Remove duplicate files
    for duplicate in file_duplicates:
        os.remove(duplicate)


if __name__ == "__main__":
    eliminate_file_duplicates(directory_path)

