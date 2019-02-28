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
        for p,d,fs in os.walk('.'):
                for f in fs:
                        if fnmatch.fnmatch(f, '*.yaml'):
                                files.append(f)
        return files

def createFile(output, fileName):
        fname = os.path.splitext(fileName)[0]
        with open(fname, 'w+') as f:
                f.write(output)
                f.close()   
                f = os.rename(fname, fname+'.text')

#Run list of yaml files through template engine
def tempBuild(ymlFiles):
        #Build vars for template engine
        ENV = Environment(loader=FileSystemLoader('.'))
        template = ENV.get_template("basetemp.j2")
        for y in range(len(ymlFiles)):
                fileName = ymlFiles[y]
                with open(fileName) as yml:
                        config = yaml.load(yml)
                        output = template.render(config)
                        createFile(output, fileName)

if __name__ == '__main__':
        print("Scanning local dir for .yaml files")
        ymlFiles = findFiles()
        print("Files found. Loading yaml, creating templates")
        tempBuild(ymlFiles)
        print("Templates created.")

