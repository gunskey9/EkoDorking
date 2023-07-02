yo# ⊗EkoDorking⊗ - Google Dorking Tool

![EkoDorking](https://example.com/path/to/logo.png)

⊗EkoDorking⊗ is a Python script designed to perform Google Dorking, a technique used to find vulnerable websites or sensitive information on the internet using specific search queries (dorks). This tool allows you to enter a single dork or a list of dorks from a file and then searches for those dorks on various search engines to gather a list of website addresses that match the query.

## Prerequisites

Before running the ⊗EkoDorking⊗ script, make sure you have the following installed:

- Python 3
- Python libraries: `os`, `requests`, `BeautifulSoup`, `tqdm`, `termcolor`

You can install the required Python libraries using `pip`:

```bash
pip install requests beautifulsoup4 tqdm termcolor
```

You also need to have the `figlet` program installed on your system. On Ubuntu, you can install it using:

```bash
sudo apt-get install figlet
```

## How to Use

1. Clone this repository or download the `ekodorking.py` file.

2. Open a terminal and navigate to the directory containing the `ekodorking.py` file.

3. To run the program, use the following command:

   ```bash
   python ekodorking.py
   ```

4. The program will display the ⊗EkoDorking⊗ banner, and then it will prompt you to enter a Google dork or the filename containing a list of Google dorks.

5. If you choose to enter a single dork, type the dork and press Enter. If you choose to use a file, make sure the file contains one dork per line.

6. Next, the program will ask you how many search results you want to display.

7. The script will then start searching for the dorks on various search engines (currently supporting Bing), and it will retrieve the top search results.

8. If you choose to see the websites, the program will display the website addresses found for each dork.

9. You have the option to save the website addresses to a file if desired.

10. If you chose not to display the websites, the program will ask if you still want to save the website addresses to a file.

## Disclaimer

This tool is intended for educational and ethical purposes only. Google Dorking can potentially lead to unauthorized access or disclosure of sensitive information. Always ensure that you have proper authorization before using this tool on any website.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Credits

This project was created by [Eko](https://github.com/gunskey9). Feel free to contribute to the project by submitting issues or pull requests.

## Contact
If you have any questions elderlyxcore@gmail.com
If you have any questions or suggestions regarding the ⊗EkoDorking⊗ tool, please feel free to contact us at [email@example.com](mailto:email@example.com).
