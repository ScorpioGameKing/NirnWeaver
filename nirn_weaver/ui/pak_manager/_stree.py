from textual.containers import Horizontal
from textual.widgets import DirectoryTree
from nirn_weaver import NirnPaths
from nirn_weaver.ui.pak_manager._uninstalleddir import UninstalledDir
from nirn_weaver.ui.pak_manager._installeddir import InstalledDir

class StagingTree():
    stage:Horizontal
    _uninstalled_dir:UninstalledDir
    _installed_dir:InstalledDir

    def __init__(self):
        self._uninstalled_dir = UninstalledDir(NirnPaths.PAK_UNINSTALLED_PATH, "uninstalled-pak", label="UNINSTALLED")
        self._installed_dir = InstalledDir(NirnPaths.PAK_INSTALLED_PATH, "installed-pak", label="INSTALLED")

        self._installed_dir.bind_reload(self._uninstalled_dir)
        self._uninstalled_dir.bind_reload(self._installed_dir)
        
        self.stage = Horizontal(
            self._uninstalled_dir,
            self._installed_dir,
            id = "pak-staging"
        )

    def show_stage(self) -> Horizontal:
        return self.stage
