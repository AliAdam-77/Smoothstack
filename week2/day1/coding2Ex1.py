import numpy as np
import os
import logging
os.chdir(os.path.dirname(__file__))
logging.basicConfig(filename="log_file.log",filemode="w",format="%(message)s",level=logging.INFO)


# Create an array of 10 zeros
arr2 = np.zeros(10)
logging.info("array of 10 zeros: ")
logging.info(arr2)
logging.info("-------------------------------------------------------")

# Create an array of 10 ones
arr3 = np.ones(10)
logging.info("array of 10 ones: ")
logging.info(arr3)
logging.info("-------------------------------------------------------")

# Create an array of 10 fives
arr4 = arr3 *5
logging.info("array of 10 fives: ")
logging.info(arr4)
logging.info("-------------------------------------------------------")

# Create an array of integers from 10 to 50
arr5 = np.arange(10,50)
logging.info("array of integers from 10 to 50: ")
logging.info(arr5)
logging.info("-------------------------------------------------------")

# Create an array of even integers from 10 to 50
arr6 = np.arange(10,50,2)
logging.info("array of even integers from 10 to 50: ")
logging.info(arr6)
logging.info("-------------------------------------------------------")

# Create a 3x3 matrix with values ranging from 0 to 8
arr7 = np.arange(0,9).reshape(3,3)
logging.info("array of 3x3 matrix with values ranging from 0 to 8: ")
logging.info(arr7)
logging.info("-------------------------------------------------------")

# Create a 3x3 identity matrix
arr8 = np.eye(3,3)
logging.info("array of 3x3 identity matrix: ")
logging.info(arr8)
logging.info("-------------------------------------------------------")

# Use numpy to randomly generate a number between 0 and 1
arr9 = np.random.rand(10)
logging.info("array of andomly generate a number between 0 and 1: ")
logging.info(arr9)
logging.info("-------------------------------------------------------")
