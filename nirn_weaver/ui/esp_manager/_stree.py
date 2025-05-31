from textual.containers import Horizontal
from textual.widgets import DirectoryTree
from textual.app import ComposeResult
from nirn_weaver import NirnPaths
from nirn_weaver.ui.esp_manager._uninstalleddir import UninstalledDir
from nirn_weaver.ui.esp_manager._installeddir import InstalledDir

class StagingTree(Horizontal):
    _uninstalled_dir:UninstalledDir
    _installed_dir:InstalledDir

    def __init__(self, opanel, **kwargs):
        super(Horizontal, self).__init__(**kwargs)
        
        self._uninstalled_dir = UninstalledDir(NirnPaths.ES_UNINSTALLED_PATH, "uninstalled-esp", label="UNINSTALLED")
        self._installed_dir = InstalledDir(NirnPaths.ES_INSTALLED_PATH, "installed-esp", label="INSTALLED")

        self._installed_dir.bind_reload(self._uninstalled_dir, opanel)
        self._uninstalled_dir.bind_reload(self._installed_dir, opanel)
        
        self.id = "esp-staging"

    def compose(self) -> ComposeResult:
        yield self._uninstalled_dir
        yield self._installed_dir
        
