import requests
import re
from bs4 import BeautifulSoup

print("\033[1;31m" + r"""
                                 
 _____ _____ _____ _____ __ __ 
|   | |   __| __  | __  |  |  |
| | | |   __| __ -| __ -|_   _|
|_|___|_____|_____|_____| |_|  
                               
""" + "\033[0m")

print("\033[1;31m" + "Made by Goof" + "\033[0m")


input("\033[1;31m" + "Press Enter to start..." + "\033[0m")

website_url = input("\033[1;31m" + "Enter the website URL: " + "\033[0m")


response = requests.get(website_url)


if response.status_code == 200:
    
    soup = BeautifulSoup(response.text, 'html.parser')

    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', soup.text)
    phone_numbers = re.findall(r'\b\d{10}\b', soup.text)

    related_links = [link.get('href') for link in soup.find_all('a')]

    print("\033[1;31m" + "\nWebsite Details:" + "\033[0m")
    print(f"Title: {soup.title.string}")
    print(f"URL: {website_url}")

    
    print("\033[1;31m" + "\nEmails found:" + "\033[0m")
    if not emails:
        print("None found")
    else:
        for email in emails:
            print(email)

    print("\033[1;31m" + "\nPhone numbers found:" + "\033[0m")
    if not phone_numbers:
        print("None found")
    else:
        for phone_number in phone_numbers:
            print(phone_number)

    print("\033[1;31m" + "\nRelated Links:" + "\033[0m")
    if not related_links:
        print("None found")
    else:
        for link in related_links:
            print(link)

else:
    print(f"Error accessing the website. Status code: {response.status_code}")


input("\033[1;31m" + "\nPress Enter to exit..." + "\033[0m")
