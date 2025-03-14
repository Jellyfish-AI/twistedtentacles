import os
import importlib

def import_all_modules_from_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = filename[:-3]
            importlib.import_module(f'company_files.{module_name}')


tagged_functions = {}

def company_specific_function(company_slug=None):
    def decorator(func):
        if company_slug not in tagged_functions:
            tagged_functions[company_slug] = []
        tagged_functions[company_slug].append(func)
        return func
    return decorator

def run_company_specific_functions(company_slug=None, *args, **kwargs):
    if company_slug:
        if company_slug in tagged_functions:
            for func in tagged_functions[company_slug]:
                func(*args, **kwargs)
    else:
        for funcs in tagged_functions.values():
            for func in funcs:
                func(*args, **kwargs)