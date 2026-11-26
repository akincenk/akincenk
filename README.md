<div align="center">

# Cenk Akın

**Python &amp; AI developer · FastAPI · data pipelines · automation that runs itself**

Vancouver, BC

<a href="https://www.linkedin.com/in/akincenk/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a> <a href="mailto:akincenk@gmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a> <a href="https://akincenk.github.io"><img src="https://img.shields.io/badge/Portfolio-24292F?style=for-the-badge&logo=githubpages&logoColor=white" alt="Portfolio" /></a>

</div>

---

I build backend services, data pipelines and AI agents in Python. My focus is software that solves operational problems: inventory, forecasting, staffing, document processing and monitoring that runs around the clock without anyone watching it.

Before I wrote code, I ran the operations this software is for. I spent eight years leading customer-operations teams of up to 150 people at **Turkcell Global Bilgi** and **KKTCELL**. At KKTCELL, I built a national operator's customer-service and CRM operation from scratch: call centre, back office, IVR and the full KPI framework. That background shapes how I engineer:

- **I start from the workflow.** I model how a warehouse, store or service centre really runs before I design a single table.
- **I build it to last.** Database migrations, Docker containers, retries and alerting are part of the design, not an afterthought.
- **I automate the boring parts.** Scheduled services pull data, apply business rules and escalate only what needs a human decision.
- **I measure before I claim.** Every AI project here ships with its own evaluation, and the README reports the weak results too.

## Featured: Heresin, a local-first personal AI system

A personal AI assistant I run 24/7 on my own Mac Studio (Apple M5 Max, 36 GB). It learns continuously from my notes and work sessions, answers from source-linked memory, uses sandboxed tools, and is measured every day. I set its goals, safety rules and acceptance tests; I build it with Claude Code as my AI pair programmer. Code is private; I am happy to walk through it.

**Why "Heresin"?** Until I was seven or eight, Heresin was my imaginary friend. As far as I know the word means nothing in any language: a child made it up, and the people closest to me still know the name. Decades later, giving it to the assistant I am building felt exactly right. The friend who was always there now remembers what matters, answers my questions and helps me get work done.

| Skill | How Heresin does it | Measured |
| --- | --- | --- |
| **RAG** | Hybrid retrieval: full-text keywords + embeddings (int8 vector index) + a local cross-encoder reranker, over memories and the source notes themselves | Recall test sets: <!--v:r1hit-->97%<!--/v--> and <!--v:r2hit-->100%<!--/v--> found, MRR <!--v:r1mrr-->0.93<!--/v--> and <!--v:r2mrr-->0.92<!--/v--> (keyword-only: MRR <!--v:kwmrr-->0.71<!--/v-->) |
| **Agents + MCP** | Agent loop that can run shell commands inside a macOS Seatbelt sandbox (no network, no home folder, no secrets); permission gate, budget reservation, kill switch; MCP client | Every command logged; 3 failures warn, 6 stop |
| **Context engineering** | Code, not the model, decides what each model sees: personal data stays on the local model, cloud tiers never receive it; tool output and documents are labelled as untrusted data | Routing local → free cloud → paid, with daily spending caps |
| **LLM evaluation** | Daily personal exam through the real chat path, cross-lingual (Turkish ↔ English) retrieval check, recall suites; models are switched only on benchmark results | Daily exam <!--v:examrange-->50<!--/v--> of <!--v:examtotal-->50<!--/v-->; cross-lingual <!--v:xl-->60/60<!--/v-->; local chat model picked by exam (Qwen 3.8 27B, 17/20 vs 15/20 for the previous model) |
| **Harness engineering** | Test gate before every install, self-check, agent-safety evals, append-only audit log, encrypted storage (SQLCipher); a release that lowers any score never ships | <!--v:tests-->832<!--/v--> automated tests, all passing |

<sub>Python (standard library first) · SQLCipher · Ollama + llama.cpp (Qwen 3.8 27B, Qwen3-Coder 30B, EmbeddingGemma 2, BGE reranker v2 m3) · macOS sandbox-exec · launchd · 232,000+ memories · v0.21.47</sub>

