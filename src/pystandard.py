from json import dump as json_dump
from json import load as json_load
from os import system, getcwd, sep, pardir
from os.path import normpath
from sys import platform, exit
from re import compile as re_compile
from time import sleep

def clearscreen():
    if platform == "win32":
        system('cls')
    elif platform == "linux":
        system('clear')
    elif platform == 'darwin':
        system('clear')

def loadshell():
    if platform == "win32":
        system('echo OFF')
        system('color A')
    elif platform == "linux":
        system('tput setaf 2')
    #elif platform == 'darwin':
    
def title_screen(data_dict):
    '''program title information'''
    print (data_dict["title"] + " v" + data_dict["version"])
    print (data_dict["copyright"])
    print ("Contact: " + data_dict["contact"])
    print ("Distributable under the " + data_dict["license"] + "\n")

def exit_farewell(data_dict):
    '''program departure information'''
    print(data_dict["farewell"])
    input("press ENTER to close")

def csv_tolist(list_var,file):
    '''create list from CSV file'''
    with open(file, "r") as f:
        for line in f.readlines():
            list_var.append(line.rstrip("\n"))

def save_path(prod=True):
    '''location query for payroll source data to be fed to pandas'''
    # base data source
    question = "Do you want to save here (Y/N):\n"
    # win \path\of\network\folder\
    prodpath = 'S:\\Finance\\Payroll\\tmp\\'
    # win \path\of\local\folder\
    winpath = normpath(getcwd() + sep + pardir) + '\\tmp\\'
    # unix path/of/local/folder/
    linpath = normpath(getcwd() + sep + pardir) + '/tmp/'
    
    # test system type
    # return location format per system
    # windows system
    if platform == 'win32':
        if prod:
            qpath = input(question + prodpath + '\n')
        else:
            qpath = input(question + winpath + '\n')
        if qpath.upper() == "Y":
            if prod:
                return prodpath
            else:
                return winpath
        else:
            save_path = input('Enter the full destination folder (e.g. C:\path\\to\\file\ :\n')
            # ensure proper ending for folder path
            if save_path[-1:] == '\\':
                pass
            else:
                return save_path + '\\'
    # linux system
    elif platform in ('linux','darwin'):
        qpath = input(question + linpath+ '\n')
        if qpath.upper() == "Y":
            return linpath
        else:
            save_path = input('Enter the full destination folder (e.g. ~/Documents/path/to/file/ :\n')
            # ensure proper ending for folder path
            if save_path[-1:] == '/':
                pass
            else:
                return save_path + '/'

def data_path(filename,prod=True):
    '''location query for payroll source data to be fed to pandas'''
    # win \path\of\network\folder\
    prodpath = 'S:\\Finance\\Payroll\\data\\'
    # win \path\of\local\folder\
    winpath = normpath(getcwd() + sep + pardir) + '\\data\\'
    # unix path/of/local/folder/
    linpath = normpath(getcwd() + sep + pardir) + '/data/'
    
    # test system type
    # return location format per system
    # windows system
    if platform == 'win32':
        if prod:
            return prodpath + filename
        else:
            return winpath + filename
    # linux system
    elif platform in ('linux','darwin'):
        return linpath + filename

def isodate(question_option,question='standard'):
    '''request, test, and return date string'''
    stdpro = True
    if question != 'standard':
        stdpro = False
    # set regex search pattern
    # full date
    datef = re_compile('([1-2]\d\d\d)(\-)([0-1]\d)(-)([0123]\d)')
    # short date
    dates = re_compile('([1-2]\d\d\d)(\-)([0-1]\d)')
    
    # question setup
    if question == "standard": 
        if int(question_option) == 1:
            question = 'Enter month-end date (YYYY-MM-DD):\n'
        elif int(question_option) == 2:
            question = 'Enter the pay period:\n'
        elif int(question_option) == 3:
            question = 'Enter date range START (YYYY-MM-DD):\n'
        elif int(question_option) == 4:
            question = 'Enter date range END (YYYY-MM-DD):\n'
        elif int(question_option) == 5:
            question = 'Enter date range END (YYYY-MM-DD):\n'
    
    # date input and testing
    while True:
        # ask for date based on question option
        ipdate = input(question)
        # test input date
        if stdpro:
            if datef.match(ipdate):
                if int(ipdate[5:7]) <= 12:
                    if int(ipdate[8:10]) <= 31:
                        break
                    else:
                        print('Day must be in range 01 - 31')
                else:
                    print('Month must be in range 01 - 12')
            else:
                print('Use ISO date format (YYYY-MM-DD)')
        else:
            if dates.match(ipdate):
                if int(ipdate[5:7]) <= 12:
                    break
                else:
                    print('Month must be in range 01 - 12')
            else:
                print('Use ISO date format (YYYY-MM)')
    return ipdate

'''**************JSON FILES**************'''
def save_obj(obj_name, file_name,obf=True):
    '''
    Save object into a json file **REQUIRES json.dump** (imported automatically)
    obj_name =  should be a dictionary type object
    file_name can be anything, if json extension to be used, do not add '.json' to file_name
    obf=True will not add a 'json' extension to the file_name
    '''
    # test type
    if type(obj_name) == dict:
        if obf:
            try:
                with open(file_name,'w') as f:
                    json_dump(obj_name, f)
            except:
                print('File save error: object not saved to file')
        # obfuscation will not use a .json extension
        else:
            try:
                with open(file_name + '.json','w') as f:
                    json_dump(obj_name, f)
            except:
                print('File save error: object not saved to file')
    else: # if not dict, return fail instructions
        print('obj_name type must be dict/dictionary')
    


def load_obj(file_name):
    '''
    Load object from a json file **REQUIRES json.load** (imported automatically)
    '''
    try:
        with open(file_name,"r") as fp:
            return json_load(fp)
    except:
        print("Unable to open JSON file.")
        print("Exiting program...")
        sleep(2)
        exit()
