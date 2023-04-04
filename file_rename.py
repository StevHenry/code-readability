import sys
import shutil
import os

def rename_file(input_file_path: str, output_file_path: str = None):
    if output_file_path is None:
        if "python" in input_file_path:
            output_file_path = input_file_path.rename('.jsnp', '.py')
        elif "java" in input_file_path:
            output_file_path = input_file_path.rename('.jsnp', '.java')
        elif "cuda" in input_file_path:
            output_file_path = input_file_path.rename('.jsnp', '.c')
        else:
            print("No output file specified and no known keyword has been found in the input path.")
            print("Aborting the renaming. Please specify the output path or \"java\","
                  " \"python\" or \"cuda\" in the input file path")
    return

rename_file('./resources/DatasetBW/snippets/java/1.jnsp')

def generate_output_file_name(index: int, output_folder_path: str, extension: str) -> str:
    """
    :param index: file index
    :param input_file_name: name of the file like "xxx.jsnp"
    :param output_folder_path: new_file_path like "C:/yyy/" or "C:\\yyy"
    :param extension: extension of the new file: "py" or "java" or "python".
    :return: the new file name as "C:/yyy/idx.extension" (replaces all the \\ by /)
    """
    output_folder_path.replace('\\', '/')
    interstitial = '' if output_folder_path.endswith('/') else '/'
    return output_folder_path + interstitial + str(index) + '.' + extension


if __name__ == '__main__':
    arguments = sys.argv
    if len(arguments) == 0:
        files = dict()
        idx = 0
        #TODO: Check if the following stuff works
        for file in os.listdir('./resources/DatasetBW/snippets/java'):
            files[idx] = os.path.abspath('./resources/DatasetBW/snippets/java') + file
            idx += 1
        for file in os.listdir('./resources/DatasetDorn/snippets/java'):
            files[idx] = os.path.abspath('./resources/DatasetDorn/snippets/java') + file
            idx += 1
        for file in os.listdir('./resources/DatasetDorn/snippets/cuda'):
            files[idx] = os.path.abspath('./resources/DatasetDorn/snippets/cuda') + file
            idx += 1
        for file in os.listdir('./resources/DatasetDorn/snippets/python'):
            files[idx] = os.path.abspath('./resources/DatasetDorn/snippets/python') + file
            idx += 1
    elif len(arguments) == 1:
        rename_file(arguments[0])
    elif len(arguments) == 2:
        rename_file(arguments[0], arguments[1])
    else:
        print("Illegal arguments given: please use 'python file_rename.py \"path/inputfile\" <\"path/outputfile\">")
        print("Please note that the input path should include the words \"java\", \"python\" or \"cuda\".")
