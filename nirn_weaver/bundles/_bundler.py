import tarfile
from os import mkdir
from shutil import rmtree
from os.path import exists
from nirn_weaver.bundles._bundle import Bundle
from nirn_weaver import NirnPaths

class Bundler:

    def create_bundle(self, bType:str, name:str, tags:list[str]=[""], description:str="") -> Bundle:
        if exists(f"{NirnPaths.BUN_INSTALLED_PATH}{name}/"):
            rmtree(f"{NirnPaths.BUN_INSTALLED_PATH}{name}")
        mkdir(f"{NirnPaths.BUN_INSTALLED_PATH}{name}/")
        return Bundle(bType, name, tags, description)

    def uninstall_bundle(self, bundle):
        #TODO Make and store page file
        with tarfile.open(f"{NirnPaths.BUN_UNINSTALLED_PATH}{bundle.name}", "w:bz2") as tar:
            tar.add(f"{NirnPaths.BUN_INSTALLED_PATH}{bundle.name}/", arcname=bundle.name)
        if exists(f"{NirnPaths.BUN_INSTALLED_PATH}{bundle.name}/"):
            rmtree(f"{NirnPaths.BUN_INSTALLED_PATH}{bundle.name}")

    def install_bundle(self, name):
        #TODO Create Bundle using page file
        if exists(f"{NirnPaths.BUN_INSTALLED_PATH}{name}/"):
            rmtree(f"{NirnPaths.BUN_INSTALLED_PATH}{name}")
        with tarfile.open(f"{NirnPaths.BUN_UNINSTALLED_PATH}{name}") as tar:
            tar.extractall(f"{NirnPaths.BUN_INSTALLED_PATH}")
