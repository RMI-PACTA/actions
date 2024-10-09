# Copy files to or from Azure Blob Store

This action uses Azure Python (Blob) SDK to move files from a local filesystem to an Azure Blob container, or vice-versa.

Note that this action requires running the `azure/login` action first.

## Inputs

### `source`

**Required**
Path to local files to upload, or Blob URL to download

### `destination`

**Required**
Blob URL to recieve files or local path.

### `overwrite`

Optional (default: `false`)
Should existing files be overwritten?

### `log_level`

Optional (default: `INFO`)
Control logging verbosity.

## Outputs

### `source-files`

Path to source files. Local path if uploading, or Blob URLs if downloading.

### `destination-files`

Path to destination files. Blob URLs if uploading, or Local path if downloading.

## Example Usage

### Upload

```yaml
      - name: Upload Directory to Container root
        id: upload-dir
        uses: RMI-PACTA/actions/actions/azure/blob-copy@main
        with:
          source: some/local/path
          destination: https://MyAccount.blob.core.windows.net/MyContainer
```

```yaml
      - name: Upload Directory to Container subfolder
        id: upload-dir-path
        uses: RMI-PACTA/actions/actions/azure/blob-copy@main
        with:
          source: some/local/path
          destination: https://MyAccount.blob.core.windows.net/MyContainer/SomeDirectory
```

```yaml
      - name: Upload file to Container subfolder
        id: upload-file
        uses: RMI-PACTA/actions/actions/azure/blob-copy@main
        with:
          source: some/local/path/foo.txt
          destination: https://MyAccount.blob.core.windows.net/MyContainer/SomeDirectory
```

### Download

```yaml
      - name: Download Directory from Container
        id: download-dir
        uses: RMI-PACTA/actions/actions/azure/blob-copy@main
        with:
          source: https://MyAccount.blob.core.windows.net/MyContainer/SomeDirectory
          destination: some/local/path
```

```yaml
      - name: Download File from Container
        id: download-file
        uses: RMI-PACTA/actions/actions/azure/blob-copy@main
        with:
          source: https://MyAccount.blob.core.windows.net/MyContainer/SomeDirectory/SomeFile.txt
          destination: some/local/path
```
