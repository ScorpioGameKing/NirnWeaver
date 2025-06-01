from textual.containers import Horizontal
from textual.widgets import DirectoryTree
from nirn_weaver import NirnPaths
from nirn_weaver.ui.ue4ss_manager._uninstalleddir import UninstalledDir
from nirn_weaver.ui.ue4ss_manager._installeddir import InstalledDir

class StagingTree():
    stage:Horizontal
    _uninstalled_dir:UninstalledDir
    _installed_dir:InstalledDir

    def __init__(self):
        self._uninstalled_dir = UninstalledDir(NirnPaths.UE4SS_UNINSTALLED_PATH, "uninstalled-ue4ss", label="UNINSTALLED")
        self._installed_dir = InstalledDir(NirnPaths.UE4SS_INSTALLED_PATH, "installed-ue4ss", label="INSTALLED")

        self._installed_dir.bind_reload(self._uninstalled_dir)
        self._uninstalled_dir.bind_reload(self._installed_dir)
        
        self.stage = Horizontal(
            self._uninstalled_dir,
            self._installed_dir,
            id = "ue4ss-staging"
        )

    def show_stage(self) -> Horizontal:
        return self.stage
