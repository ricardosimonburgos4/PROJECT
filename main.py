import matplotlib.pyplot as ply

file = open("MenSalary.csv", "w")
file.write("Men, Women")
file.close()

file = open("top5MensSalary.csv", "r")
gender = file.read()
file.close()

genders = gender.split(",")


file = open("WomenSalary.csv", "w")
file.write("7.4, 1.2")
file.close()

file = open("WomenSalary.csv", "r")
millions = file.read()
file.close()


million = millions.split(",")
million = [float(item) for item in million] 

colors = ['orange', 'green']
ply.bar(genders, million, color = colors) 
ply.title("HOW MUCH DO THE HIGHEST PAID MALE AND FEMALE TENNIS PLAYERS EARN?")
ply.xlabel("GENDER")
ply.ylabel("MILLIONS")
ply.show()