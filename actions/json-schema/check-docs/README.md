# Render JSON Schema documentation

This action checks that documentation for JSON Schemata is up to date.
It uses [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) via the `render-docs` action.

The action suceeds if documentation is rendered, or fails if there are differences between the in-repo docs, and re-rendering them.
Note that the docs must be committed to the repo in order for this action to succeed.

## Inputs

Inputs are the same as the `render-docs` action and are passed through to that action.

### `input-files`

**Required**
Path to JSON schema file or directory of files to be processed.
See [json-schema-for-humans documentation](https://github.com/coveooss/json-schema-for-humans?tab=readme-ov-file#usage) for more details.

### `outputs`

**Required**
Path to directory (or filename if rendering single file) for rendered documentation to be written..
See [json-schema-for-humans documentation](https://github.com/coveooss/json-schema-for-humans?tab=readme-ov-file#usage) for more details.

### `output-format`

Default: `html`.
Should the rendered documentation be `html` or markdown (`md`)

### `config-file`

Path in-repo to json-schema-for-humans config file.

## Outputs

None

## Example usage

```yaml
      - id: render-json-schema
        uses: RMI-PACTA/actions/actions/json-schema/render-docs@main
        with:
          input-files: 'inst/extdata/schema'
          outputs: 'inst/extdata/schema'
          output-format: html
          config-file: 'inst/extdata/schema-config.json'
```

