from nirn_weaver import NirnPaths
from nirn_weaver.ui.obse_manager._stree import StagingTree
from textual.app import ComposeResult
from textual.containers import Container

class OBSEManager(Container):

    sTree:StagingTree
    
    def __init__(self, **kwargs):
        super(Container, self).__init__(**kwargs)

        self.sTree = StagingTree()

    def compose(self) -> ComposeResult:
        yield self.sTree.show_stage()
