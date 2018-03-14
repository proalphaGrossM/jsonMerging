import json, os

# define the file names for the json files to read here
# the first file must be the one with all keys because
# the script iterates over them and searches for the
# one with the same key in the second json file
filename1 = "myFileOne.json"
filename2 = "myFileTwo.json"
resultFilename = "result.json"

# define the key name by which the json should be merged
# it may mostly be the same name in each json
mergeKeyName1 = "cInstanzName"
mergeKeyName2 = "cInstanzName"

logFilename = "log.txt" 

# creates log file
log = open(logFilename, 'w')

# Open the 2 json files and read its json
instanzKatalogJson = json.load(open(filename1))
objektInhaltJson = json.load(open(filename2))

log.write("JSON files read successfully\n")

for item in instanzKatalogJson["objektNameOne"]:
	for item2 in objektInhaltJson["objektName2"]:  
		if item[mergeKeyName1] == item2[mergeKeyName2]:
			log.write("combining " + item[mergeKeyName1] +"\n")
			item.update(item2)

f = open(resultFilename, 'w')
json.dump(instanzKatalogJson, f)
f.close()
log.close()
