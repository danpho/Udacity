{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import nltk\n",
    "nltk.download(['punkt', 'wordnet', 'averaged_perceptron_tagger'])\n",
    "\n",
    "import re\n",
    "import pandas as pd\n",
    "from nltk.tokenize import word_tokenize\n",
    "from nltk.stem import WordNetLemmatizer\n",
    "from sklearn.base import BaseEstimator, TransformerMixin\n",
    "\n",
    "url_regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'\n",
    "\n",
    "\n",
    "def tokenize(text):\n",
    "    detected_urls = re.findall(url_regex, text)\n",
    "    for url in detected_urls:\n",
    "        text = text.replace(url, \"urlplaceholder\")\n",
    "\n",
    "    tokens = word_tokenize(text)\n",
    "    lemmatizer = WordNetLemmatizer()\n",
    "\n",
    "    clean_tokens = []\n",
    "    for tok in tokens:\n",
    "        clean_tok = lemmatizer.lemmatize(tok).lower().strip()\n",
    "        clean_tokens.append(clean_tok)\n",
    "\n",
    "    return clean_tokens\n",
    "\n",
    "\n",
    "class StartingVerbExtractor(BaseEstimator, TransformerMixin):\n",
    "\n",
    "    def starting_verb(self, text):\n",
    "        sentence_list = nltk.sent_tokenize(text)\n",
    "        for sentence in sentence_list:\n",
    "            pos_tags = nltk.pos_tag(tokenize(sentence))\n",
    "            first_word, first_tag = pos_tags[0]\n",
    "            if first_tag in ['VB', 'VBP'] or first_word == 'RT':\n",
    "                return True\n",
    "        return False\n",
    "\n",
    "    def fit(self, x, y=None):\n",
    "        return self\n",
    "\n",
    "    def transform(self, X):\n",
    "        X_tagged = pd.Series(X).apply(self.starting_verb)\n",
    "        return pd.DataFrame(X_tagged)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.6.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
