# Automated AI Agenct SEO Crawler with browser-use and DeepSeek R1

This project demonstrates how to use an AI-powered browser-use agent to analyze and suggest semantic improvements for a webpage. The script uses the `langchain_openai` library with the `ChatOpenAI` model and is designed to interact with and extract insights from web pages for semantic content optimization.

## Features

- **Semantic Analysis**: Automatically analyzes a webpage's content for semantic placements.
- **Content Extraction**: Extracts current semantic content placements.
- **Suggestions**: Provides recommendations for missing long-tail queries.
- **Task Automation**: Fully automated using asyncio and an AI agent.

## Prerequisites

Ensure you have the following installed and configured:

- Python 3.9+
- `browser-use` library
- `langchain_openai` library
- `dotenv` library
- `pydantic` library

You also need an API key for `DeepSeek`, which should be stored in an `.env` file.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/metehan777/deepseek-r1-browser-use-seo-analysis.git
   cd deepseek-r1-browser-use-seo-analysis
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your `.env` file:

   Create a file named `.env` in the root directory of the project and add your `DeepSeek` API key:

   ```env
   DEEPSEEK_API_KEY=your_deepseek_api_key
   ```

## Usage

Run the script to analyze the webpage and save the results to `output.txt`:

```bash
python ai_seo_crawler.py
```

The script performs the following tasks:

1. Navigates to [AppSamurai](https://appsamurai.com).
2. Analyzes the page for the best semantic placements of content.
3. Extracts the current semantic content placements.
4. Suggests missing semantic long-tail queries.

## Code Overview

### ai_seo_crawler.py

```python
import asyncio
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import SecretStr
from browser_use import Agent

# Load environment
load_dotenv()

async def run_search():
    # Initialize agent with tasks
    agent = Agent(
        task=(
            '1. Go to https://appsamurai.com\n'
            '2. Analyze the page for the best semantic placements of contents\n'
            '3. Extract the current semantic content placements\n'
            '4. Suggest missing semantic long-tail queries'
        ),
        llm=ChatOpenAI(
            base_url='https://api.deepseek.com/v1',
            model='deepseek-reasoner',
            api_key=SecretStr(os.getenv('DEEPSEEK_API_KEY', '')),
        ),
        use_vision=False,
    )

    # Execute tasks and save raw output
    result = await agent.run()
    
    # Basic text file output
    with open('output.txt', 'w', encoding='utf-8') as f:
        f.write(str(result))

if __name__ == '__main__':
    asyncio.run(run_search())
```

### browser_use

This file contains the `Agent` class, which performs tasks such as browsing, analyzing, and suggesting improvements for a webpage. Ensure this module is implemented correctly to support the main script.

## Output

The results of the analysis will be saved in `output.txt`, which includes:

- Extracted semantic content placements.
- Suggested long-tail queries for semantic optimization.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## Author

[Metehan Yesilyurt](https://github.com/metehan777)

---
