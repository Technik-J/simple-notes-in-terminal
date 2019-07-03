import argparse
import datetime
import sys
import config_file


def fromCommandLine(words_list, simple):
    words_str = ' '.join(words_list)
    if not simple:
        user_comment = input("Comment: ")
        write("```shell\n{} # {}\n```".format(words_str, user_comment))
    else:
        write(words_str)


def fromStandartInput(stringFromStdin, user_comment, simple):
    if not simple:
        write("{}\n```shell\n{}\n```".format(user_comment, stringFromStdin))
    else:
        write(stringFromStdin)


def write(string_to_write):
    with open(config_file.file_location, 'a', encoding='utf-8') as f:
        timestamp = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        f.write("###### {}\n{}\n".format(timestamp, string_to_write))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--simple', action='store_true',
                        help='This is a simple note. Do not wrap in code block and do not add a comment')
    args = parser.parse_known_args()

    if not sys.stdin.isatty():
        fromStandartInput(sys.stdin.read(), " ".join(args[1]), args[0].simple)
    else:
        fromCommandLine(args[1], args[0].simple)
