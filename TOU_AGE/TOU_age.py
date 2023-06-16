import csv

data_list = []

# Open the CSV file for reading
with open('TOU_age.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    
    # Iterate over each row in the CSV file
    for row in reader:
        # Append the row as a list to the data_list
        data_list.append(row)

#data_list = list(zip(*data_list))

    new_data_list = []
    new_data_list.append(['YEAR','AGE','NUM'])
    # Iterate over the data_list and sum corresponding elements
    for i in range(12, len(data_list) ):
        
        new_row = []
        column = ['BELOW20', '20-24', '25-29', '30-34', '35-39', '40-44', 'ABOVE45']

        for j in range(3, 16, 2):
            new_row.append(data_list[i][0])
            sum_value = int(data_list[i][j]) + int(data_list[i][j+1])
            col=(j-3)//2
            new_row.append(column[col])
            new_row.append(sum_value)

            new_data_list.append(new_row)
            new_row=[]
        # writer.writerow([column[k], *new_data_list[k]])
        # k += 1
with open('res_TOU_age.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for row in new_data_list:
        writer.writerow(row)    
    #new_data_list = list(zip(*new_data_list))
    
    # Write the new_data_list to the CSV file
 
        
