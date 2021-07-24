import glob
import stat
import os

file_type = "py"

for file_name in glob.iglob(f'catkin_ws/**/*.{file_type}', recursive=True):
    st = os.stat(file_name)
    os.chmod(file_name, st.st_mode | stat.S_IEXEC)