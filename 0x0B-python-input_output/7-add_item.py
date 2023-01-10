#!/usr/bin/python3
""" Add Arguments to Python List Module """


if __name__ == "__main__":
    from sys import argv
    save_to = __import__('5-save_to_json_file').save_to_json_file
    load_from = __import__('6-load_from_json_file').load_from_json_file

    args = []
    try:
        args = load_from("add_item.json")
        for elem in argv[1:]:
            args.append(elem)
        save_to(args, "add_item.json")
    except FileNotFoundError:
        for elem in argv[1:]:
            args.append(elem)
        save_to(args, "add_item.json")
