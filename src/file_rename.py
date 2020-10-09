from os import walk as os_walk
from os import sep as os_sep
from os import rename as os_rename
from re import compile as re_compile
from re import sub as re_sub
from pystandard import clearscreen, title_screen, exit_farewell, isodate, load_obj

import tkinter as tk
from tkinter import filedialog

def fold_select():
    root = tk.Tk()
    root.withdraw()
    fold_path = filedialog.askdirectory(title="Select folder location to parse")
    return fold_path

def main():
    # function scope variables
    prog_info = load_obj('settings.mj')
    dates = re_compile('([2]\d\d\d)(\-)([0-1]\d)\s')
    change = None
    
    while True:
        # loop scope variables
        rename = 0
        skip = 0
        
        # display program information
        clearscreen()
        title_screen(prog_info)
        
        ##### INTRODUCTION #####
        # request input
        if change == None:
            change = isodate(5,'Enter new month reference (e.g., 2018-05): ')    
        
        #folder = input('Enter base folder location:\n')
        folder = fold_select()
        
        # month-folder reference dictionary TODO - To be used?
        #month_ref = {
        #    '01':'01 - January','02':'02 - February','03':'03 - March','04':'04 - April',
        #    '05':'05 - May','06':'06 - June','07':'07 - July','08':'08 - August',
        #    '09':'09 - September','10':'10 - October','11':'11 - November','12':'12 - December'
        #}
        
        ##### PROCEDURE #####
        # processing notification        
        print('Applying name changes...')
        # walk through existing folders and make changes
        for dpath, folders, files in os_walk(folder):
            for f in files:
                # if the file is prepended with year + date
                if dates.match(f[:7]):
                    if f[:7] == change:
                        skip += 1
                    else:
                        try:
                            # set new file name
                            f_new = re_sub(f[0:7],change,f)
                            # rename the original file
                            os_rename(dpath + os_sep + f, dpath + os_sep + f_new)
                            rename += 1
                        except:
                            skip += 1
                # if not then skip it
                else:
                    skip += 1
        
        ##### TERMINATION/CONTINIUANCE #####
        # display results
        print('Changes complete for ' + folder)
        print('   Files renamed: ' + str(rename))
        print('   Files skipped: ' + str(skip))
        print('')
        go_again = input("Change another folder? (Y/N): ")
        if go_again.upper() != "Y":
            break

    # program termination
    exit_farewell(prog_info)

if __name__ == '__main__':
    main()
