# Environment variables with defaults
schema_name := 'linkml-fitness-app'
source_schema_path := "src/linkml_fitness_app/schema/linkml_fitness_app.yaml"
gen_project_excludes := "-X graphql -X markdown -X excel -X owl -X shacl -X shex"

# List all commands as default command. The prefix "_" hides the command.
_default:
    @just --list



[group('model development')]
gen-project:
  mkdir -p project/typescript
  uv run --group dev gen-project {{gen_project_excludes}} -d project {{source_schema_path}}
  uv run --group dev gen-pydantic {{source_schema_path}} > src/linkml_fitness_app/datamodel/{{schema_name}}_pydantic.py
  mv project/*.py src/linkml_fitness_app/datamodel
  uv run --group dev gen-typescript {{source_schema_path}} > project/typescript/{{schema_name}}.ts || true ; \
  uv run --group dev gen-markdown-datadict  --anchor-style mkdocs  --diagram-dir datadict/images --pretty-format-svg {{source_schema_path}} > datadict/datadict.md
 
# Locally serve data dictionary
[group('model development')]
serve-data-dict: gen-project
  cd datadict && uv run --group dev grip --wide --with-mermaid --case-insensitive-anchors datadict.md localhost:6419 --norefresh
