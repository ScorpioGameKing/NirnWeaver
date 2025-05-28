class Bundle:
    _contents:dict
    _bType:str
    name:str
    tags:list[str]
    description:str
        
    def __init__(self, bType:str, name:str, tags:list[str], description:str):
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

    def add_package(self, key, package):
        self._contents.update(key, package)

    def get_contents(self, key):
        return self._contents[key]

    def remove_contents(self, key):
        del self._contents[key]
