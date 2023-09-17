def convert_to_time(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours*3600) // 60
    seconds = seconds % 60

    return hours,minutes,seconds

def print_time(hours, minutes, seconds):
    print("{:02d}:{:02d}:{:02d}".format(hours,minutes,seconds))

if __name__ == "__main__":
    seconds = int(input())
    hours, minutes, seconds = convert_to_time(seconds)
    print_time(hours,minutes,seconds)