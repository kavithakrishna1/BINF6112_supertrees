#input: config file 
#output: a file containing a dictionary: {cat: [cat_1, cat_2], dog: [dog_1, dog_2]...}
import sys 
# create an empty dictionary 
if len(sys.argv) != 2:
  print("only one config file allowed")
else:  
  user_input = sys.argv[1]
  config_dict = {}
  with open(user_input, "r") as config:
    for line in config:
      if (line != '\n'):
        clean = line.rstrip()
        name = line.split('.')
        split_name = name[0].split('_')
        species_name = split_name[0]
        if species_name in config_dict: 
          config_dict[species_name].append(clean)
        else:
          config_dict[species_name] = []
          config_dict[species_name].append(clean)
  
  #output to file    
  with open("abyss.config", "w") as outfile: 
    outfile.write(str(config_dict))


    
     
  

