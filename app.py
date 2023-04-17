import os
import openai
from docx import Document
import pathlib
from docx2pdf import convert
from save_story import save_as_docx, save_as_pdf

# Replace with your own OpenAI API key
openai.api_key = "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"

prompt = "Write a short Dungeons & Dragons story that follows these rules: "
rules = """
- The story takes place in a medieval fantasy world called Eldoria.
- There are five main characters: Aramil, Thalia, Grom, Nissa, Kael.
- The characters meet in a tavern located in a small town named Stoneshire.
- They form an adventuring party to explore a recently discovered ancient ruin.
- The ruin is said to contain a powerful artifact known as the Orb of Azoria.
- The main antagonist is an evil necromancer named Valthor.
- The story includes various challenges and encounters during the journey.
- The story must include a subplot involving a mysterious figure who aids the party.
- The story should contain moments of humor, suspense, and drama.
- The story must end on a hopeful note, with the possibility of future adventures.
"""

story_prompt = prompt + rules
max_tokens = int(input("Enter the length of the story (max is 4000): "))
n = 1  # Number of completions to generate
temperature = float(input("Enter the temperature (higher values = more randomness, e.g., 0.1 to 1.0): "))

response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=story_prompt,
    max_tokens=max_tokens,
    n=n,
    stop=None,
    temperature=temperature,
)

story = response.choices[0].text.strip()

filename_base = f"DnD_story_{max_tokens}_{temperature}"
folder = "generated_stories"
pathlib.Path(folder).mkdir(exist_ok=True)

# Need Office to properly save pdf
# output_format = input("Do you want to generate a PDF or keep it as DOCX? (Enter 'PDF' or 'DOCX'): ")
# if output_format.lower() == "pdf":
#     pdf_filename = save_as_pdf(folder, filename_base, story)
#     print(f"Story saved as: {pdf_filename}")
# else:

docx_filename = save_as_docx(folder, filename_base, story)
print(f"Story saved as: {docx_filename}")
