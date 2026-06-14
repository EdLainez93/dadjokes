# This is the Code in Place 2026's Capstone Project that I am submitting
# I have utilized the concepts of flow control and function calling to create a Dad Joke generator to print out the daily dad joke or to print out a random dad joke
# I have also implemented the try-except handling, which took further advanced reading to understand its use cases
# I have utilized the concepts of flow logic, conditions, user input, JSON and API parsing to best create a simple, but amusing script for people to try and enjoy!

import requests

def random_dad_jokes():
    try:
        url = "https://groandeck.com/api/v1/random"
        response = requests.get(url)
        response.raise_for_status()
        joke = response.json()

        print(f"\nSetup: {joke['setup']}")
        print(f"Punchline: {joke['punchline']}\n")
    except requests.RequestException:
        print("Dad's out of jokes for the time being. Check back later!")

def daily_dad_jokes():
  
    url="https://groandeck.com/api/v1/daily"
    response = requests.get(url)
    joke = response.json()

    print(f"\nSetup: {joke['setup']}")
    print(f"Punchline: {joke['punchline']}\n")

def main():

    while True:
        choice = input("""
Please enter one of the following options:
1. Random
2. Daily
3. Quit                      
""").lower()
        
        if choice in ["random","1"]:
            random_dad_jokes()
        elif choice in ["daily","2"]:
            daily_dad_jokes()
        elif choice in ["quit","3"]:
            print("Goodbye!")
            break
        else:
            print("Please pick a valid option!")

if __name__ == '__main__':
    main()
