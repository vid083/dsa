key_location = "chair"
locations = ["window", "chair", "closet", "living"]

for i in locations:
    if i==key_location:
      print("key is found in ", i)
      break
    else:
      print("key is not found in ", i)