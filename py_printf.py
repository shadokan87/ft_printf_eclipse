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
class compose:
    def __init__(self, headers = "", defines = "", main = "", body = ""):
        self.headers = headers
        self.defines = defines
        self.main = main
        self.body = body
    def funcInline(self, funcname, params):
        res = ""
        res += funcname + "("
        i = 0
        while (i < len(params)):
            res += params[i]
            if (i != len(params) - 1):
                res += ","
            i += 1
            res += ");\n"
            return (res)
    def startFunc(self, ret, funcname, params):
        inline = self.funcInline(funcname, params)
        self.body += ret + "\t" + str(inline) + "{" + ENDL
    #fill compose
    def Header(self, elems):
        for elem in elems:
            self.headers += "#include " + elem + ENDL
    def Define(self, elems):
        for elem in elems:
            self.defines += "# define " + elem + ENDL
    #fill compose
    def varInit(self, elems):
        self.body += "\t"
        for elem in elems:
            self.body += elem
        self.body += ";" + ENDL
    def varAssign(self, elems):
        self.body += elems[0] + " " + "=" + " " + elems[1]
    def __print__(self):
        print(self.headers)
        print(self.defines)
        print(self.body)
        print(self.main)
            #self.self.body += elems[0] + elems[1] + ";" + ENDL
    def func(self, funcname, params):
        self.body += self.funcInline(funcname, params)
    def endFunc(self):
        self.body += "}"
    def spanVar(self, elems, amount):
        self.varInit(elems)

def prep_test():
    #composet test
    orig = compose()
    orig.Header(["<stdio.h>","<stdlib.h>"])
    orig.startFunc("int", "main", ["void"])
    orig.varInit(["int *", "test"])
    orig.spanVar(["int *"])
    orig.endFunc()
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
