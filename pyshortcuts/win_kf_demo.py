#!/usr/bin/env python
"""
Create desktop shortcuts for Windows
"""
from __future__ import print_function

# Windows Known Folders (desktop, startmenu, my documents, ...)
from winknownfolders import folders as kf

def get_all_folders():
    '''Return dict of all known folders'''
    from winknownfolders import table as kf_table
    # Print all known folder names and paths
    for k,v in kf_table.items():
        print("{:<22}: {}".format(k,v))
    return kf_table

def get_menu_folder():
    '''Return user Start Menu Programs folder path'''
    return kf.Programs

def get_desktop_folder():
    '''Return user Desktop folder path'''
    return kf.Desktop

if __name__ == '__main__':
    all = get_all_folders()
    print('-'*60)
    print('Desktop, Programs menu:\n', get_desktop_folder(), get_menu_folder())