from random import sample

_hidden_number = []
_results = {'bulls': 0, 'cow': 0}
_quantity_steps = 0


def generate_number():
    symbols_for_sample = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    global _hidden_number
    _hidden_number = []

    hidden_number_big = sample(symbols_for_sample, 5)
    if hidden_number_big[0] == '0':
        _hidden_number = hidden_number_big[1:]

    else:
        _hidden_number = hidden_number_big[:4]
    return _hidden_number


def check_number(user_answer):
    global _quantity_steps
    _quantity_steps += 1
    if len(list(user_answer)) == 4:
        if len(set(list(user_answer))) == 4:

            return True
        else:
            return False


def counting_bulls_cows(user_answer):
    global _results
    _results = {'bulls': 0, 'cow': 0}
    for i, symbol in enumerate(list(user_answer)):
        if symbol == _hidden_number[i]:
            _results['bulls'] += 1
        elif symbol in _hidden_number:
            _results['cow'] += 1
    return _results


def game_over():
    if _results['bulls'] == 4:

        return False
    else:
        return True
