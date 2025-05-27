from glob import glob
from os import remove
from os.path import basename
from shutil import copy2
from nirn_weaver import NirnPaths
from nirn_weaver.ui._opanel import OrderPanel
from textual.widgets import DirectoryTree

class UninstalledDir(DirectoryTree):

    def __init__(self, path, _class, **kwargs):
        super(DirectoryTree, self).__init__(**kwargs)
        self.path = path
        self.classes = _class

    # BIND THE INSTALL TREE TO ALLOW FOR UPDATES
    def bind_reload(self, dtree, opanel):
        self.install = dtree
        self.opanel = opanel
        #self.sbar = sbar

    # INSTALL THE SELECTED FILE
    def on_directory_tree_file_selected(node, path):
        row = [(node.opanel.row_count, basename(path.path))]
        node.opanel.add_rows(row)
        copy2(path.path, f"{NirnPaths.INSTALLED_PATH}{basename(path.path)}")
        copy2(path.path, f"{NirnPaths.OB_ESP_DATA_PATH}{basename(path.path)}")
        remove(path.path)
        node.reload()
        node.install.reload()
        #node.sbar.reload()
