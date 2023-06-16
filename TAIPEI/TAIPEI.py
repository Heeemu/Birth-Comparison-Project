import csv

data_list = []
new_data_list = []
birth = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
age_range = ['SUM','BELOW15','15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49','ABOVE50']
year = ['108', '109', '110']
academic = ['TOTAL', 'PHD', 'MASTER', 'BACHELOR', 'DIPLOMA', 'SENIOR', 'JUNIOR', 'ELEMENTARY']

# Open the CSV file for reading
with open('taipei.csv', 'r', encoding='Big5') as file:
    reader = csv.reader(file)
    next(reader)
    # Iterate over each row in the CSV file
    for row in reader:
        # Append the row as a list to the data_list
        data_list.append(row)
   
    aca=0 
    count=0
    for i in range(len(data_list)):
        
        # if((i+7)%10 == 9):
        if(i%10==0):
             
            continue
            
        for j in range(4, len(data_list[0])):
            new_row = []
            if data_list[i][0] == '108':
                new_row.append('108')
            elif data_list[i][0] == '109':
                new_row.append('109')
            else:
                new_row.append('110')

            # tmprange = (i + 8) % 10

            
            new_row.append(age_range[i%10])
            
            new_row.append(academic[aca])
            # if tmprange == 9:
                
            #     new_row=[]
                
            new_row.append(birth[j - 4])
            new_row.append(data_list[i][j])
            new_data_list.append(new_row)

        count+=1
        if(count>8):
            count=0
            aca=(aca+1)%8

with open('res_TAI.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for row in new_data_list:
        writer.writerow(row)
#         new_row = []
#         column =['below20','20-24','25-29','30-34','35-39','40-44','above45']
#         for j in range(len(row1)):
#             sum_value = int(row1[j]) + int(row2[j])
#             new_row.append(str(sum_value))
#         
#         new_data_list.append(new_row)
        
     




