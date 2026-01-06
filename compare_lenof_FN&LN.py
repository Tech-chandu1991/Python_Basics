First_Name = input("Enter First Name:")
Last_Name = input("Enter Last Name:")

Length_FN = len(First_Name)
Length_LN = len(Last_Name)

if Length_FN > Length_LN:
    print(f'"{Length_FN}" is longer than "{Length_LN}"')
elif Length_LN > Length_FN:
    print(f'"{Length_LN}" is longer than "{Length_FN}"')
else:
    print(f'"{Length_FN}" and "{Length_LN}" are equal')





