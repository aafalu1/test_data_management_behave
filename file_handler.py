import os


class File_Handler:

    @staticmethod
    def get_root_path():
        return os.path.abspath(os.path.dirname(__file__))

    @staticmethod
    def generate_file_path(*args, **kwargs):
        root_path = File_Handler.get_root_path()
        directories = args
        file_name = kwargs.get('file_name', '')
        file_path = os.path.join(root_path, *directories, file_name)  # Join the root path, directories, and file name
        if not os.path.isfile(file_path):
            raise ValueError(f"{file_path} is not a valid file path.")

        return file_path

    @staticmethod
    def create_directory_on_project_root(name_of_dir):
        proj_root_path = File_Handler.get_root_path()
        new_directory = os.path.join(proj_root_path, name_of_dir)
        if os.path.exists(new_directory):
            return new_directory
        os.makedirs(new_directory)
        return new_directory