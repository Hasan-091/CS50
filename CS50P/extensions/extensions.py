filename = input("Name of the file: ")

new_filename = filename.lower().strip()

if ".gif" in new_filename:
    print("image/gif")
elif ".jpg" in new_filename:
    print("image/jpeg")
elif ".jpeg" in new_filename:
    print("image/jpeg")
elif ".png" in new_filename:
    print("image/png")
elif ".pdf" in new_filename:
    print("application/pdf")
elif ".zip" in new_filename:
    print("application/zip")
elif ".txt" in new_filename:
    print("text/plain")
# Otherwise, print "application/octet-stream"
else:
    print("application/octet-stream")
