import json


def new_game():
    return {'items': [], 'src': 10, 'dst': 0, 'events': {1: True}, 'paused': False, 'balance': 10, 'clock': 0, 'next_id': 1, 'snapshot': 5, 'value': 5, 'log': [], 'settled': False}


def bug_6(state):
    return len(state["items"])


def bug_13(state):
    if state.get("src", 0) < 5:
        return False
    state["src"] -= 5
    state["dst"] += 5
    return True


def bug_20(state):
    state["events"].pop(1, None)
    return True


def bug_27(state, a=None, b=None):
    if a is None or b is None:
        return False
    if a == b:
        return False
    return True


def bug_4(state):
    if state.get("paused"):
        return False
    return True


def bug_11(state):
    amount = 20
    if state.get("balance", 0) < amount:
        return False
    state["balance"] -= amount
    return True


def bug_18(state):
    event_id = 2
    if state["events"].get(event_id):
        return False
    state["events"][event_id] = True
    return True


def bug_25(state):
    if state.get("paused"):
        return state["clock"]
    state["clock"] += 1
    return state["clock"]


def bug_2(state):
    return None


def bug_9(state):
    return state["next_id"]


def bug_30(state):
    checkpoint_log = [
        entry for entry in state.get("log", [])
        if not (isinstance(entry, tuple) and len(entry) == 2 and entry[1] == "failed")
    ]
    staged_value = state["value"]
    staged_log = list(state["log"])
    try:
        staged_value += 1
        staged_log.append(("op", "succeeded"))
        if any(
            isinstance(entry, tuple) and len(entry) == 2 and entry[1] == "failed"
            for entry in staged_log
        ):
            raise RuntimeError("transaction step failed")
    except Exception:
        state["value"] = state["snapshot"]
        state["log"] = checkpoint_log
        return False
    state["value"] = staged_value
    state["log"] = staged_log
    return True


def bug_31(state):
    if state.get("settled"):
        return False
    return True


def main():
    print("命令: run/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()
