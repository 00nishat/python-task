user_lists=['admin','nishat','lopa','tasnim','disha']
for user_list in user_lists:
    if 'admin' in user_list:
       print("hello admin,would you like to see a status reports")
    else:
        print(f"{user_list} , thanks for login ")
