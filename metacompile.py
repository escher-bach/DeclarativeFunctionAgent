import os
import google.generativeai as genai
import json
from google.ai.generativelanguage_v1beta.types import content
import re
import ast
import shutil

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def finder(code):
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_schema": content.Schema(
            type = content.Type.OBJECT,
            enum = [],
            required = ["Functions"],
            properties = {
                "Functions": content.Schema(
                    type = content.Type.ARRAY,
                    items = content.Schema(
                        type = content.Type.OBJECT,
                        properties = {
                            "Func_name": content.Schema(
                                type = content.Type.STRING,
                            ),
                            "Implementation ": content.Schema(
                                type = content.Type.BOOLEAN,
                            ),
                            "description": content.Schema(
                                type = content.Type.STRING,
                            ),
                            "requires_genai": content.Schema(
                                type = content.Type.BOOLEAN,
                            ),
                        },
                    ),
                ),
                "number_of_functions": content.Schema(
                    type = content.Type.INTEGER,
                ),
            },
        ),
        "response_mime_type": "application/json",
    }

    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash-exp",
        generation_config=generation_config,
        system_instruction="Take in a program and identify undefined functions give a description of them too by accertaining from the code, also tell whether the said function could be better implemented by pure coding, or through human/nlp tools (False for no need of human, True for llm) (Assume the function have not been implemented else where). Also specify if the function requires genai API (True/False). The description should be about what the function should do and maybe a example of its use, no need to specify the implementation method in the description just a True or False is alright",
    )

    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    "def somber(x):\n#takes in any string and makes it not funny \nif is_funny(x):\nmake_not_funny(x)\nprintpretty(x)\nreturn x",
                ],
            },
            {
                "role": "model",
                "parts": [
                    "{\n  \"Functions\": [\n    {\n      \"Func_name\": \"is_funny\",\n      \"Implementation \": true,\n      \"description\": \"This function takes a string as input and determines whether it is considered funny. This is subjective, making it better suited for human/NLP tools.\",\n      \"requires_genai\": true\n    },\n    {\n      \"Func_name\": \"make_not_funny\",\n      \"Implementation \": true,\n      \"description\":\"This function takes a string input that is funny and modifies it to be not funny. Requires understanding of humor.\",\n      \"requires_genai\": true\n    },\n     {\n      \"Func_name\":\"printpretty\",\n      \"Implementation \": false,\n      \"description\": \"This function will take a string as an input and print it in a pretty format using formatting libraries.\",\n      \"requires_genai\": false\n    }\n  ],\n  \"number_of_functions\": 3\n}"
                ],
            },
            {
                "role": "user",
                "parts": [
                    "def dialectic_reasoner(x):\n thesis = x\nwhile not satisfied(thesis):\n   syn = synthesis(thesis,antithesis(thesis))\n   thesis = syn\nreturn thesis\n\n",
                ],
            },
            {
                "role": "model",
                "parts": [
                    "{\n  \"Functions\": [\n    {\n      \"Func_name\": \"satisfied\",\n      \"Implementation \": true,\n      \"description\": \"This function takes a statement (thesis) and evaluates if it is considered 'satisfactory' based on some criteria. It may involve complex reasoning or human judgement, making it better suited for human/NLP tools. For example, satisfied('The sky is blue.') could return True if this statement is considered a sufficient answer, or False if not.\"\n    },\n    {\n      \"Func_name\": \"antithesis\",\n      \"Implementation \": true,\n       \"description\": \"This function would take a statement (thesis) and generate an opposing statement (antithesis). This involves understanding the core meaning of the thesis and forming its logical opposite, which can require reasoning and nuanced understanding, making it better suited for human/NLP tools. For example, antithesis('All cats are cute.') could generate 'Some cats are not cute'.\"\n    },\n    {\n      \"Func_name\": \"synthesis\",\n      \"Implementation \": true,\n      \"description\": \"This function takes two statements (a thesis and its antithesis) and generates a new statement that attempts to reconcile the two, creating a synthesis of the ideas. This process involves understanding the relationship between the thesis and antithesis, then creating a higher level more refined idea. The function is better suited for human/NLP tools because the relationship between statements is complex and involves reasoning. For example, synthesis('All cats are cute.','Some cats are not cute') may return 'Most cats are cute, but not all'.\"\n    }\n  ],\n  \"number_of_functions\": 3\n}",
                ],
            },
        ]
    )

    response = chat_session.send_message(code)

    return response.text
