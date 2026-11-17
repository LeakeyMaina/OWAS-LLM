# OWASP Top 10 for LLM Applications (2026): Python demos

This folder contains ten offline Python examples based on common application flows: a RAG support assistant, customer database, agent tool calls, model artifact downloads, feedback-based fine-tuning, API usage limits, policy answers, vector retrieval, and HTML rendering. Each script shows an unsafe path and a safer control.

The examples use local SQLite/CSV/JSON data and representative model responses. They do not connect to a model provider, so no API key or cloud service is required. The LLM outputs are fixtures; the demonstrations focus on realistic application security boundaries around those outputs. These are learning examples, not production security libraries.

The current OWASP list is the **2026 edition**. OWASP revises the list, so older articles may use different names or numbering. The examples follow the 2026 categories:

1. **LLM01 Prompt Injection** — untrusted text changes model behavior.
2. **LLM02 Sensitive Information Disclosure** — responses expose private or regulated information.
3. **LLM03 Excessive Agency** — model decisions can perform actions with too much authority.
4. **LLM04 Supply Chain** — compromised or unsafe models, data, tools, or dependencies enter the application.
5. **LLM05 Data and Model Poisoning** — manipulated training, fine-tuning, or retrieval data affects behavior.
6. **LLM06 Unbounded Consumption** — unrestrained usage causes cost, resource, or service impacts.
7. **LLM07 Misinformation** — plausible but incorrect outputs mislead people or systems.
8. **LLM08 Hidden Context Exposure** — hidden prompts, internal context, or implementation details are revealed.
9. **LLM09 Vector and Embedding Weaknesses** — retrieval and vector-store design returns unsafe or unauthorized content.
10. **LLM10 Improper Output Handling** — model output is trusted as safe input to another system.

## Run a demo

Use Python 3.15 or newer. No packages are required. From the repository root:

```bash
python3 ./OWASP/01_prompt_injection.py
```

From inside this folder, run `python3 01_prompt_injection.py`. Replace the filename to run another demo. In PowerShell, use `python .\OWASP\01_prompt_injection.py` from the repository root.

## How to read the examples

- **Vulnerable** shows how a real application design can expose data, tools, or downstream systems to unsafe model output.
- **Safer** demonstrates an enforceable control in application code. Prompt wording alone is not treated as a security boundary.
- Model responses are fixed example payloads. To test a production model, replace those fixtures with your provider's SDK call while preserving the authorization and validation code around it.
- The fixtures illustrate application control failures; they do not measure a model's real-world capability. OWASP's exploit-generation study cautions that outcomes depend heavily on the harness, human intervention, environment, and evaluation design.

## What the added OWASP resources informed

- **Prompt injection and retrieval:** Retrieved articles, tool responses, and persistent memory are all untrusted input. Keep their provenance visible, constrain what enters context, and enforce tool permissions in application code. The prompt-injection demo gives the assistant only a read-only public-policy lookup.
- **Agent actions:** Treat model tool calls as proposals. Give each assistant only the tools needed for its task; require separate authenticated authorization and explicit human confirmation for irreversible actions. The excessive-agency demo blocks deletion in the assistant flow.
- **Poisoning and data integrity:** Keep source provenance and review state with training records; reject records that lack trusted provenance or integrity checks. The poisoning demo gates its training batch on all three.
- **RAG and isolation:** Apply tenant authorization before similarity ranking, as shown in the vector-retrieval demo. Similarity is not an access-control decision.

These notes draw on the added OWASP PDFs: `OWASP-GenAI-LLM-Top-10-2026-v1.0.pdf`, `Securing-Agentic-Applications-v2.pdf`, `GenAi-Data-Securty-Best-Practices-Part-1.pdf`, and `LLM_Exploit_Generation_Guide_Phase2_10.21.26-1.pdf`. The exploit-generation guide is used here to frame the demos' limits, not as a source of exploit instructions.

## Official references

- [OWASP GenAI LLM Top 10 2026 publication](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/)
- [OWASP's canonical 2026 source list](https://github.com/GenAI-Security-Project/GenAI-LLM-Top10/blob/main/2026/README.md)

