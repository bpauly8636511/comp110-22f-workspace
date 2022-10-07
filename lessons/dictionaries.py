"""testing doc strings."""

schools = {"UNC": 19400, "DUKE": 6717, "NCSU": 26150}
# print(schools["UNCC"])
# Example looping over the keys of a dict
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")

print(type(schools[school]))
