# Azurite Product Vision

## Purpose

This document is Azurite's concise product destination. Every contributor should
be able to internalize it quickly. The broader capability universe lives in the
[product capability map](product-capability-map.md), and stable geological
vocabulary lives in the
[product-language reference](reference/product-language.md).

## North Star

**Azurite is the file-sovereign context fabric for a person's life and work.**

It keeps user-owned knowledge, original source material, relationships,
conversations, automations, and agent activity continuously organized as living
context. Wherever a person chooses to think or act, Azurite lets authorized
humans and agents arrive prepared, carry work forward, and return durable
outcomes to the clusters the person owns.

The defining product test is:

> A person can begin meaningful work in any authorized surface with the right
> context already available, and trust that valuable outcomes will return to
> the right place with their provenance intact.

## The Transformation

Knowledge currently fractures across files, repositories, notes, chat histories,
automations, devices, and model providers. People repeatedly search, copy,
explain, reconcile, and file the same context.

Azurite replaces that clerical burden with continuity:

- files and original artifacts remain independently usable material the user
  owns;
- clusters organize coherent knowledge domains, and veins connect knowledge
  within and across them;
- connected clusters form lodes that make authorized context useful across
  projects and areas of life;
- the direct Azurite experience remains exceptional even when a person's most
  frequent interaction happens through Codex, Claude Code, ChatGPT, OpenCode,
  Pi, Hermes, OpenClaw, or another agent surface;
- agents and automations can receive relevant context, perform authorized work,
  and return results without manual copy-and-paste rituals; and
- every valuable interaction can improve the durable context available to the
  next one.

## Product Promises

### File Sovereignty

Users retain meaningful ownership of their knowledge and source material.
Markdown, code, PDFs, images, audio, datasets, and other native files remain
ordinary local files on the user's devices and continue to work without
Azurite. A synchronized cluster can have a local copy on several authorized
devices. Rich application state may deepen the experience, but it must not
imprison the user's knowledge in a hidden proprietary store.

### Obsidian-Level Knowledge Power

Obsidian establishes the functional floor for knowledge management. Azurite
targets complete practical parity across hierarchy, navigation, links,
backlinks, metadata, frontmatter, tags, search, graphs, references, embeds,
automation, programmability, and knowledge services.

Functional parity describes user capability. Azurite develops its own cluster
model, formats, ontology, interface, workflows, visual identity, and Modules.
Obsidian vault compatibility is not a product requirement.

### Notion-Level Human Fluency

Notion establishes the quality bar for calm, approachable, responsive
interaction. Azurite applies that fluency to a genuinely file-backed knowledge
experience. Markdown syntax and filesystem mechanics should never become an
excuse for editor friction, visual austerity, or weak mobile interaction.

### Continuous Context

The right context follows authorized work across files, clusters, lodes,
devices, conversations, automations, agents, and time. Azurite keeps that
context current, traceable, searchable, and ready for use while preserving the
origin and certainty of what it knows.

### Agency With Human Control

Agents and automations may notice, interpret, propose, initiate, and update work
through Azurite. Their authority is explicit and scoped. People can understand
what acted, why it acted, what sources it used, and what it changed.

### One Frontend Everywhere

Azurite presents one coherent PWA frontend across desktop, phone, tablet, and
future PWA-capable surfaces. Synchronized local clusters and their connected
context remain current across authorized devices without a visible handoff
ritual. Each device may offer interaction depth appropriate to its form.

### Modular Extensibility

Azurite Modules add focused product worlds without turning the core into an
undifferentiated cockpit. Project management, embedded agents, coaching,
codebase intelligence, document ingestion, and future specialist experiences
can each become Modules while respecting the same file, provenance, and access
promises.

## Product Shape

The Azurite PWA is exclusively the frontend. It presents interaction and
visualizes product state. The product definition assigns no cluster storage,
lode storage, knowledge-service runtime, or agent-runtime ownership to the PWA.
Self-hosted and Azurite-hosted delivery provide the same frontend experience.

Clusters live as ordinary local filesystem material on the user's devices.
Their Markdown knowledge and original source artifacts remain locally usable
without Azurite. Lodes connect independently usable clusters; they are not
cloud-hosted containers that replace the participating local clusters.

Azurite may provide an optional hosted synchronization service whose product
role follows the Obsidian Sync benchmark. It synchronizes cluster files and
their changes among authorized devices so that each local copy converges. When
a synchronized change affects knowledge relationships or discoverability,
Azurite automatically brings the corresponding links, backlinks, references,
tags, metadata, search results, graphs, veins, lodes, and assembled context
current on every authorized device where the relevant clusters are available.

Hosting the PWA frontend and providing cluster synchronization are distinct
product capabilities. Technical architecture determines how the hosted
frontend reaches local cluster capabilities, where indexing and knowledge
services execute, and whether relational convergence uses synchronized state,
events, local reconstruction, or another dependable mechanism.

## The Mature Experience

A code repository can also be an Azurite Cluster. LLMWiki can be another. Their
authorized veins let an external coding agent draw on accumulated methods,
research, decisions, and prior sessions. The agent's conclusions, blockers, and
work history return to the relevant files and project surfaces.

