# Trademark Application Status Automation

This project automates the process of retrieving trademark application details from the [Indian Trademark Registry](https://tmrsearch.ipindia.gov.in/eregister/) using Selenium and Optical Character Recognition (OCR). The script navigates the website, extracts CAPTCHA images, processes them using EasyOCR, and submits the application number for retrieval of relevant details.

## 📌 Features
- **Automated Navigation**: Uses Selenium WebDriver to interact with the website.
- **CAPTCHA Recognition**: Captures and processes CAPTCHA images using EasyOCR.
- **Data Extraction**: Inputs application numbers and retrieves the associated trademark details.
- **Headless Execution Support**: Can be modified to run without opening a browser window.

## 🛠️ Prerequisites & Installation
To set up the project, ensure you have the following:

- **Python 3.x** installed on your system.
- **Google Chrome** and the appropriate [ChromeDriver](https://sites.google.com/chromium.org/driver/) installed.
- Required Python libraries (listed in `requirements.txt`).

### 🔧 Install Dependencies
Clone the repository and install the required dependencies:
```sh
git clone https://github.com/your-username/trademark-scraper.git
cd trademark-scraper
pip install -r requirements.txt

⚠️ Important Notes, License & Contribution
CAPTCHA recognition is handled by EasyOCR, but its accuracy may vary based on the image clarity.

Contributions: Issues and feature requests are welcome. If you have suggestions for improvements, feel free to submit a pull request or open an issue.

🔗 Author: Rajkumar Wankhade
📧 Contact: rjkumarwankhade@gmail.com
