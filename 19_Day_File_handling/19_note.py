# File handling
# open('filename', mode)
# mode(r, a, w, x, t,b)  could be to read, write, update

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

# example:
# a = open("sample.txt")
# f = a.read(100)
# print(f)
# a.close()

# readline(): read only the first line
# f_1 = a.readline()
# print(f_1)
# a.close()

# readlines(): read all the text line by line and returns a list of lines
# f_2 = a.readlines()
# print(f_2)
# a.close()

# splitlines(): Another way to get all the lines as a list:
# f_3 = a.read().splitlines()
# print(f_3)
# a.close()

# note After we open a file, 
# note we should close it. There is a high tendency of forgetting to close them. 
# note There is a new way of opening files using with - closes the files by itself.
# with open("sample.txt") as f:
#     lines = f.read().splitlines()
#     print(type(lines))
#     print(lines)

# f = open("sample.txt","a")
# f.write("This is a txt file")
# f.close()


# import os
# if os.path.exists("sample.txt"):
#     os.remove("sample.txt")
# else:
#     print("file not exist")
    
    
import json
# # note use three quotes to make it more readable
# person_json = '''{
#     "name": "Asabeneh",
#     "country": "Finland",
#     "city": "Helsinki",
#     "skills": ["JavaScrip", "React", "Python"]
# }'''

# person_dict = json.loads(person_json)
# print(person_dict)

# note use dumps method to make a dictionaty to a JSON
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
person_json = json.dumps(person,indent=4)
print(person_json)

print(dict(zip('abc', range(3))))

# note save to json file
with open('json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person,f,ensure_ascii=False,indent=4)
    
    
    
# note python deals with csv
import csv
with open('train.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')
    
    
# import xml.etree.ElementTree as ET
# tree = ET.parse('./files/xml_example.xml')
# root = tree.getroot()
# print('Root tag:', root.tag)
# print('Attribute:', root.attrib)
# for child in root:
#     print('field: ', child.tag)