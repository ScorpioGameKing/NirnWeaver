from pathlib import Path
from shutil import copy2
from os import path, remove, mkdir
from os.path import exists
from glob import glob

class NirnPaths():
        
    USR_PATH             = f"{Path.home()}/"
    DOWNLOAD_PATH        = f"{USR_PATH}Downloads/"
    
    NW_PATH              = f"{USR_PATH}.local/share/NirnWeaver/"

    STAGING_PATH         = f"{NW_PATH}staging/"
    UNINSTALLED_PATH     = f"{STAGING_PATH}uninstalled/"
    INSTALLED_PATH       = f"{STAGING_PATH}installed/"

    BUNDLES_PATH         = f"{STAGING_PATH}bundles/"
    BUN_UNINSTALLED_PATH = f"{BUNDLES_PATH}uninstalled/"
    BUN_INSTALLED_PATH   = f"{BUNDLES_PATH}installed/"

    WEAVER_CSS           = f"./tcss/_nirn_weaver.tcss"

    NIRN_CONFIG_PATH     = f"{USR_PATH}.config/NirnWeaver/"
    
    OBR_PATH             = f"{USR_PATH}.local/share/Steam/steamapps/common/Oblivion Remastered/"
    OB_WIN_64_PATH       = f"{OBR_PATH}OblivionRemastered/Binaries/Win64/"
    OB_PAK_PATH          = f"{OBR_PATH}OblivionRemastered/Content/Paks/"
    OB_OBV_DATA_PATH     = f"{OBR_PATH}OblivionRemastered/Content/Dev/ObvData/"
    OB_ESP_DATA_PATH     = f"{OBR_PATH}OblivionRemastered/Content/Dev/ObvData/Data/"
    OB_PLUGINS_TXT       = f"{OBR_PATH}OblivionRemastered/Content/Dev/ObvData/Data/Plugins.txt"

    def check_folders():
        if not exists(NirnPaths.NW_PATH):
            mkdir(NirnPaths.NW_PATH)
        if not exists(NirnPaths.STAGING_PATH):
            mkdir(NirnPaths.STAGING_PATH)
        if not exists(NirnPaths.UNINSTALLED_PATH):
            mkdir(NirnPaths.UNINSTALLED_PATH)
        if not exists(NirnPaths.INSTALLED_PATH):
            mkdir(NirnPaths.INSTALLED_PATH)
        if not exists(NirnPaths.BUNDLES_PATH):
            mkdir(NirnPaths.BUNDLES_PATH)
        if not exists(NirnPaths.BUN_UNINSTALLED_PATH):
            mkdir(NirnPaths.BUN_UNINSTALLED_PATH)
        if not exists(NirnPaths.BUN_INSTALLED_PATH):
            mkdir(NirnPaths.BUN_INSTALLED_PATH)

    def stage_valid_es(scan_path, uninstalled_path, installed_path):
        print([path.basename(x) for x in glob(f"{scan_path}**/*.es*", recursive=True)])
        esp_list = glob(f"{scan_path}**/*.es*", recursive=True)
        for esp in esp_list:
            print(f"{esp}")
            print(f"{uninstalled_path}{path.basename(esp)}")
            if not path.exists(f"{installed_path}{path.basename(esp)}"):
                if path.exists(f"{uninstalled_path}{path.basename(esp)}"):
                    remove(f"{uninstalled_path}{path.basename(esp)}")
                copy2(esp, f"{uninstalled_path}{path.basename(esp)}")
