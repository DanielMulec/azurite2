# Legacy Technical Findings

## Purpose

This ledger preserves verified implementation evidence from the former Azurite
repository that may materially inform the restart's future CTO and architecture
work.

These findings are neither current Azurite2 architecture nor accepted restart
decisions. Re-evaluate each finding against the accepted product vision and the
implementation that exists when a relevant technical decision is made.

## Markdown Title Parsing

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

Restart consideration:

- Do not inherit this parser pipeline automatically.
- Decide whether Azurite titles come from filenames, headings, frontmatter, or
  another rule as part of product and indexing design.
- If heading-derived titles are required, evaluate one derived parsing and
  indexing pipeline that can serve titles, links, headings, tags, search, and
  graph consumers instead of reparsing every file for each list scan.

## Markdown Dialect

The former frontend depended directly on Milkdown Crepe and Kit. Crepe loaded
Milkdown's CommonMark and GFM presets internally. The former core package used
`remark-parse` for heading-title extraction and did not directly install
`remark-gfm`.

The inherited statement `CommonMark plus GitHub Flavored Markdown` therefore
overstates a single explicit Azurite-owned dialect contract. The exact Markdown
dialect, extensions, parsing ownership, and round-trip guarantees remain restart
decisions.

## ESLint Baseline

The former effective web configuration contained 172 error-level ESLint rules,
including 70 error-level TypeScript ESLint rules.

The phrase `all no-unsafe-* rules` is only an informal summary. The effective
configuration enabled nine TypeScript `no-unsafe-*` rules as errors plus core
unsafe-control-flow rules. `no-unsafe-negation` was disabled.

Restart consideration:

- Treat the executable ESLint configuration as the precise inherited baseline.
- Use prose to explain its intent without claiming a wildcard rule that ESLint
  does not provide.
- Reassess a rule only through an explicit engineering decision supported by
  concrete code evidence.
