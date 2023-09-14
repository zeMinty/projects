from PIL import Image
from sys import argv as arguments


def main():
    infile = None
    outfile = None

    for arg in arguments:
        if "if=" in arg:
            infile = arg[3:]
        elif "of=" in arg:
            outfile = arg[3:]

    if infile is None or outfile is None:
        print(
            f"~ Missing arguments!\n~ Usage example:\n$ python img2ico.py if='/path/to/some file/file.png' of='/path/to/new file/file.ico'"
        )
        return

    img = Image.open(infile)
    img.save(outfile, format="ICO")


if __name__ == "__main__":
    main()
