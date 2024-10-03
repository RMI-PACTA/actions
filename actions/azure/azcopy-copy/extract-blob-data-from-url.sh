#! /bin/sh
echo "Blob URL: $BLOB_URL"

# Extract the storage account name from the URL
# The storage account name is the part between https:// and .blob.core.windows.net
# The sed command is used to extract the storage account name
STORAGE_ACCOUNT_NAME=$(echo $BLOB_URL | sed 's/https:\/\/\(.*\).blob.core.windows.net.*/\1/')
echo "az-storage-account=$STORAGE_ACCOUNT_NAME"
echo "az-storage-account=$STORAGE_ACCOUNT_NAME" >> "$GITHUB_OUTPUT"

URL_SUFFIX=$(echo $BLOB_URL | sed 's/.*.blob.core.windows.net\/\(.*\)/\1/')
# echo "URL_SUFFIX=$URL_SUFFIX"
FILE_SYSTEM_NAME=$(echo $URL_SUFFIX | sed 's/\([^\/]*\)\/\(.*\)/\1/')
echo "az-file-system=$FILE_SYSTEM_NAME"
echo "az-file-system=$FILE_SYSTEM_NAME" >> "$GITHUB_OUTPUT"
FILE_SYSTEM_PATH=$(echo $URL_SUFFIX | sed 's/\([^\/]*\)\/\(.*\)/\2/')
echo "az-path=$FILE_SYSTEM_PATH"
echo "az-path=$FILE_SYSTEM_PATH" >> "$GITHUB_OUTPUT"
