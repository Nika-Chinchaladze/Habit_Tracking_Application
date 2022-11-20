import requests


class ApiWorker:
    def __init__(self):
        self.my_endpoint = "https://pixe.la/v1/users"

    def create_account(self, username, password):
        my_account = {
            "token": password,
            "username": username,
            "agreeTermsOfService": "yes",
            "notMinor": "yes"
        }
        response = requests.post(url=self.my_endpoint, json=my_account)
        return response.status_code

    def create_graph(self, username, password, graph_id, graph_name, unit, unit_type, color):
        my_header = {
            "X-USER-TOKEN": password
        }
        graph_endpoint = f"{self.my_endpoint}/{username}/graphs"
        graph_parameters = {
            "id": f"{graph_id}",
            "name": f"{graph_name}",
            "unit": f"{unit}",
            "type": f"{unit_type}",
            "color": f"{color}"
        }
        response = requests.post(url=graph_endpoint, json=graph_parameters, headers=my_header)
        return response.status_code

    def create_pixel(self, username, password, graph_id, chosen_date, chosen_quantity):
        my_header = {
            "X-USER-TOKEN": password
        }
        pixel_endpoint = f"{self.my_endpoint}/{username}/graphs/{graph_id}"
        pixel_parameters = {
            "date": chosen_date,
            "quantity": chosen_quantity
        }
        response = requests.post(url=pixel_endpoint, json=pixel_parameters, headers=my_header)
        return response.status_code

    def update_existing_pixel(self, username, password, graph_id, chosen_quantity, chosen_date):
        my_header = {
            "X-USER-TOKEN": password
        }
        put_endpoint = f"{self.my_endpoint}/{username}/graphs/{graph_id}/{chosen_date}"
        put_parameters = {
            "quantity": f"{chosen_quantity}"
        }
        response = requests.put(url=put_endpoint, json=put_parameters, headers=my_header)
        return response.status_code

    def delete_pixel(self, username, password, graph_id, chosen_date):
        my_header = {
            "X-USER-TOKEN": password
        }
        delete_endpoint = f"{self.my_endpoint}/{username}/graphs/{graph_id}/{chosen_date}"
        response = requests.delete(url=delete_endpoint, headers=my_header)
        return response.status_code


def color_transformer(current_name):
    my_color = ""
    if current_name == "green":
        my_color = "shibafu"
    elif current_name == "red":
        my_color = "momiji"
    elif current_name == "blue":
        my_color = "sora"
    elif current_name == "yellow":
        my_color = "ichou"
    elif current_name == "purple":
        my_color = "ajisai"
    else:
        my_color = "kuro"
    return my_color
