{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pandas in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (2.2.2)\n",
      "Requirement already satisfied: numpy>=1.22.4 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from pandas) (1.26.4)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from pandas) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from pandas) (2024.1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from pandas) (2023.3)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from python-dateutil>=2.8.2->pandas) (1.16.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "%pip install pandas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: numpy in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (1.26.4)\n",
      "Note: you may need to restart the kernel to use updated packages.\n",
      "Collecting nltk\n",
      "  Using cached nltk-3.9.1-py3-none-any.whl.metadata (2.9 kB)\n",
      "Collecting spacy\n",
      "  Downloading spacy-3.7.6-cp310-cp310-win_amd64.whl.metadata (27 kB)\n",
      "Requirement already satisfied: click in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from nltk) (8.1.7)\n",
      "Requirement already satisfied: joblib in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from nltk) (1.4.2)\n",
      "Collecting regex>=2021.8.3 (from nltk)\n",
      "  Downloading regex-2024.7.24-cp310-cp310-win_amd64.whl.metadata (41 kB)\n",
      "Collecting tqdm (from nltk)\n",
      "  Downloading tqdm-4.66.5-py3-none-any.whl.metadata (57 kB)\n",
      "Collecting spacy-legacy<3.1.0,>=3.0.11 (from spacy)\n",
      "  Downloading spacy_legacy-3.0.12-py2.py3-none-any.whl.metadata (2.8 kB)\n",
      "Collecting spacy-loggers<2.0.0,>=1.0.0 (from spacy)\n",
      "  Downloading spacy_loggers-1.0.5-py3-none-any.whl.metadata (23 kB)\n",
      "Collecting murmurhash<1.1.0,>=0.28.0 (from spacy)\n",
      "  Downloading murmurhash-1.0.10-cp310-cp310-win_amd64.whl.metadata (2.0 kB)\n",
      "Collecting cymem<2.1.0,>=2.0.2 (from spacy)\n",
      "  Downloading cymem-2.0.8-cp310-cp310-win_amd64.whl.metadata (8.6 kB)\n",
      "Collecting preshed<3.1.0,>=3.0.2 (from spacy)\n",
      "  Downloading preshed-3.0.9-cp310-cp310-win_amd64.whl.metadata (2.2 kB)\n",
      "Collecting thinc<8.3.0,>=8.2.2 (from spacy)\n",
      "  Downloading thinc-8.2.5-cp310-cp310-win_amd64.whl.metadata (15 kB)\n",
      "Collecting wasabi<1.2.0,>=0.9.1 (from spacy)\n",
      "  Using cached wasabi-1.1.3-py3-none-any.whl.metadata (28 kB)\n",
      "Collecting srsly<3.0.0,>=2.4.3 (from spacy)\n",
      "  Downloading srsly-2.4.8-cp310-cp310-win_amd64.whl.metadata (20 kB)\n",
      "Collecting catalogue<2.1.0,>=2.0.6 (from spacy)\n",
      "  Using cached catalogue-2.0.10-py3-none-any.whl.metadata (14 kB)\n",
      "Collecting weasel<0.5.0,>=0.1.0 (from spacy)\n",
      "  Downloading weasel-0.4.1-py3-none-any.whl.metadata (4.6 kB)\n",
      "Collecting typer<1.0.0,>=0.3.0 (from spacy)\n",
      "  Downloading typer-0.12.4-py3-none-any.whl.metadata (15 kB)\n",
      "Requirement already satisfied: requests<3.0.0,>=2.13.0 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from spacy) (2.32.3)\n",
      "Collecting pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4 (from spacy)\n",
      "  Using cached pydantic-2.8.2-py3-none-any.whl.metadata (125 kB)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from spacy) (3.1.4)\n",
      "Requirement already satisfied: setuptools in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from spacy) (72.1.0)\n",
      "Requirement already satisfied: packaging>=20.0 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from spacy) (24.1)\n",
      "Collecting langcodes<4.0.0,>=3.2.0 (from spacy)\n",
      "  Using cached langcodes-3.4.0-py3-none-any.whl.metadata (29 kB)\n",
      "Requirement already satisfied: numpy>=1.19.0 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from spacy) (1.26.4)\n",
      "Collecting language-data>=1.2 (from langcodes<4.0.0,>=3.2.0->spacy)\n",
      "  Downloading language_data-1.2.0-py3-none-any.whl.metadata (4.3 kB)\n",
      "Collecting annotated-types>=0.4.0 (from pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4->spacy)\n",
      "  Using cached annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)\n",
      "Collecting pydantic-core==2.20.1 (from pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4->spacy)\n",
      "  Downloading pydantic_core-2.20.1-cp310-none-win_amd64.whl.metadata (6.7 kB)\n",
      "Requirement already satisfied: typing-extensions>=4.6.1 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4->spacy) (4.11.0)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from requests<3.0.0,>=2.13.0->spacy) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from requests<3.0.0,>=2.13.0->spacy) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from requests<3.0.0,>=2.13.0->spacy) (2.2.2)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from requests<3.0.0,>=2.13.0->spacy) (2024.7.4)\n",
      "Collecting blis<0.8.0,>=0.7.8 (from thinc<8.3.0,>=8.2.2->spacy)\n",
      "  Downloading blis-0.7.11-cp310-cp310-win_amd64.whl.metadata (7.6 kB)\n",
      "Collecting confection<1.0.0,>=0.0.1 (from thinc<8.3.0,>=8.2.2->spacy)\n",
      "  Using cached confection-0.1.5-py3-none-any.whl.metadata (19 kB)\n",
      "Requirement already satisfied: colorama in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from tqdm->nltk) (0.4.6)\n",
      "Collecting shellingham>=1.3.0 (from typer<1.0.0,>=0.3.0->spacy)\n",
      "  Downloading shellingham-1.5.4-py2.py3-none-any.whl.metadata (3.5 kB)\n",
      "Collecting rich>=10.11.0 (from typer<1.0.0,>=0.3.0->spacy)\n",
      "  Using cached rich-13.7.1-py3-none-any.whl.metadata (18 kB)\n",
      "Collecting cloudpathlib<1.0.0,>=0.7.0 (from weasel<0.5.0,>=0.1.0->spacy)\n",
      "  Downloading cloudpathlib-0.18.1-py3-none-any.whl.metadata (14 kB)\n",
      "Collecting smart-open<8.0.0,>=5.2.1 (from weasel<0.5.0,>=0.1.0->spacy)\n",
      "  Downloading smart_open-7.0.4-py3-none-any.whl.metadata (23 kB)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from jinja2->spacy) (2.1.3)\n",
      "Collecting marisa-trie>=0.7.7 (from language-data>=1.2->langcodes<4.0.0,>=3.2.0->spacy)\n",
      "  Downloading marisa_trie-1.2.0-cp310-cp310-win_amd64.whl.metadata (9.0 kB)\n",
      "Collecting markdown-it-py>=2.2.0 (from rich>=10.11.0->typer<1.0.0,>=0.3.0->spacy)\n",
      "  Using cached markdown_it_py-3.0.0-py3-none-any.whl.metadata (6.9 kB)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from rich>=10.11.0->typer<1.0.0,>=0.3.0->spacy) (2.15.1)\n",
      "Requirement already satisfied: wrapt in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from smart-open<8.0.0,>=5.2.1->weasel<0.5.0,>=0.1.0->spacy) (1.14.1)\n",
      "Collecting mdurl~=0.1 (from markdown-it-py>=2.2.0->rich>=10.11.0->typer<1.0.0,>=0.3.0->spacy)\n",
      "  Using cached mdurl-0.1.2-py3-none-any.whl.metadata (1.6 kB)\n",
      "Using cached nltk-3.9.1-py3-none-any.whl (1.5 MB)\n",
      "Downloading spacy-3.7.6-cp310-cp310-win_amd64.whl (12.1 MB)\n",
      "   ---------------------------------------- 0.0/12.1 MB ? eta -:--:--\n",
      "   ------------------------------- -------- 9.7/12.1 MB 50.2 MB/s eta 0:00:01\n",
      "   ---------------------------------------- 12.1/12.1 MB 47.5 MB/s eta 0:00:00\n",
      "Using cached catalogue-2.0.10-py3-none-any.whl (17 kB)\n",
      "Downloading cymem-2.0.8-cp310-cp310-win_amd64.whl (39 kB)\n",
      "Downloading langcodes-3.4.0-py3-none-any.whl (182 kB)\n",
      "Downloading murmurhash-1.0.10-cp310-cp310-win_amd64.whl (25 kB)\n",
      "Downloading preshed-3.0.9-cp310-cp310-win_amd64.whl (122 kB)\n",
      "Using cached pydantic-2.8.2-py3-none-any.whl (423 kB)\n",
      "Downloading pydantic_core-2.20.1-cp310-none-win_amd64.whl (1.9 MB)\n",
      "   ---------------------------------------- 0.0/1.9 MB ? eta -:--:--\n",
      "   ---------------------------------------- 1.9/1.9 MB 52.9 MB/s eta 0:00:00\n",
      "Downloading regex-2024.7.24-cp310-cp310-win_amd64.whl (269 kB)\n",
      "Using cached spacy_legacy-3.0.12-py2.py3-none-any.whl (29 kB)\n",
      "Downloading spacy_loggers-1.0.5-py3-none-any.whl (22 kB)\n",
      "Downloading srsly-2.4.8-cp310-cp310-win_amd64.whl (481 kB)\n",
      "Downloading thinc-8.2.5-cp310-cp310-win_amd64.whl (1.5 MB)\n",
      "   ---------------------------------------- 0.0/1.5 MB ? eta -:--:--\n",
      "   ---------------------------------------- 1.5/1.5 MB 76.2 MB/s eta 0:00:00\n",
      "Downloading tqdm-4.66.5-py3-none-any.whl (78 kB)\n",
      "Downloading typer-0.12.4-py3-none-any.whl (47 kB)\n",
      "Using cached wasabi-1.1.3-py3-none-any.whl (27 kB)\n",
      "Downloading weasel-0.4.1-py3-none-any.whl (50 kB)\n",
      "Using cached annotated_types-0.7.0-py3-none-any.whl (13 kB)\n",
      "Downloading blis-0.7.11-cp310-cp310-win_amd64.whl (6.6 MB)\n",
      "   ---------------------------------------- 0.0/6.6 MB ? eta -:--:--\n",
      "   ---------------------------------------- 6.6/6.6 MB 67.6 MB/s eta 0:00:00\n",
      "Downloading cloudpathlib-0.18.1-py3-none-any.whl (47 kB)\n",
      "Using cached confection-0.1.5-py3-none-any.whl (35 kB)\n",
      "Downloading language_data-1.2.0-py3-none-any.whl (5.4 MB)\n",
      "   ---------------------------------------- 0.0/5.4 MB ? eta -:--:--\n",
      "   ---------------------------------------- 5.4/5.4 MB 81.3 MB/s eta 0:00:00\n",
      "Using cached rich-13.7.1-py3-none-any.whl (240 kB)\n",
      "Downloading shellingham-1.5.4-py2.py3-none-any.whl (9.8 kB)\n",
      "Downloading smart_open-7.0.4-py3-none-any.whl (61 kB)\n",
      "Downloading marisa_trie-1.2.0-cp310-cp310-win_amd64.whl (152 kB)\n",
      "Using cached markdown_it_py-3.0.0-py3-none-any.whl (87 kB)\n",
      "Using cached mdurl-0.1.2-py3-none-any.whl (10.0 kB)\n",
      "Installing collected packages: cymem, wasabi, tqdm, spacy-loggers, spacy-legacy, smart-open, shellingham, regex, pydantic-core, murmurhash, mdurl, marisa-trie, cloudpathlib, catalogue, blis, annotated-types, srsly, pydantic, preshed, nltk, markdown-it-py, language-data, rich, langcodes, confection, typer, thinc, weasel, spacy\n",
      "Successfully installed annotated-types-0.7.0 blis-0.7.11 catalogue-2.0.10 cloudpathlib-0.18.1 confection-0.1.5 cymem-2.0.8 langcodes-3.4.0 language-data-1.2.0 marisa-trie-1.2.0 markdown-it-py-3.0.0 mdurl-0.1.2 murmurhash-1.0.10 nltk-3.9.1 preshed-3.0.9 pydantic-2.8.2 pydantic-core-2.20.1 regex-2024.7.24 rich-13.7.1 shellingham-1.5.4 smart-open-7.0.4 spacy-3.7.6 spacy-legacy-3.0.12 spacy-loggers-1.0.5 srsly-2.4.8 thinc-8.2.5 tqdm-4.66.5 typer-0.12.4 wasabi-1.1.3 weasel-0.4.1\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "%pip install numpy\n",
    "%pip install nltk spacy\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                     id       asins   brand                  categories  \\\n",
      "0  AVpe7AsMilAPnD_xQ78G  B00QJDU3KY  Amazon  Amazon Devices,mazon.co.uk   \n",
      "1  AVpe7AsMilAPnD_xQ78G  B00QJDU3KY  Amazon  Amazon Devices,mazon.co.uk   \n",
      "2  AVpe7AsMilAPnD_xQ78G  B00QJDU3KY  Amazon  Amazon Devices,mazon.co.uk   \n",
      "3  AVpe7AsMilAPnD_xQ78G  B00QJDU3KY  Amazon  Amazon Devices,mazon.co.uk   \n",
      "4  AVpe7AsMilAPnD_xQ78G  B00QJDU3KY  Amazon  Amazon Devices,mazon.co.uk   \n",
      "\n",
      "  colors             dateAdded           dateUpdated  \\\n",
      "0    NaN  2016-03-08T20:21:53Z  2017-07-18T23:52:58Z   \n",
      "1    NaN  2016-03-08T20:21:53Z  2017-07-18T23:52:58Z   \n",
      "2    NaN  2016-03-08T20:21:53Z  2017-07-18T23:52:58Z   \n",
      "3    NaN  2016-03-08T20:21:53Z  2017-07-18T23:52:58Z   \n",
      "4    NaN  2016-03-08T20:21:53Z  2017-07-18T23:52:58Z   \n",
      "\n",
      "                  dimension  ean                         keys  ...  \\\n",
      "0  169 mm x 117 mm x 9.1 mm  NaN  kindlepaperwhite/b00qjdu3ky  ...   \n",
      "1  169 mm x 117 mm x 9.1 mm  NaN  kindlepaperwhite/b00qjdu3ky  ...   \n",
      "2  169 mm x 117 mm x 9.1 mm  NaN  kindlepaperwhite/b00qjdu3ky  ...   \n",
      "3  169 mm x 117 mm x 9.1 mm  NaN  kindlepaperwhite/b00qjdu3ky  ...   \n",
      "4  169 mm x 117 mm x 9.1 mm  NaN  kindlepaperwhite/b00qjdu3ky  ...   \n",
      "\n",
      "  reviews.rating                                 reviews.sourceURLs  \\\n",
      "0            5.0  https://www.amazon.com/Kindle-Paperwhite-High-...   \n",
      "1            5.0  https://www.amazon.com/Kindle-Paperwhite-High-...   \n",
      "2            4.0  https://www.amazon.com/Kindle-Paperwhite-High-...   \n",
      "3            5.0  https://www.amazon.com/Kindle-Paperwhite-High-...   \n",
      "4            5.0  https://www.amazon.com/Kindle-Paperwhite-High-...   \n",
      "\n",
      "                                        reviews.text  \\\n",
      "0  I initially had trouble deciding between the p...   \n",
      "1  Allow me to preface this with a little history...   \n",
      "2  I am enjoying it so far. Great for reading. Ha...   \n",
      "3  I bought one of the first Paperwhites and have...   \n",
      "4  I have to say upfront - I don't like coroporat...   \n",
      "\n",
      "                                reviews.title reviews.userCity  \\\n",
      "0              Paperwhite voyage, no regrets!              NaN   \n",
      "1           One Simply Could Not Ask For More              NaN   \n",
      "2  Great for those that just want an e-reader              NaN   \n",
      "3                    Love / Hate relationship              NaN   \n",
      "4                                   I LOVE IT              NaN   \n",
      "\n",
      "  reviews.userProvince    reviews.username  sizes upc     weight  \n",
      "0                  NaN          Cristina M    NaN NaN  205 grams  \n",
      "1                  NaN               Ricky    NaN NaN  205 grams  \n",
      "2                  NaN       Tedd Gardiner    NaN NaN  205 grams  \n",
      "3                  NaN              Dougal    NaN NaN  205 grams  \n",
      "4                  NaN  Miljan David Tanic    NaN NaN  205 grams  \n",
      "\n",
      "[5 rows x 27 columns]\n",
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 1597 entries, 0 to 1596\n",
      "Data columns (total 27 columns):\n",
      " #   Column                Non-Null Count  Dtype  \n",
      "---  ------                --------------  -----  \n",
      " 0   id                    1597 non-null   object \n",
      " 1   asins                 1597 non-null   object \n",
      " 2   brand                 1597 non-null   object \n",
      " 3   categories            1597 non-null   object \n",
      " 4   colors                774 non-null    object \n",
      " 5   dateAdded             1597 non-null   object \n",
      " 6   dateUpdated           1597 non-null   object \n",
      " 7   dimension             565 non-null    object \n",
      " 8   ean                   898 non-null    float64\n",
      " 9   keys                  1597 non-null   object \n",
      " 10  manufacturer          965 non-null    object \n",
      " 11  manufacturerNumber    902 non-null    object \n",
      " 12  name                  1597 non-null   object \n",
      " 13  prices                1597 non-null   object \n",
      " 14  reviews.date          1217 non-null   object \n",
      " 15  reviews.doRecommend   539 non-null    object \n",
      " 16  reviews.numHelpful    900 non-null    float64\n",
      " 17  reviews.rating        1177 non-null   float64\n",
      " 18  reviews.sourceURLs    1597 non-null   object \n",
      " 19  reviews.text          1597 non-null   object \n",
      " 20  reviews.title         1580 non-null   object \n",
      " 21  reviews.userCity      0 non-null      float64\n",
      " 22  reviews.userProvince  0 non-null      float64\n",
      " 23  reviews.username      1580 non-null   object \n",
      " 24  sizes                 0 non-null      float64\n",
      " 25  upc                   898 non-null    float64\n",
      " 26  weight                686 non-null    object \n",
      "dtypes: float64(7), object(20)\n",
      "memory usage: 337.0+ KB\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Cargar el dataset\n",
    "ruta_dataset = '7817_1.csv'\n",
    "df = pd.read_csv(ruta_dataset)\n",
    "\n",
    "# Verificar las primeras filas\n",
    "print(df.head())\n",
    "\n",
    "# Verificar la información general del dataset\n",
    "print(df.info())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import nltk\n",
    "\n",
    "# Definir la ruta de descarga\n",
    "nltk_data_path = os.path.join(os.getcwd(), 'nltk_data')\n",
    "\n",
    "# Configurar la variable de entorno NLTK_DATA\n",
    "os.environ['NLTK_DATA'] = nltk_data_path\n",
    "\n",
    "# Añadir la ruta de nltk_data a nltk\n",
    "nltk.data.path.append(nltk_data_path)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['This is a test sentence.']\n"
     ]
    }
   ],
   "source": [
    "import pickle\n",
    "import os\n",
    "\n",
    "# Ruta directa al archivo pickle\n",
    "ruta_pickle = os.path.join(os.getcwd(), 'nltk_data', 'tokenizers', 'punkt', 'english.pickle')\n",
    "\n",
    "# Intentar cargar el archivo directamente\n",
    "with open(ruta_pickle, 'rb') as f:\n",
    "    tokenizer = pickle.load(f)\n",
    "\n",
    "# Testear la tokenización\n",
    "from nltk.tokenize import word_tokenize\n",
    "\n",
    "# Usa el tokenizer cargado manualmente\n",
    "tokens = tokenizer.tokenize(\"This is a test sentence.\")\n",
    "print(tokens)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                                        reviews.text  \\\n",
      "0  I initially had trouble deciding between the p...   \n",
      "1  Allow me to preface this with a little history...   \n",
      "2  I am enjoying it so far. Great for reading. Ha...   \n",
      "3  I bought one of the first Paperwhites and have...   \n",
      "4  I have to say upfront - I don't like coroporat...   \n",
      "\n",
      "                                     texto_procesado  \n",
      "0  [i initially had trouble deciding between the ...  \n",
      "1  [allow me to preface this with a little histor...  \n",
      "2  [i am enjoying it so far great for reading had...  \n",
      "3  [i bought one of the first paperwhites and hav...  \n",
      "4  [i have to say upfront  i dont like coroporate...  \n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import string\n",
    "from nltk.corpus import stopwords\n",
    "\n",
    "# Cargar el dataset\n",
    "df = pd.read_csv('7817_1.csv')\n",
    "\n",
    "# Función para preprocesar texto usando el tokenizador cargado manualmente\n",
    "def preprocesar_texto(texto):\n",
    "    # Convertir a minúsculas\n",
    "    texto = texto.lower()\n",
    "    \n",
    "    # Eliminar puntuación\n",
    "    texto = texto.translate(str.maketrans('', '', string.punctuation))\n",
    "    \n",
    "    # Tokenización usando el tokenizador manual\n",
    "    tokens = tokenizer.tokenize(texto)\n",
    "    \n",
    "    # Eliminar stopwords\n",
    "    tokens = [word for word in tokens if word not in stopwords.words('english')]\n",
    "    \n",
    "    return tokens\n",
    "\n",
    "# Aplicar la función de preprocesamiento a la columna 'reviews.text'\n",
    "df['texto_procesado'] = df['reviews.text'].apply(lambda x: preprocesar_texto(str(x)))\n",
    "\n",
    "# Mostrar algunas filas procesadas\n",
    "print(df[['reviews.text', 'texto_procesado']].head())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting vaderSentiment\n",
      "  Downloading vaderSentiment-3.3.2-py2.py3-none-any.whl.metadata (572 bytes)\n",
      "Requirement already satisfied: requests in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from vaderSentiment) (2.32.3)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from requests->vaderSentiment) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from requests->vaderSentiment) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from requests->vaderSentiment) (2.2.2)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from requests->vaderSentiment) (2024.7.4)\n",
      "Downloading vaderSentiment-3.3.2-py2.py3-none-any.whl (125 kB)\n",
      "Installing collected packages: vaderSentiment\n",
      "Successfully installed vaderSentiment-3.3.2\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "%pip install vaderSentiment"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                                        reviews.text sentimiento\n",
      "0  I initially had trouble deciding between the p...    Positivo\n",
      "1  Allow me to preface this with a little history...    Positivo\n",
      "2  I am enjoying it so far. Great for reading. Ha...    Positivo\n",
      "3  I bought one of the first Paperwhites and have...    Positivo\n",
      "4  I have to say upfront - I don't like coroporat...    Positivo\n"
     ]
    }
   ],
   "source": [
    "from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer\n",
    "\n",
    "# Inicializar el analizador de sentimientos\n",
    "analyzer = SentimentIntensityAnalyzer()\n",
    "\n",
    "# Función para obtener el sentimiento\n",
    "def obtener_sentimiento(texto):\n",
    "    scores = analyzer.polarity_scores(texto)\n",
    "    # Clasificar como positivo, negativo o neutro basado en el puntaje compuesto\n",
    "    if scores['compound'] >= 0.05:\n",
    "        return 'Positivo'\n",
    "    elif scores['compound'] <= -0.05:\n",
    "        return 'Negativo'\n",
    "    else:\n",
    "        return 'Neutro'\n",
    "\n",
    "# Aplicar el análisis de sentimientos a las reseñas procesadas\n",
    "df['sentimiento'] = df['reviews.text'].apply(obtener_sentimiento)\n",
    "\n",
    "# Mostrar algunas filas con el sentimiento\n",
    "print(df[['reviews.text', 'sentimiento']].head())\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting en-core-web-sm==3.7.1\n",
      "  Downloading https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.7.1/en_core_web_sm-3.7.1-py3-none-any.whl (12.8 MB)\n",
      "     ---------------------------------------- 0.0/12.8 MB ? eta -:--:--\n",
      "     ----------------------- ---------------- 7.6/12.8 MB 42.7 MB/s eta 0:00:01\n",
      "     --------------------------------------- 12.8/12.8 MB 42.2 MB/s eta 0:00:00\n",
      "Requirement already satisfied: spacy<3.8.0,>=3.7.2 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from en-core-web-sm==3.7.1) (3.7.6)\n",
      "Requirement already satisfied: spacy-legacy<3.1.0,>=3.0.11 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (3.0.12)\n",
      "Requirement already satisfied: spacy-loggers<2.0.0,>=1.0.0 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (1.0.5)\n",
      "Requirement already satisfied: murmurhash<1.1.0,>=0.28.0 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (1.0.10)\n",
      "Requirement already satisfied: cymem<2.1.0,>=2.0.2 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (2.0.8)\n",
      "Requirement already satisfied: preshed<3.1.0,>=3.0.2 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (3.0.9)\n",
      "Requirement already satisfied: thinc<8.3.0,>=8.2.2 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (8.2.5)\n",
      "Requirement already satisfied: wasabi<1.2.0,>=0.9.1 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (1.1.3)\n",
      "Requirement already satisfied: srsly<3.0.0,>=2.4.3 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (2.4.8)\n",
      "Requirement already satisfied: catalogue<2.1.0,>=2.0.6 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (2.0.10)\n",
      "Requirement already satisfied: weasel<0.5.0,>=0.1.0 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (0.4.1)\n",
      "Requirement already satisfied: typer<1.0.0,>=0.3.0 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (0.12.4)\n",
      "Requirement already satisfied: tqdm<5.0.0,>=4.38.0 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (4.66.5)\n",
      "Requirement already satisfied: requests<3.0.0,>=2.13.0 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (2.32.3)\n",
      "Requirement already satisfied: pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (2.8.2)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (3.1.4)\n",
      "Requirement already satisfied: setuptools in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (72.1.0)\n",
      "Requirement already satisfied: packaging>=20.0 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (24.1)\n",
      "Requirement already satisfied: langcodes<4.0.0,>=3.2.0 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (3.4.0)\n",
      "Requirement already satisfied: numpy>=1.19.0 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (1.26.4)\n",
      "Requirement already satisfied: language-data>=1.2 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from langcodes<4.0.0,>=3.2.0->spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (1.2.0)\n",
      "Requirement already satisfied: annotated-types>=0.4.0 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4->spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (0.7.0)\n",
      "Requirement already satisfied: pydantic-core==2.20.1 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4->spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (2.20.1)\n",
      "Requirement already satisfied: typing-extensions>=4.6.1 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4->spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (4.11.0)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from requests<3.0.0,>=2.13.0->spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from requests<3.0.0,>=2.13.0->spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from requests<3.0.0,>=2.13.0->spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (2.2.2)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from requests<3.0.0,>=2.13.0->spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (2024.7.4)\n",
      "Requirement already satisfied: blis<0.8.0,>=0.7.8 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from thinc<8.3.0,>=8.2.2->spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (0.7.11)\n",
      "Requirement already satisfied: confection<1.0.0,>=0.0.1 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from thinc<8.3.0,>=8.2.2->spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (0.1.5)\n",
      "Requirement already satisfied: colorama in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from tqdm<5.0.0,>=4.38.0->spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (0.4.6)\n",
      "Requirement already satisfied: click>=8.0.0 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from typer<1.0.0,>=0.3.0->spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (8.1.7)\n",
      "Requirement already satisfied: shellingham>=1.3.0 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from typer<1.0.0,>=0.3.0->spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (1.5.4)\n",
      "Requirement already satisfied: rich>=10.11.0 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from typer<1.0.0,>=0.3.0->spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (13.7.1)\n",
      "Requirement already satisfied: cloudpathlib<1.0.0,>=0.7.0 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from weasel<0.5.0,>=0.1.0->spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (0.18.1)\n",
      "Requirement already satisfied: smart-open<8.0.0,>=5.2.1 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from weasel<0.5.0,>=0.1.0->spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (7.0.4)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from jinja2->spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (2.1.3)\n",
      "Requirement already satisfied: marisa-trie>=0.7.7 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from language-data>=1.2->langcodes<4.0.0,>=3.2.0->spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (1.2.0)\n",
      "Requirement already satisfied: markdown-it-py>=2.2.0 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from rich>=10.11.0->typer<1.0.0,>=0.3.0->spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (3.0.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from rich>=10.11.0->typer<1.0.0,>=0.3.0->spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (2.15.1)\n",
      "Requirement already satisfied: wrapt in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from smart-open<8.0.0,>=5.2.1->weasel<0.5.0,>=0.1.0->spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (1.14.1)\n",
      "Requirement already satisfied: mdurl~=0.1 in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from markdown-it-py>=2.2.0->rich>=10.11.0->typer<1.0.0,>=0.3.0->spacy<3.8.0,>=3.7.2->en-core-web-sm==3.7.1) (0.1.2)\n",
      "Installing collected packages: en-core-web-sm\n",
      "Successfully installed en-core-web-sm-3.7.1\n",
      "\u001b[38;5;2m✔ Download and installation successful\u001b[0m\n",
      "You can now load the package via spacy.load('en_core_web_sm')\n"
     ]
    }
   ],
   "source": [
    "!python -m spacy download en_core_web_sm"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                                        reviews.text  \\\n",
      "0  I initially had trouble deciding between the p...   \n",
      "1  Allow me to preface this with a little history...   \n",
      "2  I am enjoying it so far. Great for reading. Ha...   \n",
      "3  I bought one of the first Paperwhites and have...   \n",
      "4  I have to say upfront - I don't like coroporat...   \n",
      "\n",
      "                                           entidades  \n",
      "0  [(300, CARDINAL), (80 dollar, MONEY), (a week,...  \n",
      "1  [(a Nook Simple Touch, PRODUCT), (2011, DATE),...  \n",
      "2               [(2012, DATE), (Paperwhite, PERSON)]  \n",
      "3  [(one, CARDINAL), (first, ORDINAL), (every thr...  \n",
      "4  [(Apple, ORG), (Amazon, ORG), (several years, ...  \n"
     ]
    }
   ],
   "source": [
    "import spacy\n",
    "\n",
    "# Cargar el modelo de SpaCy\n",
    "nlp = spacy.load(\"en_core_web_sm\")\n",
    "\n",
    "# Función para extraer entidades\n",
    "def extraer_entidades(texto):\n",
    "    doc = nlp(texto)\n",
    "    return [(ent.text, ent.label_) for ent in doc.ents]\n",
    "\n",
    "# Aplicar la extracción de entidades a las reseñas procesadas\n",
    "df['entidades'] = df['reviews.text'].apply(extraer_entidades)\n",
    "\n",
    "# Mostrar algunas filas con las entidades\n",
    "print(df[['reviews.text', 'entidades']].head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAsAAAAIFCAYAAADcCkvoAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8fJSN1AAAACXBIWXMAAA9hAAAPYQGoP6dpAABcCUlEQVR4nO3deVxU9f7H8fewyjoCCjiGCmjmXmmamKm5L3nNumaaW25larimLW7dJM1c0vYszUq7t8LSzKI0zbBccTdLcUsRV1BARDy/P3wwv0ZQGR0caF7Px2MeD+Z7vueczxlm8O2Z7/kek2EYhgAAAAAX4ebsAgAAAIBbiQAMAAAAl0IABgAAgEshAAMAAMClEIABAADgUgjAAAAAcCkEYAAAALgUAjAAAABcCgEYwC0zfPhwlS9fXocOHXJ2KQAAF0YABq5h3rx5MplM1kepUqUUHh6uZs2aKS4uTqmpqfnWmTBhgkwmk137yczM1IQJE/TTTz/ZtV5B+6pUqZI6dOhg13Yc4XrHHR8frw8++EDffvutIiIibklNJpNJEyZMcNj2MjIyNGXKFNWpU0eBgYEKCAhQdHS0unTpolWrVjlsPwVZtmzZVY+lUqVK6t27t0P3VxTbvFJiYqImTJigM2fOFOl+nKl3796qVKnSLd/n3/9ueXl5KTo6WiNHjlR6evotreVqsrKyFBMTo+DgYE2bNk3r1q1TVFSUs8uCC/FwdgFASfDhhx/qjjvuUE5OjlJTU7VmzRpNmTJF06ZN02effaYWLVpY+/br109t2rSxa/uZmZmaOHGiJKlp06aFXu9G9lVUrlXLvn37NHDgQH3xxReqXbv2La7MMXJzc9WqVStt27ZNo0aNUv369SVJf/zxh5YsWaKff/5ZTZo0KbL9L1u2TG+88UaBITg+Pl6BgYEO3V9RbPNKiYmJmjhxonr37q3SpUsX6b5cjY+Pj1asWCFJOnPmjD7//HO99tpr2rp1q77//nsnVyetWLFCaWlpeu+99/Tqq69qwoQJevXVV51dFlwIARgohJo1a6pevXrW5w8//LCGDRum++67T507d9Yff/yhsLAwSdJtt92m2267rUjryczMlK+v7y3ZV2Fdq5aoqKgCz5aXJKtXr1ZiYqI++OAD9enTx9reunVrDR48WJcuXXJabXfddVeJ2CZuHTc3N917773W523atNG+ffuUkJCg5ORkRUZGOrE6qX379mrfvr2ky39PgVuNIRDADapQoYJee+01nT17Vu+88461vaChACtWrFDTpk0VEhIiHx8fVahQQQ8//LAyMzO1f/9+lS1bVpI0ceJE69eWeV8/521v06ZNeuSRRxQUFKTo6Oir7itPfHy8ateurVKlSikqKkqvv/66zfK84R379++3af/pp59kMpnyDcdYvny5mjdvLrPZLF9fX1WrVk1xcXHXPO5Lly5p6tSpuuOOO+Tt7a3Q0FD17NlThw8ftunXtGlT1axZU+vXr1fjxo3l6+urqKgovfLKK4UKlunp6erfv79CQkLk7++vNm3aaM+ePQX2/eOPP9StWzeFhobK29tb1apV0xtvvHHdfZw8eVKSVK5cuQKXu7nZ/jlNSUnRwIEDddttt8nLy0uRkZGaOHGiLl68aO2zf/9+mUwmTZs2TdOnT1dkZKT8/f3VsGFD/frrr9Z+vXv3ttb496+28353Vw5XyPsdfvrpp3r22WdVrlw5+fv768EHH9SxY8d09uxZDRgwQGXKlFGZMmXUp08fnTt3zqb+goZApKena+TIkYqMjJSXl5fKly+v2NhYZWRk2PQzmUwaPHiwFixYoGrVqsnX11d16tTR0qVLrX0mTJigUaNGSZIiIyOtx5T3vivse2fz5s3q0KGD9fdpsVjUvn37fP0K8sMPP6h58+YKDAyUr6+vGjVqpB9//NGmT977eseOHXrsscdkNpsVFhamJ554QmlpadfdR0HeeOMN3X///QoNDZWfn59q1aqlqVOnKicnx2HHVpC8/8QfO3bMpv2zzz5Tw4YN5efnJ39/f7Vu3VqbN2+26bNv3z517dpVFotF3t7eCgsLU/PmzZWUlGT3tnr37i1/f3/9+eefateunfz9/RUREaERI0YoOzvbpu/EiRPVoEEDBQcHKzAwUHfffbfmzp0rwzBs+l3rbyxQEM4AAzehXbt2cnd31+rVq6/aZ//+/Wrfvr0aN26sDz74QKVLl9Zff/2l5cuX68KFCypXrpyWL1+uNm3aqG/fvurXr58kWUNxns6dO6tr16568skn8wWOKyUlJSk2NlYTJkxQeHi4PvnkEz3zzDO6cOGCRo4cafdxzp07V/3791eTJk309ttvKzQ0VHv27NH27duvud5TTz2ld999V4MHD1aHDh20f/9+vfjii/rpp5+0adMmlSlTxto3JSVF3bt314gRIzR+/HjFx8dr7Nixslgs6tmz51X3YRiGOnXqpMTERI0bN0733HOPfvnlF7Vt2zZf3507dyomJsb6n5fw8HB99913Gjp0qE6cOKHx48dfdT/16tWTp6ennnnmGY0bN04PPPDAVcNwSkqK6tevLzc3N40bN07R0dFau3at/vOf/2j//v368MMPbfq/8cYbuuOOOzRz5kxJ0osvvqh27dopOTlZZrNZL774ojIyMvT5559r7dq11vWutv88zz33nJo1a6Z58+Zp//79GjlypB577DF5eHioTp06WrhwoTZv3qznnntOAQEB+f6T9HeZmZlq0qSJDh8+rOeee061a9fWjh07NG7cOG3btk0//PCDzX+AvvnmG61fv16TJk2Sv7+/pk6dqoceeki///67oqKi1K9fP506dUqzZ8/Wl19+aT2W6tWrSyrceycjI0MtW7ZUZGSk3njjDYWFhSklJUUrV67U2bNnr/nafPzxx+rZs6f+9a9/af78+fL09NQ777yj1q1b67vvvlPz5s1t+j/88MN69NFH1bdvX23btk1jx46VJH3wwQfX3E9B9u7dq27duln/I7Flyxa9/PLL2r17t3V7N3NsV5OcnCwPDw+bsbaTJ0/WCy+8oD59+uiFF17QhQsX9Oqrr6px48Zat26d9ffRrl075ebmaurUqapQoYJOnDihxMREm/Hbhd2WJOXk5Khjx47q27evRowYodWrV+ull16S2WzWuHHjrP3279+vgQMHqkKFCpKkX3/9VUOGDNFff/1l7Xe9v7G+vr439HrhH84AcFUffvihIclYv379VfuEhYUZ1apVsz4fP3688feP1ueff25IMpKSkq66jePHjxuSjPHjx+dblre9cePGXXXZ31WsWNEwmUz59teyZUsjMDDQyMjIsDm25ORkm34rV640JBkrV640DMMwzp49awQGBhr33XefcenSpasew5W17Nq1y5BkDBo0yKbfb7/9ZkgynnvuOWtbkyZNDEnGb7/9ZtO3evXqRuvWra+6T8MwjG+//daQZMyaNcum/eWXX873mrZu3dq47bbbjLS0NJu+gwcPNkqVKmWcOnXqmvuaO3eu4e/vb0gyJBnlypUzevbsaaxevdqm38CBAw1/f3/jwIEDNu3Tpk0zJBk7duwwDMMwkpOTDUlGrVq1jIsXL1r7rVu3zpBkLFy40Nr29NNP5/td56lYsaLRq1cv6/O83+GDDz5o0y82NtaQZAwdOtSmvVOnTkZwcPA1txkXF2e4ubnl+yzkvb+XLVtmbZNkhIWFGenp6da2lJQUw83NzYiLi7O2vfrqqwW+Bwv73tmwYYMhyVi8eHGBr8vVZGRkGMHBwflen9zcXKNOnTpG/fr1rW157+upU6fa9B00aJBRqlSpa34mDMMwevXqZVSsWPGqy3Nzc42cnBzjo48+Mtzd3a3vwRs9trx9+vn5GTk5OUZOTo5x4sQJ46233jLc3NxsPncHDx40PDw8jCFDhtisf/bsWSM8PNzo0qWLYRiGceLECUOSMXPmzKvus7DbyqtPkvHf//7Xpm+7du2MqlWrXnUfea/VpEmTjJCQEOtrX5i/scCVGAIB3CTjiq/irnTnnXfKy8tLAwYM0Pz587Vv374b2o894+Rq1KihOnXq2LR169ZN6enp2rRpk137TUxMVHp6ugYNGmTX7BYrV66UpHxfo9evX1/VqlXL91VzeHi49cKyPLVr19aBAwcKtZ/u3bvbtHfr1s3m+fnz5/Xjjz/qoYcekq+vry5evGh9tGvXTufPn7cZdlCQJ554QocPH9ann36qoUOHKiIiQh9//LGaNGlicwHP0qVL1axZM1ksFpv95J2VvnLGiPbt28vd3d3muCVd99iv58rZQKpVq2bd35Xtp06dyjcM4u+WLl2qmjVr6s4777Q5ptatWxc4ZKZZs2YKCAiwPg8LC1NoaGihjqmw753KlSsrKChIzz77rN5++23t3LnzutuWLr+nT506pV69etkcy6VLl9SmTRutX78+37csHTt2tHleu3ZtnT9//obGtm/evFkdO3ZUSEiI3N3d5enpqZ49eyo3N9c6dOdGjy1PRkaGPD095enpqTJlyuipp57So48+qpdfftna57vvvtPFixfVs2dPm9ehVKlSatKkifV3GhwcrOjoaL366quaPn26Nm/enG9oUmG3lcdkMunBBx+0aSvo875ixQq1aNFCZrPZ+lqNGzdOJ0+etL72jvobC9dCAAZuQkZGhk6ePCmLxXLVPtHR0frhhx8UGhqqp59+WtHR0YqOjtasWbPs2tf1vu7+u/Dw8Ku25Y1lLazjx49Lkt0X211rzKzFYslXR0hISL5+3t7eysrKuu5+PDw88q1/5Wtw8uRJXbx4UbNnz7YGg7xHu3btJEknTpy47nGZzWY99thjmjVrln777Tdt3bpVYWFhev75561fBx87dkxLlizJt58aNWoUuJ8ra/f29pak6x779QQHB9s89/Lyumb7+fPnr7qtY8eOaevWrfmOKSAgQIZhXPeYpML9PqXCv3fMZrNWrVqlO++8U88995xq1Kghi8Wi8ePH5xtPe+WxSNIjjzyS73imTJkiwzB06tSpax7Pjf6ODh48qMaNG+uvv/7SrFmz9PPPP2v9+vXWMd5527vRY8vj4+Oj9evXa/369VqyZImaNm2qhQsX6pVXXsn3Otxzzz35XofPPvvM+js1mUz68ccf1bp1a02dOlV33323ypYtq6FDh1qHYxR2W3l8fX1VqlSpfK/p39+D69atU6tWrSRJ7733nn755RetX79ezz//vM1r5ai/sXAtjAEGbsI333yj3Nzc605d1rhxYzVu3Fi5ubnasGGDZs+erdjYWIWFhalr166F2pc9Z19TUlKu2pb3D3nePz5XXnRy5T9UeWOR7b3wJm8/R48ezReejxw5YjP+92aEhITo4sWLOnnypE1IufI1CAoKkru7u3r06KGnn366wG3dyJXxNWrUUNeuXTVz5kzt2bNH9evXV5kyZVS7dm2bs21/d63/MBVXZcqUkY+Pz1XHvDrq9ynZ996pVauWFi1aJMMwtHXrVs2bN0+TJk2Sj4+PxowZc81aZ8+ebTNTwt/lzeriaIsXL1ZGRoa+/PJLVaxY0dp+5cVk0o0dWx43NzebmWtatmypunXrauLEierevbsiIiKsr8Pnn39uU0tBKlasqLlz50qS9uzZo//+97+aMGGCLly4oLffftuubRXWokWL5OnpqaVLl9qE5cWLF+fr64i/sXAtBGDgBh08eFAjR46U2WzWwIEDC7WOu7u7GjRooDvuuEOffPKJNm3apK5duzrsjF+eHTt2aMuWLTbDID799FMFBATo7rvvliTr5Pxbt25V1apVrf2+/vprm23FxMTIbDbr7bffVteuXQsdxB944AFJly82uueee6zt69ev165du6xncW5Ws2bNNHXqVH3yyScaOnSotf3TTz+16efr66tmzZpp8+bNql27tvWsZ2GdPHlSAQEBBa63e/duSf8fbDt06KBly5YpOjpaQUFB9h5Sgf7+HvHx8XHINu3RoUMH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QgAGAACASyEAAwAAwKUQgAEAAOBSCMAAAABwKQRgAAAAuBQCMAAAAFwKARgAAAAuhQAMAAAAl0IABgAAgEshAAMAAMClEIABAADgUgjAAAAAcCkEYAAAALgUAjAAAABcCgEYAAAALoUADAAAAJdCAAYAAIBLIQADAADApRCAAQAA4FIIwAAAAHApBGAAAAC4FAIwAAAAXAoBGAAAAC6FAAwAAACXQgAGAACASyEAAwAAwKUQgAEAAOBSCMAAAABwKQRgAAAAuBSnBuDVq1frwQcflMVikclk0uLFi63LcnJy9Oyzz6pWrVry8/OTxWJRz549deTIEZttZGdna8iQISpTpoz8/PzUsWNHHT582KbP6dOn1aNHD5nNZpnNZvXo0UNnzpy5BUcIAACA4sapATgjI0N16tTRnDlz8i3LzMzUpk2b9OKLL2rTpk368ssvtWfPHnXs2NGmX2xsrOLj47Vo0SKtWbNG586dU4cOHZSbm2vt061bNyUlJWn58uVavny5kpKS1KNHjyI/PgAAABQ/JsMwDGcXIUkmk0nx8fHq1KnTVfusX79e9evX14EDB1ShQgWlpaWpbNmyWrBggR599FFJ0pEjRxQREaFly5apdevW2rVrl6pXr65ff/1VDRo0kCT9+uuvatiwoXbv3q2qVasWqr709HSZzWalpaUpMDDwpo/X2UwTTc4uAddgjC8WH0sAAEqUwua1EjUGOC0tTSaTSaVLl5Ykbdy4UTk5OWrVqpW1j8ViUc2aNZWYmChJWrt2rcxmszX8StK9994rs9ls7VOQ7Oxspaen2zwAAABQ8pWYAHz+/HmNGTNG3bp1syb6lJQUeXl5KSgoyKZvWFiYUlJSrH1CQ0PzbS80NNTapyBxcXHWMcNms1kREREOPBoAAAA4S4kIwDk5OeratasuXbqkN99887r9DcOQyfT/X/H//eer9bnS2LFjlZaWZn0cOnToxooHAABAsVLsA3BOTo66dOmi5ORkJSQk2IznCA8P14ULF3T69GmbdVJTUxUWFmbtc+zYsXzbPX78uLVPQby9vRUYGGjzAAAAQMlXrANwXvj9448/9MMPPygkJMRmed26deXp6amEhARr29GjR7V9+3bFxMRIkho2bKi0tDStW7fO2ue3335TWlqatQ8AAABch4czd37u3Dn9+eef1ufJyclKSkpScHCwLBaL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SiEhIVddB86Rnp6uiIgIHTp0SIGBgc4uBygx+OwA9uNzU7wZhqGzZ8/KYrFcs59LBOAyZcrI3d0939ne1NTUfGeF83h7e8vb29umrXTp0kVVIhwgMDCQP0bADeCzA9iPz03xda0zv3lc4iI4Ly8v1a1bVwkJCTbtCQkJiomJcVJVAAAAcAaXOAMsScOHD1ePHj1Ur149NWzYUO+++64OHjyoJ5980tmlAQAA4BZymQD86KOP6uTJk5o0aZKOHj2qmjVratmyZapYsaKzS8NN8vb21vjx4/MNWQFwbXx2APvxuflnMBnXmycCAAAA+AdxiTHAAAAAQB4CMAAAAFwKARgAAAAuhQAMAAAAl0IABgAAgEshAAMAAMCluMw8wAAAADfr+PHj+v3332UymXT77berbNmyzi4JN4AAjBJr7969mjlzpnbt2iWTyaRq1arpmWeeUXR0tLNLA4q1M2fOaO7cuTafnb59+8psNju7NKDYysjI0JAhQ7RgwQLl5uZKktzd3dWzZ0/Nnj1bvr6+Tq4Q9mAIBEqk7777TtWrV9e6detUu3Zt1axZU7/99ptq1KihhIQEZ5cHFFsbNmxQdHS0ZsyYoVOnTunEiROaMWOGoqOjtWnTJmeXBxRbw4cP16pVq/T111/rzJkzOnPmjL766iutWrVKI0aMcHZ5sBN3gkOJdNddd6l169Z65ZVXbNrHjBmj77//nn/Igato3LixKleurPfee08eHpe/BLx48aL69eunffv2afXq1U6uECieypQpo88//1xNmza1aV+5cqW6dOmi48ePO6cw3BACMEqkUqVKadu2bapSpYpN+549e1S7dm2dP3/eSZUBxZuPj482b96sO+64w6Z9586dqlevnjIzM51UGVC8+fr6auPGjapWrZpN+44dO1S/fn1lZGQ4qTLcCIZAoEQqW7askpKS8rUnJSUpNDT01hcElBCBgYE6ePBgvvZDhw4pICDACRUBJUPDhg01fvx4mxMsWVlZmjhxoho2bOjEynAjuAgOJVL//v01YMAA7du3TzExMTKZTFqzZo2mTJnCWCzgGh599FH17dtX06ZNs/nsjBo1So899pizywOKrZkzZ6pt27a67bbbVKdOHZlMJiUlJalUqVL67rvvnF0e7MQQCJRIhmFo5syZeu2113TkyBFJksVi0ahRozR06FCZTCYnVwgU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",
      "text/plain": [
       "<Figure size 800x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Contar la cantidad de reseñas por cada sentimiento\n",
    "sentimientos = df['sentimiento'].value_counts()\n",
    "\n",
    "# Crear un gráfico de barras\n",
    "plt.figure(figsize=(8, 5))\n",
    "sentimientos.plot(kind='bar', color=['green', 'red', 'blue'])\n",
    "plt.title('Distribución de Sentimientos en las Reseñas')\n",
    "plt.xlabel('Sentimiento')\n",
    "plt.ylabel('Cantidad de Reseñas')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Crear un gráfico de barras\n",
    "sentimientos = df['sentimiento'].value_counts()\n",
    "plt.figure(figsize=(8, 5))\n",
    "sentimientos.plot(kind='bar', color=['green', 'red', 'blue'])\n",
    "plt.title('Distribución de Sentimientos en las Reseñas')\n",
    "plt.xlabel('Sentimiento')\n",
    "plt.ylabel('Cantidad de Reseñas')\n",
    "plt.savefig('static/sentimientos.png')  # Guardar el gráfico en la carpeta static\n",
    "plt.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting plotly\n",
      "  Downloading plotly-5.23.0-py3-none-any.whl.metadata (7.3 kB)\n",
      "Collecting tenacity>=6.2.0 (from plotly)\n",
      "  Downloading tenacity-9.0.0-py3-none-any.whl.metadata (1.2 kB)\n",
      "Requirement already satisfied: packaging in c:\\users\\william\\anaconda3\\envs\\py310\\lib\\site-packages (from plotly) (24.1)\n",
      "Downloading plotly-5.23.0-py3-none-any.whl (17.3 MB)\n",
      "   ---------------------------------------- 0.0/17.3 MB ? eta -:--:--\n",
      "   --------------- ------------------------ 6.8/17.3 MB 42.0 MB/s eta 0:00:01\n",
      "   -------------------------------- ------- 13.9/17.3 MB 38.0 MB/s eta 0:00:01\n",
      "   ---------------------------------------- 17.3/17.3 MB 40.4 MB/s eta 0:00:00\n",
      "Downloading tenacity-9.0.0-py3-none-any.whl (28 kB)\n",
      "Installing collected packages: tenacity, plotly\n",
      "Successfully installed plotly-5.23.0 tenacity-9.0.0\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "%pip install plotly"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "Value of 'x' is not the name of a column in 'data_frame'. Expected one of ['id', 'asins', 'brand', 'categories', 'colors', 'dateAdded', 'dateUpdated', 'dimension', 'ean', 'keys', 'manufacturer', 'manufacturerNumber', 'name', 'prices', 'reviews.date', 'reviews.doRecommend', 'reviews.numHelpful', 'reviews.rating', 'reviews.sourceURLs', 'reviews.text', 'reviews.title', 'reviews.userCity', 'reviews.userProvince', 'reviews.username', 'sizes', 'upc', 'weight', 'texto_procesado'] but received: sentimiento",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[47], line 3\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mplotly\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mexpress\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mpx\u001b[39;00m\n\u001b[1;32m----> 3\u001b[0m fig \u001b[38;5;241m=\u001b[39m \u001b[43mpx\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mbar\u001b[49m\u001b[43m(\u001b[49m\u001b[43mdf\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mx\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43msentimiento\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mtitle\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mDistribución de Sentimientos\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[0;32m      4\u001b[0m fig\u001b[38;5;241m.\u001b[39mwrite_html(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mstatic/sentimientos_interactivo.html\u001b[39m\u001b[38;5;124m'\u001b[39m)\n",
      "File \u001b[1;32mc:\\Users\\William\\anaconda3\\envs\\py310\\lib\\site-packages\\plotly\\express\\_chart_types.py:373\u001b[0m, in \u001b[0;36mbar\u001b[1;34m(data_frame, x, y, color, pattern_shape, facet_row, facet_col, facet_col_wrap, facet_row_spacing, facet_col_spacing, hover_name, hover_data, custom_data, text, base, error_x, error_x_minus, error_y, error_y_minus, animation_frame, animation_group, category_orders, labels, color_discrete_sequence, color_discrete_map, color_continuous_scale, pattern_shape_sequence, pattern_shape_map, range_color, color_continuous_midpoint, opacity, orientation, barmode, log_x, log_y, range_x, range_y, text_auto, title, template, width, height)\u001b[0m\n\u001b[0;32m    325\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mbar\u001b[39m(\n\u001b[0;32m    326\u001b[0m     data_frame\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mNone\u001b[39;00m,\n\u001b[0;32m    327\u001b[0m     x\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mNone\u001b[39;00m,\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m    367\u001b[0m     height\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mNone\u001b[39;00m,\n\u001b[0;32m    368\u001b[0m ) \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m go\u001b[38;5;241m.\u001b[39mFigure:\n\u001b[0;32m    369\u001b[0m \u001b[38;5;250m    \u001b[39m\u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[0;32m    370\u001b[0m \u001b[38;5;124;03m    In a bar plot, each row of `data_frame` is represented as a rectangular\u001b[39;00m\n\u001b[0;32m    371\u001b[0m \u001b[38;5;124;03m    mark.\u001b[39;00m\n\u001b[0;32m    372\u001b[0m \u001b[38;5;124;03m    \"\"\"\u001b[39;00m\n\u001b[1;32m--> 373\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mmake_figure\u001b[49m\u001b[43m(\u001b[49m\n\u001b[0;32m    374\u001b[0m \u001b[43m        \u001b[49m\u001b[43margs\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43mlocals\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    375\u001b[0m \u001b[43m        \u001b[49m\u001b[43mconstructor\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mgo\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mBar\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    376\u001b[0m \u001b[43m        \u001b[49m\u001b[43mtrace_patch\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43mdict\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43mtextposition\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mauto\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    377\u001b[0m \u001b[43m        \u001b[49m\u001b[43mlayout_patch\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43mdict\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43mbarmode\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mbarmode\u001b[49m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    378\u001b[0m \u001b[43m    \u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32mc:\\Users\\William\\anaconda3\\envs\\py310\\lib\\site-packages\\plotly\\express\\_core.py:2090\u001b[0m, in \u001b[0;36mmake_figure\u001b[1;34m(args, constructor, trace_patch, layout_patch)\u001b[0m\n\u001b[0;32m   2087\u001b[0m layout_patch \u001b[38;5;241m=\u001b[39m layout_patch \u001b[38;5;129;01mor\u001b[39;00m {}\n\u001b[0;32m   2088\u001b[0m apply_default_cascade(args)\n\u001b[1;32m-> 2090\u001b[0m args \u001b[38;5;241m=\u001b[39m \u001b[43mbuild_dataframe\u001b[49m\u001b[43m(\u001b[49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mconstructor\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m   2091\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m constructor \u001b[38;5;129;01min\u001b[39;00m [go\u001b[38;5;241m.\u001b[39mTreemap, go\u001b[38;5;241m.\u001b[39mSunburst, go\u001b[38;5;241m.\u001b[39mIcicle] \u001b[38;5;129;01mand\u001b[39;00m args[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpath\u001b[39m\u001b[38;5;124m\"\u001b[39m] \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[0;32m   2092\u001b[0m     args \u001b[38;5;241m=\u001b[39m process_dataframe_hierarchy(args)\n",
      "File \u001b[1;32mc:\\Users\\William\\anaconda3\\envs\\py310\\lib\\site-packages\\plotly\\express\\_core.py:1492\u001b[0m, in \u001b[0;36mbuild_dataframe\u001b[1;34m(args, constructor)\u001b[0m\n\u001b[0;32m   1489\u001b[0m     args[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcolor\u001b[39m\u001b[38;5;124m\"\u001b[39m] \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[0;32m   1490\u001b[0m \u001b[38;5;66;03m# now that things have been prepped, we do the systematic rewriting of `args`\u001b[39;00m\n\u001b[1;32m-> 1492\u001b[0m df_output, wide_id_vars \u001b[38;5;241m=\u001b[39m \u001b[43mprocess_args_into_dataframe\u001b[49m\u001b[43m(\u001b[49m\n\u001b[0;32m   1493\u001b[0m \u001b[43m    \u001b[49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mwide_mode\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mvar_name\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mvalue_name\u001b[49m\n\u001b[0;32m   1494\u001b[0m \u001b[43m\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m   1496\u001b[0m \u001b[38;5;66;03m# now that `df_output` exists and `args` contains only references, we complete\u001b[39;00m\n\u001b[0;32m   1497\u001b[0m \u001b[38;5;66;03m# the special-case and wide-mode handling by further rewriting args and/or mutating\u001b[39;00m\n\u001b[0;32m   1498\u001b[0m \u001b[38;5;66;03m# df_output\u001b[39;00m\n\u001b[0;32m   1500\u001b[0m count_name \u001b[38;5;241m=\u001b[39m _escape_col_name(df_output, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcount\u001b[39m\u001b[38;5;124m\"\u001b[39m, [var_name, value_name])\n",
      "File \u001b[1;32mc:\\Users\\William\\anaconda3\\envs\\py310\\lib\\site-packages\\plotly\\express\\_core.py:1213\u001b[0m, in \u001b[0;36mprocess_args_into_dataframe\u001b[1;34m(args, wide_mode, var_name, value_name)\u001b[0m\n\u001b[0;32m   1211\u001b[0m         \u001b[38;5;28;01mif\u001b[39;00m argument \u001b[38;5;241m==\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mindex\u001b[39m\u001b[38;5;124m\"\u001b[39m:\n\u001b[0;32m   1212\u001b[0m             err_msg \u001b[38;5;241m+\u001b[39m\u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m To use the index, pass it in directly as `df.index`.\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m-> 1213\u001b[0m         \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(err_msg)\n\u001b[0;32m   1214\u001b[0m \u001b[38;5;28;01melif\u001b[39;00m length \u001b[38;5;129;01mand\u001b[39;00m \u001b[38;5;28mlen\u001b[39m(df_input[argument]) \u001b[38;5;241m!=\u001b[39m length:\n\u001b[0;32m   1215\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\n\u001b[0;32m   1216\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mAll arguments should have the same length. \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1217\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mThe length of column argument `df[\u001b[39m\u001b[38;5;132;01m%s\u001b[39;00m\u001b[38;5;124m]` is \u001b[39m\u001b[38;5;132;01m%d\u001b[39;00m\u001b[38;5;124m, whereas the \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m   1224\u001b[0m         )\n\u001b[0;32m   1225\u001b[0m     )\n",
      "\u001b[1;31mValueError\u001b[0m: Value of 'x' is not the name of a column in 'data_frame'. Expected one of ['id', 'asins', 'brand', 'categories', 'colors', 'dateAdded', 'dateUpdated', 'dimension', 'ean', 'keys', 'manufacturer', 'manufacturerNumber', 'name', 'prices', 'reviews.date', 'reviews.doRecommend', 'reviews.numHelpful', 'reviews.rating', 'reviews.sourceURLs', 'reviews.text', 'reviews.title', 'reviews.userCity', 'reviews.userProvince', 'reviews.username', 'sizes', 'upc', 'weight', 'texto_procesado'] but received: sentimiento"
     ]
    }
   ],
   "source": [
    "import plotly.express as px\n",
    "\n",
    "fig = px.bar(df, x='sentimiento', title='Distribución de Sentimientos')\n",
    "fig.write_html('static/sentimientos_interactivo.html')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['id', 'asins', 'brand', 'categories', 'colors', 'dateAdded',\n",
      "       'dateUpdated', 'dimension', 'ean', 'keys', 'manufacturer',\n",
      "       'manufacturerNumber', 'name', 'prices', 'reviews.date',\n",
      "       'reviews.doRecommend', 'reviews.numHelpful', 'reviews.rating',\n",
      "       'reviews.sourceURLs', 'reviews.text', 'reviews.title',\n",
      "       'reviews.userCity', 'reviews.userProvince', 'reviews.username', 'sizes',\n",
      "       'upc', 'weight', 'texto_procesado', 'resumen', 'entidades'],\n",
      "      dtype='object')\n"
     ]
    }
   ],
   "source": [
    "print(df.columns)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "env",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
