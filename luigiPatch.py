import subprocess
import shutil
import os
import re
import sys

luigiPath = list(filter(lambda x: re.search("site-packages$",x), sys.path))[0] + "\\luigi\\"
shutil.copyfile(os.getcwd() + "\\patch\\one.patch", luigiPath + "one.patch")
subprocess.call("cd {} & git init & git add 1.txt & git apply one.patch".format(luigiPath), shell=True)