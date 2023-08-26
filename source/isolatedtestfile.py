def edit(filename, old_key, new_value):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        with open(filename, "w") as file:
            for line in lines:
                if ":" in line:
                    key, value = line.strip().split(":")
                    key = key.strip()
                    value = value.strip()
                    if key == old_key:
                        file.write(f"{key}:{new_value}\n")
                    else:
                        file.write(line)

    except FileNotFoundError:
        raise Exception(f'File named "{filename}" not found')
input("...")
edit("reminders.chi", "7", "i REALLy love cats!")