#! /bin/python3.7

###################################
# Author: Billy Downing           #   
# Date: 27 Feb 2019               #
# Purpose: Build config templates #
###################################

from jinja2 import Environment, FileSystemLoader
import yaml, os, fnmatch


def findFiles():
        #Gather list of files with .yaml
        files = []
        for _,_,fs in os.walk('.'):
                for f in fs:
                        if fnmatch.fnmatch(f, '*.yaml'):
                                files.append(f)
        return files

def createFile(output, fileName, OS, IP):
        fname = os.path.splitext(fileName)[0]
        rootDir = os.getcwd()
        newDir = os.getcwd()+'\\'+fname
        os.mkdir(newDir)
        os.chdir(newDir)
        with open(fname, 'w+') as f:
                f.write(output)
                f.close()   
                f = os.rename(fname, fname+'.text')
        with open("config.setup", 'w+') as s:
                s.write(IP+" "+fname+".text"+" "+OS)
                s.close()
        os.chdir(rootDir)

#Run list of yaml files through template engine
def tempBuild(ymlFiles, OS, IP, tmplt):
        #Build vars for template engine
        ENV = Environment(loader=FileSystemLoader('.'))
        template = ENV.get_template(tmplt)
        for y in range(len(ymlFiles)):
                fileName = ymlFiles[y]
                with open(fileName) as yml:
                        config = yaml.load(yml)
                        output = template.render(config)
                        createFile(output, fileName, OS, IP)
#Main function
if __name__ == '__main__':
        print("Scanning local dir for .yaml files")
        ymlFiles = findFiles()
        print("Files found. Loading yaml, creating templates")
        #Needed attributes for .setup file
        OS = input("OS Image Name: ")
        IP = input("MGMT IP: ")
        tmplt = input("Template: ")
        tempBuild(ymlFiles, OS, IP, tmplt)
        print("Templates created.")

