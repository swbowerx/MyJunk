#!/usr/bin/python
#######################################################################################################################
# Written for python 2.7, cento natively supports 2.7 not 3.x
# This module folows the PEP8 standards.
# There are 2 configuration files that accompany this script, they are for the logging and config and are in same dir.
# Description: This is the template module for automation and test.
# TODO: work out statndard header and attribuits and comments for def functions.
__all__ = ['a', 'b', 'c']
__version__ = '0.1'
__author__ = 'Foo Bar'



# template imports, import what you need and delete this comment
import platform
import subprocess
import re
import os
import fnmatch
import glob
import argparse
from argparse import RawDescriptionHelpFormatter
import logging.config
import ConfigParser

# TODO: make this a class with example file that calls and functions and inherites attribuites from this file.
# class MyTemplateClass:


# TODO: create standard comments for def functions.
def main(prog_args, logger, config):
    status = True
    config.sections()

    logger.info("You are running %s, %s.", platform.dist()[0], platform.dist()[1])
    template_config_call = config.get("General", "myvar")
    
    if not template_check(prog_args, logger, config):
        status = False

    if not status:
        exit(1)

def proxy_check(prog_args, logger, config):
    try:
        logger.info("PASS: tried and passed")
    except Exception as e:
        status = False

    return status

def shellcmd(cmd):
    status = subprocess.call(cmd, shell=True)
    return status




#######################################################################################################################
# description: main, function called if class file is used directly.
# comments: use arguments to do these things..
#

if __name__ == '__main__':
    # Setup the logger
    # TODO: refine the logging file.
    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger('base_logger')

    # Add args here. This is the help and this file must be self documenting so the help needs to explain
    # to the user how to use this file and give example calls that show how one might want to use the args.
    description = 'syssetup uses the syssetup.cfg to check the xtensa and project setup.\n' \
                  'usage: python syssetup\n' \
                  'This script defaults to info only and will not make changes unless an option is specified\n' \
                  'To make changes to some files using options like"-i" you may need to run the script as root.\n' \
                  'sudo python syssetup # by default only reports back, but does not change the system at all.\n' \
                  'sudo python syssetup -p # does default and sets up the proxy for you if possible. \n'

    parser = argparse.ArgumentParser(description=description,
                                     add_help=True,
                                     formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('-i', '--install_all', action='store_true', default=False, dest='install_all', help='Install everything if possible and notify of steps unacomplished.')
    parser.add_argument('-p', '--proxy_all', action='store_true', default=False, dest='proxy_all', help='Check the users proxy setup.')
    parser.add_argument('-b', '--bashrc_check', action='store_true', default=False, dest='bashrc_check', help='Legacy: See if a users bashrc has the evn and proxy setups.')
    myargs = parser.parse_args()

    # Setup config from file.
    config = ConfigParser.ConfigParser()
    try:
        config.read('template.cfg')
        logger.info("Start System Check: %s\n" % config.get("General", "thisversion"))
    except Exception as e:
        logger.error(e.message)
        logger.error("SCRIPT ERROR: could not read the syssetup.cfg file. please make sure it exists in the same path as this file. \n EXITING.")
        exit(1)

    main(myargs, logger, config)