"""
def api_caller(about):
    # Create the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash-exp",
        generation_config=generation_config,
        system_instruction="Create a Python function that uses the Gemini API. Make sure the function has proper error handling and docstrings. The function should be self-contained and use the globally configured API using genai.configure(api_key=api_key) api key is there in common you just have configure it"
    )

    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(about)
    return response.text
"""

def api_caller(about):
 genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
 generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

 model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
  system_instruction="Prompts are instructions given to language models, these models then respond in accordance to those prompts, if prompted correctly they can perform correctly otherwise they sometimes lead to error, given instructions you can ask the model to give output in json and also of a particular type and it is always ensured that they stick to the format, I will give you example of a sample api call in python\n\"\"\"\nimport os\nimport google.generativeai as genai\nfrom google.ai.generativelanguage_v1beta.types import content\n\ngenai.configure(api_key=os.environ[\"GEMINI_API_KEY\"])\n\n# Create the model\ngeneration_config = {\n  \"temperature\": 1,\n  \"top_p\": 0.95,\n  \"top_k\": 40,\n  \"max_output_tokens\": 8192,\n  \"response_schema\": content.Schema(\n    type = content.Type.OBJECT,\n    properties = {\n      \"Sample-array\": content.Schema(\n        type = content.Type.ARRAY,\n        items = content.Schema(\n          type = content.Type.OBJECT,\n          properties = {\n            \"nested_Value\": content.Schema(\n              type = content.Type.STRING,\n            ),\n          },\n        ),\n      ),\n      \"Integer_value\": content.Schema(\n        type = content.Type.INTEGER,\n      ),\n    },\n  ),\n  \"response_mime_type\": \"application/json\",\n}\n\nmodel = genai.GenerativeModel(\n  model_name=\"gemini-2.0-flash-exp\",\n  generation_config=generation_config,\n  system_instruction=\"These are instruction that the model must follow\",\n)\n\nchat_session = model.start_chat(\n  history=[\n  ]\n)\n\nresponse = chat_session.send_message(\"INSERT_INPUT_HERE\")\n\nprint(response.text)\n\"\"\"\nAs you can see we were also able to define a json schema for the output to follow, \nWhat I want you do is that I will give you a description of a function and I want you to take inspiration from this api and also ensure that you process the json output  \"response.text contains our json output\"",
 )

 chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "{\n\"Func_name\": \"synthesis\",\n\"Implementation \": true,\n\"description\": \"This function takes two statements (a thesis and its antithesis) and generates a new statement that attempts to reconcile the two, creating a synthesis of the ideas. This process involves understanding the relationship between the thesis and antithesis, then creating a higher level more refined idea. The function is better suited for human/NLP tools because the relationship between statements is complex and involves reasoning. For example, synthesis('All cats are cute.','Some cats are not cute') may return 'Most cats are cute, but not all'.\"\n}",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Okay, I understand. You want me to create a Python function that leverages a language model (like Gemini) to perform the \"synthesis\" task you described. I'll use the provided example API call as a guide and ensure we parse the JSON output appropriately.\n\nHere's a Python function that encapsulates this process:\n\n```python\nimport os\nimport google.generativeai as genai\nimport json\nfrom google.ai.generativelanguage_v1beta.types import content\n\ngenai.configure(api_key=os.environ.get(\"GEMINI_API_KEY\")) # Use get to avoid KeyError\n\ndef synthesis(thesis: str, antithesis: str) -> str:\n    \"\"\"\n    Synthesizes a thesis and its antithesis into a new statement.\n\n    Args:\n        thesis: The initial statement.\n        antithesis: The opposing statement.\n\n    Returns:\n        A synthesized statement, or an error message if the synthesis fails.\n    \"\"\"\n\n    try:\n        # Define the generation config with the desired output schema\n        generation_config = {\n            \"temperature\": 0.7, # Adjusted temperature for more consistent synthesis\n            \"top_p\": 0.95,\n            \"top_k\": 40,\n            \"max_output_tokens\": 8192,\n             \"response_schema\": content.Schema(\n                type=content.Type.OBJECT,\n                properties={\n                    \"synthesis_statement\": content.Schema(\n                        type=content.Type.STRING,\n                    ),\n                },\n             ),\n            \"response_mime_type\": \"application/json\",\n\n        }\n\n        model = genai.GenerativeModel(\n            model_name=\"gemini-2.0-flash-exp\", # Or your preferred model\n            generation_config=generation_config,\n            system_instruction=\"You are an expert in generating synthesis between a thesis and antithesis statement\",\n        )\n\n        chat_session = model.start_chat(\n           history=[ ]\n        )\n        prompt = f\"Synthesize the following statements into a single, coherent statement:\\nThesis: {thesis}\\nAntithesis: {antithesis}\"\n        response = chat_session.send_message(prompt)\n\n        # Attempt to parse the JSON response\n        try:\n            json_output = json.loads(response.text)\n            return json_output.get(\"synthesis_statement\", \"Error: Could not extract synthesis statement from json.\")\n        except json.JSONDecodeError:\n            return f\"Error: Could not decode json. The response is: {response.text}\"\n\n    except Exception as e:\n      return f\"An error occurred: {e}\"\n\n\nif __name__ == '__main__':\n    thesis1 = \"All cats are cute.\"\n    antithesis1 = \"Some cats are not cute.\"\n    synthesis1 = synthesis(thesis1, antithesis1)\n    print(f\"Thesis: {thesis1}\\nAntithesis: {antithesis1}\\nSynthesis: {synthesis1}\\n\")\n    \n    thesis2 = \"The earth is flat\"\n    antithesis2 = \"The earth is spherical\"\n    synthesis2 = synthesis(thesis2, antithesis2)\n    print(f\"Thesis: {thesis2}\\nAntithesis: {antithesis2}\\nSynthesis: {synthesis2}\\n\")\n    \n    thesis3 = \"Artificial intelligence is harmless.\"\n    antithesis3 = \"Artificial intelligence can pose many risks.\"\n    synthesis3 = synthesis(thesis3, antithesis3)\n    print(f\"Thesis: {thesis3}\\nAntithesis: {antithesis3}\\nSynthesis: {synthesis3}\\n\")\n```\n\n**Explanation:**\n\n1.  **Import Necessary Libraries:**\n    *   `os` for environment variables.\n    *   `google.generativeai` for the Gemini API.\n    *   `json` for parsing JSON responses.\n\n2.  **`synthesis(thesis: str, antithesis: str) -> str` Function:**\n    *   Takes two strings, `thesis` and `antithesis`, as input.\n    *   **Error Handling:** It uses a `try-except` block to catch potential errors during the API call or JSON parsing.\n    *   **`generation_config`:**\n        *   Defines parameters for the language model's output.\n        *  Most importantly it contains the JSON schema to be followed `response_schema`.\n    *   **Gemini Model Initialization:**\n        *   Initializes the `gemini-2.0-flash-exp` model with the given configurations and prompt.\n    *   **Prompt Creation:**\n        *   Creates a clear and informative prompt for the model including thesis and antithesis statement.\n    *   **API Call and Response Handling:**\n        *   Sends the prompt to the model using `chat_session.send_message()`.\n        *   Attempts to parse the JSON response:\n            *   Uses `json.loads(response.text)` to parse the JSON.\n            *   Extracts the synthesis string using `json_output.get(\"synthesis_statement\", \"Error: Could not extract synthesis statement.\")`.\n        *   Returns an error message if JSON decoding fails.\n    *  **Exception handling:** handles any other exception during the synthesis process\n3.  **Example Usage (`if __name__ == '__main__':`)**\n    *   Demonstrates how to use the `synthesis` function with example thesis/antithesis pairs.\n\n**Key Improvements:**\n\n*   **JSON Schema:** The `response_schema` is defined in the  `generation_config` which constrains the model to output json with a particular format.\n*   **JSON Parsing:** The `json.loads()` function is used to properly parse the JSON response, and error handling was put in place for JSON decode errors.\n*   **Error Handling:**  Error handling (`try-except`) is included throughout the function, providing informative messages if something goes wrong.\n*   **Clear Return Values:** Returns the synthesis statement as a string or an error string if something goes wrong.\n*   **Clear Documentation:**  The function includes clear docstrings to explain its purpose and parameters.\n\n**To Use This Code:**\n\n1.  **Install the Gemini API Library:**\n    ```bash\n    pip install google-generativeai\n    ```\n2.  **Set Your API Key:**\n    *   Make sure you have your Gemini API key.\n    *   Set the `GEMINI_API_KEY` environment variable using:\n        ```bash\n        export GEMINI_API_KEY=\"YOUR_API_KEY\" # On Linux/macOS\n        set GEMINI_API_KEY=\"YOUR_API_KEY\"    # On Windows\n        ```\n        or you can use the method used in the example `os.environ.get(\"GEMINI_API_KEY\")`\n3.  **Run the Python Script:**\n    ```bash\n    python your_script_name.py\n    ```\n\nThis enhanced version provides a more robust and reliable way to use the Gemini model for synthesis tasks, incorporating proper JSON handling and error management. Let me know if you have further questions or want to customize it further.\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "great from now on write only the functions no other code\n{\n\"Func_name\": \"make_not_funny\",\n\"Implementation \": true,\n\"description\":\"This function takes a string input that is funny and modifies it to be not funny. Requires understanding of humor, making it better suited for human/NLP tools.\"\n}",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```python\nimport os\nimport google.generativeai as genai\nimport json\nfrom google.ai.generativelanguage_v1beta.types import content\n\ngenai.configure(api_key=os.environ.get(\"GEMINI_API_KEY\"))\n\ndef make_not_funny(funny_text: str) -> str:\n    \"\"\"\n    Takes a funny string and modifies it to be not funny.\n\n    Args:\n        funny_text: The input string that is considered funny.\n\n    Returns:\n        A modified string that is not funny, or an error message if the process fails.\n    \"\"\"\n    try:\n        generation_config = {\n            \"temperature\": 0.7,\n            \"top_p\": 0.95,\n            \"top_k\": 40,\n            \"max_output_tokens\": 8192,\n            \"response_schema\": content.Schema(\n                type=content.Type.OBJECT,\n                properties={\n                    \"not_funny_text\": content.Schema(\n                        type=content.Type.STRING,\n                    ),\n                },\n            ),\n            \"response_mime_type\": \"application/json\",\n        }\n\n        model = genai.GenerativeModel(\n            model_name=\"gemini-2.0-flash-exp\",\n            generation_config=generation_config,\n            system_instruction=\"You are an expert at making humorous text not funny.\",\n        )\n\n        chat_session = model.start_chat(\n            history=[],\n        )\n\n        prompt = f\"Modify the following text to make it not funny:\\n{funny_text}\"\n        response = chat_session.send_message(prompt)\n        \n        try:\n            json_output = json.loads(response.text)\n            return json_output.get(\"not_funny_text\", \"Error: Could not extract not funny text from json.\")\n        except json.JSONDecodeError:\n             return f\"Error: Could not decode json. The response is: {response.text}\"\n\n\n    except Exception as e:\n      return f\"An error occurred: {e}\"\n```\n",
      ],
    },
  ]
)

 response = chat_session.send_message(about)

 return response.text
