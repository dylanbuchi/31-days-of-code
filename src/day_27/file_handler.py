import os
import json

PASSWORDS_DATA_FILE_PATH = os.path.join(os.getcwd(),
                                        'src/day_27/data/passwords.txt')


class PasswordsDataFileHandler:
    def __init__(self):
        pass

    def save_passwords_data_to_file(self, passwords_data):
        """save passwords_data to the passwords file in a JSON format"""
        data_to_write = None
        website, email, password = passwords_data
        new_passwords_data = {website: {"email": email, "password": password}}

        updated_passwords_data = self.update_passwords_data_file(
            new_passwords_data)

        if updated_passwords_data:
            data_to_write = updated_passwords_data
        else:
            data_to_write = new_passwords_data

        with open(PASSWORDS_DATA_FILE_PATH, 'w') as password_data_file:
            json.dump(data_to_write, password_data_file, indent=4)

    def update_passwords_data_file(self, new_passwords_data):
        try:
            with open(PASSWORDS_DATA_FILE_PATH) as password_data_file:
                password_data = json.load(password_data_file)
                password_data.update(new_passwords_data)
        except:
            return False
        else:
            return password_data
