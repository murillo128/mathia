---
type: adversarial-review
target: research/weil_positivity/findings/WP-066-base-shell-hardy-gram-recovers-mangoldt-only-through-a-nonnormalizable-anchor.md
---

# Adversarial review

## Adversary

The target claim in §§7–8 is stronger than the calculation currently establishes. Equations (30)–(35) prove that the **particular zero-finite-part normalization**

\[
\widetilde{\mathcal E}_N(B)=\mathcal E_N(B)-E_N
\]

has limit

\[
\mathcal R(B)=Q_H(B)-2\operatorname{Re}L(B)
\]

and cannot be nonnegative because `R(0)=0` while its first variation is nonzero. They do not show that every scalar renormalization retaining the same exact `Lambda` cross term loses positivity. For any fixed real `c`, subtracting `E_N-c` instead gives the equally finite limit

\[
\mathcal R_c(B)=Q_H(B)-2\operatorname{Re}L(B)+c,
\]

with exactly the same von Mangoldt polarization. A nonzero first variation does not prevent such a shifted quadratic from being nonnegative: already on one shell,

\[
q_m t^2-2(\log p)t+c\ge0\quad\forall t
\]

whenever `c >= (log p)^2/q_m`.

The global issue is precisely whether `L` is bounded in the `Q_H` norm on the completion of the shell span. If it is bounded, Riesz gives a representing vector `g` and

\[
Q_H(B)-2\operatorname{Re}L(B)+\|g\|_H^2
=\|B-g\|_H^2\ge0,
\]

so a finite renormalization constant restores positivity while retaining the exact arithmetic linear term. If `L` is unbounded, then `\inf_B(Q_H(B)-2\operatorname{Re}L(B))=-\infty`, and no finite constant can repair the sign. The finding explicitly says in §9 that it has **not** ruled out a representing vector in the shell completion, so this dichotomy is presently unresolved.

This is material to the advertised “sharp trilemma” and the strategic conclusion that the line should move away from single-anchor renormalization. Either prove that

\[
\sup_{B\ne0}\frac{|L(B)|^2}{Q_H(B)}=\infty
\]

(or an equivalent no-Riesz-representer statement) to obtain the claimed scheme-independent obstruction, or narrow §§7–8 and the status/consequence language to the canonical normalization subtracting exactly `E_N`. A proof that a finite additive renormalization constant is forbidden by an independently stated normalization principle would also resolve the objection, but that principle is not currently present in the finding.
