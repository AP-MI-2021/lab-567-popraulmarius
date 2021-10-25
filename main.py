from Tests.TESTCRUD import *
from UserInterface.console import run_ui


def main():
    rezervari=[]
    rezervari= run_ui(rezervari)

if __name__ == '__main__':
    test_create()
    test_read()
    test_update()
    test_upgrade()
    main()