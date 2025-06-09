# Nirn Weaver
## A simple and fast Oblivion Mod Manager in your Terminal

## Features

### Current Features

	[x] Stage ESP/ESM files for quick Install/Uninstall
	[x] Install and Uninstall ESP/ESM files
	[X] Modify and save the load order to Plugins.txt
	[x] Stage & Install/Uninstall OBSE Plugins

### Work In Progress Features

	[-] Bundle Mods for bulk Install/Uninstall
	[-] Stage & Install/Uninstall Pak mods
	[-] Stage & Install/Uninstall UE4SS Mods
	
### Planned Features

	[] Config Options
	[] Windows Support

## Useage Requirements

> [!IMPORTANT]
> Nirn Weaver currently only supports Oblivion Remaster Installed on Linux.

> [!IMPORTANT]
> Nirn Weaver currently has no build and can only be run via CLI.

To run Nirn Weaver ensure you have Textual installed in your env/venv with:

```
pip install textual textual-dev
```

To run:

```
python main.py
```

Or:

```
textual run main.py
```

To exit simply press `Ctrl + q`

## Menu Overviews

### ESP Manager

![The default ESP Managing view.](https://github.com/ScorpioGameKing/NirnWeaver/blob/main/assets/images/NirnWeaverESPTUI.png)


The ESP Manager helps automatically stage any valid esp files found in the Downloads directory and inside the game files. With 
these staged files you can easily install and uninstall quickly while having quick tools for adjusting your load order.

#### Load Order

![The ESP Load Order Manager.](https://github.com/ScorpioGameKing/NirnWeaver/blob/main/assets/images/NirnWeaverESPLoadOrder.png)


Within this view you can see and adjust your current load order with `Ctrl + Up/Down`. To save an order press `Shift + S`.

#### Staging View

![The ESP Staging Manager.](https://github.com/ScorpioGameKing/NirnWeaver/blob/main/assets/images/NirnWeaverESPStaging.png)

> [!NOTE]
> The ESP Staging Manager

This is a split view of NirnWeaver's ESP/ESM staging directory. Any mod you select in the uninstalled section (Left side) will
be moved to the installed directory and added into the appropriate directory in the game. The same goes for the installed
section, just in reverse.

#### Status Bar and Keybinds

![The Status-bar and Keybinds.](https://github.com/ScorpioGameKing/NirnWeaver/blob/main/assets/images/NirnWeaverESPKeys.png)

> [!IMPORTANT]
> The Reactive Elements of the status bar are WIP

On any screen of NirnWeaver is a footer bar with helpful keybinding reference.

### PAK Manager

> [!IMPORTANT]
> This Manager is still WIP

![The default PAK Managing view.](https://github.com/ScorpioGameKing/NirnWeaver/blob/main/assets/images/NirnWeaverPAKTUI.png)

The PAK Manager will stage all files from a directory containing the relavant file types into a `Bundle` for easier handling 
and improved storage space. Using these bundles you can easily install the groups of files included by a PAK mod.

### OBSE Manager

![The default OBSE Managing view.](https://github.com/ScorpioGameKing/NirnWeaver/blob/main/assets/images/NirnWeaverOBSETUI.png)

The PAK Manager will stage all files from a directory containing the relavant file types into a `Bundle` for easier handling 
and improved storage space. Using these bundles you can easily install the groups of files included by an OBSE plugin.

### UE4SS Manager

> [!IMPORTANT]
> This Manager is still WIP

![The default UE4SS Managing view.](https://github.com/ScorpioGameKing/NirnWeaver/blob/main/assets/images/NirnWeaverUE4SSTUI.png)

The PAK Manager will stage all files from a directory containing the relavant file types into a `Bundle` for easier handling 
and improved storage space. Using these bundles you can easily install the groups of files included by a UE4SS mod.

### Bundles

> [!NOTE]
> Currently this is used internally, there are plans to allow users to bundle groups of mods

Bundles are NirnWeaver's method of handling groups of files. When a manager scans a directory for files it will first create 
a key of the valid files. From there they are staged and a Bundle is created to track and manage files for each mod found. 
This allows us to quickly find everything we need for installing and uninstalling mods. When Bundles are uninstalled they are
compressed into a into a tarball with bz2 saving plenty of space. Currently Bundles are not saved between runs requiring a new
indexing process each launch, this is known and will be addressed.
