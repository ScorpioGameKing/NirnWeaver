from glob import glob
from os import path, mkdir, remove
from shutil import copy2
from nirn_weaver import NirnWeaver, NirnPaths
        
def main():
    app = NirnWeaver()

    NirnPaths.check_folders()
    NirnPaths.stage_valid_es(NirnPaths.DOWNLOAD_PATH, NirnPaths.UNINSTALLED_PATH, NirnPaths.INSTALLED_PATH)
    
    app.run()

if __name__ == "__main__":
    main()
