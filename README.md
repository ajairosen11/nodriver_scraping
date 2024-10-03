
# Social Media Scraper using NoDriver and Asyncio

This Python project scrapes social media metrics from URLs provided in an Excel file and saves the results to another Excel file. It uses the **NoDriver** library, an asynchronous browser controller, to handle headless browsing and web scraping.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Explanation of NoDriver](#explanation-of-nodriver)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started, you need to have Python 3.x installed. You can then install the required libraries using the `pip` package manager.

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/social-media-scraper.git
   ```

2. Install dependencies:

   ```bash
   pip install pandas nodriver asyncio
   ```

3. Place the Excel file containing the URLs to be scraped in the root directory of the project and name it `urls_to_scrap.xlsx`.


## Usage

The script reads URLs from an Excel file named `urls_to_scrap.xlsx` and scrapes social media metrics from those pages. The scraped data is saved to an Excel file named `socialblade.xlsx`.

To run the script, use the following command:

```bash
python nodriver_script.py
```

### Input File Format

The input Excel file (`urls_to_scrap.xlsx`) should have a column named `URL to Scrap` which lists the URLs that the script will scrape.

### Output

The script will create an output file named `socialblade.xlsx` that contains the following columns:
- `Date`: The date of the metric.
- `Day`: The day of the week.
- `Change in Likes`: The change in likes on the social media platform.
- `Likes`: The total number of likes.
- `Change in Talking About`: The change in the "Talking About" metric.
- `Talking About`: The total number of "Talking About" mentions.
- `URL`: The URL of the scraped page.

## Project Structure

```text
social-media-scraper/
│
├── nodriver_script.py           # Main script that performs the web scraping
├── urls_to_scrap.xlsx   # Input Excel file containing the URLs to scrape
├── socialblade.xlsx     # Output Excel file with scraped data
└── README.md            # Project documentation
```

## Explanation of NoDriver

[NoDriver](https://ultrafunkamsterdam.github.io/nodriver/) is a lightweight, asynchronous browser automation tool. It allows for controlling a web browser (such as Chrome or Firefox) without needing to install the official browser drivers like `chromedriver` or `geckodriver`. This makes it highly suitable for automation and scraping tasks where you need to interact with web pages but want to avoid the overhead of setting up and maintaining driver dependencies.

### Key Features of NoDriver:
- **Headless Browsing**: NoDriver allows controlling browsers in headless mode, meaning no graphical user interface (GUI) is needed.
- **Asynchronous Execution**: By using `asyncio`, NoDriver enables you to perform non-blocking operations. This is particularly useful for web scraping because it allows you to interact with multiple web elements without freezing or blocking other operations.
- **Simple Setup**: Unlike traditional browser automation tools that require setting up external drivers, NoDriver simplifies the process by eliminating the need for such drivers.

### Use Case

In this project, NoDriver is used to:
- Launch a headless browser session asynchronously.
- Navigate to specific URLs and interact with dynamic web content to extract social media metrics.
- Manage timeouts and retries to ensure that the script doesn't hang while waiting for elements to load on the page.

By utilizing NoDriver, the script becomes more efficient and scalable, allowing you to scrape data from multiple URLs with minimal setup.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Contributions in the form of bug reports, feature suggestions, or code improvements are welcome.

## License
