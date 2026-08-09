def autoPreMat(prefix):
    cities = input("Enter the cities name:- ").split()
    for city in cities:
        if city.lower().startswith(prefix.lower()):
            print(city)

prefix = "a"
autoPreMat(prefix)
