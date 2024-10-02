#! /bin/sh
azcopy_path="$(command -v azcopy 2>&1 >/dev/null)"
if [ -n "$azcopy_path" ]
then
  echo "azcopy is installed at: $azcopy_path"
  echo "azcopy-installed=true"
  echo "azcopy-installed=true" >> "$GITHUB_OUTPUT"
else
  echo "azcopy is not installed."
  echo "azcopy-installed=false"
  echo "azcopy-installed=false" >> "$GITHUB_OUTPUT"
fi

echo "azcopy is installed at: $azcopy_path"
echo "PATH=$PATH"
