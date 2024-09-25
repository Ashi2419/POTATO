{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "10c972ab",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import dask.dataframe as dd\n",
    "\n",
    "# Read the TSV file using dask\n",
    "ddf = dd.read_csv('correct_twitter_201904.tsv', sep='\\t', header=0)\n",
    "\n",
    "# Convert the dask dataframe to a pandas dataframe\n",
    "df = ddf.compute()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f1f06f88",
   "metadata": {},
   "outputs": [],
   "source": [
    "class POTATO:\n",
    "    def __init__(self, df):\n",
    "        self.df = df\n",
    "\n",
    "    def query_term(self, term):\n",
    "        # Filter the dataframe to only include tweets containing the term\n",
    "        term_df = self.df[self.df['text'].str.contains(term, case=False)]\n",
    "\n",
    "        # Calculate the number of tweets posted containing the term on each day\n",
    "        daily_tweets = term_df.groupby('created_at').size().reset_index(name='count')\n",
    "\n",
    "        # Calculate the number of unique users who posted a tweet containing the term\n",
    "        unique_users = term_df['user_id'].nunique()\n",
    "\n",
    "        # Calculate the average number of likes for tweets containing the term\n",
    "        avg_likes = term_df['likes'].mean()\n",
    "\n",
    "        # Calculate the place IDs where the tweets came from\n",
    "        place_ids = term_df['place_id'].value_counts().index.tolist()\n",
    "\n",
    "        # Calculate the times of day when the tweets were posted\n",
    "        times_of_day = term_df['created_at'].dt.hour.value_counts().index.tolist()\n",
    "\n",
    "        # Calculate the user who posted the most tweets containing the term\n",
    "        top_user = term_df['user_id'].value_counts().index[0]\n",
    "\n",
    "        return {\n",
    "            'daily_tweets': daily_tweets,\n",
    "            'unique_users': unique_users,\n",
    "            'avg_likes': avg_likes,\n",
    "            'place_ids': place_ids,\n",
    "            'times_of_day': times_of_day,\n",
    "            'top_user': top_user\n",
    "        }"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "75baf5e9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pandas in c:\\users\\acs\\anaconda3\\lib\\site-packages (1.5.3)\n",
      "Requirement already satisfied: dask in c:\\users\\acs\\anaconda3\\lib\\site-packages (2023.6.0)\n",
      "Requirement already satisfied: python-dateutil>=2.8.1 in c:\\users\\acs\\anaconda3\\lib\\site-packages (from pandas) (2.8.2)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\acs\\anaconda3\\lib\\site-packages (from pandas) (2022.7)\n",
      "Requirement already satisfied: numpy>=1.21.0 in c:\\users\\acs\\anaconda3\\lib\\site-packages (from pandas) (1.24.3)\n",
      "Requirement already satisfied: click>=8.0 in c:\\users\\acs\\anaconda3\\lib\\site-packages (from dask) (8.0.4)\n",
      "Requirement already satisfied: cloudpickle>=1.5.0 in c:\\users\\acs\\anaconda3\\lib\\site-packages (from dask) (2.2.1)\n",
      "Requirement already satisfied: fsspec>=2021.09.0 in c:\\users\\acs\\anaconda3\\lib\\site-packages (from dask) (2023.3.0)\n",
      "Requirement already satisfied: packaging>=20.0 in c:\\users\\acs\\anaconda3\\lib\\site-packages (from dask) (23.0)\n",
      "Requirement already satisfied: partd>=1.2.0 in c:\\users\\acs\\anaconda3\\lib\\site-packages (from dask) (1.2.0)\n",
      "Requirement already satisfied: pyyaml>=5.3.1 in c:\\users\\acs\\anaconda3\\lib\\site-packages (from dask) (6.0)\n",
      "Requirement already satisfied: toolz>=0.10.0 in c:\\users\\acs\\anaconda3\\lib\\site-packages (from dask) (0.12.0)\n",
      "Requirement already satisfied: importlib-metadata>=4.13.0 in c:\\users\\acs\\anaconda3\\lib\\site-packages (from dask) (6.0.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\acs\\anaconda3\\lib\\site-packages (from click>=8.0->dask) (0.4.6)\n",
      "Requirement already satisfied: zipp>=0.5 in c:\\users\\acs\\anaconda3\\lib\\site-packages (from importlib-metadata>=4.13.0->dask) (3.11.0)\n",
      "Requirement already satisfied: locket in c:\\users\\acs\\anaconda3\\lib\\site-packages (from partd>=1.2.0->dask) (1.0.0)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\acs\\anaconda3\\lib\\site-packages (from python-dateutil>=2.8.1->pandas) (1.16.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install pandas dask"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bd0f055f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "95d2aaca",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0308753a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "11e2dc49",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9294ba20",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "41ed58bb",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "01ea6b20",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2c945615",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
