from glob import glob
from os import remove
from os.path import basename, exists
from shutil import copy2
from nirn_weaver import NirnPaths
from textual.widgets import DirectoryTree

class InstalledDir(DirectoryTree):

    def __init__(self, path, _class, **kwargs):
        super(DirectoryTree, self).__init__(**kwargs)
        self.path = path
        self.classes = _class

    # BIND THE UNINSTALL TREE TO ALLOW FOR UPDATES
    def bind_reload(self, dtree, opanel):
        self.uninstall = dtree
        self.opanel = opanel

    # UNINSTALL THE SELECTED FILE
    def on_directory_tree_file_selected(node, path):
        removal:RowKey
        for row in node.opanel.rows:
            if basename(path.path) == node.opanel.get_row(row)[1]:
                removal = row
        node.opanel.remove_row(removal)
        copy2(path.path, f"{NirnPaths.ES_UNINSTALLED_PATH}{basename(path.path)}")
        remove(path.path)
        remove(f"{NirnPaths.OB_ESP_DATA_PATH}{basename(path.path)}")
        node.reload()
        node.uninstall.reload()

    def stage_valid_es(self, scan_path):
        esp_list = glob(f"{scan_path}**/*.es*", recursive=True)
        for esp in esp_list:
            if not exists(f"{NirnPaths.ES_INSTALLED_PATH}{path.basename(esp)}"):
                if exists(f"{NirnPaths.ES_UNINSTALLED_PATH}{path.basename(esp)}"):
                    remove(f"{NirnPaths.ES_UNINSTALLED_PATH}{path.basename(esp)}")
                copy2(esp, f"{NirnPaths.ES_UNINSTALLED_PATH}{path.basename(esp)}")
