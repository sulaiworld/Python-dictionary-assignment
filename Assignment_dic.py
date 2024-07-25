#Create a dictionary that contains basic bio info with must have property of skills which is list of skills
#Loop through the bio dict and print key and values to stdout, make skills  an heading and print skils out too
bio_skills = {"Name": "Sulaimon", "Age": 36, "skills": ["Design", "Engineering", "Consulting", "Project management"]}
for keys, values, in bio_skills.items():
  if keys == "Name" or keys == "Age":
     print(f"My {keys} is {values}")
  else:
       print(f"My {keys} are :")
       for val in values:
          print(f"{val}")
