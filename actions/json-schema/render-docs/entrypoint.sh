#!/bin/sh

# Check arguments
if [ -z "$INPUTS" ]; then
  echo "Input path is required"
  exit 1
fi

if [ -z "$OUTPUTS" ]; then
  echo "Output path is required"
  exit 1
fi

TEMPLATE_NAME=$(
  case "$INPUT_TEMPLATE_NAME" in
    (md) echo "md";;
    (html|js) echo "js_offline";;
    (*) echo "";;
  esac
)

if [ -n "$TEMPLATE_NAME" ]; then
  CONFIG_OPTIONS="--config template_name=$TEMPLATE_NAME"
fi

if [ -z "$CONFIG_FILE" ]; then
  CONFIG_PATH="/app/config.json"
else
  CONFIG_PATH="/github/workspace/$CONFIG_FILE"
fi

# Use INPUT_<INPUT_NAME> to get the value of an input
INPUT_PATH="/github/workspace/$INPUTS"
OUTPUT_PATH="/github/workspace/$OUTPUTS"

# Create directory if needed
if [ ! -d "$OUTPUT_PATH" ]; then
  echo "Creating directory $OUTPUT_PATH"
  mkdir -p "$OUTPUT_PATH"
fi

# Write outputs to the $GITHUB_OUTPUT file
#shellcheck disable=SC2086 
#(passing a command flag)
generate-schema-doc \
  $CONFIG_OPTIONS \
  --config-file "$CONFIG_PATH" \
  "$INPUT_PATH" \
  "$OUTPUT_PATH"

ls -l "$OUTPUT_PATH"
