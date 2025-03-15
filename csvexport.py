import csv
#output to csv
def csv_output(output_text):
    with open("cabot_trail_output.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(output_text)
        
def csv_array_appender(imageName,yesNo,error,array):
    error = error*100
    errorPercentage = str(error)+ "%"
    array.append([imageName,yesNo,errorPercentage])