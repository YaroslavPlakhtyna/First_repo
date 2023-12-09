def show(name, age, gender="Male"): # gender ключовий параметр
    print(f"{name=}")
    print(f"{age=}")
    print(f"{gender=}")


show("20", "Bob", "Male") #позиційни аргумент 
show(age=30, name="Bill") #іменованні аргументи 