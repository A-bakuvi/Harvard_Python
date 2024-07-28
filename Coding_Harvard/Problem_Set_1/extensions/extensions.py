inp = input("File name: ")
new_inp = inp.strip().lower()
if ".gif" in new_inp:
    print ("image/gif")
elif ".jpg" in new_inp:
    print ("image/jpeg")
elif ".jpeg" in new_inp:
    print ("image/jpeg")
elif ".png" in new_inp:
    print ("image/png")
elif ".pdf" in new_inp:
    print ("application/pdf")
elif ".txt" in new_inp:
    print ("text/plain")
elif ".zip" in new_inp:
    print ("application/zip")
else:
    print("application/octet-stream")