An invoice can enter as its original PDF or image. Extraction, metadata,
synthesis, and relationships become durable knowledge while the original
remains intact and traceable. A budget workflow receives the updated context. A
coaching agent can use relevant long-term context when the user has granted
that access. Unrelated private or project knowledge remains outside its reach.

The person may speak into the same PWA from a phone and receive a durable
transcript through a locally hosted speech model. An Azurite agent may answer in
text and, when requested, provide generated speech for listening. Voice becomes
a natural input and output mode across devices rather than a separate product.

When the person opens Azurite directly, the interface reveals a coherent current
world instead of accumulated chat debris. Sources remain traceable. Authored,
observed, and inferred relationships remain distinguishable. External agents,
Azurite Modules, and the human have contributed to one continuous body of owned
context.

## Canonical Product Truth

Azurite protects several kinds of truth without forcing them into one storage
shape:

- **Authored knowledge:** Markdown is the canonical, portable representation for
  notes, decisions, documentation, syntheses, metadata, and naturally
  Markdown-backed work artifacts.
- **Original source artifacts:** PDFs, images, recordings, code, datasets, and
  other native files remain canonical originals for their own content.
- **Durable product state:** Accounts, permissions, agent-session associations,
  collaboration, personalization, and other meaningful product truths may use
  serious application state. State whose loss would destroy user value must be
  understandable, governable, and portable where appropriate.
- **Derived intelligence:** Indexes, previews, caches, embeddings, extracted
  text, summaries, and inferred relationships remain attributable and
  rebuildable or reproducible wherever possible.

Generated extraction, summary, or inference remains derived until a human or
authorized workflow deliberately materializes it as durable knowledge. Its
materialized file then becomes canonical while retaining its generation
provenance.

External tools and synchronized devices may change cluster files. Azurite must
recognize those changes and automatically reconcile affected knowledge and
relationships without becoming a second competing source of truth.

## Context Fabric And Agents

Azurite continuously discovers, indexes, relates, refreshes, and routes
authorized context. It provides the fabric through which work can happen.
Agents and automations perform observation, inference, decision, and action.

The core product remains addressable by external agents. A visible agent inside
Azurite can be delivered as an installable Module, with provider choice that may
include supported subscription-backed services, user-supplied API providers,
local models, and future agent systems.

Agent sessions can become knowledge artifacts in their own right. They may be
linked to files, decisions, cards, questions, and projects. Changes in Azurite
can reach the relevant ongoing session, and useful outcomes from that session
can return to Azurite with their actor, source, and history intact.

## Ownership And Distribution

Azurite should offer a polished open-source self-hosted product environment
using the same PWA frontend, plus an Azurite-hosted production PWA frontend. An
optional hosted synchronization service can provide account-based, Obsidian
Sync-style continuity for effectively unlimited clusters, bounded by chosen
storage and service realities rather than artificial organization limits.
Daniel's daily use should run through the real production product so dogfooding
continuously tests the promise made to future users.

Self-hosted, locally hosted, Tailscale-accessible, and Azurite-hosted frontend
delivery must preserve the same local-file sovereignty and portability
promises. Subscription or synchronization never changes the canonical role of
local cluster files. Private operation is the default posture. Sharing and
collaboration are deliberate capabilities.

## Independent Product Identity

Azurite's destination can be summarized through three benchmarks:

- Obsidian-level knowledge capability;
- Notion-level interaction quality; and
- Azurite-native context continuity across clusters, lodes, agents,
  automations, devices, and time.

The first two establish the floor. The third is Azurite's own territory.

## Product Boundaries

- A relationship never grants access by itself.
- Candidate or inferred relationships do not silently become authored fact or
  materialized cross-cluster topology.
- Ingestion and conversion never silently replace or destroy an original
  source artifact. Retention and deliberate discard remain user-controlled.
- Agent and automation activity remains attributable, inspectable, and
  governable.
- The context fabric has no mandatory assistant personality.
- The PWA's product role is exclusively frontend presentation and interaction.
- Hosted frontend delivery and hosted cluster synchronization remain distinct
  capabilities.
- A synchronized file change automatically converges the affected knowledge and
  relationships across authorized devices where the relevant clusters are
  available.
- Rich experiences and Modules may use serious application state while keeping
  canonical knowledge and source material independently usable.
- Product decisions define user outcomes. Technical architecture owns the
  mechanisms that deliver them.

## Open Product Frontiers

- The researched boundary of complete Obsidian capability parity across core,
  first-party extensions, community workflows, and user scripting.
- The exact boundary between universal Azurite capabilities and installable
  Modules.
- The relationship between derived lode topology and named or intentionally
  scoped lode experiences.
- Human-configurable autonomy levels for agent initiation, canonical writeback,
  and cross-system work.
- The exact synchronized product state, if any, required beyond cluster files
  for dependable cross-device continuity.
- The subscription model, collaboration model, and movement between self-hosted
  and Azurite-hosted frontend and synchronization services.
- The product boundary and promises for coaching and therapy-support Modules.
