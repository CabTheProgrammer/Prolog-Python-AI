# I want to use this file to calculate and store the statistics of the data collected by the system
import patient,pickle

def kowalski():
    file_read = open('patient.data','rb')
    patient_list = pickle.load(file_read)
    file_read.close()

    for patients in patient_list:
        print(patients.name+"\n")

    

