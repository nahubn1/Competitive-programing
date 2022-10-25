def gradingStudents(grades):
    updated = []
    for grade in grades:
        if grade < 38:
            updated.append(grade)
        else:
            rem = grade % 5
            if rem >= 3:
                updated.append(grade + (5-rem))
            else:
                updated.append(grade)
