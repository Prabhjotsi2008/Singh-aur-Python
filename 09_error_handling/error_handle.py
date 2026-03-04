file = open("youtube.txt","w")

# OLD-WAY # does the same 
try:
    file.write("ChaiAurCode")
finally:
    file.close()

#MODERN-WAY # close the file itself
with open("youtube.txt",'w') as file:
    file.write("Chai aur Python")