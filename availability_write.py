import os
import datetime

# check internet
# check uptime
# write to file (every 2 hours?)
# statusfile structure:
#   total pings
#   accepted pings
#   last runtime
#   expected iterations
#   actual iterations

hostname = "8.8.8.8"
frequency = 2 # hours
time_buffer = 60 * 5 # seconds

def main():
    connection, response = pingInternet()
    uptime = checkUptime()
    writeToFile(connection, response, uptime)
    return

def pingInternet():
    response = os.system("ping -c 1 " + hostname)
    if response == 0:
        return ["success", response]
    else:
        return ["failure", response]

def checkUptime():
    try:
        uptime = open("/proc/uptime", "r")
        uptime_seconds = float(uptime.readline().split()[0])
        uptime.close()
    except Exception as e:
        print("checkUptime failure")
        print(e)
        return "failure"
    return uptime_seconds

def writeToFile(connection, response, uptime):
    current_time = datetime.datetime.now()
    write_status = True
    
    if not os.path.isfile("status.txt"):
        status = open("status.txt", "w")
        content = [0, 0, current_time, 0, 0]
        status.write(str(content[0]) + "\n")
        status.write(str(content[1]) + "\n")
        status.write(str(content[2]) + "\n")
        status.write(str(content[3]) + "\n")
        status.write(str(content[4]) + "\n")
        status.write("\n\n")
        status.close()

    # Status file
    new_content = []
    try:
        status = open("status.txt", "r+")
        old_content = status.read().split("\n")

        new_content.append(int(old_content[0]) + 1)
        if connection == "success":
            new_content.append(int(old_content[1]) + 1)
        else:
            new_content.append(int(old_content[1]))
        new_content.append(str(current_time))
        last_run = datetime.datetime.strptime(old_content[2], "%Y-%m-%d %H:%M:%S.%f")
        delta_time = (current_time - last_run).total_seconds() + time_buffer
        delta_hours = int(divmod(delta_time, 3600)[0])
        expected_iterations = delta_hours / frequency
        if expected_iterations == 0:
            expected_iterations = 1
        new_content.append(int(old_content[3]) + expected_iterations)
        new_content.append(int(old_content[4]) + 1)
        
        status.seek(0)
        status.write(str(new_content[0]) + "\n")
        status.write(str(new_content[1]) + "\n")
        status.write(str(new_content[2]) + "\n")
        status.write(str(new_content[3]) + "\n")
        status.write(str(new_content[4]) + "\n")
        status.write("\n\n")
        
        status.close()
    except Exception as e:
        print("status.txt write failure")
        print(e)
        write_status = False

    # Log file
    try:
        log = open("log.txt", "a")
        log.write("current_time: " + str(current_time) + "\n")
        log.write("connection: " + connection + "\n")
        log.write("uptime: " + str(uptime) + "\n")
        if write_status == False:
            log.write("Write to status.txt failed \n")
        log.write("\n\n")
        log.close()
    except Exception as e:
        print("log.txt write failure")
        print(e)
        write_status = False
    return
    
main()
