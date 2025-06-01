from nirn_weaver.ui import ESPManager
from nirn_weaver.ui import PAKManager
from nirn_weaver.ui import OBSEManager
from nirn_weaver.ui import UE4SSManager
from nirn_weaver import NirnPaths
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, TabbedContent, TabPane, Label

class NirnWeaver(App):

    CSS_PATH = NirnPaths.WEAVER_CSS
    
    espman   : ESPManager
    pakman   : PAKManager
    obseman  : OBSEManager
    ue4ssman : UE4SSManager

    BINDINGS = [
        ("ctrl+r", "re_stage()", "Re-Stage Files"),
    ]

    def __init__(self):
        super().__init__()
        
        self.espman   = ESPManager()
        self.pakman   = PAKManager()
        self.obseman  = OBSEManager()
        self.ue4ssman = UE4SSManager()

    def on_mount(self) -> None:
        self.theme = "gruvbox"
        
        self.espman.oPanel.build_table()
        
        self.pakman.sTree._installed_dir.scan_installed_paks()
        self.pakman.sTree._installed_dir.stage_valid_paks(NirnPaths.DOWNLOAD_PATH)
        
        self.obseman.sTree._installed_dir.scan_installed_plugins()
        self.obseman.sTree._installed_dir.stage_valid_plugins(NirnPaths.DOWNLOAD_PATH)

        self.ue4ssman.sTree._installed_dir.scan_installed_mods()
        self.ue4ssman.sTree._installed_dir.stage_valid_mods(NirnPaths.DOWNLOAD_PATH)

        self.espman.sTree._uninstalled_dir.reload()
        self.pakman.sTree._installed_dir.reload()
        self.obseman.sTree._installed_dir.reload()
        self.ue4ssman.sTree._installed_dir.reload()
        
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

        with TabbedContent(initial="esp-manager"):
            with TabPane("Settings", id="settings"):
                yield Label("WIP")
            with TabPane("ESP Manager", id="esp-manager"):
                yield self.espman
            with TabPane("PAK Manager", id="pak-manager"):
                yield self.pakman
            with TabPane("OBSE Manager", id="obse-manager"):
                yield self.obseman
            with TabPane("UE4SS Manager", id="ue4ss-manager"):
                yield self.ue4ssman

    def action_re_stage(self) -> None:
        self.espman.sTree._installed_dir.stage_valid_es(NirnPaths.DOWNLOAD_PATH)
        self.pakman.sTree._installed_dir.stage_valid_paks(NirnPaths.DOWNLOAD_PATH)
        self.obseman.sTree._installed_dir.stage_valid_plugins(NirnPaths.DOWNLOAD_PATH)
        self.ue4ssman.sTree._installed_dir.stage_valid_mods(NirnPaths.DOWNLOAD_PATH)
        
        self.pakman.sTree._installed_dir.scan_installed_paks()
        self.obseman.sTree._installed_dir.scan_installed_plugins()
        self.ue4ssman.sTree._installed_dir.scan_installed_mods()

        self.espman.sTree._uninstalled_dir.reload()
        self.pakman.sTree._installed_dir.reload()
        self.obseman.sTree._installed_dir.reload()
