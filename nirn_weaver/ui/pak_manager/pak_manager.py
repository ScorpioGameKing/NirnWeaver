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

    def compose(self) -> ComposeResult:
        yield self.sTree.show_stage()
