
 
# # age_Days = int(input("Enter The Number :\n"))

# # years = int(age_Days /365)
# # remainingDays = age_Days % 365
# # months = int(remainingDays / 30)
# # month = remainingDays % 30


# # print(years)
# # # print(remainingDays)
# # print(months)
# # print(month)

# # Now converting my Age year to days


birth_day= int(input("Enter your birhday number :\n"))
birth_month = int(input("Enter your birh-month :\n"))
birth_year= int(input("Enter your birhyear :\n"))

present_day= int(input("Enter present days:\n"))
present_month = int(input("Enter present month :\n"))
present_year= int(input("Enter present year :\n"))

total_day = birth_day - present_day
total_month = birth_month - present_month
total_year = present_year - birth_year

print("Years",total_year)
print("Months",total_month)
print("Days",total_day)






