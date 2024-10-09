import logging
import os
import re
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
from pathlib import Path
from mime_types import mime_types

# create logger
logger = logging.getLogger(__name__)
# create console handler and set level to debug
ch = logging.StreamHandler()
# create formatter
formatter = logging.Formatter('%(levelname)s: %(asctime)s %(message)s')
# add formatter to ch
ch.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)

logger.info("Accessing Azure Crendentials.")
default_credential = DefaultAzureCredential()

source = str(os.getenv("SOURCE"))
logger.info(f"Source: {source}")
destination = str(os.getenv("DESTINATION"))
logger.info(f"Destination: {destination}")
overwrite_flag = bool(os.getenv("OVERWRITE", "False").lower() == "true")

blob_pattern = re.compile(r"^(https://.*.blob.core.windows.net)/(.*?)(/.*)?$")
source_account_url = blob_pattern.match(source)
destination_account_url = blob_pattern.match(destination)

if source_account_url and destination_account_url:
    logger.error("Both source and destination are valid blob URLs. One of them should be a local file path.")
    exit(1)

if not source_account_url and not destination_account_url:
    logger.error("Neither source nor destination are valid blob URLs. One of them should be a blob URL.")
    exit(1)

if destination_account_url and not source_account_url:
    logger.info("Destination is a blob URL. Copying from local file to blob.")

    logger.debug("Extracting source file path.")
    source_path = Path(source)
    if not source_path.exists():
        logger.error("Source file does not exist.")
        exit(1)
    if source_path.is_dir():
        source_files = list(source_path.glob("**/*"))
        source_files = [file for file in source_files if file.is_file()]
    else:
        source_files = [source_path]

    account_url = destination_account_url.group(1)
    logger.debug(f"Account URL: {account_url}")
    container_name = destination_account_url.group(2)
    logger.debug(f"Container Name: {container_name}")
    blob_path = destination_account_url.group(3)
    if not blob_path: 
        blob_path = ""
    blob_path = Path(blob_path)
    logger.debug(f"Blob Path: {blob_path}")

    blob_service_client = BlobServiceClient(
            account_url=account_url,
            credential=default_credential
        )
    container_client = blob_service_client.get_container_client(container_name)

    for source_file in source_files:
        logger.info(f"Copying {source_file} to Blob Storage.")
        file_mime = mime_types.get(source_file.suffix, None).mime_type
        logger.debug("File MIME: {file_mime}")
        with open(source_file, "rb") as data:
            upload_path = blob_path.joinpath(source_file)
            logger.debug(f"Upload Path: {upload_path}")
            blob_client = container_client.get_blob_client("/" + str(upload_path))
            blob_client.upload_blob(
                data,
                overwrite = overwrite_flag,
                content_settings = {"content_type": file_mime}
            )
    


if source_account_url and not destination_account_url:
    logger.info("Source is a blob URL. Copying from blob to local file.")

    account_url = source_account_url.group(1)
    logger.debug(f"Account URL: {account_url}")
    container_name = source_account_url.group(2)
    logger.debug(f"Container Name: {container_name}")
    blob_path = source_account_url.group(3)
    if not blob_path: 
        blob_path = ""
    logger.debug(f"Blob Path: {blob_path}")

    blob_service_client = BlobServiceClient(
            account_url=account_url,
            credential=default_credential
        )
    container_client = blob_service_client.get_container_client(container_name)

    blob_list = container_client.list_blobs(
        name_starts_with=str(blob_path)
    )

    for blob in blob_list:
        logger.debug(f"Processing Blob: {blob.name}.")
        if blob.size == 0:
            logger.debug(f"Blob {blob.name} is 0 Bytes. This usually indicate s a directory. Skipping.")
            continue
        else:
            logger.info(f"Downloading {blob.name} to local file.")
            download_path = Path(destination).joinpath(blob.name)
            logger.debug(f"Download Path: {download_path}")
            if not overwrite_flag and download_path.exists():
                logger.error(f"File {download_path} already exists. Aborting.")
                exit(1)
            download_path.parent.mkdir(parents=True, exist_ok=True)
            with open(download_path, "wb") as data:
                blob_client = container_client.get_blob_client(blob.name)
                data.write(blob_client.download_blob().readall())


    logger.debug(f"Blob Path: {blob_path}")
    blob_service_client = BlobServiceClient(
            account_url=account_url,
            credential=default_credential
        )
    container_client = blob_service_client.get_container_client(container_name)