def direct_implement(about):
    # Create the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash-exp",
        generation_config=generation_config,
        system_instruction="Create a Python function that implements the given functionality without using the Gemini API. The function should be self-contained with proper docstrings and error handling where necessary. Also ensure that all the packages that need to be imported are imported import all nessecary package inside the function",
    )


    chat_session = model.start_chat(
        history=[
    {
      "role": "user",
      "parts": [
        "{\n\"Func_name\":\"printpretty\",\n\"description\": \"This function will take a string as an input and print it in a pretty format. It can be implemented using pure code, such as formatting libraries.\"\n}\ndef somber(x):\n#takes in any string and makes it not funny\nif is_funny(x):\nmake_not_funny(x)\nprintpretty(x)\nreturn x",
      ],
    },
    {
      "role": "model",
      "parts": [
        "```python\ndef printpretty(text):\n    \"\"\"This function will take a string as an input and print it in a pretty format. \n    It can be implemented using pure code, such as formatting libraries.\"\"\"\n    \n    print(\"-\" * (len(text) + 4))\n    print(\"| \" + text + \" |\")\n    print(\"-\" * (len(text) + 4))\n```\n",
      ],
    },
  ]
)    
    response = chat_session.send_message(about)
    return response.text

def strip_code(code):
 # Match from the first `def` to the last ```
 pattern_with_backticks = r"(def .*?)```"

 # Match starting from the first `def` if no backticks are present
 pattern_without_backticks = r"(def .*?)$"

 # Try to match with the backticks pattern first
 match = re.search(pattern_with_backticks, code, flags=re.DOTALL)

 if match:
    # Extract the matched content including backticks
    stripped_code = match.group(1)
 elif re.search(pattern_without_backticks, code, flags=re.DOTALL):
    # Fallback to match without backticks
    match = re.search(pattern_without_backticks, code, flags=re.DOTALL)
    stripped_code = match.group(1)
 else:
    stripped_code = ""
 return stripped_code

