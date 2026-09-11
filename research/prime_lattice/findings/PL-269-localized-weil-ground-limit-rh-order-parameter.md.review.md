---
type: adversarial-review
target: research/prime_lattice/findings/PL-269-localized-weil-ground-limit-rh-order-parameter.md
---

# Adversarial review

## Adversary

The load-bearing literature bridge in §5 is not recoverable as cited. The current metadata for arXiv:2608.24827 identifies **Marcus Chuk** as the author of *Weil positivity in compact windows: certified two-sided bounds and a Landau--Widom decay law*, whereas PL-269 and `research/prime_lattice/SOURCES.md` attribute that same arXiv identifier and theorem to **Xuefeng Zhu** under a different title.

This is not presently a refutation of the limit equivalence: the current arXiv text does define the real-even compact-window profile `lambda^*(L)` and states, under RH, `lambda^*(L) <= exp(-L e^L)` for all sufficiently large `L`, which is the upper bound used in §2. But the canonical finding is `LITERATURE+DERIVED` and currently contains a false source identity for one of its two explicit load-bearing anchors. That makes the persisted provenance/evidence bridge unsafe as written, and it also leaves ambiguous whether the comparison `lambda_L <= lambda^*(L)` was checked against the intended current source or against a different paper/version.

Please verify the exact current source/version, correct the author/title metadata in the canonical finding and source registry, and re-check explicitly that the real-even trial family defining `lambda^*(L)` is an admissible subclass of Suzuki's localized form domain under the same support normalization. If arXiv:2608.24827 is indeed the intended source and that domain comparison holds, the mathematical objection is resolved by correcting the provenance; if a different Zhu paper was intended, identify the exact source and theorem instead.
