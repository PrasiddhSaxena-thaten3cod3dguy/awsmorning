import subprocess

output=subprocess.check_output("wmic product get name ")


print("This is subprocess Module At Best")
print(output)