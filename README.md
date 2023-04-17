# GPT-3.5 Turbo Story Generator

This project explores the capabilities and limitations of the GPT-3.5 Turbo model from OpenAI. It's designed to generate stories based on user input, with a focus on the Dungeons & Dragons fantasy genre.

## Limitations

GPT-3.5 Turbo has some limitations regarding the length of stories it can generate. The maximum token limit for a given prompt is 4,000 tokens, which is roughly equivalent to 3,000 words. However, the actual story length may vary depending on the randomness and the prompt provided. Longer stories might be cut short to fit within these constraints.

## Technologies Used

- Python
- OpenAI API
- GPT-3.5 Turbo

## Installation and Setup

1. Clone this repository.
2. Install the required Python packages by running `pip install -r requirements.txt`.
3. Create a `.env` file in the project root directory and add your OpenAI API key like this: `OPENAI_API_KEY=your_api_key_here`.

## Usage

Customize the prompts and rules according to your own needs.

To start the story generation, run the `app.py` script:

Specify the desired length of the story and the level of randomness, and save the generated story as a PDF or DOCX file.

## Contribution

Feel free to contribute to this project by opening issues, submitting pull requests, or suggesting improvements.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.