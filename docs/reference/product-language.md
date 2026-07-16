# Azurite Product Language

## Purpose

This page is the authoritative home for Azurite's stable product vocabulary.
Product documentation, UI copy, architecture decisions, and implementation
names should use these terms consistently without recreating their full
definitions elsewhere.

## Brand World

Azurite's core metaphor is geological and mining-based. New product language
should belong naturally to that world and should preserve the meanings defined
on this page.

Celestial language is outside the brand metaphor. The possible astronomical
reading of "cluster" does not make constellations, stars, or other celestial
terms part of Azurite's vocabulary.

## Compact Language

> Files form clusters. Veins connect knowledge. Connected clusters form lodes.

## Cluster

Cluster is established mineral language, including for azurite crystal
groupings. An **Azurite Cluster** is one coherent, portable knowledge domain.
Markdown files remain its canonical, portable knowledge source. Azurite may
maintain rich application state and rebuildable derived state around those
files without compromising their independent use.

A cluster can be a dedicated notes collection, a project Git repository,
LLMWiki, or another knowledge collection. It remains usable through ordinary
filesystem tools and through its own native workflows when Azurite is absent.

Obsidian's vault is a capability benchmark for knowledge management. Azurite
uses its own cluster model, formats, ontology, and brand language while pursuing
that level of capability. Product language calls these domains clusters, never
vaults.

## Vein

A **vein** is Azurite's product-level umbrella term for a relationship between
knowledge artifacts. A vein can connect files within one cluster or cross a
cluster boundary.

The precise relationship type remains visible. Examples include:

- authored links and their backlinks;
- references and embeds;
- shared metadata or tags;
- agent-session relationships;
- inferred semantic relationships.

Relationship origin and certainty remain part of the product truth:

- **Authored** relationships express deliberate human or agent intent.
- **Observed** relationships report a factual connection found in source or
  system activity.
- **Inferred** relationships express a derived semantic judgment and remain
  distinguishable and explainable.

Azurite must preserve these distinctions instead of presenting every vein with
identical certainty.

## Lode

A **lode** is a connected group of at least two clusters. A cross-cluster vein
connecting two clusters is enough for those clusters to form a lode. The term
extends transitively across a connected group as further clusters join through
cross-cluster veins.

Lode describes a product relationship between independently usable clusters.
It does not prescribe storage, indexing, synchronization, graph, or deployment
architecture, and it does not merge the participating clusters into one
knowledge domain.

## Access And Authorization

A vein or membership in a lode never grants access by itself. Human and agent
authorization remains deliberate across every cluster boundary, especially for
personal, coaching, therapy-support, project, and code clusters.

Relationship visibility and content access are separate product decisions.
Implementations must preserve that distinction when they make cross-cluster
knowledge discoverable or actionable.

## Reserved And Rejected Terms

- **Modules** remains the user-facing term for installable Azurite extensions.
- **Vault** belongs to Obsidian and may appear only when describing an external
  capability benchmark or interoperability context.
- **Constellation** was considered for connected clusters and rejected because
  it breaks the geological brand world.
- **Matrix** was researched for connected clusters and superseded by **lode**.

## Geological Grounding

This vocabulary is product language inspired by real geological usage rather
than a literal scientific data model.

- The Utah Geological Survey describes collectible azurite crystal clusters in
  its account of the Lisbon Valley copper project: [Azurite and Malachite from
  the Blue Crystal Mine](https://geology.utah.gov/map-pub/survey-notes/lisbon-valley-copper-project/).
- Geology.com documents an azurite specimen as a cluster of blade-shaped
  crystals: [Azurite: The blue gem material, ore of copper, and
  pigment](https://geology.com/minerals/azurite.shtml).
- USGS mining terminology describes a lode as an assemblage of veins, veinlets,
  or stringers treated as one ore body: [The Lodes of the South Tintic Mining
  District, Utah](https://pubs.usgs.gov/unnumbered/70047750/report.pdf).
- A USGS mineral-deposit manual describes stockwork as mineralized veins that
  traverse rock and form a network through mutual intersection: [MAS Deposit
  Information Manual](https://pubs.usgs.gov/of/1998/0512/pdf/masnpdictionary.pdf).
