# skillport

## Setup

Install the package and verify:

```bash
pip install -e .
python -c "import skillport; print(skillport.__version__)"
```

## Commands

- `skillport sync` -- re-pull the latest skill pack from the registry
- `skillport --help` -- show available commands

## Testing

```bash
pip install pytest
pytest -q
```
