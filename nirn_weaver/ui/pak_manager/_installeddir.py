from glob import glob
from os import remove, listdir
from os.path import basename, join, exists
from shutil import copy2
from nirn_weaver import NirnPaths
from nirn_weaver.bundles import Bundler, Bundle
from textual.widgets import DirectoryTree

class InstalledDir(DirectoryTree):

    BINDINGS = [
        ("shift+enter", "uninstall_pak()", "Uninstall PAK"),
    ]

    def __init__(self, path, _class, **kwargs):
        super(DirectoryTree, self).__init__(**kwargs)
        self.path = path
        self.classes = _class
        self.bundles = {}

    # BIND THE UNINSTALL TREE TO ALLOW FOR UPDATES
    def bind_reload(self, dtree):
        self.uninstall = dtree
    
    # SCAN AND BUILD THE TREE
    def scan_installed_paks(self):
        bndlr = Bundler()
        pak_list = glob(f"{NirnPaths.OB_PAK_PATH}/*")
        for pak in pak_list:
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

    def stage_valid_paks(self, scan_path):
        pak_list = glob(f"{scan_path}**/*", recursive=True)
        _keyed_paks = {}
        for pak in pak_list:
            _split = basename(pak).split(".")
            if not exists(f"{NirnPaths.PAK_INSTALLED_PATH}{_split[0]}/"):
                if len(_split) > 1:
                    if _split[1] in ["pak", "utoc", "ucas"]:
                        if _split[0] in _keyed_paks.keys():
                            _keyed_paks[_split[0]].append(pak)
                        else:
                            _keyed_paks.update({_split[0]:[pak]})

        for key_pak in _keyed_paks:
                bndlr = Bundler()
                _pFull = f"{NirnPaths.PAK_INSTALLED_PATH}{key_pak}/"
                _bun = bndlr.create_bundle(
                    _pFull,
                    "PAK",
                    key_pak
                )
                for _fName in _keyed_paks[key_pak]:
                    copy2(_fName, _pFull)
                self.bundles.update({key_pak:_bun})
                bndlr.uninstall_bundle(
                    _bun,
                    _pFull,
                    _pFull, 
                    NirnPaths.PAK_UNINSTALLED_PATH
                )
                self.uninstall.reload()
            
    def action_uninstall_pak(self):
        if self.cursor_node.data.path != NirnPaths.PAK_INSTALLED_PATH:
            bndlr = Bundler()
            bndlr.uninstall_bundle(
                self.bundles[f"{self.cursor_node.label}"],
                f"{NirnPaths.OB_PAK_PATH}{self.cursor_node.label}",
                self.cursor_node.data.path, 
                NirnPaths.PAK_UNINSTALLED_PATH
            )
            self.reload()
            self.uninstall.reload()
