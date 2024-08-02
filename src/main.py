import os
import json
import deepl


# set working directory
working_dir = os.path.dirname(os.path.abspath(__file__))
config_file = json.load(open(f"{working_dir}/config.json"))


# get log file path from user input
log_file = input("Enter filename of log file: ")
log_file_path = f"{working_dir}/logs/{log_file}.txt"


# read file line for line and store into list
f = open(log_file_path, "r", encoding="utf-8")
lines = f.readlines()


# read config.json for API key
DEEPL_API_KEY = config_file["DEEPL_API_KEY"]


# initialize translator
translator = deepl.Translator(DEEPL_API_KEY)


# translate lines -> ***ENTER TARGET LANGUAGE IN THE target_lang= ARGUMENT***
translated_text = [translator.translate_text(line, target_lang="EN-US") for line in lines]


# save translated text to new text document
with open(f"{working_dir}/logs/{log_file}-TRANSLATED.txt", "w+", encoding="utf-8") as f:
    for line in translated_text:
        f.write(f"{line}\n")
