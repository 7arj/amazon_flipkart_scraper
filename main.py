import os

def run_amazon():
    os.system('python amazon.py')


def run_flipkart():
    os.system('python flipkart.py')

def main():

    print("Welcome to the Web Scraper")


    while True:
        should_countinue = True
        print("\nEnter 1 to run Amazon Scraping")
        print("Enter 2 to run Flipkart Scraping")
        print("Enter 3 to exit")

        user_input = input("\nPlease enter your choice » ")

        if user_input == '1':
              run_amazon()
              print("Do you want to compare the price on Flipkart")
              comp_inp=input("\nYes/No: ")
              if comp_inp == 'Yes':
                  run_flipkart()
              elif comp_inp == 'No':
                  should_countinue=False
              else:
                  print("Please enter either Yes or No")
        elif user_input == '2':
            run_flipkart()
            print("Do you want to compare the price on Flipkart")
            comp_inp = input("\nYes/No: ")
            if comp_inp == 'Yes':
                run_amazon()
            elif comp_inp == 'No':
                should_countinue = False
            else:
                print("Please enter either Yes or No")
        elif user_input == '3':
            print(
                "\nThank You! for using Web Scraper")
            print("\n")
            break
        else:
            print("Please enter 1, 2 or 3")


if __name__ == '__main__':
    main()