import json
import sys


class Person:
    def __init__(self, score, location):
        self.state = location
        self.credit_score = score

    def set_credit_score(self, score):
        self.credit_score = score

    def get_credit_score(self):
        return self.credit_score

    def set_state(self, location):
        self.state = location

    def get_state(self):
        return self.state


class Product:
    def __init__(self, product_name, rate):
        self.name = product_name
        self.interest_rate = rate
        self.disqualified = False

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_interest_rate(self, rate):
        self.interest_rate = rate

    def get_interest_rate(self):
        return self.interest_rate

    def set_disqualified(self, disqualified):
        self.disqualified = disqualified

    def get_disqualified(self):
        return self.disqualified


class RulesEngine:
    def __init__(self):
        self.data = None

    def get_rules(self):
        return self.data

    def set_rules(self, json_data):
        self.data = json_data

    def load_rules(self, path):
        file = open(path, )
        self.set_rules(json.load(file))
        file.close()

    def run_rules(self, person_data, product_data):
        person = person_data
        product = product_data
        json_data = self.get_rules()

        # walk through each rule and evaluate the condition, if the condition is true, execute the action,
        # if not true move onto the next rule
        for i in json_data['rules']:
            boolean = eval(i['condition'])
            if boolean:
                eval(i['action'])
        print("product.interest_rate ==", (product.get_interest_rate()))
        print("product.disqualified ==", (product.get_disqualified()))


if __name__ == '__main__':
    person = Person(720, 'Florida')

    product = Product('7-1 ARM', 5.0)

    rules_engine = RulesEngine()

    rules_engine.load_rules(sys.argv[1])

    rules_engine.run_rules(person, product)
