from glob import glob
from os import remove, listdir
from os.path import basename, join, exists
from shutil import copy2
from nirn_weaver import NirnPaths
from nirn_weaver.bundles import Bundler, Bundle
from textual.widgets import DirectoryTree

class InstalledDir(DirectoryTree):

    BINDINGS = [
        ("shift+enter", "uninstall_plugin()", "Uninstall Plugin"),
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
    def scan_installed_plugins(self):
        bndlr = Bundler()
        plugin_list = glob(f"{NirnPaths.OB_OBSE_PLUGINS_PATH}/*")
        for plugin in plugin_list:
            _pBase = basename(plugin)
            _pFull = f"{NirnPaths.OBSE_INSTALLED_PATH}{_pBase}/"
            _bun = bndlr.create_bundle(
                _pFull, 
                "OBSE", 
                _pBase
            )
            _files = listdir(f"{plugin}/")
            for _fName in _files:
                copy2(join(f"{plugin}/", _fName), _pFull)
            self.bundles.update({_pBase:_bun})

    def stage_valid_plugins(self, scan_path):
        plugin_list = glob(f"{scan_path}**/*", recursive=True)
        _keyed_plugins = {}
        for plugin in plugin_list:
            _split = basename(plugin).split(".")
            if not exists(f"{NirnPaths.OBSE_INSTALLED_PATH}{_split[0]}/"):
                if len(_split) > 1:
                    if _split[1] in ["dll", "pdb"]:
                        if _split[0] in _keyed_plugins.keys():
                            _keyed_plugins[_split[0]].append(plugin)
                        else:
                            _keyed_plugins.update({_split[0]:[plugin]})

        for key_plugin in _keyed_plugins:
                bndlr = Bundler()
                _pFull = f"{NirnPaths.OBSE_INSTALLED_PATH}{key_plugin}/"
                _bun = bndlr.create_bundle(
                    _pFull,
                    "OBSE",
                    key_plugin
                )
                for _fName in _keyed_plugins[key_plugin]:
                    copy2(_fName, _pFull)
                self.bundles.update({key_plugin:_bun})
                bndlr.uninstall_bundle(
                    _bun,
                    _pFull,
                    _pFull, 
                    NirnPaths.OBSE_UNINSTALLED_PATH
                )
                self.uninstall.reload()
            
    def action_uninstall_plugin(self):
        if self.cursor_node.data.path != NirnPaths.OBSE_INSTALLED_PATH:
            bndlr = Bundler()
            bndlr.uninstall_bundle(
                self.bundles[f"{self.cursor_node.label}"],
                f"{NirnPaths.OB_OBSE_PLUGINS_PATH}{self.cursor_node.label}",
                self.cursor_node.data.path, 
                NirnPaths.OBSE_UNINSTALLED_PATH
            )
            self.reload()
            self.uninstall.reload()
        pass
