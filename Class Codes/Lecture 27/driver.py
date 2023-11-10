from agent import *
from functions import *

def main():
    agent = Agent()
    while True:
        print_menu()
        choice = int(input ('Enter Your Choice: '))
        if choice == 1:
            agent.add_property()
        elif choice == 2:
            agent.show_match_property()
        elif choice == 3:
            agent.show_all_properties()
        elif choice == 4:
            agent.modify_property()
        else:
            print ('Thank, for using the system')
            break
main()

