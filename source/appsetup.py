import sys
def read_write_string(filename, readwrite, key, string=None):
    if readwrite == "read" or readwrite == "r":
        try:
            with open(filename, "r") as file:
                data = file.readlines()
                for line in data:
                    if key in line:
                        return line.strip().split(":")[1]
        except FileNotFoundError:
            return None
    elif readwrite == "write" or readwrite == "w":
        data = {}
        try:
            with open(filename, "r") as file:
                for line in file:
                    k, v = line.strip().split(":")
                    data[k] = v

            data[key] = string

            with open(filename, "w") as file:
                for k, v in data.items():
                    file.write(f"{k}:{v}\n")
        except FileNotFoundError:
            with open(filename, "w") as file:
                file.write(f"{key}:{string}\n")
def firstrun():
    read_write_string("appsettings.chi", "w", "firstrun", "false")
    read_write_string("appsettings.chi", "w", "openaiapikey", input("OpenAI API key: "))
    read_write_string("appsettings.chi", "w", "weatherapikey", input("WeatherAPI key: "))
    print("Press enter to continue...")
    input()
def setupcheck():
    if read_write_string("appsettings.chi", "r", "firstrun") == "true":
        firstrun()
        return False
    elif read_write_string("appsettings.chi", "r", "firstrun") == "false":
        return True
    else:
        print("Your setup file has been corrupted, please download and install this program again...")
        input()
        sys.exit(1)
def openaiapikey():
    return read_write_string("appsettings.chi", "r", "openaiapikey")
def weatherapikey():
    return read_write_string("appsettings.chi", "r", "weatherapikey")