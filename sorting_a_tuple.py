def sorting_exam_marks(exam_marks):
    sorted_marks=sorted(exam_marks,key=lambda x:(x[1],x[0]))
    return sorted_marks


exam_marks=[("Sami",99),("Wali Ahmad",80),("Omar",90),("Sahel",98)]
sorting_exam_marks(exam_marks)
print(exam_marks)

