"""skillport - drop-in skills and presets for your coding agent."""
import os

from skillport_presets import DEFAULT_PACK, get_pack

__version__ = "0.6.2"

_STATE = os.path.expanduser("~/.skillport/installed")


class SkillportNotConfigured(RuntimeError):
    pass


def installed_pack():
    """Return the currently installed skill pack, or raise if none is synced yet."""
    if not os.path.exists(_STATE):
        raise SkillportNotConfigured(
            "no skill pack installed yet. Run: skillport sync"
        )
    with open(_STATE) as f:
        return f.read().strip()
