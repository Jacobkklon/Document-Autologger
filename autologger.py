"""
Features:
1. Type in a txt file and have code watching it (running continuously). 
2. A specific exit indicator code should save the file and auto-open a new one.
3. Files should be saved into a logical folder structure with a specified name, taken from the first line of each file.
   Ex: jacob/klonsky/myfile.txt would save myfile.txt in folder klonsky within folder jacob (sitting at same level as the code)
   Part of this use is so that it is easily uploadable to google drive.
4. Additional feature: File Combining - specify the highest level folder and it will combine all the files, segmenting them by
   folder with headers.
   - This feature likely requires a separate txt file that is aware of the folder schema 

"""