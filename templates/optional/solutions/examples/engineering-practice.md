---
title: "Protect every path that can modify a user-owned resource"
type: "engineering-practice"
status: "illustrative"
date: "2026-11-01"
applies_to:
  - "A tool or service has multiple code paths that can replace, move or delete the same resource"
tags:
  - "data-integrity"
  - "filesystem"
  - "destructive-operations"
related_work: "docs/work/<objective>/"
---

# Protect every path that can modify a user-owned resource

> Illustrative example. Validate the exact paths and behavior in the project before adopting this guidance.

## Context and problem

A file-management feature must preserve user-managed files when refreshing generated content. A guard was added to the main update path, but a cleanup path could still move or delete the same file.

## Evidence and finding

The primary update test passed, but a separate test that exercised the cleanup path showed that the user-managed file was still modified.

The protection rule covered one operation, not every operation capable of changing the protected resource.

## What did not work

Adding another check only to the currently failing call site would leave the same omission possible in sibling paths.

## Solution or guidance

Enumerate every operation that can overwrite, remove, rename or move the protected resource. Prefer placing the preservation check at a shared, well-defined boundary through which those operations pass. Test the original reproduction through each relevant path.

## Why it works

The invariant is enforced at the point where the resource is actually modified, rather than relying on every caller to remember a separate check.

## When to apply

Use this approach when multiple functions or workflows can mutate the same user-owned resource.

## Limits and revisit conditions

A shared boundary is useful only if all relevant operations really pass through it. If a path bypasses that boundary, either route it through the boundary or protect and test it explicitly.

## Verification and references

- Related Spec / work item: docs/work/<objective>/spec.md
- Tests: exercise the main update path and each cleanup / migration path.
- Commit / PR / source: To add after implementation.
- Last verified: To add after project verification.
