import pandas as pd 
import matplotlib.pyplot as plt

# task 1
df = pd.read_csv('student_habits_performance.csv')
# print(df.head(10)) 
# print(df.info())
df.dropna(inplace=True)

NewDf=df.drop_duplicates()
# print(NewDf.head(10))
# print(NewDf.describe())

# task 2
group_gender=NewDf.groupby('gender')['exam_score'].mean()
print(group_gender)
# students who have an undeclared gender lead the pack, followed by female students, and then male students.

group_parent=NewDf.groupby('parental_education_level')[['study_hours_per_day','exam_score']].mean()
print(group_parent)
# the educational level of parents seemto bring no difference in the amount of study hours, as indicated by the mean values, but the exam scores do differ significantly.

# task 3
x=NewDf.groupby('parental_education_level')['exam_score'].mean()
# Bar graph for Average exam score by parental education level
plt.bar(x.index,x.values,color='blue')
plt.title("Average exam score by parental education level")
plt.xlabel("Parental education level")
plt.ylabel("Average exam score")
plt.show()

# Histogram for exam score
plt.hist(NewDf['exam_score'], bins=10, color='purple')
plt.title("Exam score Distribution")
plt.xlabel("Exam score")
plt.ylabel("Frequency")
plt.show() 

# Scatter plot for study hours per day against exam score
plt.scatter(NewDf['study_hours_per_day'],NewDf['exam_score'])
plt.title("Study hours per day vs Exam score")
plt.xlabel("Study hours per day")
plt.ylabel("Exam score")
plt.show()