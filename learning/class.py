class person:
    name = "harry"
    occupation = "sod"
    networth = "1cr"
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a =person()
b=person()
print(a.name, a.occupation)

b.occupation ="tender"
b.name= "gaurav"

a.info()
b.info()