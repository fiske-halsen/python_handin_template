import utils as u

#Method 1
u.get_file_names("/home/jovyan/python_handin_template")

#Method 2
u.get_all_file_names("/home/jovyan/python_handin_template/week_2_folder")

#Method 3
list_file_names = ['text.txt', 'history.csv', 'index.html']
u.print_line_one(list_file_names)

#Method 4
list_file_names_emails = ['text.txt', 'history.csv', 'index.html', 'index@html.com']
u.print_emails(list_file_names_emails)

#Method 5
md_list = ['read.md']
u.write_headlines(md_list)