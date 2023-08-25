limit=42
flength=int(put("Enter the length of the zander in centimeters"))
if flength<42:
    difference=limit-flength
    print("Release the zander, it is"+str(flength)+"centimeters short of minimum length")
else:
    print("Mission successful, return to base soldier")