## Open-source AI engineering

Three public projects, each measured with its own evaluation and every result reported, including the weak ones. All evaluated on local models.

<table>
  <tr>
    <td width="33%" valign="top">
      <a href="https://github.com/akincenk/agent-harness"><img src="assets/agent-harness.svg" alt="agent-harness" width="100%" /></a>
      <h3><a href="https://github.com/akincenk/agent-harness">agent-harness</a></h3>
      <p>A tested harness for long-running LLM agents: the model proposes tool calls, plain code decides. Budgets, failure limits, loop detection, a kill switch, prompt-injection guardrails, sandboxed tools, parallel sub-agents and traces.<br><b>8 / 8</b> tasks done and <b>6 / 6</b> attacks harmless with a local 27B model; 26 tests make each guardrail hold even when the model obeys the attacker.</p>
      <p><sub>Python stdlib · OpenAI-compatible API · macOS sandbox</sub></p>
    </td>
    <td width="33%" valign="top">
      <a href="https://github.com/akincenk/insightai"><img src="assets/insightai.svg" alt="InsightAI" width="100%" /></a>
      <h3><a href="https://github.com/akincenk/insightai">InsightAI</a></h3>
      <p>Question answering over PDFs with page citations: vector, BM25 keyword and hybrid retrieval, with the default chosen by measurement.<br>Vector search ranked the right page best (MRR <b>0.94</b> on 30 questions, against 0.78 for keywords and 0.90 for hybrid) and had it in the top 3 every time.</p>
      <p><sub>FastAPI · PyMuPDF · embeddings · recall@k / MRR</sub></p>
    </td>
    <td width="33%" valign="top">
      <a href="https://github.com/akincenk/llm-router"><img src="assets/llm-router-card.svg" alt="llm-router" width="100%" /></a>
      <h3><a href="https://github.com/akincenk/llm-router">llm-router</a></h3>
      <p>Sends each question to the cheapest model that can answer it and skips the model when the same question was already answered: explainable rules, a cascade with escalation, a semantic cache that never mixes up numbers.<br>Same <b>100%</b> accuracy as always using the large model at <b>58% lower cost</b>; the cache answered 14 / 15 reworded questions and was fooled by <b>0 / 5</b> number traps.</p>
      <p><sub>Python stdlib · semantic cache · cost and accuracy evaluation</sub></p>
    </td>
  </tr>
</table>

## Selected work

