from glob import glob
from os import remove, listdir
from os.path import basename, join, exists, isdir
from shutil import copy2, copytree
from nirn_weaver import NirnPaths
from nirn_weaver.bundles import Bundler, Bundle
from textual.widgets import DirectoryTree

class InstalledDir(DirectoryTree):

    BINDINGS = [
        ("shift+enter", "uninstall_mod()", "Uninstall Mod"),
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
    def scan_installed_mods(self):
        bndlr = Bundler()
        mod_list = glob(f"{NirnPaths.OB_UE4SS_MODS_PATH}/*")
        for mod in mod_list:
            if basename(mod) not in ["mods.txt", "shared"]:
                #print(mod)
                _pBase = basename(mod)
                _pFull = f"{NirnPaths.UE4SS_INSTALLED_PATH}{_pBase}/"
                if not exists(_pFull):
                    _bun = bndlr.create_bundle(
                        _pFull, 
                        "UE4SS", 
                        _pBase
                    )
                    _files = listdir(f"{mod}/")
                    for _fName in _files:
                        if isdir(join(f"{mod}/", _fName)):
                            copytree(join(f"{mod}/", _fName), f"{_pFull}{_fName}")
                        else:
                            copy2(join(f"{mod}/", _fName), _pFull)
                    self.bundles.update({_pBase:_bun})

    def stage_valid_mods(self, scan_path):
        mod_list = glob(f"{scan_path}**/*", recursive=True)
        _keyed_mods = {}
        for mod in mod_list:
            _split = basename(mod).split(".")
            _folder = mod.strip(scan_path).split('/')[0]
            if not exists(f"{NirnPaths.UE4SS_INSTALLED_PATH}{_folder}/"):
                if len(_split) > 1:
                    if _split[1] in ["lua"]:
                        print(f"MOD PATHS: {mod.strip(scan_path).split('/')[0]}")
                        if _folder not in _keyed_mods.keys():
                            _keyed_mods.update({_folder:[_folder]})

        for key_mod in _keyed_mods:
                print(f"MOD: {key_mod} FOLDER: {_keyed_mods[key_mod]}")
                bndlr = Bundler()
                _pFull = f"{NirnPaths.UE4SS_INSTALLED_PATH}{key_mod}/"
                print(f"STAGING PATH: {_pFull}")
                print(f"ORIGIN PATH: {NirnPaths.DOWNLOAD_PATH}{key_mod}/")
                _bun = bndlr.create_bundle(
                    _pFull,
                    "UE4SS",
                    key_mod
                )

                _files = listdir(f"{NirnPaths.DOWNLOAD_PATH}{key_mod}/")
                for _fName in _files:
                    if isdir(join(f"{NirnPaths.DOWNLOAD_PATH}{key_mod}/", _fName)):
                        copytree(join(f"{NirnPaths.DOWNLOAD_PATH}{key_mod}/", _fName), f"{_pFull}{_fName}")
                    else:
                        copy2(join(f"{NirnPaths.DOWNLOAD_PATH}{key_mod}/", _fName), _pFull)
                
                '''
                for _fName in _keyed_mods[key_mod]:
                    copy2(_fName, _pFull)
                '''    
                self.bundles.update({key_mod:_bun})
                bndlr.uninstall_bundle(
                    _bun,
                    _pFull,
                    _pFull, 
                    NirnPaths.UE4SS_UNINSTALLED_PATH
                )
                self.uninstall.reload()
            
    def action_uninstall_plugin(self):
        if self.cursor_node.data.path != NirnPaths.UE4SS_INSTALLED_PATH:
            bndlr = Bundler()
            bndlr.uninstall_bundle(
                self.bundles[f"{self.cursor_node.label}"],
                f"{NirnPaths.OB_UE4SS_MODS_PATH}{self.cursor_node.label}",
                self.cursor_node.data.path, 
                NirnPaths.UE4SS_UNINSTALLED_PATH
            )
            self.reload()
            self.uninstall.reload()
        pass
