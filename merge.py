import os
import shutil

def merge_projects(project1: str, project2: str, output_project: str) -> None:
    """
    Merge two projects into a new project.
    
    Args:
        project1: Name of the first project
        project2: Name of the second project
        output_project: Name of the merged project
        
    Raises:
        ValueError: If projects don't exist or required files are missing
        OSError: If there are permission or I/O errors
    """
    cwd = os.getcwd()
    project1_path = os.path.join(cwd, project1)
    project2_path = os.path.join(cwd, project2)
    output_path = os.path.join(cwd, output_project)

    # Validate input projects exist and have required structure
    for project_path in [project1_path, project2_path]:
        if not os.path.exists(project_path):
            raise ValueError(f"Project doesn't exist: {os.path.basename(project_path)}")
        if not os.path.exists(os.path.join(project_path, 'src')):
            raise ValueError(f"Project {os.path.basename(project_path)} is missing src directory")
        required_files = ['main.py', os.path.join('src', 'common.py')]
        for file in required_files:
            if not os.path.exists(os.path.join(project_path, file)):
                raise ValueError(f"Project {os.path.basename(project_path)} is missing {file}")

    try:
        # Create new project structure
        if os.path.exists(output_path):
            shutil.rmtree(output_path)
        os.makedirs(output_path)
        os.makedirs(os.path.join(output_path, 'src'))

        # Copy common.py and __init__.py
        shutil.copy2(
            os.path.join(project1_path, 'src', 'common.py'),
            os.path.join(output_path, 'src', 'common.py')
        )
        with open(os.path.join(output_path, 'src', '__init__.py'), 'w') as f:
            pass

        # Copy all function files from both projects
        imported_functions = []
        for project_path in [project1_path, project2_path]:
            src_path = os.path.join(project_path, 'src')
            for file in os.listdir(src_path):
                if file not in ['common.py', '__init__.py', '__pycache__'] and file.endswith('.py'):
                    shutil.copy2(
                        os.path.join(src_path, file),
                        os.path.join(output_path, 'src', file)
                    )
                    imported_functions.append(file[:-3])  # Remove .py extension

        # Create merged main.py
        with open(os.path.join(output_path, 'main.py'), 'w') as outfile:
            outfile.write("import os\n")
            
            # Check if any project requires genai by looking at their function files
            requires_genai = False
            for project_path in [project1_path, project2_path]:
                src_path = os.path.join(project_path, 'src')
                for file in os.listdir(src_path):
                    if file.endswith('.py'):
                        with open(os.path.join(src_path, file), 'r') as f:
                            content = f.read()
                            if 'from .common import' in content and ('genai' in content or 'content' in content or 'json' in content):
                                requires_genai = True
                                break
            
            if requires_genai:
                outfile.write("from src.common import genai, content, json\n")
            
            # Import all functions
            outfile.write("\n# Import implemented functions\n")
            for func in imported_functions:
                outfile.write(f"from src.{func} import {func}\n")
            
            # Combine main.py contents from both projects
            outfile.write("\n# Code from project 1\n")
            with open(os.path.join(project1_path, 'main.py'), 'r') as f:
                main1_content = f.read()
                # Skip imports and write the rest
                main1_lines = main1_content.split('\n')
                for line in main1_lines:
                    if not line.startswith(('import', 'from')):
                        outfile.write(line + '\n')
            
            outfile.write("\n# Code from project 2\n")
            with open(os.path.join(project2_path, 'main.py'), 'r') as f:
                main2_content = f.read()
                # Skip imports and write the rest
                main2_lines = main2_content.split('\n')
                for line in main2_lines:
                    if not line.startswith(('import', 'from')):
                        outfile.write(line + '\n')

        # Merge requirements.txt
        requirements = set()
        for project_path in [project1_path, project2_path]:
            req_path = os.path.join(project_path, 'requirements.txt')
            if os.path.exists(req_path):
                with open(req_path, 'r') as f:
                    requirements.update(f.read().splitlines())
        
        with open(os.path.join(output_path, 'requirements.txt'), 'w') as f:
            f.write('\n'.join(sorted(requirements)))

        # Create merged README.md
        with open(os.path.join(output_path, 'README.md'), 'w') as f:
            f.write(f"# {output_project}\n\n")
            f.write(f"This project is a merge of {project1} and {project2}\n\n")
            f.write("## Setup\n\n")
            f.write("1. Install requirements:\n")
            f.write("```bash\npip install -r requirements.txt\n```\n\n")
            f.write("2. Set up environment variables:\n")
            f.write("```bash\nexport GEMINI_API_KEY='your_api_key_here'\n```\n\n")
            f.write("## Project Structure\n\n")
            f.write("- `src/`: Contains individual function implementations\n")
            f.write("- `main.py`: Main program that uses the implemented functions\n")
            f.write("- `requirements.txt`: Project dependencies\n\n")
            f.write("## Available Functions\n\n")
            for func in imported_functions:
                f.write(f"### {func}\n")
                f.write(f"Imported from one of the source projects\n\n")
    except OSError as e:
        raise OSError(f"Failed to create or modify project files: {e}")
    except Exception as e:
        raise Exception(f"Unexpected error during merge: {e}")

def main():
    print("Project Merger - Combine two AI compiler projects into one")
    print("-" * 50)
    project1 = input("Enter the name of the first project: ").strip()
    project2 = input("Enter the name of the second project: ").strip()
    output_project = input("Enter the name for the merged project: ").strip()
    
    if not all([project1, project2, output_project]):
        print("Error: All project names must be non-empty")
        return
    
    if project1 == project2:
        print("Error: Cannot merge a project with itself")
        return
        
    if output_project in [project1, project2]:
        print("Error: Output project name must be different from input projects")
        return
    
    try:
        merge_projects(project1, project2, output_project)
        print(f"\nSuccess! Projects have been merged into: {output_project}")
        print(f"You can find the merged project at: {os.path.join(os.getcwd(), output_project)}")
    except (ValueError, OSError) as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nUnexpected error: {e}")

if __name__ == "__main__":
    main()