# AlexGPT

AlexGPT is an AI assistant that takes user input and executes predefined actions from an `actions.json` file. It uses OpenAI's `gpt-4-1106-preview`` model to process and understand the user's input.

## Getting Started

These instructions will help you setup the project and run on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6 or higher
- OpenAI's API KEY to run gpt-4-1106-preview model

### Installation

1. Clone the repo
    ```sh
    git clone https://github.com/kavienanj/AlexGPT.git
    ```
2. Install Python packages
    ```sh
    pip install -r requirements.txt
    ```
3. Create a `.env` file in the root directory and add the following variables:
    ```sh
    OPENAI_API_KEY=<your_openai_api_key>
    ```

### Usage
Run the main.py script:
```py
python main.py
```

The AI assistant will start and wait for your input. You can type in your commands and the assistant will execute the corresponding actions defined in the `actions.json` file.

## Adding a New Action

An action is a task that can be executed by the system. Actions are defined in the `actions.json` file.

Each action has the following structure:

```json
{
    "task_name": "TaskName",
    "description": "Description of the task",
    "script": "Script to run",
    "variables": [
        {
            "name": "VariableName",
            "type": "VariableType",
            "required": true/false,
            "default": "DefaultValue"
        }
    ],
    "parameters": {
        "commands": [
            "Command to execute"
        ]
    }
}
```

- task_name: A unique name for the task.
- description: A brief description of what the task does.
- script: The script that will be run to execute the task.
- variables: A list of variables that the task uses. Each variable has a name, type, required flag, and a default value.
- parameters: A list of commands that the task will execute.

To add a new action, simply add a new object to the actions.json file following the structure above.

### Contributing
Any contributions you make are greatly appreciated.

### Fork the Project
- Create your Feature Branch (git checkout -b feature/AmazingFeature)
- Commit your Changes (git commit -m 'Add some AmazingFeature')
- Push to the Branch (git push origin feature/AmazingFeature)
- Open a Pull Request

### Contact
Kavienan J - kavienanj@gmail.com

Project Link: https://github.com/kavienanj/AlexGPT
