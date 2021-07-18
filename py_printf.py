import subprocess
import os
import sys
import random

header="""                                                                              
 __________________________________________________________________________________________
/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/
___________      .____    ._____________  ____________________                             
\_   _____/ ____ |    |   |   \______   \/   _____/\_   _____/                             
 |    __)__/ ___\|    |   |   ||     ___/\_____  \  |    __)_                              
 |        \  \___|    |___|   ||    |    /        \ |        \                             
/_______  /\___  >_______ \___||____|   /_______  //_______  /                             
        \/     \/        \/                     \/         \/                              
             .__        __    _____               __                   __                  
_____________|__| _____/  |__/ ____\            _/  |_  ____   _______/  |_  ___________   
\____ \_  __ \  |/    \   __\   __\             \   __\/ __ \ /  ___/\   __\/ __ \_  __ \  
|  |_> >  | \/  |   |  \  |  |  |                |  | \  ___/ \___ \  |  | \  ___/|  | \/  
|   __/|__|  |__|___|  /__|  |__|________________|__|  \___  >____  > |__|  \___  >__|     
|__|                 \/        /_____/_____/_____/         \/     \/            \/         
    ___    _____ ________   ___                                                            
   /  /   /  |  |\_____  \  \  \                                                           
  /  /   /   |  |_/  ____/   \  \                                                          
 (  (   /    ^   /       \    )  )                                                         
  \  \  \____   |\_______ \  /  /                                                          
   \__\      |__|        \/ /__/                                                                                  
                                                                        cursus 2021
                                                                        made 18/06/21
                                                                        by motoure
 ____________________________________________________________________________________      
/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/      
"""
ENDL = "\n"
def execCmd(prog, concat):
	proc=subprocess.Popen(prog + " " + concat, shell=True, stdout=subprocess.PIPE)
	output=proc.communicate()[0]
	return (output)
def start_main(args):
    res = """int   main(""" + args + """)\n{""" 
    return (res)
class compose:
    headers = ""
    defines = ""
    main = ""
    body = ""
    #fill compose
    def Header(self, elems):
        for elem in elems:
            self.headers += "#include " + elem + ENDL
    def Define(self, elems):
        for elem in elems:
            self.defines += "# define " + elem + ENDL
    #fill compose
    def __print__(self):
        print(self.headers)
        print(self.defines)
        print(self.body)
        print(self.main)

def prep_test():
    #composet test
    orig = compose()
    orig.Header(["<stdio.h>","<stdlib.h>"])
    orig.Define(["TEST \"test\""])
    orig.__print__()
    #
    #prog_name = "p_p_cbuild"
    #main_fd = open("./py_printf_main.c", "w+")
    #main_fd.write(main_file)
   # execCmd("cc", "*.c" + " -o " + prog_name)
    return ("null")

def main():
    print(header)
    orig = prep_test()

main()