def remove_trailing_backquotes_from_string(input_string):
    """
    Removes three backquotes (```) from the end of a string if they exist.

    Parameters:
        input_string (str): The input string to modify.

    Returns:
        str: The modified string with trailing backquotes removed, if present.
    """
    if input_string.endswith('```'):
        return input_string[:-3]
    return input_string


#hi ok so here is the flow for this code
#We get a filename from the user
#We read the file and store the code in a variable
#We then parse the code into a json object using finder
#Now for every function in the json object we create a new file with the functions name and write the code using either the direct_write or apicaller function
#we create a new file that is the copy of the original file but we import all the functions from the other files (which have the name of the function)
#say bye to the user
"""
json template
{
  "type": "object",
  "properties": {
    "Functions": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "Func_name": {
            "type": "string"
          },
          "Implementation ": {
            "type": "boolean"
          },
          "description": {
            "type": "string"
          },
          "programminglanguage": {
            "type": "string"
          }
        },
        "required": [
          "programminglanguage"
        ]
      }
    },
    "number_of_functions": {
      "type": "integer"
    }
  },
  "required": [
    "Functions"
  ]
}
"""
def merge_python_files(input_files, output_file):
    """This function takes a list of python files as input and merges them into a 
    destination file adding import statements for each function."""

    function_names = []
    with open(output_file, 'w') as outfile:
        for input_file in input_files:
            with open(input_file, 'r') as infile:
                tree = ast.parse(infile.read())
                for node in ast.walk(tree):
                    if isinstance(node, ast.FunctionDef):
                        function_names.append((node.name, input_file.replace(".py", "")))

        # Write import statements
        for name, module in function_names:
            outfile.write(f"from {module} import {name}\n")

        outfile.write("\n")

        # Write file content
        for input_file in input_files:
            with open(input_file, 'r') as infile:
                outfile.write(infile.read())
                outfile.write("\n")

