while True:
    command = input()
    if input() == 'End':
        break
    split_command = command.split("-")
    current_command = split_command[0]
    file_name = split_command[1]
    if current_command == "Create":
        with open(f'files/{file_name}', "w") as create_file:
            pass

    elif current_command == "Add":
        with open(f"files/{file_name}", "a") as adding_file:
            adding_file.write(f'{split_command[2]}' + "\n")
    elif current_command == "Replace":
        pass
    elif current_command == "Delete":
        pass
