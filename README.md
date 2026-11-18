# OWASP Top 10 for LLM Applications (2026)

Small Python demos for learning the ten risks in the OWASP Top 10 for LLM Applications. Every issue has its own package directory containing separate vulnerable, secure, demo, and explanation files. The examples use synthetic data and local-only side effects.

These are teaching examples, not production security libraries. The default demos use fixed fixtures and run without an API key. The optional prompt-injection live demo uses LangChain, LangGraph, and the OpenAI chat model integration; it requires `OPENAI_API_KEY`.

## Setup

The project targets Python 3.15 or newer. Create a virtual environment, then install the project and its dependencies:

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
```

On macOS or Linux:

```bash
source .venv/bin/activate
python -m pip install -e .
```

## Run demos

List the available issue package names:

```bash
owasp
```

Run one demo:

```bash
owasp llm01_prompt_injection
```

The optional live tool-calling run for prompt injection uses real LangChain `@tool` functions in a custom LangGraph loop. Its email tool records only to an in-memory demo outbox:

```bash
owasp llm01_prompt_injection --live
```

The repository also supports `python -m owasp` and `python -m owasp.llm01_prompt_injection.demo` after installation.

## Learning structure

Each issue package separates concerns:

- `vulnerable.py` shows the insecure application path.
- `secure.py` shows the control enforced in application code.
- `demo.py` wires the two paths together and prints the result.
- `README.md` describes the scenario, code walkthrough, and security lesson.
- Some issues have additional files for data fixtures, tool definitions, or live agent wiring.

Each executable demo has an `if __name__ == "__main__":` entry point. Shared helper modules remain import-safe and do not start model calls or perform side effects when imported.

| OWASP issue | Package | Focus |
| --- | --- | --- |
| LLM01 | `llm01_prompt_injection` | Untrusted retrieved text and restricted tools |
| LLM02 | `llm02_sensitive_information_disclosure` | Authorization and data minimization |
| LLM03 | `llm03_excessive_agency` | Least privilege and tool approval |
| LLM04 | `llm04_supply_chain` | Artifact integrity and provenance |
| LLM05 | `llm05_data_model_poisoning` | Dataset provenance and review |
| LLM06 | `llm06_unbounded_consumption` | Input/output and user-budget limits |
| LLM07 | `llm07_misinformation` | Claim verification against source data |
| LLM08 | `llm08_hidden_context_exposure` | Keep credentials out of model context |
| LLM09 | `llm09_vector_embedding_weaknesses` | Tenant and provenance filters before ranking |
| LLM10 | `llm10_improper_output_handling` | Context-specific output encoding |

## Tool-calling example

The prompt-injection package uses LangChain's `@tool` decorator to create schema-backed tool functions. LangGraph's `StateGraph` and `ToolNode` handle the model/tool loop. The offline demo uses deterministic fixtures so it is easy to step through in a debugger; `--live` sends the same scenario through the graph. The secure graph is read-only and never receives the email tool.

Tool calls from an LLM are proposals, not authorization. Retrieved articles and tool outputs remain untrusted input. Enforce access decisions and side-effect controls in application code, independent of prompt wording.

## Added OWASP resources

The demos incorporate guidance from these bundled PDFs:

- `OWASP-GenAI-LLM-Top-10-2026-v1.0.pdf`
- `Securing-Agentic-Applications-v2.pdf`
- `GenAi-Data-Securty-Best-Practices-Part-1.pdf`
- `LLM_Exploit_Generation_Guide_Phase2_10.21.26-1.pdf`

The exploit-generation study also informs an important limitation: these fixture-based examples demonstrate application controls, not a model's real-world offensive capability. The results of agentic evaluations depend on the harness, environment, human intervention, and evaluation design.

## Official references

- [OWASP GenAI LLM Top 10 2026 publication](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/)
- [OWASP canonical 2026 source list](https://github.com/GenAI-Security-Project/GenAI-LLM-Top10/blob/main/2026/README.md)
- [LangChain tool documentation](https://docs.langchain.com/oss/python/langchain/tools)
- [LangGraph ToolNode documentation](https://reference.langchain.com/python/langgraph/prebuilt/tool_node/ToolNode)
- [Python 3.15.2 release](https://www.python.org/downloads/release/python-3152/)
