# -*- coding: utf-8 -*-

import os, time, re

prog_info = {'title':'Month-End File Renaming Utility',
             'author':'Michael J. Armstrong',
             'copyright':'© 2018 Michael J. Armstrong, Toronto, Canada',
             'contact':'marmstrong310@gmail.com',
             'version':'2.0',
             'versiondate': '2018-09-26',
             'description':'a file system tool to rename the carry-forward files to the current month.',
             'inputs':'currently none',
             'warning':'Note: Any user notes or warnings'
             }

def title_screen():
    '''program title information'''
    print('')
    print(prog_info['title'] + ' v' + prog_info['version'])
    print(prog_info['copyright'])
    print(prog_info['title'] + ' is ' + prog_info['description'])
    print('')

def exit_farewell():
    '''program departure information'''
    print('')
    print('File renaming complete.')
    input('press ENTER to close')
    cls()

def cls():
    '''clears screen'''
    from os import system as os_sys
    from os import name as os_name
    os_sys('cls' if os_name == 'nt' else 'clear')

def main():
    # display program information
    cls()
    title_screen()

    # request input
    base = input('enter old date (e.g., 2018-04): ')
    change = input('enter new date (e.g., 2018-05): ')

    # set variables for folders to search in
    new_year = str(change[:4])
    new_month = str(change[-2:])

    
    # month-folder reference dictionary
    month_ref = {
        '01':'01 - January','02':'02 - February','03':'03 - March','04':'04 - April',
        '05':'05 - May','06':'06 - June','07':'07 - July','08':'08 - August',
        '09':'09 - September','10':'10 - October','11':'11 - November','12':'12 - December'
    }

    # group of folders to search in (dynamically set by input variable month)
    me_folders = [r'M:\02 Financial Controls - Canada\{} - Toronto Finance\01 - Month-End\01 - Month-End Journals\{}\01 - Canada'.format(new_year,month_ref[new_month]),
                  r'M:\02 Financial Controls - Canada\{} - Toronto Finance\01 - Month-End\01 - Month-End Journals\{}\01 - Canada\Closed BU Clearing'.format(new_year,month_ref[new_month]),
                  r'M:\02 Financial Controls - Canada\{} - Toronto Finance\01 - Month-End\01 - Month-End Journals\{}\02 - Canada (Epic)'.format(new_year,month_ref[new_month]),
                  r'M:\02 Financial Controls - Canada\{} - Toronto Finance\01 - Month-End\01 - Month-End Journals\{}\02 - Canada (Epic)\Late Cash Adjustment'.format(new_year,month_ref[new_month]),
                  r'M:\02 Financial Controls - Canada\{} - Toronto Finance\01 - Month-End\01 - Month-End Journals\{}\03 - GBS New Glasgow'.format(new_year,month_ref[new_month]),
                  r'M:\02 Financial Controls - Canada\{} - Toronto Finance\01 - Month-End\01 - Month-End Journals\{}\04 - Norcan'.format(new_year,month_ref[new_month]),
                  r'M:\02 Financial Controls - Canada\{} - Toronto Finance\01 - Month-End\01 - Month-End Journals\{}\05 - GBS Quickbooks'.format(new_year,month_ref[new_month]),
                  r'M:\02 Financial Controls - Canada\{} - Toronto Finance\01 - Month-End\01 - Month-End Journals\{}\06 - GPL'.format(new_year,month_ref[new_month]),
                  r'M:\02 Financial Controls - Canada\{} - Toronto Finance\01 - Month-End\01 - Month-End Journals\{}\07 - Palmer'.format(new_year,month_ref[new_month]),
                  r'M:\02 Financial Controls - Canada\{} - Toronto Finance\03 - Financial Controls\01 - Month-End\{}'.format(new_year,month_ref[new_month]),
                  r'M:\02 Financial Controls - Canada\{} - Toronto Finance\03 - Financial Controls\01 - Month-End\{}\Balance Sheet Review\Post Close'.format(new_year,month_ref[new_month]),
                  r'M:\02 Financial Controls - Canada\{} - Toronto Finance\03 - Financial Controls\01 - Month-End\{}\Balance Sheet Review\Pre Close Docs'.format(new_year,month_ref[new_month]),
                  r'M:\02 Financial Controls - Canada\{} - Toronto Finance\03 - Financial Controls\01 - Month-End\{}\Collectability Analysis'.format(new_year,month_ref[new_month]),
                  r'M:\02 Financial Controls - Canada\{} - Toronto Finance\03 - Financial Controls\01 - Month-End\{}\Revenue Data Analysis\Final'.format(new_year,month_ref[new_month]),
                  r'M:\02 Financial Controls - Canada\{} - Toronto Finance\03 - Financial Controls\01 - Month-End\{}\Revenue Data Analysis\Pre-Close'.format(new_year,month_ref[new_month]),
                  r'M:\02 Financial Controls - Canada\{} - Toronto Finance\03 - Financial Controls\01 - Month-End\{}\Revenue Reconciliation'.format(new_year,month_ref[new_month]),
                  r'M:\02 Financial Controls - Canada\{} - Toronto Finance\04 - Trial Balance\{}'.format(new_year,month_ref[new_month]),
                  r'M:\02 Financial Controls - Canada\{} - Toronto Finance\05 - Sales Tax\{}'.format(new_year,month_ref[new_month])
                  ]

    # create counter variables
    rename = 0
    skip = 0
    location_error = False
    ok_list = []
    fail_list = []

    # processing notification
    print('')
    print('Checking folder existence...')

    # remove missing folders from change search
    for fold_path in me_folders:
        #fold_path = input('enter folder path: ')
        try:
            for f in os.listdir(fold_path):
                pass
            ok_list.append(fold_path)
        except FileNotFoundError:
            location_error = True
            fail_list.append(fold_path)
            continue
    
    # processing notification
    print('')
    print('Applying name changes...')
    # walk through existing folders and make changes
    for fold_path in ok_list:        
        for f in os.listdir(fold_path):
            if f[:7] == change:
                skip += 1
            else:
                # set new file name
                f_new = re.sub(base,change,f)
                # rename the original file
                os.rename(fold_path + '\\' + f, fold_path + '\\' + f_new)
                rename += 1
        
    # display results
    print('')
    print('Changes complete.')
    print('   files renamed: ' + str(rename))
    print('   files skipped: ' + str(skip))
    print('')
    
    # missing/complete folder notification
    if location_error:
        print('The following locations were not found:')
        for i in fail_list:
            print(i)
    else:
        print('All locations were found.')

    # pause on completion
    exit_farewell()

if __name__ == "__main__":
    main()
