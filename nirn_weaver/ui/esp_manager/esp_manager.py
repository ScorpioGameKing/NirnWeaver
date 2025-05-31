from textual.containers import Container
from textual.app import ComposeResult
from nirn_weaver import NirnPaths
from nirn_weaver.ui.esp_manager._opanel import OrderPanel
from nirn_weaver.ui.esp_manager._stree import StagingTree
from nirn_weaver.ui.esp_manager._statusbar import StatusBar

class ESPManager(Container):
    oPanel:OrderPanel
    sTree:StagingTree
    sBar:StatusBar
    load_order:list

    BINDINGS = [
        
  
    ]

    BINDINGS = [
        ("ctrl+down", "move_entry_down()", "Move Entry Down"),      
        ("ctrl+up", "move_entry_up()", "Move Entry up"),
        ("ctrl+shift+s", "save_load_order()", "Save Load Order"),
    ]

    def __init__(self, **kwargs):
        super(Container, self).__init__(**kwargs)
        
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

    def compose(self) -> ComposeResult:
        yield self.oPanel.show_table()
        yield self.sTree
        yield self.sBar.show_bar()
        
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
