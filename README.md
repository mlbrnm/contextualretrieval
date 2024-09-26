https://www.anthropic.com/news/contextual-retrieval

This is a script / proof of concept that follows Anthropic's suggestions for improving RAG performance using 'contextual retrieval'.

The document to ingest is split by a predefined delimiter (I'm using ---------- and inserting them manually where I want the chunks split).

The chunks are sent 1 by 1 to the Ollama model, with a prompt requesting a succinct summary of all the context required to understand the chunk.

The chunks and their new context blocks are then turned into embeddings and ingested into the qdrant database for use in a RAG system.
