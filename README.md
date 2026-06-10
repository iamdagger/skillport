# skillport

[![CI](https://github.com/iamdagger/skillport/actions/workflows/ci.yml/badge.svg)](https://github.com/iamdagger/skillport/actions/workflows/ci.yml)
![python](https://img.shields.io/badge/python-3.8%2B-blue)
![license](https://img.shields.io/badge/license-MIT-green)

**Superpowers for your coding agent.** Add battle-tested skills, presets, and
guardrails to Claude Code and Cursor in one command. Stop copy-pasting the same
prompts into every repo. Run `skillport sync` and your agent picks up your
stack, your conventions, and your review checklist.

## Install

```bash
pip install -e .
```

## Getting started

Pull the latest skill pack and install it for this machine:

```bash
skillport sync
```

Then check what's loaded:

```python
import skillport
skillport.installed_pack()   # raises SkillportNotConfigured if you skipped `skillport sync`
```

## Why

Every engineer reinvents the same agent setup. skillport centralizes skills and
presets so a new machine is productive in one command instead of an afternoon of
copy-paste.

## License

MIT
