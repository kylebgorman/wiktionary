"""Opens a Wiktionary page for a given word.

The user can also control which Wiktionary with `--langcode` or can specify an
anchor tag with `--anchor`.
"""

import argparse
from urllib import parse
import webbrowser


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--langcode",
        default="en",
        help="two-character language code identifying the language of "
        "Wiktionary (not necessary of the target word). "
        "Default: %(default)s.",
    )
    parser.add_argument("--anchor", help="optional anchor tag")
    parser.add_argument("word", help="target word")
    args = parser.parse_args()
    base_url = f"https://{args.langcode}.wiktionary.org"
    word_encoded = parse.quote(args.word)
    anchor = f"#{args.anchor}" if args.anchor else ""
    webbrowser.open(f"{base_url}/wiki/{word_encoded}{anchor}")


if __name__ == "__main__":
    main()
