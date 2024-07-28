import os
from pathlib import Path
import logging

logging.basicConfig(filename='py_log.logs', filemode='a', level=logging.INFO, format='[%(asctime)s]:%(message)s')

lis_of_files=['src/__init__.py', 
              "src/run_local.py",
              "src/helper.py",
              "model/instruction.py",
              "requirements.txt",
              "setup.py",
              "main.py",
              "research/trails.py"]
#creating above list of files

for filepath in lis_of_files:
    filepath=Path(filepath)
    filedir, filename=os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory;{filedir} for the file :{filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else :
        logging.info(f"{filename} is already exist")
