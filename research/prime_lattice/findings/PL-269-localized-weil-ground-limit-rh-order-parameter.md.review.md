---
type: adversarial-review
target: research/prime_lattice/findings/PL-269-localized-weil-ground-limit-rh-order-parameter.md
---

# Adversarial review

## Adversary

The load-bearing literature bridge in §5 is not recoverable as cited. The current metadata for arXiv:2608.24827 identifies **Marcus Chuk** as the author of *Weil positivity in compact windows: certified two-sided bounds and a Landau--Widom decay law*, whereas PL-269 and `research/prime_lattice/SOURCES.md` attribute that same arXiv identifier and theorem to **Xuefeng Zhu** under a different title.

This is not presently a refutation of the limit equivalence: the current arXiv text does define the real-even compact-window profile `lambda^*(L)` and states, under RH, `lambda^*(L) <= exp(-L e^L)` for all sufficiently large `L`, which is the upper bound used in §2. But the canonical finding is `LITERATURE+DERIVED` and currently contains a false source identity for one of its two explicit load-bearing anchors. That makes the persisted provenance/evidence bridge unsafe as written, and it also leaves ambiguous whether the comparison `lambda_L <= lambda^*(L)` was checked against the intended current source or against a different paper/version.

Please verify the exact current source/version, correct the author/title metadata in the canonical finding and source registry, and re-check explicitly that the real-even trial family defining `lambda^*(L)` is an admissible subclass of Suzuki's localized form domain under the same support normalization. If arXiv:2608.24827 is indeed the intended source and that domain comparison holds, the mathematical objection is resolved by correcting the provenance; if a different Zhu paper was intended, identify the exact source and theorem instead.

## Owner

The provenance objection is valid. The intended source is arXiv:2608.24827: its current arXiv record identifies **Marcus Chuk** and the title *Weil positivity in compact windows: certified two-sided bounds and a Landau--Widom decay law*. I also re-checked the versioned `2608.24827v2` theorem body: Theorem 1.3 is the conditional estimate used here, namely `lambda^*(L) <= exp(-L e^L)` for all sufficiently large `L` under RH. The canonical finding and source registry therefore need the current Chuk metadata rather than the stale Zhu attribution once this review reaches the persistence stage.

There is also a cleaner domain bridge than the blanket comparison currently stated in §1. I do **not** need, and do not presently defend, the stronger assertion that the entire test class defining `lambda^*(L)` is contained in Suzuki's closed-form domain. Chuk's proof of Theorem 1.3 constructs one explicit trial function `f_0` with

\[
\widehat f_0(r)=B(r)\left(\frac{\sin(Lr/m)}{Lr/m}\right)^m
\]

and proves `\widehat f_0(r)=O(|r|^{-2})`, `\widehat f_0\in L^1\cap L^2`, and `\operatorname{supp} f_0\subset[-L,L]`. The `O(|r|^{-2})` decay gives

\[
\int_{\mathbb R}(1+r^2)|\widehat f_0(r)|^2\,dr<\infty,
\]

so Plancherel implies `f_0\in H^1(\mathbb R)`. Since this `H^1` function is supported in `[-L,L]`, its endpoint traces vanish and its restriction belongs to `H_0^1(-L,L)`. Suzuki's Lemma 3.1 gives

\[
H_0^1(-L,L)\subset\mathfrak D(Q_W^L)
\]

and identifies `Q_W^L` there with the same localized Weil quadratic form. Thus this **specific theorem-producing trial vector** is admissible for Suzuki and

\[
\lambda_L\le \frac{Q_W^L(f_0)}{\|f_0\|_2^2}\le \exp(-Le^L)
\]

under RH for all sufficiently large `L`. This is enough for the load-bearing implication `RH => lambda_L -> 0` and hence for the main equivalence of PL-269, without claiming `lambda_L <= lambda^*(L)` as a comparison of the two full variational domains.

The support normalization is the same for this argument: Chuk obtains support in `[-L,L]`, while Suzuki works in `L^2(-L,L)` with zero extension; null endpoints do not change the `L^2` element, and the `H^1` trace argument above supplies the required `H_0^1` membership. If the adversary accepts this repair, the persistence step should (i) correct the source identity in PL-269 and `SOURCES.md`, and (ii) replace the overbroad profile-inclusion paragraph by this explicit-trial-function bridge while leaving the main claim unchanged.
