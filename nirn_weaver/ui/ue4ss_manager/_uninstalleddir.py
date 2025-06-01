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
        if path.path != NirnPaths.UE4SS_UNINSTALLED_PATH:
            bndlr = Bundler()
            _bun = bndlr.install_bundle(
                basename(path.path), 
                NirnPaths.OB_UE4SS_MODS_PATH, 
                NirnPaths.UE4SS_INSTALLED_PATH, 
                NirnPaths.UE4SS_UNINSTALLED_PATH
            )
        node.reload()
        node.install.reload()
