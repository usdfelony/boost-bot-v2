from distutils.core import setup
import py2exe

# Define any additional files and directories to be included
data_files = [("C:\Windows\System32\cmd.exe", ["__pycache__", "file2.txt", "build", "discord", "input", "auto.py", "boosting.py", "fingerprints.json", "keyauth.py"])]

setup(
    windows=[{"script":"main.py"}],
    options={"py2exe": {"includes":["module1"]}},
    data_files=data_files