import pandas as pd
x = "hello"
y = "bye"
z = "shalom"

thisdict = {
  x: "Ford",
  y: "Mustang",
  z: 1964
}
thisdict["year"] = 2018, 1020

df = pd.DataFrame(thisdict)

print(thisdict)
print(df)

jobs = {
    'Job Name': [],
    'Link' : [],
    'Start date' : []
}

list=[]
for x in range(0,10):
    list.append(x)
print(list)

jobs['Job Name']=list
jobs['Link']="Apprentice"
jobs['Start date']="Apprentice"

df = pd.DataFrame(jobs)
print(df)
