# ER Diagram Generation

The ER diagram is generated from the SDE schema as a PlantUML file, then rendered to SVG/PDF via a local [Kroki](https://kroki.io/) server.

## Prerequisites

- **Docker** — to run the Kroki rendering server
- **rsvg-convert** — to convert SVG to PDF (`librsvg2-bin` on Debian/Ubuntu)
- **gcover** — to generate the `.puml` file from the SDE schema

```bash
# Install rsvg-convert (Linux)
sudo apt install librsvg2-bin
```

## 1. Start/stop the Kroki server

```bash
make kroki-up    # start (detached, auto-removed on stop)
make kroki-down  # stop
```

This runs `docker run -d --rm --name kroki -p 1234:8000 yuzutech/kroki`.  
The Makefile variable `KROKI_URL` defaults to `http://localhost:1234`.

## 2. Generate the PlantUML file

```bash
make diagram
```

This calls `gcover schema diagram` and writes `outputs/diagram.puml`.  
It requires the SDE export at `sources/<latest-date>/geocover-schema-sde.json`.

## 3. Render to SVG and PDF

```bash
# SVG only
make puml-svg PUML_FILE=outputs/diagram.puml

# PDF (renders SVG first, then converts with rsvg-convert)
make puml-pdf PUML_FILE=outputs/diagram.puml
```

Output files: `outputs/diagram.svg` and `outputs/diagram.pdf`.

## CI (GitHub Actions)

The `build.yaml` workflow runs Kroki as a service container and generates the diagram automatically:

1. Kroki starts as a service (`yuzutech/kroki`, mapped to `localhost:1234`)
2. `make diagram` generates `outputs/diagram.puml` from the SDE schema
3. `make puml-svg` and `make puml-pdf` render it via Kroki
4. `outputs/diagram.svg` and `outputs/diagram.pdf` are uploaded as release artifacts

## Overriding defaults

| Variable          | Default                  | Description                       |
|-------------------|--------------------------|-----------------------------------|
| `KROKI_URL`       | `http://localhost:1234`  | URL of the Kroki server           |
| `KROKI_CONTAINER` | `kroki`                  | Docker container name             |
| `PUML_FILE`       | `diagram.puml`           | Input `.puml` file path           |

Example with a custom Kroki instance:

```bash
make puml-pdf PUML_FILE=outputs/diagram.puml KROKI_URL=http://kroki.example.com
```
