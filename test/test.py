# -*- coding: utf-8 -*-
# from : https://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path
import imp
import os
import sys
PWD = os.path.dirname(os.path.abspath(__file__));
#print()
#sys.exit(1)
php = imp.load_source('module', PWD+"\\..\\php.py")
my = php.kit()

reload(sys)
sys.setdefaultencoding('utf-8')
my.echo(my.pwd())
my.echo("\n")
fp = my.pwd()+"\\test.py"
my.echo(my.is_file(fp))
my.echo("\n")
my.echo(my.dirname(fp))
my.echo("\n")
my.echo(my.basename(fp))
my.echo("\n")
my.echo(my.mainname(fp))
my.echo("\n")
my.echo(my.subname(fp))
my.echo("\n")