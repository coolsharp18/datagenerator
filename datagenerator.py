import logging as log


class RandomInteger:
    import random as rd
    in_use = False

    def __init__(self, start_value, increment):
        self.start_value = start_value
        self.increment = increment

    def get(self):
        if self.in_use:
            self.start_value = self.start_value + self.increment
        else:
            self.in_use = True
        return self.start_value


class RandomStringFromList:
    from random import choice

    def __init__(self, values):
        self.values = values

    def get(self):
        return self.choice(self.values)


class RandomDecimal:
    from random import uniform

    def __init__(self, start_value, end_value):
        self.start_value = start_value
        self.end_value = end_value

    def get(self):
        return self.uniform(self.start_value, self.end_value)


def get_generator(g_def):
    if g_def['type'] == 'RandomInteger':
        return RandomInteger(g_def['start_value'], g_def['increment'])
    elif g_def['type'] == 'RandomStringFromList':
        return RandomStringFromList(tuple(g_def['values']))
    elif g_def['type'] == 'RandomDecimal':
        return RandomDecimal(g_def['start_value'], g_def['end_value'])


def generate_data(data_template, i):
    return data_template.format(id=i)


def generate_file(data_template):
    with open('C:/Dev/test_data.csv', 'w') as f:
        for i in range(1, 10):
            f.write(f"{generate_data(data_template, i)}\n")


def load_schema(filepath) -> str:
    try:
        log.info("Importing JSON")
        import json
    except Exception as e:
        "Cannot find JSON module"
        log.error(e.__str__())
    schema = []
    with open(filepath) as file:
        schema = json.load(file)

    return schema


def generator_list(schema):
    g_list = []
    i = 0

    for entry in schema:
        i = i + 1
        gen = get_generator(entry['generator_definition'])
        g_list.append(gen)

    return g_list


def generate_data(template, g_dict, record_count, num_cols, output_path):

    with open(output_path, 'w') as f:
        for i in range(1, record_count + 1):
            values = [g.get() for g in g_dict]
            f.write(template.format(*values))


def generate_data_from_schema(config_file, output_file, record_count):
    schema = load_schema(config_file)
    num_cols = len(schema)
    template = ('{},' * num_cols)[:-1] + "\n"
    g_list = generator_list(schema)
    generate_data(template, g_list, record_count, num_cols, output_file)


generate_data_from_schema('./resources/data_schema.json', 'C:/Dev/output.csv', 1000000)
