import tarfile
from os import mkdir, remove
from shutil import rmtree
from os.path import exists
from nirn_weaver.bundles._bundle import Bundle
from nirn_weaver import NirnPaths

class Bundler:

    def create_bundle(self, to_path:str, bType:str, name:str, tags:list[str]=[""], description:str="") -> Bundle:
        if not exists(f"{to_path}"):
            mkdir(f"{to_path}")
        return Bundle(bType, name, tags, description)

    def uninstall_bundle(self, bundle, from_path:str, staged_at:str, to_path:str):
        #TODO Make and store page file
        with tarfile.open(f"{to_path}{bundle.name}", "w:bz2") as tar:
            tar.add(f"{from_path}", arcname=bundle.name)
        if exists(f"{from_path}"):
            rmtree(f"{from_path}")
        if exists(f"{staged_at}"):
            rmtree(f"{staged_at}")

    def install_bundle(self, name, to_path, stage_to, from_path):
        #TODO Create Bundle using page file
        if exists(f"{to_path}{name}/"):
            rmtree(f"{to_path}{name}")
        if exists(f"{stage_to}{name}/"):
            rmtree(f"{stage_to}{name}")
        with tarfile.open(f"{from_path}{name}") as tar:
            tar.extractall(f"{to_path}")
            tar.extractall(f"{stage_to}")
        remove(f"{from_path}{name}")
