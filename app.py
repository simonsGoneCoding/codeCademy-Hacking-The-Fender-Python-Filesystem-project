#Use your knowledge of working with Python files to retrieve, manipulate, obscure, and create data in your quest for justice. Work with CSV files and other text files in this exploration of the strength of Python file programming.


######### Reading In The Passwords
# 1 - 7
import csv
import json

compromised_users = []

with open('passwords.csv') as password_file:
  parsed_csv = csv.DictReader(password_file)

  for password_row in parsed_csv: 
    # print(password_row["Username"])
    compromised_users.append(password_row["Username"])

# print(compromised_users)


# 8, 9, 10
with open("compromised_users.txt", "w") as compromised_users_file: 
  for compromised_user in compromised_users:
    compromised_users_file.write(compromised_user)


######## Notifying the Boss 
## 11 - 15
with open("boss-message.json", "w") as boss_message: 
  boss_message_dict = {
    "recipient": "The Boss", 
    "message": "Mission Success"
  }
  json.dump(boss_message_dict, boss_message)


####### Scrambling the Password
# 16, 17
with open("new_passwords.csv", "w") as new_passwords_obj: 
  slash_null_sig = """
   _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""
  new_passwords_obj.write(slash_null_sig)
