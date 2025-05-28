from glob import glob
from os import path, mkdir, remove
from shutil import copy2
from nirn_weaver.ui import OrderPanel, StagingTree, StatusBar
from nirn_weaver import NirnPaths
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, TabbedContent, TabPane, Label

class NirnWeaver(App):

    CSS_PATH = NirnPaths.WEAVER_CSS
    
    oPanel:OrderPanel
    sTree:StagingTree
    sBar:StatusBar
    load_order:list

    BINDINGS = [
        ("ctrl+down", "move_entry_down()", "Move Entry Down"),
        ("ctrl+up", "move_entry_up()", "Move Entry up"),
        ("ctrl+shift+s", "save_load_order()", "Save Load Order"),
        ("ctrl+r", "re_stage()", "Re-Stage Files"),
    ]

    def __init__(self):
        super().__init__()
        
        with open(NirnPaths.OB_PLUGINS_TXT, "r") as f:
            self.load_order = [(i, name) for i, name in enumerate(f.read().splitlines())]

        self.oPanel = OrderPanel(
            [
                ("LOAD ORDER", "PLUGIN NAME")
            ],
            self.load_order
        )

        self.sTree = StagingTree(self.oPanel.table)

    def on_mount(self) -> None:
        self.theme = "gruvbox"
        self.oPanel.build_table()
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

        with TabbedContent(initial="esp-manager"):
            with TabPane("Settings", id="settings"):
                yield Label("WIP")
            with TabPane("ESP Manager", id="esp-manager"):
                yield self.oPanel.show_table()
                yield self.sTree.show_stage()
                yield StatusBar().show_bar()
            with TabPane("PAK Manager", id="pak-manager"):
                yield Label("WIP")
            with TabPane("OBSE Manager", id="obse-manager"):
                yield Label("WIP")
            with TabPane("UE4SS Manager", id="ue4ss-manager"):
                yield Label("WIP")

    def action_move_entry_down(self) -> None:
        row_index = self.oPanel.table.cursor_coordinate[0]
        if row_index + 1 > self.oPanel.table.row_count - 1:
            return
        else:
            selected = tuple(self.oPanel.table.get_row_at(row_index))
            below = tuple(self.oPanel.table.get_row_at(row_index + 1))
            self.oPanel.table.update_cell_at((row_index, 1), below[1])
            self.oPanel.table.update_cell_at((row_index + 1, 1), selected[1])
            self.oPanel.table.move_cursor(row=row_index + 1)

    def action_move_entry_up(self) -> None:
        row_index = self.oPanel.table.cursor_coordinate[0]
        if row_index - 1 < 0:
            return
        else:
            selected = tuple(self.oPanel.table.get_row_at(row_index))
            above = tuple(self.oPanel.table.get_row_at(row_index - 1))
            self.oPanel.table.update_cell_at((row_index, 1), above[1])
            self.oPanel.table.update_cell_at((row_index - 1, 1), selected[1])
            self.oPanel.table.move_cursor(row=row_index - 1)

    def action_save_load_order(self) -> None:
        with open(NirnPaths.OB_PLUGINS_TXT, "w") as f:
            for i in range(0, self.oPanel.table.row_count):
                f.write(f"{self.oPanel.table.get_row_at(i)[1]}\n")

    def action_re_stage(self) -> None:
        print(glob(f"{NirnPaths.DOWNLOAD_PATH}*.es*"))
        NirnPaths.stage_valid_es(NirnPaths.DOWNLOAD_PATH, NirnPaths.UNINSTALLED_PATH, NirnPaths.INSTALLED_PATH)
        self.sTree._uninstalled_dir.reload()
