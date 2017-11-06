

# Input is text of article, categories and the classifying model
# Predicts and returns the category of the article text
def news_predictor(article_text, categories, clf):

    predicted = clf.predict(article_text)
    category = categories.target_names[predicted[0]]
    return category