def create_project_structure(project_name, code, functions):
    """Creates an organized project structure with separate files for each function."""
    # Create project directory
    project_dir = os.path.join(os.getcwd(), project_name)
    if os.path.exists(project_dir):
        shutil.rmtree(project_dir)
    os.makedirs(project_dir)

    # Create src directory for function implementations
    src_dir = os.path.join(project_dir, "src")
    os.makedirs(src_dir)

    # Create __init__.py in src directory to make it a package
    with open(os.path.join(src_dir, "__init__.py"), "w") as f:
        pass

    # Create common.py for shared imports and utilities
    common_file = os.path.join(src_dir, "common.py")
    with open(common_file, 'w') as file:
        file.write("import os\n")
        file.write("import google.generativeai as genai\n")
        file.write("import json\n")
        file.write("from google.ai.generativelanguage_v1beta.types import content\n\n")
        file.write("# Configure Gemini API globally\n")
        file.write("api_key = os.environ.get('GEMINI_API_KEY')\n")
        file.write("if not api_key:\n")
        file.write('    raise EnvironmentError("GEMINI_API_KEY environment variable is not set")\n')
        file.write("genai.configure(api_key=api_key)\n")

    # Generate function files
    for function in functions:
        func_filename = os.path.join(src_dir, f"{function['Func_name']}.py")
        with open(func_filename, 'w') as file:
            if function.get("requires_genai", False):
                file.write("from .common import os, genai, content, json\n\n")
            else:
                file.write("# No Gemini imports needed for this function\n\n")
            if function["Implementation "] == False:
                file.write(strip_code(direct_implement(json.dumps(function))))
            else:
                file.write(strip_code(api_caller(json.dumps(function))))

    # Create main.py that imports and uses the functions
    main_file = os.path.join(project_dir, "main.py")
    with open(main_file, 'w') as file:
        # Write imports
        file.write("import os\n")
        
        # Import from common if any function requires genai
        if any(function.get("requires_genai", False) for function in functions):
            file.write("from src.common import genai, content, json\n")
        
        # Import all functions from src
        file.write("\n# Import implemented functions\n")
        for function in functions:
            file.write(f"from src.{function['Func_name']} import {function['Func_name']}\n")
        
        # Write the original code
        file.write("\n# Original implementation\n")
        file.write(code)

    # Create requirements.txt
    requirements = os.path.join(project_dir, "requirements.txt")
    with open(requirements, 'w') as file:
        file.write("google-generativeai\n")

    # Create README.md with project documentation
    readme = os.path.join(project_dir, "README.md")
    with open(readme, 'w') as file:
        file.write(f"# {project_name}\n\n")
        file.write("## Setup\n\n")
        file.write("1. Install requirements:\n")
        file.write("```bash\npip install -r requirements.txt\n```\n\n")
        file.write("2. Set up environment variables:\n")
        file.write("```bash\nexport GEMINI_API_KEY='your_api_key_here'\n```\n\n")
        file.write("## Project Structure\n\n")
        file.write("- `src/`: Contains individual function implementations\n")
        file.write("- `main.py`: Main program that uses the implemented functions\n")
        file.write("- `requirements.txt`: Project dependencies\n\n")
        file.write("## Available Functions\n\n")
        for function in functions:
            file.write(f"### {function['Func_name']}\n")
            file.write(f"{function['description']}\n\n")

def main():
    filename = input("Enter the filename: ")
    project_name = input("Enter project name (press Enter to use filename without extension): ").strip()
    
    if not project_name:
        project_name = os.path.splitext(os.path.basename(filename))[0]

    with open(filename, 'r') as file:
        code = file.read()
        json_object = json.loads(finder(code))
        create_project_structure(project_name, code, json_object["Functions"])
        print(f"Project '{project_name}' has been created successfully!")
        print(f"You can find the project files in: {os.path.join(os.getcwd(), project_name)}")

if __name__ == "__main__":
    main()