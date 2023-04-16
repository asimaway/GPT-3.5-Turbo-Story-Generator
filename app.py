import openai
import os
import pathlib
from docx import Document
from ruleset import rules

openai.api_key = "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" #replace this with your own key 

story_prompt = "Write a Dungeons & Dragons story that follows these rules:\n" + rules #change the promt and rules as required

response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=story_prompt,
    max_tokens=1500, #controls the length of the story
    n=1,
    stop=None,
    temperature=1.0, #this field controls randomness 1.0 is the highest and 0.1 is the lowest
)

story = response['choices'][0]['text'].strip()

# Function to find the next available file name
def find_next_available_filename(filename_base, extension):
    i = 1
    while True:
        file_name = f"{filename_base}_{i}.{extension}"
        if not pathlib.Path(file_name).exists():
            break
        i += 1
    return file_name

filename_base = "dnd_story"
extension = "docx"
available_filename = find_next_available_filename(filename_base, extension)

folder = "stories"  # Change this to the desired folder name
pathlib.Path(folder).mkdir(exist_ok=True)  # Create the folder if it doesn't exist
available_filename = os.path.join(folder, find_next_available_filename(filename_base, extension))


document = Document()
document.add_paragraph(story)
document.save(available_filename)