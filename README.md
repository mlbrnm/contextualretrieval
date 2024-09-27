https://www.anthropic.com/news/contextual-retrieval

This is a script / proof of concept that follows Anthropic's suggestions for improving RAG performance using 'contextual retrieval'.

The document to ingest is split by a predefined delimiter (I'm using ---------- and inserting them manually where I want the chunks split).

The chunks are sent 1 by 1 to the Ollama model, with a prompt requesting a succinct summary of all the context required to understand the chunk.

The chunks and their new context blocks are then turned into embeddings and ingested into the qdrant database for use in a RAG system.

## Installation / Prerequisites
Testing was done in a Python 3.11.0b4 environment because I'm using [PrivateGPT](https://docs.privategpt.dev/installation/getting-started/installation) and that's what they use.

I used [pyenv](https://github.com/pyenv-win/pyenv-win) for the virtual environment.

Navigate to repository folder and do the following to use the right Python. I'm sure you could also use Anaconda or something.
```
pyenv install 3.11.0b4
pyenv local 3.11.0b4
```
Install the ollama module.
```
pyenv exec pip install ollama
```
Run main.py.
```
python main.py
```
