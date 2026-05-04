# Spam Detection Program

def calculate_spam_score(message):
    spam_keywords = [
        "free", "win", "winner", "cash", "prize",
        "claim now", "urgent", "act now", "limited time", "risk free",
        "guaranteed", "no obligation", "click here", "subscribe now",
        "buy now", "order now", "exclusive deal", "congratulations",
        "you have been selected", "earn money", "work from home",
        "double your income", "investment opportunity", "credit card",
        "debt relief", "loan approval", "cheap", "discount",
        "save big", "100% free"
    ]

    message = message.lower()
    score = 0
    found_keywords = {}

    for keyword in spam_keywords:
        count = message.count(keyword)
        if count > 0:
            score += count
            found_keywords[keyword] = count

    return score, found_keywords


def get_spam_rating(score):
    if score <= 2:
        return "Low likelihood of spam"
    elif score <= 6:
        return "Moderate likelihood of spam"
    elif score <= 10:
        return "High likelihood of spam"
    else:
        return "Very high likelihood of spam"


def display_results(score, rating, found_keywords):
    print("\n--- Spam Analysis Results ---")
    print(f"Spam Score: {score}")
    print(f"Spam Likelihood: {rating}")

    if found_keywords:
        print("\nDetected Spam Words/Phrases:")
        for word, count in found_keywords.items():
            print(f"- '{word}' found {count} time(s)")
    else:
        print("\nNo spam keywords detected.")


def main():
    print("Spam Email Detector")
    print("--------------------")

    user_message = input("Enter an email message:\n")

    score, found_keywords = calculate_spam_score(user_message)
    rating = get_spam_rating(score)

    display_results(score, rating, found_keywords)


if __name__ == "__main__":
    main()