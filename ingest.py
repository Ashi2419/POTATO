{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "857e9acd",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import dask.dataframe as dd\n",
    "\n",
    "def ingest_data(file_path):\n",
    "    # Read the TSV file using dask\n",
    "    ddf = dd.read_csv(file_path, sep='\\t', header=0)\n",
    "\n",
    "    # Convert the dask dataframe to a pandas dataframe\n",
    "    df = ddf.compute()\n",
    "\n",
    "    return df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "073a72dd",
   "metadata": {},
   "outputs": [],
   "source": [
    "from ingest_data import ingest_data\n",
    "from potato import POTATO\n",
    "\n",
    "# Ingest the data\n",
    "df = ingest_data('correct_twitter_201904.tsv')\n",
    "\n",
    "# Create a POTATO instance\n",
    "potato = POTATO(df)\n",
    "\n",
    "# Query the data\n",
    "results = potato.query_term('music')\n",
    "\n",
    "# Print the results\n",
    "print(results)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5a9b9922",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "886ce328",
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
