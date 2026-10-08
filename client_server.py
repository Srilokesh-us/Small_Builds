def server(request):
    if request == "Give me student 101":
        return "Student 101 is Ravi"
    return "Student not found"

request = "Give me student 101"
response = server(request)
print(response)