from pathlib import Path
from os import mkdir
from os.path import exists

class NirnPaths():

    # - SYSTEM -
    USR_PATH               = f"{Path.home()}/"
    DOWNLOAD_PATH          = f"{USR_PATH}Downloads/"

    # - PROGRAM -
    NIRN_CONFIG_PATH       = f"{USR_PATH}.config/NirnWeaver/"
    NW_PATH                = f"{USR_PATH}.local/share/NirnWeaver/"
    STAGING_PATH           = f"{NW_PATH}staging/"

    # - ESP/ESM -
    ES_PATH                = f"{STAGING_PATH}es/"
    ES_UNINSTALLED_PATH    = f"{ES_PATH}uninstalled/"
    ES_INSTALLED_PATH      = f"{ES_PATH}installed/"

    # - PAK -
    PAK_PATH               = f"{STAGING_PATH}pak/"
    PAK_UNINSTALLED_PATH   = f"{PAK_PATH}uninstalled/"
    PAK_INSTALLED_PATH     = f"{PAK_PATH}installed/"

    # - OBSE -
    OBSE_PATH              = f"{STAGING_PATH}obse/"
    OBSE_UNINSTALLED_PATH  = f"{OBSE_PATH}uninstalled/"
    OBSE_INSTALLED_PATH    = f"{OBSE_PATH}installed/"

    # - UE4SS -
    UE4SS_PATH             = f"{STAGING_PATH}ue4ss/"
    UE4SS_UNINSTALLED_PATH = f"{UE4SS_PATH}uninstalled/"
    UE4SS_INSTALLED_PATH   = f"{UE4SS_PATH}installed/"
    
    # - BUNDLES -
    BUN_PATH               = f"{STAGING_PATH}bundles/"
    BUN_UNINSTALLED_PATH   = f"{BUN_PATH}uninstalled/"
    BUN_INSTALLED_PATH     = f"{BUN_PATH}installed/"

    # - OBLIVION -    
    OBR_PATH               = f"{USR_PATH}.local/share/Steam/steamapps/common/Oblivion Remastered/"
    OB_WIN_64_PATH         = f"{OBR_PATH}OblivionRemastered/Binaries/Win64/"
    OB_PAK_PATH            = f"{OBR_PATH}OblivionRemastered/Content/Paks/~mods/"
    OB_OBV_DATA_PATH       = f"{OBR_PATH}OblivionRemastered/Content/Dev/ObvData/"
    OB_ESP_DATA_PATH       = f"{OBR_PATH}OblivionRemastered/Content/Dev/ObvData/Data/"
    OB_PLUGINS_TXT         = f"{OBR_PATH}OblivionRemastered/Content/Dev/ObvData/Data/Plugins.txt"

    # - TCSS -
    WEAVER_CSS             = f"./tcss/_nirn_weaver.tcss"

    # This is starting to feel bad but is probably fine
    def check_folders():
        # - PROGRAM -
        if not exists(NirnPaths.NW_PATH):
            mkdir(NirnPaths.NW_PATH)
        if not exists(NirnPaths.STAGING_PATH):
            mkdir(NirnPaths.STAGING_PATH)

        # - ESP/ESM -
        if not exists(NirnPaths.ES_PATH):
            mkdir(NirnPaths.ES_PATH)
        if not exists(NirnPaths.ES_UNINSTALLED_PATH):
            mkdir(NirnPaths.ES_UNINSTALLED_PATH)
        if not exists(NirnPaths.ES_INSTALLED_PATH):
            mkdir(NirnPaths.ES_INSTALLED_PATH)

        # - PAK -
        if not exists(NirnPaths.PAK_PATH):
            mkdir(NirnPaths.PAK_PATH)
        if not exists(NirnPaths.PAK_UNINSTALLED_PATH):
            mkdir(NirnPaths.PAK_UNINSTALLED_PATH)
        if not exists(NirnPaths.PAK_INSTALLED_PATH):
            mkdir(NirnPaths.PAK_INSTALLED_PATH)

        # - OBSE -
        if not exists(NirnPaths.OBSE_PATH):
            mkdir(NirnPaths.OBSE_PATH)
        if not exists(NirnPaths.OBSE_UNINSTALLED_PATH):
            mkdir(NirnPaths.OBSE_UNINSTALLED_PATH)       
        if not exists(NirnPaths.OBSE_INSTALLED_PATH):
            mkdir(NirnPaths.OBSE_INSTALLED_PATH)

        # - UE4SS -
        if not exists(NirnPaths.UE4SS_PATH):
            mkdir(NirnPaths.UE4SS_PATH)
        if not exists(NirnPaths.UE4SS_UNINSTALLED_PATH):
            mkdir(NirnPaths.UE4SS_UNINSTALLED_PATH)
        if not exists(NirnPaths.UE4SS_INSTALLED_PATH):
            mkdir(NirnPaths.UE4SS_INSTALLED_PATH)

        # - BUNDLES -
        if not exists(NirnPaths.BUN_PATH):
            mkdir(NirnPaths.BUN_PATH)
        if not exists(NirnPaths.BUN_UNINSTALLED_PATH):
            mkdir(NirnPaths.BUN_UNINSTALLED_PATH)
        if not exists(NirnPaths.BUN_INSTALLED_PATH):
            mkdir(NirnPaths.BUN_INSTALLED_PATH)

        # - OBLIVION -
        if not exists(NirnPaths.OB_PAK_PATH):
            mkdir(NirnPaths.OB_PAK_PATH)
