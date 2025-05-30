from glob import glob
from os.path import basename
from nirn_weaver import NirnPaths
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Header, Footer, TabbedContent, TabPane, Label

class PAKManager:

    

    def __init__(self):
        pass

    def show_manager(self) -> Container:
        # Globbing for files test
        _paks = glob(f"{NirnPaths.OB_PAK_PATH}/*", recursive=True)
        _panel = Container()
        for pak in _paks:
            _panel._add_child(Label(basename(pak)))
        return _panel
