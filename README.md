Simple Template Generator using YAML, Python, and Jinja

Purpose:
Generate configuration templates and file structure to use Dell's OS6 based switches AutoInstall feature. This allow quick provisioning and upgrade for Dell OS6 Switches. AutoInstall requires a USB drive with a *.setup, *.text and Image name to be successfull. This application takes YAML files, parses them to create configuration files for Dell OS6 Switches (the *.text) and additionally build the files to be placed on a USB drive. The directories are created local to the application.

Process:
-Scans current directory for *.yaml files.
-Takes user input to build *.setup files and jinja template to use (searches current directory)
-Parses YAML files, iterates through each and runs through Jinja2 template.
--For each file, creates a unique directory containing *.setup and *.text

*Currently only support Dell OS6 template building

How To Use:

$ python Gen.py
--
OS Image Name: < This is the name of the OS to be added within the *.setup file>
MGMT IP: < This is the IP added to the *setup file for the mgmt interface >
Template: < This is the j2 template to use to parse YAML into >
--
Templates Created -- Success!