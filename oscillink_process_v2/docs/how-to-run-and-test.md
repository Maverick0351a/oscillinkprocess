# How to Run and Test (Oscillink Process v2)

This guide covers running the demo, using the CLI, viewing logs, and running tests. The project is stdlib-only and vendor-neutral.

## Prerequisites
- Python 3.x (no extra packages required)

## Paths
- Repository root: `oscillink_process_v2/`
- Package root: `oscillink_process_v2/oscillink_process_v2/`

## Run the demo

Windows (PowerShell):

```powershell
cd "C:\Users\Maver\Downloads\oscillink_process_v2"
python -m oscillink_process_v2.examples.quickstart_demo
```

macOS/Linux:

```bash
cd /path/to/oscillink_process_v2
python -m oscillink_process_v2.examples.quickstart_demo
```

What happens:
- End-to-end run: Idea → Plan → Scaffold → Build → Test → Benchmark → Publish → Maintain.
- Workspace created at `workspace/project/`.
- On success, published release at `published/<build-id>/`.
- Maintenance log appended at `maintenance/maintenance_log.txt`.

## CLI usage

Single-metric threshold override:

```powershell
python -m oscillink_process_v2.cli --max-mse 0.005
```

Multi-metric thresholds via JSON:

```powershell
python -m oscillink_process_v2.cli --thresholds '{"mse":{"lte":0.01},"mae":{"lte":0.02}}'
```

Notes:
- Defaults load from `policies/default.json` if present.
- `--thresholds` overrides the policy file.

## Logs
- Console output plus a persistent log at: `workspace/logs/oscillink.log`.
- Useful for demos, counsel, and auditability.

## Run tests

Windows (PowerShell):

```powershell
python -m unittest discover -s oscillink_process_v2\tests -p "test_*.py" -v
```

macOS/Linux:

```bash
python -m unittest discover -s oscillink_process_v2/tests -p "test_*.py" -v
```

What’s covered:
- Default end-to-end lifecycle (threshold pass).
- Multi-metric thresholds (MSE + MAE) passing.

## Troubleshooting
- If you see `ModuleNotFoundError` for internal modules, ensure you’re running from the repository root with `python -m ...` so package-relative imports resolve.
- Remove or clear any stale `workspace/` or `published/` directories if you’re testing multiple runs.
