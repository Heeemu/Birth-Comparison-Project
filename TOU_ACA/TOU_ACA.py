import csv

def detect_characters(string):
    if len(string) >= 8:
        third = string[3]
        fourth = string[4]
        if third == '博':
            return [0, string[6]]
        elif third =='碩':
            return [1,string[6]]
        elif third =='大':
            return [2,string[6]]
        elif third =='專':
            return [3,string[6]]
        elif third =='高':
            return [4,string[6]]
        else:
            if fourth == '中':
                return [5, string[6]]
            elif string[5] == '以':
                return [6, string[8]]
            else:
                return [6, string[6]]
    else:
        return[0,'error']

data_list = []
new_data_list = []
new_data_list.append(['YEAR','ACADEMIC','BIRTH','NUM'])
academic = ['PHD', 'MASTER', 'BACHELOR', 'DIPLOMA', 'SENIOR', 'JUNIOR', 'ELEMENTARY']
with open('touage.csv', 'r', encoding='UTF-8-SIG') as file:
    reader = csv.reader(file)
    for row in reader:
        data_list.append(row)
    
    for i in range(1,len(data_list)):
        
        for j in range(2,len(data_list[0])):
            newrow=[]
            newrow.append(data_list[i][0]);#add year
           
            B = detect_characters(data_list[0][j])
            aca=B[0]
            birth= B[1]
            newrow.append(academic[aca])
            newrow.append(birth)
            newrow.append(data_list[i][j])
            new_data_list.append(newrow)
with open('res_touaca.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for row in new_data_list:
        writer.writerow(row)    


