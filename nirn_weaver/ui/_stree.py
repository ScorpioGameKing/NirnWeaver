from textual.containers import Horizontal
from textual.widgets import DirectoryTree
from nirn_weaver import NirnPaths
from nirn_weaver.ui._uninstalleddir import UninstalledDir
from nirn_weaver.ui._installeddir import InstalledDir

class StagingTree():
    stage:Horizontal
    _uninstalled_dir:UninstalledDir
    _installed_dir:InstalledDir

    def __init__(self, opanel, sbar):
        self._uninstalled_dir = UninstalledDir(NirnPaths.UNINSTALLED_PATH, "uninstalled-esp", label="UNINSTALLED")
        self._installed_dir = InstalledDir(NirnPaths.INSTALLED_PATH, "installed-esp", label="INSTALLED")

        self._installed_dir.bind_reload(self._uninstalled_dir, opanel, sbar)
        self._uninstalled_dir.bind_reload(self._installed_dir, opanel, sbar)
        
        self.stage = Horizontal(
            self._uninstalled_dir,
            self._installed_dir,
            id = "esp-staging"
        )

    def show_stage(self) -> Horizontal:
        return self.stage
