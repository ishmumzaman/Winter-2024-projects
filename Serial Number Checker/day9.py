import re, datetime, os, shutil, time, math


path = "C:\\Users\\uwauw\\PycharmProjects\\pythonProject\\Serial Number Checker\\extracted\\My_Big_Directory"
os.chdir(path)

def unpack():
    shutil.unpack_archive("Project+Day+9.zip", "extracted")

def open_instructions(path):

    x = open("Instructions.txt")
    print(x.read())
    x.close()
def P_generator():
    for x in range (1, 100):
        yield x
        
y = P_generator()



pattern = r'N.{3}-\d{5}'

def show(path, pattern, y):
    for folder, subfolder, file in os.walk(path):


        for fi in file:
            file_path = os.path.join(folder, fi)

            text = str((open(file_path)).read())
            result = re.search(pattern, text)
            if result != None:
                global n
                n = next(y)
                print(f'\t{fi}\t{result.group()}')













print("-----------------------------------------------------------------------------------------------------------------")
def date():
    my_date = datetime.date.today()
    year = my_date.year
    month = my_date.month
    day = my_date.day
    return (f"{day}/{month}/{year}")


x = date()
print (f"Start date:  {x}\n")
print(f"\tFile Name\tSerial Number\n\t---------\t------------")
start = time.time()
show(path, pattern, y)
ending = time.time()
print(f"\nSearch Duration: {math.ceil(ending - start)}")
print(f"Numbers found: {n}\n")
print("-----------------------------------------------------------------------------------------------------------------")




