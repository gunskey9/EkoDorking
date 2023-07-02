#!/usr/bin/python3
import os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from termcolor import colored
import random
import subprocess

# Clear the screen
os.system('clear')

# Use subprocess to run the figlet command and capture its output
output = subprocess.check_output(["figlet", "-f", "slant", "-l", "-w", "160", "⊗EkoDorking⊗"])

# Print the output
print('\033[93m' + output.decode() + '\033[0m')

# Ask the user for the Google dork(s)
dorks = input("Please enter a Google dork or the filename containing the list of Google dorks: ")

# Check if the input is a file or a single dork
if os.path.isfile(dorks):
    # Read the Google dorks from the file
    with open(dorks, 'r') as file:
        dorks = file.readlines()
else:
    dorks = [dorks]

# Ask the user how many results they want to display
num_results = int(input("How many results would you like to display? "))

# Initialize the result list
results = []

# Define the search engines and user agents
search_engines = {
    'Bing': 'https://www.bing.com/search?q=',
}
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
]

# Loop through each dork and search on the search engines
with tqdm(total=len(dorks), desc="Searching dorks") as pbar1:
    for dork in dorks:
        # Shuffle the user agents for randomization
        random.shuffle(user_agents)

        # Loop through each search engine and search with the dork
        for engine_name, engine_url in search_engines.items():
            # Shuffle the user agents for each search engine
            random.shuffle(user_agents)

            # Pick a random user agent for each search engine
            headers = {'User-Agent': user_agents[0]}

            # Search with the dork on the search engine
            url = engine_url + dork.strip()
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract the results from the search engine
            search_results = soup.find_all('li', class_='b_algo')[:num_results]

            # Add the results to the list
            results.extend(search_results)

            # Update the progress bar with the number of sites found so far
            pbar1.set_postfix({'Sites found': len(results)})
            pbar1.update()

# Extract the website addresses from the results
website_addresses = []
for result in results:
    if result.a:
        link = result.a['href']
        if engine_name == 'Google':
            if link.startswith('/url?q='):
                link = link[7:]
            if '&' in link:
                link = link[:link.find('&')]
        elif engine_name == 'Bing':
            if link.startswith('http') or link.startswith('https'):
                link = link.split()[0]
                if 'bing' not in link.lower():  # Exclude results with 'bing' in the URL
                    website_addresses.append(link)
            else:
                continue  # Skip any results that are not valid URLs

# Prompt the user if they want to see the websites
show_websites = input("Would you like to see the websites? (y/n): ")
if show_websites.lower() == "y":
    # Display the website addresses
    print("" + '-'*80)
    print(colored("Here are the top {} website addresses:".format(num_results), "yellow"))
    for website in website_addresses:
        print(website)

    # Save the website addresses to a file
    save_websites = input("Would you like to save the website addresses to a file? (y/n): ")
    if save_websites.lower() == "y":
        file_path = input("Where would you like to save the file? ")
        with open(file_path, 'w') as file:
            for website in website_addresses:
                file.write(website + "")

# Save the website addresses to a file without displaying them
else:
    save_websites = input("Would you like to save the website addresses to a file? (y/n): ")
    if save_websites.lower() == "y":
        file_path = input("Where would you like to save the file? ")
        with open(file_path, 'w') as file:
            for website in website_addresses:
                file.write(website + "")
