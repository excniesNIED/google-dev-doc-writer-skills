# Architecture Documentation

How Google Cloud documents architecture. Grounded in the [Google Cloud Well-Architected Framework](https://cloud.google.com/architecture/framework) and the Cloud Architecture Center.

## Framework structure

The Well-Architected Framework organizes recommendations into pillars and cross-pillar perspectives:

| Pillar | Focus |
| :--- | :--- |
| Operational excellence | Efficiently deploy, operate, monitor, and manage workloads. |
| Security, privacy, and compliance | Maximize data and workload security; align with regulations. |
| Reliability | Design and operate resilient, highly available workloads. |
| Cost optimization | Maximize business value of the cloud investment. |
| Performance optimization | Design and tune resources for optimal performance. |
| Sustainability | Build and manage environmentally sustainable workloads. |

Perspectives (for example AI and ML, financial services) are cross-pillar views for a specific technology, domain, or sector.

## Core principles

State these principles explicitly when reviewing an architecture:

1. **Design for change** — deliver small changes regularly and get fast feedback.
2. **Document your architecture** — documentation is a common language; keep a change log.
3. **Simplify and use managed services** — resist over-engineering; start with an MVP.
4. **Decouple your architecture** — independent components, independent upgrades and reliability goals.
5. **Use a stateless architecture** — scale quickly, tolerate hard restarts, minimize boot dependencies.

## Guide structure

Structure an architecture guide as follows:

1. **Overview** — the problem the architecture solves and the target outcome.
2. **Architecture diagram** — a topology diagram with labels for every component.
3. **Architecture components** — a table mapping each component to its purpose.
4. **Design decisions** — what you chose and why, including tradeoffs.
5. **Deployment steps** — numbered steps to reproduce the topology.
6. **Cost estimate** — a table of components and estimated monthly cost.
7. **What's next** — related guides and advanced configurations.

## Component table shape

| Component | Purpose |
| :--- | :--- |
| Cloud Load Balancing | Distributes traffic across the backend instances. |
| Cloud Run | Runs the stateless API service, autoscaling to zero. |
| Cloud SQL | Stores relational data with automated backups. |

## Reliability and security guidance

- **Reliability**: define reliability from user-experience goals, set realistic targets, build redundancy, use horizontal scalability, and design for graceful degradation. Test recovery from failures and data loss; run postmortems.
- **Security**: apply security by design, zero trust (never trust, always verify), shift-left security, and preemptive cyber defense.

## Tradeoff documentation

For every design decision, give the alternatives considered and the reason for the choice:

- **Chosen**: managed service X for component Y.
- **Alternative**: self-managed cluster Z.
- **Reason**: lower operational overhead; acceptable for the workload's scale.
