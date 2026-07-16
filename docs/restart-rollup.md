# Azurite Restart Rollup

## Purpose

This document preserves verified findings, Daniel's explicit corrections, and
open handoffs while Azurite is restarted from a clean implementation.

It is preparation evidence. It does not replace the authoritative product
vision, capability map, working agreement, or future technical architecture.
Those documents should change only after their owning product or engineering
conversation settles the relevant decisions.

Verified low-level inheritance evidence for the future CTO lives separately in
`docs/restart/legacy-technical-findings.md`.

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

The PWA's product role is exclusively frontend presentation and interaction.
References to application state or browser technology do not assign cluster
storage, lode storage, knowledge-service runtime, or agent-runtime ownership to
the PWA.

### Cross-Device Experience

Azurite presents the same PWA frontend across desktop and mobile. Clusters live
as ordinary local filesystem material on the user's devices. The hosted
frontend and the optional hosted synchronization service are distinct product
capabilities.

The synchronization service follows the product role established by Obsidian
Sync: it keeps authorized local cluster copies current across devices. An edit
inside a cluster on one device propagates to its synchronized local copies on
the other authorized devices. Azurite then converges every affected link,
backlink, reference, tag, metadata view, search result, graph, vein, lode, and
piece of assembled context wherever the relevant clusters are authorized and
available.

The experience has no manual or product-visible handoff ritual. Technical
architecture must determine how the hosted frontend reaches device-local
cluster capabilities and how file, index, relationship, and context convergence
is delivered dependably.

### Product Horizon

The inherited product vision captures only an early subset of Daniel's intended
product. The fuller vision includes, among other areas:

- file-native knowledge with hierarchy, links, backlinks, search, graphs,
  metadata, references, and knowledge services;
- a highly polished, performant, fluent, Notion-quality document and knowledge
  experience;
- one coherent desktop and mobile PWA frontend experience over local cluster
  material;
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

The next CTO must preserve the settled product boundary that the PWA is
exclusively the frontend and clusters remain local filesystem material on user
devices. The architecture must determine how self-hosted and Azurite-hosted
frontends reach local cluster capabilities, where knowledge services and agent
participation execute, and how the optional Obsidian Sync-style service produces
both file convergence and automatic relational convergence across authorized
devices. The product decision does not prescribe whether that convergence uses
synchronized state, events, local reconstruction, or another mechanism.

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