<table>
  <tr>
    <td width="33%" valign="top">
      <a href="https://github.com/akincenk/Retail-Demand-Staffing-Optimizer"><img src="assets/staffing-optimizer.svg" alt="Demand &amp; Staffing Optimizer" width="100%" /></a>
      <h3><a href="https://github.com/akincenk/Retail-Demand-Staffing-Optimizer">Demand &amp; Staffing Optimizer</a></h3>
      <p>Forecasts demand for every store and product, then turns it into a staffing plan that meets service-level targets.</p>
      <p><sub>FastAPI · PostgreSQL · forecasting · Docker</sub></p>
    </td>
    <td width="33%" valign="top">
      <a href="https://github.com/akincenk/Warehouse-inventory-api"><img src="assets/warehouse-inventory-api.svg" alt="Warehouse Inventory API" width="100%" /></a>
      <h3><a href="https://github.com/akincenk/Warehouse-inventory-api">Warehouse Inventory API</a></h3>
      <p>Tracks SKUs, suppliers, stock and purchase orders, and flags low inventory before it becomes a stockout.</p>
      <p><sub>FastAPI · PostgreSQL · SQLAlchemy · Alembic · Docker</sub></p>
    </td>
    <td width="33%" valign="top">
      <a href="https://github.com/akincenk/ics-tidy"><img src="assets/ics-tidy-card.svg" alt="ics-tidy" width="100%" /></a>
      <h3><a href="https://github.com/akincenk/ics-tidy">ics-tidy</a></h3>
      <p>Merges calendar files, removes duplicate events and expands recurring events into an agenda or CSV.</p>
      <p><sub>Rust CLI and library</sub></p>
    </td>
  </tr>
  <tr>
    <td width="33%" valign="top">
      <a href="https://github.com/akincenk/cron-explain"><img src="assets/cron-explain-card.svg" alt="cron-explain" width="100%" /></a>
      <h3><a href="https://github.com/akincenk/cron-explain">cron-explain</a></h3>
      <p>Explains cron schedules in plain English, lists the next runs in any time zone with daylight-saving details, and warns about common mistakes.</p>
      <p><sub>Go library and CLI</sub></p>
    </td>
    <td width="33%" valign="top">
      <a href="https://github.com/akincenk/gs1-parse"><img src="assets/gs1-parse-card.svg" alt="gs1-parse" width="100%" /></a>
      <h3><a href="https://github.com/akincenk/gs1-parse">gs1-parse</a></h3>
      <p>Parses GS1-128, GS1 DataMatrix and GS1 QR barcode scans into checked, typed values.</p>
      <p><sub>Kotlin library and CLI</sub></p>
    </td>
    <td width="33%" valign="top">
      <a href="https://github.com/akincenk/warehouse-management-system"><img src="assets/wms.svg" alt="Warehouse Management System" width="100%" /></a>
      <h3><a href="https://github.com/akincenk/warehouse-management-system">Warehouse Management System</a></h3>
      <p>Inventory and order API with role-based permissions and JWT authentication.</p>
      <p><sub>FastAPI · SQLAlchemy · JWT · RBAC</sub></p>
    </td>
  </tr>
</table>

**Private builds** · code not public, happy to walk through them

- **Personal AI assistant.** Local-first, runs 24/7 on my own hardware, with source-linked memory, one-command agents, encrypted storage and strict spending limits.
- **Multi-model AI council.** Several language models debate a question and return one reviewed answer.
- **Unattended monitoring pipelines.** A family of GitHub Actions services that watch public data sources on a schedule, filter by business rules and alert by email, Telegram or voice, with retry and outage handling built in.

## Background

| Years | Role |
|---|---|
| 2023 – present | Software Developer, freelance: Python automation, data pipelines, LLM tooling |
| 2020 – 2023 | Founder, UDM Marketing (US): design and marketing agency, e-commerce, in-house web and software development |
| 2012 – 2020 | Independent software developer, remote contracts |
| 2011 – 2012 | Line Manager, Turkcell Global Bilgi: Turkcell Platinum operation |
| 2010 – 2011 | Line Manager, KKTCELL: built the customer-service and CRM operation from zero |
| 2004 – 2010 | Operations Manager, Turkcell Global Bilgi: Black and Platinum operations, teams of up to 150 |

## Toolbox

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=flat-square&logo=sqlalchemy&logoColor=white" alt="SQLAlchemy" />
  <img src="https://img.shields.io/badge/Pydantic-E92063?style=flat-square&logo=pydantic&logoColor=white" alt="Pydantic" />
</p>
<p>
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white" alt="scikit-learn" />
  <img src="https://img.shields.io/badge/OpenAI_API-412991?style=flat-square" alt="OpenAI API" />
</p>
<p>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" alt="GitHub Actions" />
  <img src="https://img.shields.io/badge/Pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white" alt="Pytest" />
  <img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=white" alt="Linux" />
  <img src="https://img.shields.io/badge/WebSockets-010101?style=flat-square&logo=socketdotio&logoColor=white" alt="WebSockets" />
</p>

## GitHub activity

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/top-langs-dark.svg" />
    <img src="assets/top-langs.svg" alt="Top languages" height="165" />
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/streak-dark.svg" />
    <img src="assets/streak.svg" alt="Contribution streak" height="165" />
  </picture>
</p>

---

<div align="center">

*Good software is readable. Complexity is not a skill, it's a mistake.*

</div>
