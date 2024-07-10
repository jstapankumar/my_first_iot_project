import requests
from config import *

def retrive_ae():
    url = f"{registrarUrl}/{GROUP_ID}/{registrarCseBaseResourceId}"

    #path to your client certificate and key
    client_cert = "/home/cdot/Downloads/http testing with CCSp/SP109736.crt"
    client_key = "/home/cdot/Downloads/http testing with CCSp/SP109736.key"
    ca_cert = "/home/cdot/Downloads/http testing with CCSp/ca.crt"  #CA certificate

    try:
        response = requests.get(url, headers=headers, cert=(client_cert, client_key), verify=ca_cert)
        response.raise_for_status()  #raise error for bad response status

        if response.status_code == 200:
            print("AE retrieved successfully")
            return response.json()  #return JSON response if successful
        else:
            print(f"Failed to retrieve AE. Status code: {response.status_code}, Response: {response.text}")
            return None
    except requests.exceptions.SSLError as ssl_err:
        print("SSL Error:", ssl_err)
        return None
    except requests.exceptions.RequestException as e:
        print("Request Exception:", e)
        return None

if __name__ == "__main__":
    retrive_ae()

