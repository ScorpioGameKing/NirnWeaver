from glob import glob
from os import path, mkdir, remove
from shutil import copy2
from nirn_weaver import NirnWeaver, NirnPaths
from nirn_weaver.bundles import Bundler, Bundle
        
def main():
    app = NirnWeaver()

    NirnPaths.check_folders()
    NirnPaths.stage_valid_es(NirnPaths.DOWNLOAD_PATH, NirnPaths.UNINSTALLED_PATH, NirnPaths.INSTALLED_PATH)

    # Testing Bundles
    # bndlr = Bundler()
    # bun = bndlr.create_bundle("TEST", "Test Bundle", ["ALPHA", "0.0.0", "TESTING"], "The first test bundle")
    # bun.add_package("", f"{NirnPaths.STAGING_PATH}loose/AdjustedTimescale_10.esp")
    # bun.add_package("", f"{NirnPaths.STAGING_PATH}loose/Alternative Start.esp")
    # bndlr.uninstall_bundle(bun)
    # bndlr.install_bundle("Test Bundle")
    
    app.run()
    
if __name__ == "__main__":
    main()
