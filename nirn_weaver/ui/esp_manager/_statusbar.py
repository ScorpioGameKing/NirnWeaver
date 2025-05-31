from nirn_weaver import NirnPaths
from glob import glob
from textual.containers import Horizontal
from textual.widgets import Label
from textual.reactive import Reactive

class StatusBar():

    def show_bar(self) -> Horizontal:
        return self.reload()

    def reload(self):
        un_count:Reactive[int | None] = Reactive(len(glob(f"{NirnPaths.ES_UNINSTALLED_PATH}*.es*")))
        in_count:Reactive[int | None] = Reactive(len(glob(f"{NirnPaths.ES_INSTALLED_PATH}*.es*")))
        
        uninstall_count = Label(f"UNINSTALLED: {un_count} / ", classes="un-install")
        install_count = Label(f"INSTALLED: {in_count}", classes="install")
                
        bar = Horizontal(
            uninstall_count,
            install_count,
            id = "status-bar"
        )
        return bar
