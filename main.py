from glob import glob
from os import path, mkdir, remove
from shutil import copy2
from nirn_weaver import NirnWeaver, NirnPaths
from nirn_weaver.bundles import Bundler, Bundle
        
def main():
    app = NirnWeaver()
    NirnPaths.check_folders()
    app.run()
    
if __name__ == "__main__":
    main()
