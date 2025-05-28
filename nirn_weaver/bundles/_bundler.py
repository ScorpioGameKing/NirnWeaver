import tarfile
from nirn_weaver.bundles._bundle import Bundle
from nirn_weaver import NirnPaths

class Bundler:

    def create_bundle(self, bType:str, name:str, tags:list[str]=[""], description:str="") -> Bundle:
        return Bundle(bType, name, tags, description)

    def uninstall_bundle(self, bundle):
        with tarfile.open(f"{NirnPaths.BUN_UNINSTALLED_PATH}{bundle.name}", "w:bz2")as tar:
            tar.add(f"{NirnPaths.BUN_INSTALLED_PATH}{bundle.name}/", arcname=bundle.name)

    def install_bundle(self, name):
        with tarfile.open(f"{NirnPaths.BUN_INSTALLED_PATH}{name}.tar.bz2") as tar:
            tar.extractall(f"{NirnPaths.BUN_INSTALLED_PATH}{name}/")
