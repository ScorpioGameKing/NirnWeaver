from nirn_weaver import NirnPaths
from glob import glob
from os import remove
from os.path import basename
from textual.containers import Horizontal
from textual.widgets import Label
from textual.reactive import Reactive

class StatusBar():

    def show_bar(self) -> Horizontal:
        return self.reload()

    def reload(self):
        un_count:Reactive[int | None] = Reactive(len(glob(f"{NirnPaths.UNINSTALLED_PATH}*.es*")))
        in_count:Reactive[int | None] = Reactive(len(glob(f"{NirnPaths.INSTALLED_PATH}*.es*")))
        
        uninstall_count = Label(f"UNINSTALLED: {un_count} / ", classes="un-install")
        install_count = Label(f"INSTALLED: {in_count}", classes="install")
                
        bar = Horizontal(
            uninstall_count,
            install_count,
            id = "status-bar"
        )
        print(un_count, in_count, uninstall_count, install_count)
        return bar
