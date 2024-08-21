# Render JSON Schema documentation

This action uses [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) to render documentation for JSON schemata.

## Inputs

## `input-files`

**Required**
Path to JSON schema file or directory of files to be processed.
See [json-schema-for-humans documentation](https://github.com/coveooss/json-schema-for-humans?tab=readme-ov-file#usage) for more details.

## `outputs`

**Required**
Path to directory (or filename if rendering single file) for rendered documentation to be written..
See [json-schema-for-humans documentation](https://github.com/coveooss/json-schema-for-humans?tab=readme-ov-file#usage) for more details.

## `output-format`

Default: `html`.
Should the rendered documentation be `html` or markdown (`md`)

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
```

