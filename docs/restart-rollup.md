# Azurite Restart Rollup

## Purpose

This document preserves verified findings, Daniel's explicit corrections, and
open handoffs while Azurite is restarted from a clean implementation.

It is preparation evidence. It does not replace the authoritative product
vision, capability map, working agreement, or future technical architecture.
Those documents should change only after their owning product or engineering
conversation settles the relevant decisions.

## Restart Position

- The product remains **Azurite**. Only the GitHub repository is named
  `azurite2`.
- This is an implementation restart of the same product ambition.
- The former repository remains research evidence. Its current-state claims do
  not describe this repository.
- Azurite should pursue the knowledge capability associated with Obsidian and
  the interaction quality associated with Notion while developing its own
  product language, ontology, workflows, visual identity, and architecture.
- Obsidian's vault model is not automatically Azurite's model. The product term
  currently selected for a folder-backed knowledge container is `cluster`.

## Product Corrections Captured During Restart

### Markdown And Application State

Markdown files are the canonical, portable knowledge source. This principle
does not restrict Azurite to primitive runtime state.

Zustand, Dexie, TanStack Router, indexes, caches, event systems, and
observability may each own the live, durable, addressable, derived, or
diagnostic state required for a fluent and dependable PWA. Their exact
responsibilities remain an architecture decision for the restart.

### Cross-Device Experience

Azurite is the same PWA across desktop and mobile. The intended human
experience is that the product, account, knowledge, context, and work are simply
available across devices.

Do not frame this as a manual or product-visible data handoff between separate
applications. The future product and identity architecture must determine how
the seamless shared experience is delivered.

### Product Horizon

The inherited product vision captures only an early subset of Daniel's intended
product. The fuller vision includes, among other areas:

- file-native knowledge with hierarchy, links, backlinks, search, graphs,
  metadata, references, and knowledge services;
- a highly polished, performant, fluent, Notion-quality document and knowledge
  experience;
- one coherent desktop and mobile PWA experience;
- event-driven integration between Azurite, Codex, supported ChatGPT surfaces,
  API-key LLM providers, and future agent workflows; and
- private, local-first operation with Tailscale-oriented access and durable user
  ownership.

These are discovery inputs for the Visionary task, not a complete capability
map.

## Verified Former-Repository Baseline

Direct inspection of the former repository established that it implemented:

- filesystem cluster identity and Markdown discovery;
- note listing and reading;
- Milkdown and Crepe editing;
- manual save for existing notes with content-hash conflict protection;
- TanStack Router navigation;
- Zustand live state;
- Dexie draft recovery;
- React StrictMode across product and dedicated QA roots; and
- extensive routing, editor-lifecycle, persistence, and Sentry machinery.

It did not implement complete note CRUD, file rename or move, trash or restore,
search, backlinks, graph behavior, file watching, or a derived knowledge index.

`docs/technical-architecture.md` is therefore a historical snapshot mixed with
deferred decisions. It must not be treated as the current architecture of this
empty implementation.

## Verified Technical Findings

### Markdown Title Parsing

The former `packages/core/src/title-extraction.ts` used `unified`,
`remark-parse`, and `mdast-util-to-string` to select the first level-one heading
as a note title and fall back to the filename without `.md`.

This code was used by note listing and reading. It correctly handled formatted
heading text and avoided a fragile heading regular expression, so it was not
dead code.

The original Slice 1 also justified the parser as the future AST foundation for
links, headings, tags, and indexing. That future index was not implemented.
Filesystem discovery instead read and parsed every Markdown file to produce
list metadata. Later documentation measured a direct scan of 555 copied files
at roughly 2.8 to 3.2 seconds.

Restart disposition:

- Do not inherit this parser pipeline automatically.
- Decide whether Azurite titles come from filenames, headings, frontmatter, or
  another rule as part of product and indexing design.
- If heading-derived titles are required, prefer one derived parsing and
  indexing pipeline that serves titles, links, headings, tags, search, and graph
  consumers instead of reparsing every file for each list scan.

### Markdown Dialect

The former frontend depended directly on Milkdown Crepe and Kit. Crepe loaded
Milkdown's CommonMark and GFM presets internally. The former core package used
`remark-parse` for heading-title extraction and did not directly install
`remark-gfm`.

The inherited statement `CommonMark plus GitHub Flavored Markdown` therefore
overstates a single explicit Azurite-owned dialect contract. The exact Markdown
dialect, extensions, parsing ownership, and round-trip guarantees remain restart
decisions.

### ESLint Baseline

The former effective web configuration contained 172 error-level ESLint rules,
including 70 error-level TypeScript ESLint rules.

The phrase `all no-unsafe-* rules` is only an informal summary. The effective
configuration enabled nine TypeScript `no-unsafe-*` rules as errors plus core
unsafe-control-flow rules. `no-unsafe-negation` was disabled.

Restart disposition:

- Treat the executable ESLint configuration as the precise inherited baseline.
- Use prose to explain its intent without claiming a wildcard rule that ESLint
  does not provide.
- Reassess a rule only through an explicit engineering decision supported by
  concrete code evidence.

## Delivery-System Finding

The former delivery process repeatedly subjected implementation plans to
adversarial review. Review findings expanded plans, introduced additional
contracts and proof machinery, and triggered further review. This created a
feedback loop in which specification and defensive architecture could advance
faster than primary product capability.

Daniel still wants ambitious scope, excellent architecture, strict engineering
quality, and serious verification. The restart must discover a delivery model
that builds substantial product capability at high speed without repeating
specification and adversarial-review spirals. Product programs with coherent
vertical delivery slices are a leading candidate, but the working agreement has
not yet been revised.

## Leadership Handoffs

### Visionary

A dedicated long-running Codex task should explore the full product destination
with Daniel. It owns discovery and eventual proposals for the concise product
vision and expansive capability map. Its conversation should be imaginative and
freeflowing inside a clear outcome boundary. It should not prematurely reduce
vision to the former implementation, current documentation, or engineering
feasibility.

### COO

The COO task preserves decisions, maintains program coherence, coordinates role
handoffs, and later sequences delivery toward the accepted vision. It should not
author the product destination in place of the Visionary and Daniel.

### CTO

A future long-running CTO task should translate accepted product horizons into
durable, understandable architecture. Its mandate must explicitly combine speed,
quality, performance, and simplicity without recreating review-driven scope
inflation.

Researchers, implementers, and reviewers should normally be bounded tasks with
clear outputs rather than additional permanent leadership centers.

## Current Sequence

1. Conduct the first Visionary discovery session.
2. Let the Visionary and Daniel propose the product vision and capability map.
3. Reconcile and commit those documents after Daniel accepts them.
4. Revise the working agreement around the accepted ambition and delivery model.
5. Re-baseline technical architecture and state ownership for the empty
   implementation.
6. Scaffold and deliver the first approved product program and vertical slice.
