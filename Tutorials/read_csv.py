#import csv file from Kaggle
import pandas as pd
data = pd.read_csv('/kaggle/input/folder-name/file-name.csv')

#import csv file from Google Drive in Colab
#Mount google drive
from google.colab import drive
drive.mount('/content/drive')
#Read csv file
import pandas as pd
data = pd.read_csv('/content/drive/My Drive/file-name.csv')