from shutil import move

class Bundle:
    _contents:dict
    _bType:str
    name:str
    tags:list[str]
    description:str
        
    def __init__(self, bType:str, name:str, tags:list[str], description:str):
        self._contents = {}
        self._bType = bType
        self.name = name
        self.tags = tags
        self.description = description

    def update_name(self, name):
        self.name = name

    def update_tags(self, tags):
        self.tags = tags

    def update_description(self, description):
        self.description = description

    def add_content(self, key, _cont):
        self._contents.update({key:_cont})

    def dump_contents(self):
        return self._contents

    def get_content(self, key):
        return self._contents[key]

    def remove_contents(self, key):
        del self._contents[key]
