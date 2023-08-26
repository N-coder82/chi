def file_edit(filename, action, key, string=None):
    if action == "read" or action == "r":
        try:
            with open(filename, "r") as file:
                data = file.readlines()
                for line in data:
                    if key in line:
                        return line.strip().split(":")[1]
        except FileNotFoundError:
            return None
    elif action == "write" or action == "w":
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
    elif action == "delete" or action == "d":  # New condition for deletion
        try:
            with open(filename, "r") as file:
                data = file.readlines()

            with open(filename, "w") as file:
                for line in data:
                    if str(line.split(":")[0]) != key:
                        file.write(line)
        except FileNotFoundError:
            raise Exception(f'File named "{filename}" not found')


def getkeytowrite(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            if lines:
                key = lines[-1].split(":")
                print(lines[-1])
                return int(key[0]) + 1
            else:
                raise OSError("Empty file.")
    except FileNotFoundError:
        raise FileNotFoundError("File doesn't exist.")


def write(
    filename, title, desc, datetodone, timetodone, repeat, place, priority, flagged
):
    keytowrite = getkeytowrite(filename)
    print("key is", keytowrite)
    try:
        with open(filename, "a") as file:
            value = f"{title},{desc},{datetodone},{timetodone},{repeat},{place},{priority},{flagged}"
            file.write(f"{keytowrite}:{value}\n")
    except PermissionError:
        raise PermissionError("No permission to edit file.")
    except IOError as exep:
        raise IOError(f"Unknown IO error: {exep}.")


def read(filename, key):
    title = ""
    desc = ""
    datetodone = ""
    timetodone = ""
    repeat = True
    place = ""
    priority = ""
    flagged = True
    try:
        with open(filename, "r") as file:
            data = file.readlines()
            for line in data:
                if str(line.split(":")[0]) == key:
                    rawdata = line.strip().split(":")[1]
                    (
                        title,
                        desc,
                        datetodone,
                        timetodone,
                        repeat,
                        place,
                        priority,
                        flagged,
                    ) = rawdata.split(",")
                    if repeat == "true" or "True":
                        repeat = True
                    elif repeat == "false" or "False":
                        repeat = False
                    if flagged == "true" or "True":
                        flagged = True
                    elif flagged == "false" or "False":
                        flagged = False
                    return [
                        title,
                        desc,
                        datetodone,
                        timetodone,
                        repeat,
                        place,
                        priority,
                        flagged,
                    ]

    except FileNotFoundError:
        raise FileNotFoundError("File doesn't exist.")


def delete(filename, key):
    # key NEEDS TO BE A STRING
    try:
        with open(filename, "r") as file:
            data = file.readlines()

        with open(filename, "w") as file:
            for line in data:
                if str(line.split(":")[0]) != key:
                    file.write(line)
    except FileNotFoundError:
        raise Exception(f'File named "{filename}" not found')



