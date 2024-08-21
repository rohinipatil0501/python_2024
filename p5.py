#Accept average score from the studentof his exam and print his result as follows:0-49:Fail, 50-74:Second class, 75-90: First class,91-100:Distinction.Also check for invalid score
avg_score=(int(input('Enter your gross average :')))
print('RESULT')
if avg_score>=75 and avg_score<=90:
    print('congratulations you have passed with first class')
elif avg_score>=91 and avg_score<=100:
    print('congratulations you have passed with distinction')
elif avg_score>=50 and avg_score<=74:
    print('congratulations you have passed with second class')
elif avg_score>=0 and avg_score<=49:
    print('You habe Failed')
else:
    print('Invalid score')