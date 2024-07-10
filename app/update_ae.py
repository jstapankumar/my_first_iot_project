import requests
from config import *

def update_ae():
    url = f"{registrarUrl}/{GROUP_ID}"  #assuming GROUP_ID is defined in config.py

    headers.update({
        "Content-Type": "application/json",
        "Accept": "application/json"
    })

    #path to your client certificate and key
    client_cert = "/home/cdot/Downloads/http testing with CCSp/SP109736.crt"
    client_key = "/home/cdot/Downloads/http testing with CCSp/SP109736.key"
    ca_cert = "/home/cdot/Downloads/http testing with CCSp/ca.crt"  #CA certificate

    payload = {
        "m2m:grp": {
            "mid": ["<mid-ReceivedinResponseOfGroupRetrieveRequest>", AE_ID]
        }
    }

    try:
        response = requests.put(url, json=payload, headers=headers, cert=(client_cert, client_key), verify=ca_cert)
        response.raise_for_status()  #raise error for bad response status

        if response.status_code == 200:
            print("AE updated successfully")
        else:
            print(f"Failed to update AE. Status code: {response.status_code}, Response: {response.text}")
    except requests.exceptions.SSLError as ssl_err:
        print("SSL Error:", ssl_err)
    except requests.exceptions.RequestException as e:
        print("Request Exception:", e)

if __name__ == "__main__":
    update_ae()
