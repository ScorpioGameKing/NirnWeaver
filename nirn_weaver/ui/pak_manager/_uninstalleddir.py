from os import remove
from os.path import basename
from shutil import copy2
from nirn_weaver import NirnPaths
from nirn_weaver.bundles import Bundler, Bundle
from textual.widgets import DirectoryTree

class UninstalledDir(DirectoryTree):

    def __init__(self, path, _class, **kwargs):
        super(DirectoryTree, self).__init__(**kwargs)
        self.path = path
        self.classes = _class

    # BIND THE INSTALL TREE TO ALLOW FOR UPDATES
    def bind_reload(self, dtree):
        self.install = dtree

    # INSTALL THE SELECTED FILE
    def on_directory_tree_file_selected(node, path):
        bndlr = Bundler()
        _bun = bndlr.install_bundle(
            basename(path.path), 
            NirnPaths.OB_PAK_DATA_PATH, 
            NirnPaths.PAK_INSTALLED_PATH, 
            NirnPaths.PAK_UNINSTALLED_PATH
        )
        
        #copy2(path.path, f"{NirnPaths.PAK_INSTALLED_PATH}{basename(path.path)}")
        #copy2(path.path, f"{NirnPaths.OB_PAK_DATA_PATH}{basename(path.path)}")
        #remove(path.path)
        node.reload()
        node.install.reload()
