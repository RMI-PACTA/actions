# Copy files to or from Azure Blob Store using `azcopy`

This action uses `azcopy` (installing if required) to move files from a local filesystem to an Azure Blob container, or vice-versa.

## Inputs

### `source`

**Required**
Path to local files to upload, or Blob URL to download

### `destination`

**Required**
Blob URL to recieve files or local path.

### `flags`

Additional flags to pass to `azcopy copy`.
Passing `--recursive` allows for directory upload.
See the [azcopy documtentation](https://learn.microsoft.com/en-us/azure/storage/common/storage-ref-azcopy-copy?toc=%2Fazure%2Fstorage%2Fblobs%2Ftoc.json#options) for more information.

## Outputs

None

## Example usage

```yaml
      - id: upload-file
        uses: RMI-PACTA/actions/actions/azure/azcopy-copy@main
        with:
          source: 'foo.txt'
          destination: https://MyStorageAccount.blob.core.windows.net/MyContainer/path/to/file
```

```yaml
      - id: download-file
        uses: RMI-PACTA/actions/actions/azure/azcopy-copy@main
        with:
          source: https://MyStorageAccount.blob.core.windows.net/MyContainer/path/to/file.txt
          destination: 'some/local/dir/'
```

```yaml
      - id: upload-directory
        uses: RMI-PACTA/actions/actions/azure/azcopy-copy@main
        with:
          source: 'foo/'
          destination: https://MyStorageAccount.blob.core.windows.net/MyContainer/path/to/file
          flags: |
            --recursive
```
