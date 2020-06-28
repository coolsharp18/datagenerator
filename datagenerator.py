import logging as log


class RandomInteger:
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
    '''
    Returns Generator as per configuration
    :param g_def:
    :return:
    '''
    #TODO: Load the classes dynamically
    if g_def['type'] == 'RandomInteger':
        return RandomInteger(g_def['start_value'], g_def['increment'])
    elif g_def['type'] == 'RandomStringFromList':
        return RandomStringFromList(tuple(g_def['values']))
    elif g_def['type'] == 'RandomDecimal':
        return RandomDecimal(g_def['start_value'], g_def['end_value'])

def load_schema(filepath) -> str:
    '''
    Loads the JSON file as a dictionary
    :param filepath:
    :return: dictionary representing the configuration
    '''
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
    '''
    Creates a list of Generators as per configuration
    :param schema: Configuration
    :return: List of generators
    '''
    g_list = []
    i = 0

    for entry in schema:
        i = i + 1
        gen = get_generator(entry['generator_definition'])
        g_list.append(gen)

    return g_list


def generate_data(template, g_list, record_count, output_path):
    '''
    Method that creates the records with random values and writes the data into the file

    :param template: Record template for the file
    :param g_list: A list of data generator
    :param record_count: number of records
    :param output_path:
    :return: None
    '''

    with open(output_path, 'w') as f:
        for i in range(1, record_count + 1):
            values = [g.get() for g in g_list]
            f.write(template.format(*values))


def generate_data_from_schema(config_file, output_file, record_count):
    '''
    Entry method which accepts a config file, output path and record count and generates a file with random test data

    :param config_file: Path to JSON file containing the schema details and configuration
    :param output_file: Path where output file should be written to
    :param record_count: number of records to be generated
    :return: None
    '''
    schema = load_schema(config_file)
    num_cols = len(schema)
    template = ('{},' * num_cols)[:-1] + "\n"
    g_list = generator_list(schema)
    generate_data(template, g_list, record_count, output_file)

generate_data_from_schema('./resources/data_schema.json', 'C:/Dev/output.csv', 1000000)