#! python3
import os, re, shutil

def main():
    #cFolder = input('enter base folder (e.g., C:\\temp\\05 - May):')
    cFolder = '/home/michael/Documents/2018-05 Folder/'
    #base = input('enter old date (e.g., 2018-04): ')
    datePattern = re.compile(r'^20\d\d-\d\d.*')

    base = '2018-05'
    #change = input('enter new date (e.g., 2018-05): ')
    change = '2018-06'
    rename = 0
    skip = 0
    
    for oldfile in os.listdir(cFolder):
        if oldfile[:7] == base:
            newfile = str(change + oldfile[7:])
            shutil.move(os.path.join(cFolder,oldfile), os.path.join(cFolder,newfile))
        #mo = datePattern.search(oldfile)

        if mo = None:
            continue
        

    '''

    for root, dirs, files in os.walk(cFolder):
        # make sure to use full path (root/dirs/) and os.join the file name when changing
        for d in dirs:
            for f in files:
                # if f[:7] == change:
                if f.beginswith(change):
                    # set new file name
                    f_new = re.sub(base,change,f)
                    # rename the original file
                    os.rename(os.path.join(cFolder,f), os.path.join(cFolder,f_new))
                    rename += 1
# START REVIEW HERE
            else:
                skip += 1

    print('files renamed: ' + str(rename))
    print('files skipped: ' + str(skip))
    print('')
    input('file renaming complete, press ENTER to close')

if __name__ == "__main__":
    main()

# update

    
	
