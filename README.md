# multiagent_research-lab
This repository contains a simulation of a multi-agent research collaboration where autonomous AI agents gather, analyze, and synthesize information about an AI-related topic using open-source frameworks and the Hugging Face Inference API. Each agent acts as part of a “virtual research lab” working to produce a coherent research summary.


# README.md — Exercise 1: AI Research Team

Joaquín — Perú  
17 nov 2025, 12:20 AM

¿Qué hace?
3 agentes trabajan juntos:
- Researcher: busca en DuckDuckGo.
- Writer: escribe informe (~500 palabras).
- Reviewer: revisa y corrige.

Tema: Sesgos en LLMs.  
Salida: research_summary.md (Markdown).

Archivos
src/agents.py
notebooks/workflow_demo.ipynb
research_summary.md
requirements.txt

Requisitos
crewai
langchain
huggingface_hub
duckduckgo-search
chromadb
pandas
langchain-community

pip install -r requirements.txt

Ejecutar (Colab)
1. Abre workflow_demo.ipynb.
2. Pega tu token de Hugging Face.
3. Corre todo.
4. Descarga research_summary.md.

Listo.