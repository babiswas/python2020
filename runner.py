import glob
import os



     

python_files=glob.glob('*.py')



for file in python_files:
       os.system('python'+' '+file)
