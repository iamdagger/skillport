import re

import skillport


def test_version_shape():
    assert re.match(r"^\d+\.\d+\.\d+$", skillport.__version__)


def test_installed_pack_raises_before_sync(tmp_path, monkeypatch):
    monkeypatch.setattr(skillport, "_STATE", str(tmp_path / "missing"))
    try:
        skillport.installed_pack()
        assert False, "expected SkillportNotConfigured"
    except skillport.SkillportNotConfigured:
        pass
