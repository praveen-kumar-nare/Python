
import datetime 


filename = datetime.datetime.now() 

 
def create_file(): 
	
	with open(filename.strftime("%d %B %Y")+".txt", "w") as file: 
		file.write("") 


create_file() 
