import os
import csv
def get_file_names(folderpath,out='output.txt'):
    entries = os.listdir(folderpath)
    with open(out, 'w') as file:
        for entry in entries:
            file.write(entry + ", ")
            
        
#get_file_names("/home/jovyan/python_handin_template")



def get_all_file_names(folderpath,out='output.txt'):
    str = " "
    with open(out, 'w') as file:
        for root,d_names,f_names in os.walk(folderpath):
            for name in f_names:
                file.write(name + "\n")
                
   

get_all_file_names("/home/jovyan/python_handin_template/week_2_folder")


def print_line_one(file_names):
    for file_name in file_names:
        print(file_name.rsplit('.')[0])


#list_file_names = ['text.txt', 'history.csv', 'index.html']
#print_line_one(list_file_names)


def print_emails(file_names):
    for file_name in file_names:
        if "@" in file_name:
            print(file_name)


#list_file_names_emails = ['text.txt', 'history.csv', 'index.html', 'index@html.com']
#print_emails(list_file_names_emails)

def write_headlines(md_files, out='output.txt'):
    with open(out, 'w') as file:
        for md_file in md_files:
            with open(md_file) as file_obj:
                lines = file_obj.readlines()
                for line in lines:
                    if line.startswith("#"):
                        file.write(line)




#write_headlines(md_list)