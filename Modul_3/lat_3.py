data_list = [
    "3 minggu 3 hari 7 jam 21 menit",
    "5 minggu 5 hari 8 jam 11 menit",
    "7 minggu 1 hari 5 jam 33 menit",
]

def extract_integers(data):
    parts = data.split()
    integers = map(int, filter(str.isdigit, parts))
    return tuple(integers)

output = [extract_integers (data) for data in data_list]
print(output)