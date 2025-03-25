from etls.azure_etl import connect_to_storage_account, create_container, upload_blob

from utils.constants import AZURE_CONNECTION_STRING, AZURE_CONTAINER_NAME

def upload_azure_pipeline():
    service_client = connect_to_storage_account(AZURE_CONNECTION_STRING)
    create_container(service_client, AZURE_CONTAINER_NAME)
    # file_path = 
    # upload_blob(service_client, AZURE_CONTAINER_NAME, file_path, file_path.split('/')[-1])