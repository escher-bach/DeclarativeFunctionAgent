# AI Function Compiler

This project provides a tool that helps break down Python functions into smaller, maintainable components by analyzing code and implementing undefined functions using the Gemini API or direct implementation.

## Features

- Analyzes Python code to identify undefined functions
- Automatically determines whether functions need Gemini API or can be directly implemented
- Creates organized project structures with separate files for each function
- Generates comprehensive documentation
- Handles dependencies and requirements automatically

## Prerequisites

- Python 3.x
- Google Gemini API key

## Installation

1. Clone the repository:
```bash
git clone [your-repo-url]
cd ai_compiler
```

2. Install required packages:
```bash
pip install google-generativeai
```

3. Set up your Gemini API key:
```bash
# For Windows
set GEMINI_API_KEY=your_api_key_here

# For Unix/Linux/MacOS
export GEMINI_API_KEY=your_api_key_here
```

## Usage

1. Run metacompile.py:
```bash
python metacompile.py
```

2. When prompted:
   - Enter the path to your Python file
   - Enter a project name (or press Enter to use the filename)

3. The tool will:
   - Analyze your code
   - Identify undefined functions
   - Create a new project structure with:
     - Separate implementation files for each function
     - A common.py file for shared utilities
     - A main.py file that imports and uses all functions
     - A requirements.txt file
     - A README.md with documentation

## Project Structure Generated

```
your_project_name/
├── src/
│   ├── __init__.py
│   ├── common.py
│   └── [function_name].py
├── main.py
├── requirements.txt
└── README.md
```

## Key Components

- **metacompile.py**: Main script that handles the compilation process
- **finder()**: Analyzes code and identifies undefined functions
- **api_caller()**: Generates implementations using Gemini API
- **direct_implement()**: Creates implementations without using AI
- **create_project_structure()**: Organizes the project files

## Function Implementation Types

The tool automatically determines how each function should be implemented:

1. **Direct Implementation**: For functions that can be implemented with pure code
2. **AI-Assisted Implementation**: For functions that require natural language processing or complex reasoning

## Error Handling

- Validates environment variables
- Handles API errors gracefully
- Provides informative error messages
- Ensures proper file structure creation

## Contributing

Feel free to submit issues and enhancement requests!

## License

[Your License Here]