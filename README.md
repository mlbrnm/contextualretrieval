<p align="center">
<img src="https://i.imgur.com/NUs8MWf.png" width="600" />
</p>
<p align="center">https://www.anthropic.com/news/contextual-retrieval</p>

---

This is a script / proof of concept that follows Anthropic's suggestions for improving RAG performance using 'contextual retrieval'.

Documents are ingested from a folder (`\docs2process`), and split into chunks based on a predefined delimiter. I am using `-+-+-+-` and manually inserting them where I think the documents should be divided.

The chunks are sent one-by-one to the Ollama model, with a prompt requesting a succinct summary of all the context required to understand the chunk.

A new document is then saved as `contexted_ORIGINALFILENAME.EXT`.

I am working on improving the script so that chunks and their new context blocks are then turned into embeddings and ingested into the qdrant database for direct use in a RAG system.

## Installation / Prerequisites
Testing was done in a Python 3.11.0b4 environment because I'm using [PrivateGPT](https://docs.privategpt.dev/installation/getting-started/installation) and that's what they use.

I used [pyenv](https://github.com/pyenv-win/pyenv-win) for the virtual environment.

Navigate to repository folder and do the following to use the right Python. I'm sure you could also use Anaconda or something.
```
pyenv install 3.11.0b4
pyenv local 3.11.0b4
```
Install the ollama module and qdrant.
```
pyenv exec pip install ollama
pyenv exec pip install qdrant-client
```
Run main.py.
```
python main.py
```
