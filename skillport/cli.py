"""skillport command line interface."""
import argparse
import os
import sys

from skillport_presets import get_pack
from skillport_presets._sync import ensure_synced, _SYNC_MARKER


def _sync():
    if os.path.exists(_SYNC_MARKER):
        os.unlink(_SYNC_MARKER)
    print("skillport: fetching latest skill pack ...")
    try:
        ensure_synced()
    except Exception:
        print(
            "skillport: warning - registry unreachable, keeping current pack.",
            file=sys.stderr,
        )
        return 0
    print("skillport: skill pack installed.")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(prog="skillport", description=__doc__)
    sub = parser.add_subparsers(dest="command")
    sub.add_parser(
        "sync",
        help="pull the latest skill pack from the registry and install it",
    )
    args = parser.parse_args(argv)

    if args.command == "sync":
        sys.exit(_sync())
    parser.print_help()


if __name__ == "__main__":
    main()
