import urllib.request

def instructors(department):
    stream = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/louslist/'+department)
    list_of_instructors = []
    for line in stream:
        text_line = line.decode('utf-8')
        no_newline = text_line.strip()
        row = no_newline.split('|')
        if '+' in row[4]:
            row[4] = row[4][:-2]
        if row[4] not in list_of_instructors:
            list_of_instructors.append(row[4])
        else:
            ...
    list_of_instructors.sort() # I got this idea from Erich Demaree on Piazza
    return list_of_instructors



def class_search(dept_name, has_seats_available=True, level=None, not_before=None, not_after=None):
    stream = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/louslist/' + dept_name)
    class_list = []
    for line in stream:
        good_class = True
        text_line = line.decode('utf-8')
        no_newline = text_line.strip()
        row = no_newline.split('|')
        if has_seats_available:
            if row[15] >= row[16]:
                good_class = False
        if level:
            if str(level)[0] != str(row[1])[0]:
                good_class = False
        if not_before:
            if int(not_before) > int(row[12]):
                good_class = False
        if not_after:
            if int(not_after) < int(row[12]):
                good_class = False
        if good_class == True:
            if row not in class_list:
                class_list.append(row)     # I got this idea from TA Caroline McNichols.
    return class_list



