# Lightweight Architecture Decision Records

> **_"Lightweight Architecture Decision Records is a technique for capturing important architectural decisions along
> with their context and consequences."_**

— ["Lightweight Architecture Decision Records", ThoughtWorks Technology Radar](https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records)

## Capturing architecture and design decisions

The records in this directory help us capture architecture and design decisions that are often made in the
context of mobbing and pairing while developing solutions to the problems at hand. These records are meant
to be as lightweight as possible while still capturing the important context of the decision and the
decision itself.

We generally follow guidance from the [Agile Manifesto](https://agilemanifesto.org/) to value working software
over comprehensive documentation. Highly readable code and tests are of primary importance. Architecture needs to
evolve over time in response to challenges encountered, and capturing the context that a decision was made within
helps foster more effective conversations about evolution. These records also help new team members get up to
understanding of the architecture of the system quickly and efficiently. We believe our lightweight approach
represents the minimum we want to document to achieve these goals.

We are using [a template from Peter Evans](https://github.com/peter-evans/lightweight-architecture-decision-records/).
As a starting point for our records.

## Details

We have adopted a short document with just five sections:

- Title
- Context
- Decision
- Status [Proposed, Accepted, Deprecated, Superseded]
- Consequences

There is (an example markdown template](0001-ladr-template.md) that can serve as a starting point.

## Tips for using Lightweight Architecture Decision Records

- Use markdown and store along with the component it relates to in source control
- Number the files sequentially
- Keep it brief and use plain, easy to understand language
- Peer review as you would code
- When you make a decision, document it immediately!
- Add the record to the list in this document
