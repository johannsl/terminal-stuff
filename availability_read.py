# Read file and present output

def main():
    content = []
    try:
        status = open("status.txt", "r")
        content = status.read().split("\n")
        status.close()
    except Exception as e:
        print("status.txt read failure")
        print(e)
        return
    
    internet_availability = float(content[1]) / float(content[0]) * 100
    if content[3] == "0":
        server_availability = 100.0
    else:
        server_availability = float(content[4]) / float(content[3]) * 100

    print("SERVER AVAILABILITY STATUS:")
    print("Internet availability: " + str(internet_availability) + " %")
    print("Server availability: " + str(server_availability) + " %")
    print("\n\n")
    return

main()
