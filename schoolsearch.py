


def student(lastname, isbus):
    file = open('file.txt', 'r')
    for line in file: 
        line.split(",")
        
    #search through text file, for each last name there that matches the given lastname
    #if bus is false: print the last name, first name, grade and classroom assignment for each student 
    #found and the name of their teacher (last and first name).
    #if bus is true then print out print the last name, first name and the bus route the student takes.

def teacher(lastname):
    # search for the data where the techers last name matches
    #For each entry found, print the last and the first name of the student.

def grade(number):
    #search for data where grades match
    # output name (last and first) of the student

def bus(number):
    #serach for same bus number
    # output the name of the student (last and first) and their grade and classroom.

def grade(number, HL):
    #search for grade match
    #if L :  find the entry in the students.txt file
    #for the given grade with the lowest GPA. Report the contents of this entry (name of the
    #student, GPA, teacher, bus route).
    #if H: then its highest GPA

def average(number):
    #find where grades match the number
    #Compute the average GPA score for the entries found. Output the grade level (the number
    #provided in command) and the average GPA score computed.

def info():
    #For each grade (from 0 to 6) compute the total number of students in that grade.
    #Report the number of students in each grade in the format
    #<Grade>: <Number of Students>
    #sorted in ascending order by grade.
    
    
# Geneva Laurain


def main():
    file = open('students.txt', 'r')
    while True:
        search = input("Enter a search query: ").strip()
        if search == 'Q':
            print("Exiting")
            break
        token = search.split(':')
        if len(token) != 2:
            print("Invalid Search Query")
            continue
        
        key = token[0].upper()
        params = token[1].strip()
        if key == 'S':
            lastname = params.split()[0]
            if 'B' in params.upper():
                student(lastname, True, file)
            else:
                student(lastname, False, file)
        elif key == 'T':
            lastname = params
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
                grade(number, 0, file)
        elif key == 'A':
            number = int(params)
            average(number, file)
        elif key == 'I':  
            info(file) 
        else:
            print("Command not Found")
                 
    
if __name__ == "__main__":
    main()

