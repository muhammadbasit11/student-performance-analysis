import pandas as pd
#getting data from a csv file
df=pd.read_csv("Student_performance_data _.csv")
#phase 1
#total students
total_students=df["StudentID"].count()
print(f"THE TOTAL NUMBER OF STUDENTS ARE {total_students}")
#average_cgpa 
average_cgpa=df["GPA"].mean()
print(f"THE AVERAGE CGPA OF STUDENTS IS {average_cgpa}")
# RANGE OF GPA
maximum_gpa=df["GPA"].max()
minimum_gpa=df["GPA"].min()
print(f"THE GPA RANGE FROM {minimum_gpa} to {maximum_gpa}")
 
 #finding grade which is common
common_grade=df["GradeClass"].mode()[0]
print(f"THE MOST COMMON GRADE CLASS IS {common_grade}") 

# 🟢 PHASE 2 — Academic Performance Analysis

# 1️⃣ Average GPA by Gender
genders={0:"male",1:"female"}
df["Gender"]=df["Gender"].map(genders)
gender_wise_gpa=df.groupby("Gender")["GPA"].mean()
print(f"THE GENDER WISE GPA IS {gender_wise_gpa}")

# 1️⃣ Average GPA by Gender
gender_wise_gpa=df.groupby("Gender")["GPA"].mean()
print(f"THE GENDER WISE GPA IS {gender_wise_gpa}")
# Do males or females have higher GPA?
print(f"\nTHE MAXIMUM GPA GENDER IS {gender_wise_gpa.idxmax()}") 

# 2️⃣ GPA by Study Time
# Group students into categories:
# Low study time
# Medium
# High
df.loc[df["StudyTimeWeekly"]<=5,"Studentcategory"]="LOW"
df.loc[(df["StudyTimeWeekly"]>5) & (df["StudyTimeWeekly"]<=15),"Studentcategory"]="MEDIUM"
df.loc[(df["StudyTimeWeekly"]>15),"Studentcategory"]="HIGH"
# --Question:
# Does more study time increase GPA?
student_category_gpa=df.groupby("Studentcategory")["GPA"].mean()
print(f"THE GPA OF THE STUDENTS DEPENDING UPON THE TIME THEY STUDIED LIES\n{student_category_gpa}")

# Correlation between GPA and Absences
corr=df["GPA"].corr(df["Absences"])
if corr<-0.6:
    print("THE GPA IS STRONGLY DECREASING WITH ABSENCES")
elif corr<0:
    print("THE GPA IS MODERATELY DECREASING WITH ABSENCES")
else:
    print("THE GPA IS NOT DECREASING WITH ABSENCES") 
# Compare students with high absences vs low absences 
stu_absence_Cat=["LOW","MEDIUM","HIGH"]
df.loc[df["Absences"]<=4,"AbsenceCategory"]="LOW"
df.loc[(df["Absences"]>4) & (df["Absences"]<=15),"AbsenceCategory"]="MEDIUM"
df.loc[df["Absences"]>15,"AbsenceCategory"]="HIGH"
absence_gpa=df.groupby("AbsenceCategory")["GPA"].mean()
# Do absences reduce GPA?  
diff_gpa=(absence_gpa["HIGH"]) -(absence_gpa["LOW"]) 
print(f"THE GPA OF STUDENTS WHO HAS MORE ABSENCES VS THOSE WHO DON'T HAVE MUCH IS {abs(diff_gpa):.2f}")


# 🟢 PHASE 3 — Influence of Activities

# GPA of students who do Sports vs not
sport_status={0:"playing",1:"not playing"}
df["Sports"]=df["Sports"].map(sport_status)
sporting_stu_gpa=df.groupby('Sports')["GPA"].mean()
print(f"THE GPA OF STUDENTS PLAYING IS {sporting_stu_gpa['playing']} AND STUDENT WHO DON'T PLAY HAS {sporting_stu_gpa['not playing']}")
# GPA of students who do Music vs not
music_status={1:"YES",0:"NO"}
df["Music"]=df["Music"].map(music_status)
music_stu_gpa=df.groupby("Music")["GPA"].mean()
print(f"THE STUDENTS WHO PARTICIPATE IN MUSIC HAS GPA {music_stu_gpa['YES']} and who don't has {music_stu_gpa['NO']}")
# GPA of students who volunteer vs not
vol_status={1:"YES",0:"NO"}
df["Volunteering"]=df["Volunteering"].map(vol_status)
vol_stu_gpa=df.groupby("Volunteering")["GPA"].mean()

print(f"THE STUDENTS WHO VOLUNTEER HAS GPA {vol_stu_gpa['YES']:.2f} and who don't has {vol_stu_gpa['NO']:.2f}")
df["AnyActivity"]=( (df["Sports"]=="playing")|(df["Music"] =="YES")|(df["Volunteering"]=="YES") )
avg_gpa=df.groupby("AnyActivity")["GPA"].mean()
print(f"THE DIFFERENCE OF GPA BETWEEN THE STUDENTS WHO INVOLVED IN ACTIVIES VS NOT INVOLVED IS {avg_gpa[True]-avg_gpa[False]:.3f}")

# 🟢 PHASE 4 — Parental Influence
# GPA by ParentalEducation
stu_gpa_parent_edu=df.groupby("ParentalEducation")["GPA"].mean()
print(f"THE GPA OF THE STUDENTS DEPENDING THEIR PARENTAL EDUCATION IS\n{stu_gpa_parent_edu}")
print("THE PARENTAL EDUCATION IS NOT CONSISTENTLY IMPROVING THE GPA ")

# GPA by ParentalSupport
stu_gpa_parent_sup=df.groupby("ParentalSupport")["GPA"].mean()
print(f"THE GPA OF THE STUDENTS DEPENDING THEIR PARENTAL SUPPORT IS\n{stu_gpa_parent_sup}")
print("THE PARENTAL SUPPORT HAS BEEN PLAYING AN IMPORTANT ROLE IN THE GPA OF THE STUDENTS")

# Does tutoring improve GPA?
stu_gpa_tutoring=df.groupby('Tutoring')["GPA"].mean()
print(f"THE GPA OF THE STUDENTS DEPENDING THEIR TUTORING IS\n{stu_gpa_tutoring}")
print("THE STUDENTS WHO TAKE TUTORING HAS HIGHER GPA THAN THE THOSE WHO DON'T")
print("THE PARENTAL EDUCATION IS NOT CONSISTENTLY IMPROVING THE GPA ")

#  PHASE 5 — Ranking & Filtering
# Top 10 GPA students
df["RANKS"]=df["GPA"].rank(ascending=False,method="dense")
sorted_rank=df.sort_values("RANKS").copy()
top_10_students=sorted_rank.iloc[0:10]
top_10_students.reset_index(drop=True,inplace=True)
print(top_10_students)
# Bottom 10 GPA students
df["RANKS"]=df["GPA"].rank(ascending=True,method="dense")
sorted_rank=df.sort_values("GPA").copy()
bottom_10_gpa=sorted_rank.iloc[0:10]
bottom_10_gpa.reset_index(drop=True,inplace=True)
print(bottom_10_gpa)
# Students with GPA > 3.5 and low absences
stu=df[(df["GPA"]>3.5) & (df["Absences"]<=5)]
print(stu)
# Students with high study time but low GPA (interesting case)
high_study_low_gpa_stu=df[(df["Studentcategory"]=="HIGH") & (df["GPA"]<1)]
