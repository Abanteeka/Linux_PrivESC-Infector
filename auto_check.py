import os

# import subprocess
# os.system("ls")
# os.popen("ls").read()
# subprocess.run()
def os_kernel_check():
    # this function will check for os, and kernel info
    if flag != 0:
        print("os/kernel check function")
        os.system('uname -a')
        os.system('cat /etc/os-release')
        #os.system('cat /etc/issue')
        os.system('clear')
        print("-------------------------------------------------")
        root_check()

    else:
        print("os/kernel check function")
        os.system('uname -a')
        os.system('cat /etc/os-release')
        os.system('cat /etc/issue')
        

def network_info():  #later
    try:
        os.system('cmd /k "ipconfig"')
    except:
        print("Invalid command")

# this function will check for services running as root
def root_check():
    if flag != 0:
        print("Root Service Check Function")
        os.system('ps aux | grep root')
        print("-------------------------------------------------")
        SUID_GUID_check()

    else:
        os.system('clear')
        print("root service check function")
        os.system('ps aux | grep root')
        

# this function will check for abusable SUID/GUID binaries
def SUID_GUID_check():
    if flag != 0:
        #print(flag)
        os.system('clear')
        print("SUID/GUID Check")
        print("")
        print("SUID Check")
        os.system('find / -perm -u=s -type f 2>/dev/null')
        print("-------------------------------------------------")
        print("GUID Check")
        os.system('find / -perm -g=s -type f 2>/dev/null')
        print("-------------------------------------------------")
        
    else:
        os.system('clear')
        #print(flag)
        os.system('find / -perm -u=s -type f 2>/dev/null')
        print("GUID Check")
        os.system('find / -perm -g=s -type f 2>/dev/null')
        print("-------------------------------------------------")
        print("SUID/GUID binaries check function")
        

def Sudoer_Permission_Check():
    try:
        print("Sudoer_Permission_Check")
        os.system('sudo -l')
        print("-------------------------------------------------")

    except:
        print("You don't have sudoer permission")
        

def Cronjobs():
        print("Cronjobs")
        os.system('cat /etc/crontab')   #any possible failure

def Improper_permission_check():
    print("Improper_permission_check")
    os.system('ls -l /etc | grep shadow')
    
def passwords_keys_historyfiles():
    print("Check pass keys")
    os.system('cat ~/.*history | less')
    
#Main Menu
def main():
    
    while True:
        global flag
        flag = 0
        print("This is the main function")  # Press Ctrl+F8 to toggle the breakpoint.
        OPTION = int(input("""
            1. OS/Kernel Check
            2. Root Service Check
            3. SUID/GUID Check
            4. Full Scan
            5. Sudoer Permission Check
            6. Cronjobs
            7. EXIT
            LPC>>
            """))

        if OPTION == 1:
            # print("You chose option 1")
            os_kernel_check()
        elif OPTION == 2:
            print("You chose option 2")
            root_check()
        elif OPTION == 3:
            print("You chose option 3")
            SUID_GUID_check()
        elif OPTION == 4:
            flag = flag + 1
            os_kernel_check()
        elif OPTION == 5:
            print("You chose option 5")
            Sudoer_Permission_Check()
        elif OPTION == 6:
            print("You chose option 6")
            Cronjobs()
        elif OPTION == 7:
            break

        else:
            BAD_OPTION = input("Invalid option. Press ENTER to continue.")
            main()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
    #auto_check()
