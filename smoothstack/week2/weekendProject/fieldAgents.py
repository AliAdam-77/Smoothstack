import os
import sys
import pandas as pd
import numpy as np
import logging
import csv
import phonenumbers
import us
from email_validator import validate_email
import yagmail
import matplotlib.pyplot as plt
import datetime

os.chdir(os.path.dirname(__file__))
logging.basicConfig(filename ='logFile.log',filemode = "w",format="%(asctime)s:%(levelname)s:%(message)s",level= logging.INFO)


def get_processing_file(files):
    logging.info("Extracting the file that needs to be processed")
    files = check_format(files)
    if len(files) == 0:
        logging.error("NO CSV files in the correct format")
        return None

    f1 = max(files)
    files.remove(f1)
    f2 = max(files)
    
    f = check_2_recent_files(f1,f2)
    
    return f 





def check_format(files):
    logging.info("Checking the format")
    if len(files) == 0:
        logging.error("No CSV files in the current dir")
        return list()
    
    for f in files:
        if f[:15] != "NYL_FieldAgent_" and f[15:-4].isdigit() == False:
            files.remove(f)

    return files








def check_2_recent_files(f1,f2):
    logging.info("checking the two recent files")
    try:
        file1 = open(f1)
    except:
        logging.exception("File didnt open correctly")
        return None
    else:
        reader = csv.reader(file1)
        l1= len(list(reader))
        file1.close()


    try:
        file2 = open(f2)
    except:
        logging.exception("File didnt open correctly")
        return None
    else:
        reader = csv.reader(file2)
        l2= len(list(reader))
        file2.close()
    
    diff = l1 - l2
    if diff > 500 or diff < -500:
        logging.exception("The difference is more than 500 lines")
        return None
    else:
        return f1






def addFile(f):
    logging.info("Adding the file name")
    try:
        ref = open("NYL_lst.txt","a+")
    except:
        logging.exception("Reference File does not exist")
    else:
        ref.write(f+"\n")
        logging.info("File name was added to the refrence file")
        ref.close()

def Check_refrence_file(f):
    logging.info("checking if the file is in the refrence file")
    try:
        ref = open("NYL_lst.txt","r+")
    except:
        logging.exception("Reference File does not exist")
        return True
    else:
        data = ref.readlines()
        for i in data:
            if i == f+"\n":
                logging.info("The file has been processed already")
                return False
        return True



def sendEmail():
    logging.info("Sending an email")

    receiver = "adamx083@gmail.com"
    body = "This is the log file"
    filename = "logFile.log"

    yag = yagmail.SMTP("adamx083@gmail.com")
    yag.send(
        to=receiver,
        subject="Log File",
        contents=body, 
        attachments=filename,
    )

def processing(f):

    logging.info("Processing the file = %s"%f)
    df = pd.read_csv(f)
    headers = set(df)
    df = change_headers(df,headers)
    
    check_state( df['Agency State'].dropna())
    check_state( df['Agent State'].dropna())
    
    check_phonenumbers( df["Agency Phone Number"].dropna())
    check_phonenumbers( df["Agent Phone Number"].dropna()) 
    
   
    email_col = df['Agent Email Address'].dropna()
    check_email(email_col)
    visualizing(df)
    addFile(f)
    




def change_headers(df,headers):
    if 'Agent Writing Contract Start Date (Carrier appointment start date)' in headers:
        logging.info("Changing column name")
        df.rename(columns={'Agent Writing Contract Start Date (Carrier appointment start date)':'Agent Writing Contract Start Date'},inplace = True)

    if 'Agent Writing Contract Status (actually active and cancelled\'s should come in two different files)' in headers:
        df.rename(columns={'Agent Writing Contract Status (actually active and cancelled\'s should come in two different files)':'Agent Writing Contract Status'},inplace = True)
        logging.info("Changing the column name")
    return df


def check_phonenumbers(phone_col):
    logging.info("Checking for invalid Phone Numbers")
    for pn in phone_col:
        pn = pn.replace(".","")
        if pn.isdigit() == False or len(pn) < 2:
            #missing data
            #logging.error("Missing phone number: %s: " %pn)
            continue         
        else:
            y = phonenumbers.parse(pn, "US")
            if phonenumbers.is_possible_number(y) == False:
                #invalid number
                logging.error("Invalid phone number: %s: " %pn)



def check_state(state_col):
    logging.info("Checking for invalid State Name")
    for st in state_col:
        if us.states.lookup(st) == None:
            #invalid State
            logging.error("Invalid state name: %s " %st)
    return

def check_email(email_col):
    logging.info("Checking for invalid Email Address")
    for e in email_col:
        try:
            validate_email(e)
        except:
            #invalid Email
            logging.exception("Invalid email: %s" %e)
    return


def getGraph(df):

    df10 = df[["Agency State","Agent Id"]].groupby("Agency State").agg("count")

    fig = plt.figure(figsize=(20, 3))
    state = list(df10.index)    #x axis 
    count = list(df10["Agent Id"].values) #y axis
    y = np.arange(0,47)
    ax = fig.add_axes([0,0,1,1])
    ax.bar(state,count,width = 0.3)
    ax.set_frame_on(True)
    ax.xaxis.set_ticks(y)
    ax.set_xlabel('States')
    ax.set_ylabel('Number of Agents')
    plt.savefig('graph1.png')
    logging.info("Graph 1 is saved")




def visualizing(df):
    df9 = df.transpose()
    logging.info("Data frame of the headers as index:")
    logging.info(df9)
    logging.info("------------------------------------")

    getGraph(df)

    df11 = df[['Agent Last Name','Agent Writing Contract Start Date','Date when an agent became A2O']]
    logging.info("Dataframe which gives the Agent Name , Agent Writing ContractStart Date , Date when an agent became A2O")
    logging.info(df11)
    logging.info("------------------------------------")
    
    
   
        
if __name__ == "__main__":

    
    files = filter(os.path.isfile, os.listdir( os.curdir ) )  # files only
    files = [ f for f in os.listdir( os.curdir ) if os.path.isfile(f) and f[-3:] == "csv"] #list comprehension version.
    
    f = get_processing_file(files)

    if f != None:
        if Check_refrence_file(f):#     # check if the file is been processed before 
            #(true = not been processed before)
            processing(f) #process the file
            #sendEmail()
        else:
            print("the file was processed before")
            #sendEmail()
            
        




    
    
    
    
    
    

    