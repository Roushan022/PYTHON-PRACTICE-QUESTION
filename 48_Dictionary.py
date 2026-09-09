students={
    "Priya":[("Math",87),("English",78),("Science",99)],
    "Roushan":[("Math",98),("English",91),("Science",100)],
    "Ganashree":[("Math",88),("English",82),("Science",85)],
    "Smita":[("Math",78),("English",89),("Science",72)],
    "Rahul":[("Math",45),("English",75),("Science",88)],
}
for name,subjects in students.items():
    print("Student Name",name)
    total=0
    for subject,marks in subjects:
        print(f"{subject}:{marks}")
        total+=marks
        per=total/len(subjects)
        print("Total marks-",total)
        print("Percentage ",round(per,2))
    print("           --------         ")
