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
          elif params.upper() not in ('H', 'L', ''):
            print("Invalid Input.")
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
