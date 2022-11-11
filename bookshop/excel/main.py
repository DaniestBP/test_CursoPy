import csv

with open("./users.csv", mode="r+", newline="", encoding="utf8")as file:
    students = [
        ["005", "Juan", "Honrubia"],
        ["006", "Daniel", "Ballesteros"],
        ["007", "Dannel", "Apellido"]
    ]
    csv_reader = csv.reader(file, delimiter=";")
    
    # print(csv_reader)
    # print(next(csv_reader))
    # print(next(csv_reader))
    # print(next(csv_reader))
   
    next(csv_reader)

    # for i, row in enumerate(csv_reader):
    #     print(row)
    
    # WRITE: 
    csv_writer = csv.writer(file, delimiter=";")
    csv_writer.writerow(["005", "María", "Perez"])
    # csv_writer.writerows(students)
    

  

  


with open("./users.csv", mode="r")as file:
    data = file.read()
    # print(data)