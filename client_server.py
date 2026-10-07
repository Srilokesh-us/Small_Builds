def server(request):
    if request == "Give me student 101":
        return "Student 101 is Ravi"
    return "Student not found"


# Client
request = "Give me student 101"

# Request → Server
response = server(request)

# Server → Response
print(response)