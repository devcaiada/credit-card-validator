import re


def luhn_algorithm(card_number):
    """Check if the card number is valid using the Luhn algorithm."""
    card_number = card_number.replace(' ', '')
    total = 0
    reverse_digits = card_number[::-1]
    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    return total % 10 == 0


def get_card_brand(card_number):
    """Identify the card brand based on the card number."""
    card_number = card_number.replace(' ', '')
    card_patterns = {
        'Visa': r'^4[0-9]{12}(?:[0-9]{3})?$|^4[0-9]{15}$',
        'MasterCard': r'^5[1-5][0-9]{14}$',
        'American Express': r'^3[47][0-9]{13}$',
        'Discover': r'^6(?:011|5[0-9]{2})[0-9]{12}$',
        'JCB': r'^(?:2131|1800|35\d{3})\d{11}$',
        'Diners Club': r'^3(?:0[0-5]|[68][0-9])[0-9]{11}$'
    }
    for brand, pattern in card_patterns.items():
        if re.match(pattern, card_number):
            return brand
    return 'Unknown'


def validate_credit_card(card_number):
    """Validate the credit card number and identify its brand."""
    if luhn_algorithm(card_number):
        brand = get_card_brand(card_number)
        return f"Card is valid and the brand is {brand}."
    else:
        return "Card is invalid."

# Example usage
card_number = "4111 1111 1111 1111"
print(validate_credit_card(card_number))