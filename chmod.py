import glob
import stat
import os

for file_name in glob.iglob('catkin_ws/**/*.py', recursive=True):
    st = os.stat(file_name)
    os.chmod(file_name, st.st_mode | stat.S_IEXEC)