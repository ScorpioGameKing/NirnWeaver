from textual.containers import Container
from nirn_weaver import NirnPaths
from nirn_weaver.ui.esp_manager._opanel import OrderPanel
from nirn_weaver.ui.esp_manager._stree import StagingTree
from nirn_weaver.ui.esp_manager._statusbar import StatusBar

class ESPManager():
    oPanel:OrderPanel
    sTree:StagingTree
    sBar:StatusBar
    load_order:list

    def __init__(self):
        with open(NirnPaths.OB_PLUGINS_TXT, "r") as f:
            self.load_order = [(i, name) for i, name in enumerate(f.read().splitlines())]

        self.oPanel = OrderPanel(
            [
                ("LOAD ORDER", "PLUGIN NAME")
            ],
            self.load_order
        )

        self.sBar = StatusBar()
        self.sTree = StagingTree(self.oPanel.table)

    def show_manager(self) -> Container:
        return Container(
            self.oPanel.show_table(),
            self.sTree.show_stage(),
            self.sBar.show_bar()
        )
