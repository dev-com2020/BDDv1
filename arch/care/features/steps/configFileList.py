class ConfigFileList(object):
    def __init__(self):
        self.list_of_files = []
        self.name = {}

    def add_filename(self, name):
        assert name not in self.list_of_files
        self.list_of_files.append(name)
