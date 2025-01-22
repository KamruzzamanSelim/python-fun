# IMPORT DATA FROM GOOGLE DRIVE TO KAGGLE OR GOOGLE COLAB

In most cases, when we are working with CSV file that is stored in Google Drive, we can easliy read the file either in Kaggle or Google Colab. You have to follow below steps to read CSV files.

---

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Data Import Examples](#data-import-examples)
6. [Contributing](#contributing)
7. [License](#license)

---

## Overview
This project demonstrates how to work with datasets in Python using Pandas, including importing data from various sources such as Kaggle and Google Drive. It includes step-by-step examples and error-handling tips for seamless execution.

---

## Features
- **Import CSV Files**: Example code for reading datasets from Kaggle and Google Drive.
- **Data Analysis**: Use Pandas for inspecting and manipulating datasets.
- **Error Handling**: Ensure file paths are correct and handle missing files gracefully.

---

## Installation

### Prerequisites
- Python 3.x
- Pandas Library
- Jupyter Notebook / Google Colab

### Setting Up
Clone this repository:
```bash
git clone https://github.com/KamruzzamanSelim/python-fun.git
cd your-repo
```

Install required libraries:
```bash
pip install pandas
```

---

## Usage

### Example 1: Importing CSV from Kaggle
```python
import pandas as pd
# Read CSV file
data = pd.read_csv('/kaggle/input/folder-name/file-name.csv')
print(data.head())
```

### Example 2: Importing CSV from Google Drive in Colab
#### Mount Google Drive
```python
from google.colab import drive
drive.mount('/content/drive')
```
#### Read CSV File
```python
import pandas as pd
data = pd.read_csv('/content/drive/My Drive/file-name.csv')
print(data.head())
```

---

## Data Import Examples

### Kaggle
1. Ensure you have set up the dataset in the Kaggle environment.
2. Use the correct path to the file as shown in the usage example.

### Google Drive
1. Mount Google Drive in your Colab notebook.
2. Copy the exact file path and use it in your code.

---

## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

---

## Acknowledgments
- [Google Colab](https://colab.research.google.com/)
- [Kaggle](https://www.kaggle.com/)
- Pandas Documentation: [https://pandas.pydata.org/](https://pandas.pydata.org/)

