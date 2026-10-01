import json


def new_game():
    return {'items': [], 'src': 10, 'dst': 0, 'events': {1: True}, 'paused': False, 'balance': 10, 'clock': 0, 'next_id': 1, 'snapshot': 5, 'value': 5, 'log': [], 'settled': False}

def bug_6(state):
    return len(state["items"]) - 1

def bug_13(state):
    state["src"] -= 5
    return True

def bug_20(state):
    return True

def bug_27(state):
    return True

def bug_4(state):
    return True

def bug_11(state):
    state["balance"] -= 20
    return True

def bug_18(state):
    return True

def bug_25(state):
    state["clock"] += 1
    return state["clock"]

def bug_2(state):
    return "empty"

def bug_9(state):
    state["next_id"] += 1
    return state["next_id"]

def bug_30(state):
    return True

def bug_31(state):
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
