

def student(lastname, isbus, file):
    for line in file: 
        linearr = line.split(",")
        if(linearr[0] == lastname):
            if (isbus == True):
                print(f"{linearr[0]} {linearr[1]} {linearr[4]}\n")
            else:
                print(f"{linearr[0]} {linearr[1]} {linearr[2]} {linearr[3]}\n")


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
            print(f"{linearr[0]} {linearr[1]} \n")

def grade(number, file):
    #search for data where grades match
    # output name (last and first) of the student
    for line in file: 
        linearr = line.split(",")
        if(linearr[2] == number):
            print(f"{linearr[0]} {linearr[1]} \n")

def bus(number, file):
    #serach for same bus number
    # output the name of the student (last and first) and their grade and classroom.
    for line in file: 
        linearr = line.split(",")
        if(linearr[4] == number):
            print(f"{linearr[0]} {linearr[1]} {linearr[2]} \n")

def grade(number, HL, file):
    #search for grade match
    #if L :  find the entry in the students.txt file
    #for the given grade with the lowest GPA. Report the contents of this entry (name of the
    #student, GPA, teacher, bus route).
    #if H: then its highest GPA
    maxval = 0;
    minval = 100;
    maxarr = []
    minarr = []
    for line in file:
        linearr = line.split(",")
 
        if( HL != "L" or HL != "H"):
            if(linearr[2] == number):
                print(f"{maxarr[0]} {maxarr[1]}")
        else:    
            if(linearr[2] == number):
                if (linearr[5] > maxval):
                    maxval = linearr[5]
                    maxarr = linearr
                if (linearr[5]< minval):
                    minval = linearr[5]
                    minarr = linearr
            if (HL == "L"):
                print(f"{minarr[0]} {minarr[1]} {minarr[5]}, {minarr[6]} {minarr[7]} {minarr[4]}")
            if (HL == "H"):
                print(f"{maxarr[0]} {maxarr[1]} {maxarr[5]}, {maxarr[6]} {maxarr[7]} {maxarr[4]}")


def average(number):
    #find where grades match the number
    #Compute the average GPA score for the entries found. Output the grade level (the number
    #provided in command) and the average GPA score computed.

def info():
    #For each grade (from 0 to 6) compute the total number of students in that grade.
    #Report the number of students in each grade in the format
    #<Grade>: <Number of Students>
    #sorted in ascending order by grade.