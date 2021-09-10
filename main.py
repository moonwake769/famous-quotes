#! /usr/bin/python3

"""
Import all libraries.

    argparse    -   Command line parsing library.
    ast         -   Safely evaluate an expression node or a string
                    containing a Python literal or container display.
    json        -   Lightweight format for storing and transporting data.
    random      -   Random variable generators.
"""
import argparse
import ast
import json
import random

PATH =
filename = f'{PATH}/famous-quotes/data.json'

def read_data():
    """ Get data with quotes from data.json.

    Try to open the file with data and safely evaluate it from string
    to Python dictionary using ast.literal_eval()-method.

    Except if the file not found then create the file with
    empty json-template to be uploaded in.

    Return data.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as data_json:
            data = ast.literal_eval(data_json.read())
    except FileNotFoundError:
        template = "[\n\t{\n\" \":\" \"\n}\n\b]"
        with open(filename, 'w') as data_json:
            data = data_json.write(template)

    return data


def update_data(new_data):
    """ Write all quotes to data.json.

    Try to open data file and dump new data to it.

    Except if the file not found then let the user know that
    file can't be found.
    """
    try:
        with open(filename, 'w') as data_json:
            json.dump(new_data, data_json, indent=4)
    except FileNotFoundError:
        msg = "Can't find {0}".format(filename)
        print(msg)


def add_data():
    """Get a name and a quote of a person from a user."""
    name = input('\n' + "Type in the name of the person: ")
    quote = input("Type in the quote of the person: ")

    data = read_data()

    name_quote = {}
    name_quote[name] = quote

    data.append(name_quote.copy())
    print("The quote is successfully added." + '\n')

    return data


def show_data():
    """Display a quote to the user."""
    data = read_data()
    if data:
        content = data[random.randint(0, len(data) - 1)]
        for name, quote in content.items():
            output = list(name.title() + " said once: " + "\"" + quote + "\"")

            if len(output) > 80:
                if ' ' in output[65:80]:
                    output.insert(output.index(' ', 65, 80), "\n\t")
                if ' ' in output[132:152]:
                    output.insert(output.index(' ', 132, 152), "\n\t")
                if ' ' in output[212:232]:
                    output.insert(output.index(' ', 212, 232), "\n\t")

            print("~" * 80)
            print('\n\n\t' + ''.join(output) + '\n\n\t')
            print("~" * 80)
    else:
        msg = '\n' + "Your quote's list is empty." + '\n'
        print(msg)


def remove_data():
    """Remove a quote from data.json."""
    data = read_data()
    if data:
        count = 1
        for content in data:
            for name, quote in content.items():
                content = (str(count) + ") " + name.title() +
                    ": \"" + quote[:50] + "...\"")
                print(content)
                count += 1
        print("\nEnter q to quit.")
        user_input = input(
            "\nChoose the number of the quote that you would like to remove: "
        )
        if user_input == "q":
            exit()
        else:
            del data[int(user_input) - 1]
            print("The quote is successfully removed." + '\n')
            update_data(data)
    else:
        msg = '\n' + "Your quote's list is already empty." + '\n'
        print(msg)


def cli_parser():
    """Run the programme from CLI."""
    parser = argparse.ArgumentParser(
        prog = 'fq',
        description = "Display a quote of a famous person.",
        formatter_class = argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-s", "--show",
        default = False,
        action = "store_true",
        help = "Show a quote."
    )
    parser.add_argument(
        "-a", "--add",
        default = False,
        action = "store_true",
        help = "Add a new quote."
    )
    parser.add_argument(
        "-r", "--remove",
        default = False,
        action = "store_true",
        help = "Remove a quote."
    )
    parser.add_argument(
        "-d", "--delete",
        default = False,
        action = "store_true",
        help = "Delete the programme."
    )
    args = parser.parse_args()

    if args.show:
        show_data()

    if args.add:
        new_data = add_data()
        update_data(new_data)

    if args.remove:
        remove_data()

    if args.delete:
        # See fq script.
        pass


def run():
    """Run the programme."""
    cli_parser()


if __name__ == '__main__':
    run()
