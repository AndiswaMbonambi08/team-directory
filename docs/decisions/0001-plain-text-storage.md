## Title: Store team data as blank-line-separated plain text, not CSV/JSON

**Status:** Accepted

**Context:** team.txt needs to hold a small list of team member records for a CLI tool. Options considered: CSV (structured, one row per member), JSON (structured, nested fields), or plain text with a blank line between free-form entries.

**Decision:** Use plain text, entries separated by a blank line, parsed with content.strip().split("\n\n").

**Consequences:** Trivial to hand-edit in any text editor with no schema to maintain, which fits a small internal tool. Trade-off: no field structure, so search_by_name and filter_by_role can only do substring matching across an entire entry rather than targeting a specific field — if the tool grows to need precise field-based queries, this format will need to be replaced with something structured.
