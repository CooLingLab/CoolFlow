---
title: "Make retried create requests safe against duplicate submissions"
type: "bug-fix"
status: "verified"
date: "2026-11-01"
applies_to:
  - "Client retries a create operation after a timeout"
tags:
  - "http"
  - "retries"
  - "idempotency"
related_work: "docs/work/<objective>/"
---

# Make retried create requests safe against duplicate submissions

> Illustrative example. Replace the scenario and evidence with findings verified in the actual project.

## Context and problem

A mobile client sends a request to create a resource. The server completes the operation, but the response is lost before the client receives it. The client retries and the server creates a second resource.

## Evidence and finding

A test simulating a successful server-side create followed by a dropped response reproduces two resources after the client retry.

The issue is not simply that the client retries. The server cannot distinguish a retry of the same logical operation from a new create request.

## What did not work

- Disabling retries avoids duplicates but leaves users exposed to transient network failures.
- Checking for a matching resource by a non-unique display field can incorrectly treat two legitimate creates as the same operation.

## Solution or guidance

Give each logical create operation a stable idempotency key. Reuse that key for retries of the same operation. The server stores the result associated with the key and returns the original result when it receives the same key again.

## Why it works

The server can identify repeated delivery of one logical operation and avoid applying the side effect twice.

## When to apply

Use this pattern when a request may be retried after an uncertain outcome and duplicate side effects would be harmful.

## Limits and revisit conditions

The server must persist idempotency results for an appropriate period and scope keys to the correct user or resource. The client must not reuse a key for a genuinely new operation.

## Verification and references

- Related Spec / work item: docs/work/<objective>/spec.md
- Tests: simulate timeout after commit, retry with the same key, and confirm only one resource exists.
- Commit / PR / source: To add after implementation.
- Last verified: To add after project verification.
