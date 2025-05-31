from glob import glob
from os import remove, listdir
from os.path import basename, join
from shutil import copy2
from nirn_weaver import NirnPaths
from nirn_weaver.bundles import Bundler, Bundle
from textual.widgets import DirectoryTree

class InstalledDir(DirectoryTree):

    def __init__(self, path, _class, **kwargs):
        super(DirectoryTree, self).__init__(**kwargs)
        self.path = path
        self.classes = _class
        self.bundles = {}

    # BIND THE UNINSTALL TREE TO ALLOW FOR UPDATES
    def bind_reload(self, dtree):
        self.uninstall = dtree

    # UNINSTALL THE SELECTED FILE
    def on_directory_tree_file_selected(node, path):
        bndlr = Bundler()
        bndlr.uninstall_bundle(node.bundles[f"{basename(path.path)}"], path, NirnPaths.PAK_UNINSTALLED_PATH)
        node.reload()
        node.uninstall.reload()

    # SCAN AND BUILD THE TREE
    def scan_installed_paks(self):
            bndlr = Bundler()
            pak_list = glob(f"{NirnPaths.OB_PAK_PATH}/*")
            for pak in pak_list:
                print(self.bundles)
                print(basename(pak))
                _pBase = basename(pak)
                _pFull = f"{NirnPaths.PAK_INSTALLED_PATH}{_pBase}/"
                _bun = bndlr.create_bundle(
                    _pFull, 
                    "PAK", 
                    _pBase
                )
                _files = listdir(f"{pak}/")
                for _fName in _files:
                    copy2(join(f"{pak}/", _fName), _pFull)
                self.bundles.update({_pBase:_bun})
