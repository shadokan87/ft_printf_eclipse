import subprocess
import os
import sys
import random
from random import seed
from random import randint

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
#utils
def rand_int_arr(min, max, amount):
    i = 0
    tmp = max
    val = list(range(0, amount))
    while (i < amount):
        val[i] = str(randint(min, max))
        max /= randint(1, 10)
        if (max <= 1):
            max = tmp
        i += 1
    return (val)
#
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
        res += "\t" + funcname + "("
        i = 0
        while (i < len(params)):
            res += params[i]
            if (i != len(params) - 1):
                res += ", "
            i += 1
        res += ");\n"
        return (res)
    def startFunc(self, ret, funcname, params):
        inline = self.funcInline(funcname, params)
        concat = ""
        for elem in inline:
            if (elem != ";"):
                concat += elem
        self.body += ret + "\t" + str(concat) + "{" + ENDL
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
    def varInitAssign(self, elems, val):
        self.body += "\t"
        for elem in elems:
            self.body += elem
        self.body += " = " + str(val) + ";" + ENDL

    def varAssign(self, elems):
        self.body += "\t"
        for elem in elems:
            self.body += elem
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
    def spawnVar(self, elems, amount):
        i = 0
        concat = []
        while (i < amount):
            concat = elems[0]
            concat += str(elems[1])+ str(i)
            self.varInit(concat)
            i += 1
    def spawnVarAssign(self, elems, val):
        i = 0
        concat = []
        while (i < len(val)):
            concat = elems[0]
            concat += str(elems[1]) + str(i)
            self.varInitAssign(concat, val[i])
            i += 1
def prep_dp(orig):
    orig.Define(["$MOD_D_POSITIVE int"])
    orig.startFunc("void", "__d", ["void"])
    orig.spawnVarAssign(["$MOD_D_POSITIVE ", "_dp"], rand_int_arr(0, 2147483647,30))
    orig.body += ENDL
    i = 0
    while (i < 30):
        orig.body += orig.funcInline("printf", ["\"%s\"", "_dp" + str(i)])
        i += 1
    orig.endFunc()
def prep_np(orig):
    orig.Define(["$MOD_D_NEGATIVE int"])
    orig.startFunc("void", "__d", ["void"])
    orig.spawnVarAssign(["$MOD_D_POSITIVE ", "_np"], rand_int_arr(0, 2147483647,30))
    orig.body += ENDL
    i = 0
    while (i < 30):
        orig.body += orig.funcInline("printf", ["\"%s\"", "_np" + str(i)])
        i += 1
    orig.endFunc()

    #orig.Define(["$MOD_D_NEG int"])
    #orig.Define(["$MOD_S char *"])
    #orig.Define(["$MOD_C char"])
    #orig.Define(["$MOD_U unsigned int"])

def prep_test():
    #composet test
    orig = compose()
    orig.Header(["<stdio.h>","<stdlib.h>"])
    prep_dp(orig)
    orig.__print__()
    #
    prog_name = "p_p_cbuild"
    main_fd = open("./py_printf_main.c", "w+")
    main_fd.write(orig.headers + orig.defines + orig.body)
    execCmd("cc", "*.c" + " -o " + prog_name)
    return ("null")

def main():
    print(header)
    orig = prep_test()

main()
