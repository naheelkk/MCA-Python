#------------------------------------------------------------------------------------------#
# a dict to repr. det. of a stud.(name,rollno.,reg.no., dep., sem., )                             |
# add new element total mark                                                                |
# based on total mark find grade of student                                                 |
# total mark >= 90 -A                                                                       |
# total mark >= 82 -B                                                                       |
# total mark >= 75 -C                                                                       |
# total mark >= 60 -D                                                                       |
# total mark >= 50 -P                                                                       |
# Delete Roll NO.                                                                           |
#-------------------------------------------------------------------------------------------#

Bibi = {
    "name" : "Bibi",
    "roll.no" : "18",
    "reg.no" : "20150",
    "Department" : "History",
    "Semester" : 8,   
}
marks = []
subjects = 6
Bibi.update({"total_mark" : 76})
print(Bibi)
def calculateGrade(total_mark):
    if total_mark >= 90:
        return 'A'
    elif total_mark >= 82:
        return 'B'
    elif total_mark >= 75:
        return 'C'
    elif total_mark >= 60:
        return 'D' 
    elif total_mark >= 50:
        return 'P'
    
Bibi['grade'] = calculateGrade(Bibi['total_mark'])
print(Bibi)
print('After Deleting')
del Bibi["roll.no"]
print(Bibi)
