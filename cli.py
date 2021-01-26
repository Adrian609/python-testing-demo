import argparse

def main():
    parser = argparse.ArgumentParser(prog='cli')
    parser.add_argument('--foo', help="the foo option, doesn't work nice!")
    parser.parse_args()
    parser.print_help()

if __name__ == '__main__':
    main()