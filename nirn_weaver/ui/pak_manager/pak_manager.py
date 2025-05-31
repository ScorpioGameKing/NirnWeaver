from glob import glob
from os.path import basename
from nirn_weaver import NirnPaths
from nirn_weaver.ui.pak_manager._stree import StagingTree
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Header, Footer, TabbedContent, TabPane, Label

class PAKManager(Container):

    sTree:StagingTree
    
    def __init__(self, **kwargs):
        super(Container, self).__init__(**kwargs)

        self.sTree = StagingTree()

    def show_manager1(self) -> Container:
        # Globbing for files test
        _paks = glob(f"{NirnPaths.OB_PAK_PATH}/*")
        _panel = Container()
        for pak in _paks:
            _panel._add_child(Label(basename(pak)))
        return _panel

    def compose(self) -> ComposeResult:
        yield self.sTree.show_stage()
