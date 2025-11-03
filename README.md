# Fitness App LinkML Model

This is a LinkML model for a fitness tracking application. It defines classes and slots to represent users, workouts, exercises, and related data.

## Development Tools

This project uses modern Python development tools for efficient development:

- **[uv](https://docs.astral.sh/uv/)**: A fast Python package manager and virtual environment tool
- **[just](https://just.systems/)**: A command runner for project tasks (similar to make, but simpler)

## Model

The model is documented in [datadict.md](datadict/datadict.md)

## Getting Started

### Using GitHub Codespaces

For the easiest setup, create a GitHub Codespace which will provide a pre-configured development environment:

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/vladistan/fitness-app)

### Available Commands

This project uses `just` to manage common development tasks. Run `just` without arguments to see all available commands:

```bash
just
```

Key commands include:

- `just gen-project` - Generate all project artifacts (schemas, types, documentation)
- `just serve-data-dict` - Generate and serve the data dictionary documentation locally
