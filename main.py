import pandas as pd
def main():

    c_type = int(input("Enter the c** type you're interested in:\n"+
                        "1 - Phase\n2 - Digital Input\n3 - Digital Output\n"+
                        "4 - Analog Input\n5 - Analog Output\n\nEnter Here: "))
    if c_type == 1:
        c_type = "PHZ"
    elif c_type == 2:
        c_type = "DI"
    elif c_type == 3:
        c_type = "DO"
    elif c_type == 4:
        c_type = "AI"
    elif c_type == 5:
        c_type = "AO"
    
    
    file_name = input("Enter the filename: ")

    before_keyword = input("Enter the before and after keywords. Example for a duplication mixer11 to mixer 31, befre keyword would be 11 and after keyword would be 31.\n\nBefore Keyword: ")
    after_keyword = input("After Keyword: ")

    # read in the table
    df = pd.read_excel(file_name)

    # get the headers should be name of input which should have 
    header = df.columns.values.tolist()[3:]
    print(df.mode(axis='rows',numeric_only=True).values.tolist())
    modes = df.mode(axis='rows',numeric_only=True).values.tolist()[0][1:]
    names_to_not_change = []
    names_to_change = []
    for index,row in df.iterrows():
        c_name = row['Name']
        if after_keyword in c_name and c_type in row['Base Tags']:
            names_to_change.append(c_name)
        elif c_type in row['Base Tags']:

            names_to_not_change.append(c_name)
    # load in local_size for loop
    local_size = 'MOV('+ str(len(names_to_change)-1) + ',local_size);'

    # load in array indexes
    array_indexes = ''
    local_index = 0
    for index, row in df.iterrows():
        if row['Name'] in names_to_change:
            array_index = row['Base Tags'].split("[")[1][:-1]
            array_indexes += 'MOV(' + array_index + ',local_c'+c_type+'[' + str(local_index) + '])'
            local_index+=1

    array_indexes+=';'

    # initialize loop
    loop = "MOV(-1,index_local);LBL(LOOP)ADD(index_local,1,index_local)MOV(local_c"+c_type+"[index_local],index_C);"
    

    # initialize values
    initialize_values = ''
    for column_name, mode in zip(header,modes):
        initialize_values += 'MOV(' + str(int(mode)) + ',c'+c_type+'[index_C].' + column_name + ')'
    initialize_values +=';'

    # get odd_values
    odd_values = ''
    for index, row in df.iterrows():
        if row['Name'] in names_to_not_change:
            if index >= len(names_to_not_change):
                tmp = 'EQU(' + df.iloc[index-len(names_to_not_change)]['Base Tags'].split("[")[1][:-1] + ',index_C)'
            else:
                tmp = 'EQU(' + df.iloc[index+len(names_to_not_change)]['Base Tags'].split("[")[1][:-1] + ',index_C)'
            for i,x in enumerate(row[3:]):
                if x != modes[i]:
                    tmp+='MOV(' + str(int(x)) +',c'+c_type+'[index_C].' + header[i] + ')'
            tmp += ';'
            if 'MOV' in tmp:
                odd_values+=tmp

    # end loop
    end_loop = 'LES(index_local,local_size)JMP(LOOP);'
    print(local_size,array_indexes,loop,initialize_values,odd_values,end_loop)    
if __name__ == "__main__":
    main()
