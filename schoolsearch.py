def student(lastname, isbus, file):
    for line in file: 
        linearr = line.split(",")
        if(linearr[0] == lastname):
            if (isbus == True):
                print(f"{linearr[0]},{linearr[1]},{linearr[4]}")
            else:
                print(f"{linearr[0]},{linearr[1]},{linearr[2]},{linearr[3]},{linearr[6]},{linearr[7]}")


    #search through text file, for each last name there that matches the given lastname
    #if bus is false: print the last name, first name, grade and classroom assignment for each student 
    #found and the name of their teacher (last and first name).
    #if bus is true then print out print the last name, first name and the bus route the student takes.

def teacher(lastname, file):
    # search for the data where the techers last name matches
    #For each entry found, print the last and the first name of the student.
    for line in file: 
        linearr = line.split(",")
        if(linearr[6] == lastname):
            print(f"{linearr[0]},{linearr[1]}")

# def grade(number, file):
#     #search for data where grades match
#     # output name (last and first) of the student
#     for line in file: 
#         linearr = line.split(",")
#         if(int(linearr[2]) == number):
#             print(f"{linearr[0]},{linearr[1]} \n")

def bus(number, file): #does not have title
    #serach for same bus number
    # output the name of the student (last and first) and their grade and classroom.
    for line in file: 
        linearr = line.split(",")
        if(linearr[4] == number):
            print(f"{linearr[0]},{linearr[1]},{linearr[2]},{linearr[3]}")

def grade(number, HL, file):
    #search for grade match
    #if L :  find the entry in the students.txt file
    #for the given grade with the lowest GPA. Report the contents of this entry (name of the
    #student, GPA, teacher, bus route).
    #if H: then its highest GPA
    maxval = 0
    minval = 100
    maxarr = []
    minarr = []
    for line in file:
        linearr = line.split(",")
        if( HL != "L" and HL != "H"):
            if(int(linearr[2]) == int(number)):
                print(f"{linearr[0]},{linearr[1]}")
            continue
        else:  
            #print(f"{linearr[2]} ---- {number} /// {type(linearr[2])} -----{type(number)}" ) 
            if(int(linearr[2]) == int(number)): 
                if (float(linearr[5]) > maxval):
                    maxval = float(linearr[5]) 
                    maxarr = linearr
                if (float(linearr[5])< minval):
                    minval = float(linearr[5])
                    minarr = linearr
    if (HL == "L"):
        print(f"{minarr[0]},{minarr[1]},{minarr[5]},{minarr[6]},{minarr[7]},{minarr[4]}")
    if (HL == "H"):
        print(f"{maxarr[0]},{maxarr[1]},{maxarr[5]},{maxarr[6]},{maxarr[7]},{maxarr[4]}")



def average(number, file):
    #find where grades match the number
    #Compute the average GPA score for the entries found. Output the grade level (the number
    #provided in command) and the average GPA score computed.
    totalstudents = 0.0
    totalgpa = 0.0
    for line in file: 
        linearr = line.split(",")
        if(int(linearr[2]) == number):
            totalstudents += 1.0
            totalgpa += float(linearr[5])
    if(totalstudents > 0):
        avg = totalgpa/totalstudents
        print(f"{number}, {round(avg,2)}\n")
    else:
        print("no one in grade provided")
    


def info(file):
    map = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for line in file: 
        linearr = line.split(",")
        if(int(linearr[2])<= 6):
            map[int(linearr[2])] += 1
    for key, value in map.items():
        print(f"{key}: {value}")
    #For each grade (from 0 to 6) compute the total number of students in that grade.
    #Report the number of students in each grade in the format
    #<Grade>: <Number of Students>
    #sorted in ascending order by grade. 
    
    
def main(): 
    while True:
        file = open('students.txt', 'r')
        search = input("Enter a search query ('Q' to quit): ").strip()
        if search == 'Q':
            print("Exiting")
            break
        token = search.split(':')
        if len(token) != 2:
            print("Invalid Search Query")
            continue

        key = token[0].strip().upper()
        params = token[1].strip()
        if key == 'S':
            lastname = params.split()[0]
            if 'B' in params.upper():
                student(lastname.upper(), True, file)
            else:
                student(lastname.upper(), False, file)
        elif key == 'T':
            lastname = params.upper()
            teacher(lastname, file)
        elif key == 'B':
            number = params
            bus(number, file)
        elif key == 'G':
            number = params.split()[0]
            if 'H' in params.upper():
                grade(number, "H", file)                
            elif 'L' in params.upper():
                grade(number, "L", file)
            else:
                number = int(params)
                grade(number, 0, file)
        elif key == 'A':
            number = int(params)
            average(number, file)
        elif key == 'I':  
            info(file) 
        else:
            print("Command not Found")
        file.close()


if __name__ == "__main__":
  main()
