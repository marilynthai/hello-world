import random
names = ["MARILYN THAI",  "CAMERON JOHNSON",  "SALLY BAYER",  "TASHUAN WILLIAMSON",  "DELILA ALANE"]

ids = []
for i in range(5):
  ids.append(random.randint(1111,9999))

emails = []
i = 0
for name in names:
  [first,last] = name.split(" ")
  emails.append(first[0]+last+str(ids[i])[-3:]+"@adadev.org")
  i += 1

accounts = []
for i in range(len(ids)):
  accounts.append(
    {"name": names[i],
    "id": ids[i],
    "email": emails[i]}
  )

print(accounts)
