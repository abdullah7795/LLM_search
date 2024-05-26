# llm_search

`llm_search` is an advanced AI system designed to assist users in various tasks by leveraging a set of tools and a team of AI Assistants. This project utilizes multiple AI models and tools to provide comprehensive assistance, including web searching, data analysis, Python code execution, financial analysis, and more.

## Setup and Usage

Follow the steps below to set up and run the project.

### Step 1: Run the Setup Script

First, execute the `setup.py` script to install the necessary dependencies and set up the environment.
```bash
python setup.py
```
### Step 2: Start the Ollama Server

Next, start the Ollama server which will serve the AI models.

```bash
ollama serve
```
### Step 3: Run the Main Script

Finally, run the main.py script to start the llm_search assistant.

```bash
python main.py
```
## Project Structure

setup.py: Script to set up the project environment.
main.py: Main script to initialize and run the llm_search assistant.
llm_search: Directory containing the core code for the AI assistant and its tools.

## Features

Web Searching: Uses DuckDuckGo to search the web.
Data Analysis: Analyzes data using DuckDB.
Python Code Execution: Executes Python code and provides results.
Financial Analysis: Generates investment reports based on stock data.
Research Assistance: Writes research reports on given topics.

## Example Usage

The following example demonstrates how to use the llm_search assistant to search for the top 10 songs till date.

```python
question = "Search the internet and give me top 10 songs till date."
response = question_assistant(assistant, question)
print("Question:", question)
print("Response:", response)
```
## Contact
If you have any questions, feel free to reach out to me on Gmail: mohammedabdullah0212@gmail.com