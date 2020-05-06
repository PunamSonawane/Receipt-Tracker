import json
import os
def dumps_json_in_files(json_file, json_data):
    """
    dumps_json_in_files function is used to dumps the json in file

    @param:
    json_file = json file
    json_data = json data dictionary
    """
    file_status = False
    with open(json_file, 'w') as file:
        json.dump(json_data, file, indent=4)
        file_status = True
    return file_status
type_=os.environ["type"]
pid=os.environ["project_id"]
private_key_id=os.environ["private_key_id"]
private_key=os.environ["private_key"]
client_email=os.environ["client_email"]
client_id=os.environ["client_id"]
auth_uri=os.environ["auth_uri"]
token_uri=os.environ["token_uri"]
auth_provider_x509_cert_url=os.environ["auth_provider_x509_cert_url"]
client_x509_cert_url=os.environ["client_x509_cert_url"]
json_data={
"type":type_,
"project_id":pid,
"private_key_id":private_key_id,
"private_key":private_key,
"client_email":client_email,
"client_id":client_id,
"auth_uri":auth_uri,
"token_uri":token_uri,
"auth_provider_x509_cert_url":auth_provider_x509_cert_url,
"client_x509_cert_url":client_x509_cert_url
}

print(dumps_json_in_files('/app/google-credentials.json', json_data))
