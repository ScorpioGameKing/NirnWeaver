from textual.containers import Horizontal
from textual.widgets import DirectoryTree
from nirn_weaver import NirnPaths
from nirn_weaver.ui.esp_manager._uninstalleddir import UninstalledDir
from nirn_weaver.ui.esp_manager._installeddir import InstalledDir

class StagingTree():
    stage:Horizontal
    _uninstalled_dir:UninstalledDir
    _installed_dir:InstalledDir

    def __init__(self, opanel):
        self._uninstalled_dir = UninstalledDir(NirnPaths.ES_UNINSTALLED_PATH, "uninstalled-esp", label="UNINSTALLED")
        self._installed_dir = InstalledDir(NirnPaths.ES_INSTALLED_PATH, "installed-esp", label="INSTALLED")

        self._installed_dir.bind_reload(self._uninstalled_dir, opanel)
        self._uninstalled_dir.bind_reload(self._installed_dir, opanel)
        
        self.stage = Horizontal(
            self._uninstalled_dir,
            self._installed_dir,
            id = "esp-staging"
        )

    def show_stage(self) -> Horizontal:
        return self.stage
