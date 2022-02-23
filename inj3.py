import os

email = input("Enter email for delivery notification: ")
msg = input("Optional message: ")
cmd = 'echo "' + msg + '" | mailx -s "Package arriving soon" ' + email
# -- Real command would be run later
print(cmd)
