from nirn_weaver.ui.esp_manager import ESPManager
from nirn_weaver.ui.pak_manager import PAKManager
from nirn_weaver import NirnPaths
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, TabbedContent, TabPane, Label

class NirnWeaver(App):

    CSS_PATH = NirnPaths.WEAVER_CSS
    
    espman:ESPManager
    pakman:PAKManager

    BINDINGS = [
        ("ctrl+r", "re_stage()", "Re-Stage Files"),
    ]

    def __init__(self):
        super().__init__()
        
        self.espman = ESPManager()
        self.pakman = PAKManager()

    def on_mount(self) -> None:
        self.theme = "gruvbox"
        self.espman.oPanel.build_table()
        self.pakman.sTree._installed_dir.scan_installed_paks()
        self.pakman.sTree._installed_dir.stage_valid_paks(NirnPaths.DOWNLOAD_PATH)
    
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
                yield Label("WIP")
            with TabPane("UE4SS Manager", id="ue4ss-manager"):
                yield Label("WIP")

    def action_re_stage(self) -> None:
        NirnPaths.stage_valid_es(NirnPaths.DOWNLOAD_PATH)
        self.pakman.sTree._installed_dir.stage_valid_paks(NirnPaths.DOWNLOAD_PATH)
        
        self.pakman.sTree._installed_dir.scan_installed_paks()

        self.espman.sTree._uninstalled_dir.reload()
        self.pakman.sTree._installed_dir.reload()
