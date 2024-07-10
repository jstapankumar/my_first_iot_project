import requests
from config import *

def create_ae():
    url = f"{registrarUrl}/{registrarCseBaseResourceId}"

    headers.update({
        "Content-Type": "application/json;ty=2",
        "Accept": "application/json"
    })

    payload = {
        "m2m:ae": {
            "api": "N.tapan.test",
            "srv": ["3"],
            "rr": True,
            "lbl": ["ADN"],
            "rn": "tapan.smartbulb",
            "acpi": "[R1672]"
        }
    }

    client_cert = "/home/cdot/Downloads/http testing with CCSp/SP109736.crt"
    client_key = "/home/cdot/Downloads/http testing with CCSp/SP109736.key"
    ca_cert = "/home/cdot/Downloads/http testing with CCSp/ca.crt"

    try:
        response = requests.post(url, json=payload, headers=headers, cert=(client_cert, client_key), verify=ca_cert)
        response.raise_for_status()  #raise error for bad response status

        if response.status_code == 201:
            print("AE created successfully")
        else:
            print(f"Failed to create AE. Status code: {response.status_code}, Response: {response.text}")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Request Exception occurred: {err}")

if __name__ == "__main__":
    create_ae()
