# Implementation sequence

1. Agree on typed inventory, occurrence, reference, capability, plan and validation contracts. Demonstrate synthetic end-to-end flow.
2. Inventory the corpus and representative samples; investigate native CAD API availability immediately.
3. Add SQLite job state, atomic writes and resumability keyed by input hash, handler version, plan version and relevant path context.
4. Add a private identity registry with provenance and explicit alias merges. Freeze centrally allocated pseudonyms before processing.
5. Plan collision-free path changes and reference updates together. Block unsafe renames.
6. Implement format-aware handlers incrementally. Report metadata, visible text, attachments, previews and reference capabilities separately.
7. Recursively discover and transform archives with traversal protection and resource limits. Validate repacked members.
8. Validate file usability, engineering preservation, reference resolution and residual identifiers independently.
9. Package full corpus, code and neutral README. Check object limits, files over 2 GB and excluded private artifacts.
10. Freeze versioned attempts, submit only when authorized and use score categories to prioritize changes.

## First coding-agent task

Read AGENTS.md. Define typed contracts for inventory records, identity occurrences with location/context, references, handler capabilities, replacement plans, transformation results and validation results. A handler exposes discovery, transformation and validation. Transformations consume a shared immutable plan and write separately from input. Validation distinguishes passed, failed, unsupported and not checked. Build a synthetic demonstration before implementing real handlers. Coordinate contracts with the other developer.

## Review checklist

- Source defects distinguished from introduced failures
- Every source file and archive member accounted for
- Identities consistent, distinct entities separate
- No stale resume outputs or unsafe duplicate reuse
- References updated whenever paths change
- Native usability checked with actual tools where available
- Unsupported checks reported honestly
- No private data in commits or submission code
