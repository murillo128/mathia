# WI-293 — the current Cramér-scale prime-gap preprint cannot close the Lambert-screening branch as written

## Status

- **Evidence:** `EXACT-DERIVED + LITERATURE-AUDIT + DECISIVE-NEGATIVE + PRIOR-ART-AUDITED`.
- **Scope:** the live arithmetic endpoint of the **one-signed, completely screened, symmetric two-island** branch in `WI-288`--`WI-292`. This finding audits a recent prime-gap preprint which, if valid, would immediately close that branch.
- **Result:** Cheng-Ting Wang's current arXiv v5 of *On Maximal Prime Gaps* claims the unconditional bound
  \[
  g_n=p_{n+1}-p_n<\frac{13}{3}\log^2 p_n
  \]
  for every `n`. Such a bound would contradict the `WI-288` necessary gap scale `g \gtrsim \sqrt{x}\log x` and therefore eliminate all sufficiently large two-island completely screened candidates. However, the proof of the load-bearing Lemma 2.3 contains a false weighted-telescoping identity. With the paper's own definitions,
  \[
  B_n=\sum_{k=2}^n\frac{g_k}{k-1},\qquad
  y_n=B_n-B_{n-1},
  \]
  one has exactly `B_n-B_2=sum_{k=3}^n y_k`, whereas v5 states
  \[
  \sum_{k=3}^n\frac{k}{k-1}y_k=B_n-B_2.
  \]
  The difference is strictly positive. Already at `n=3`, the stated left side is `3/2` while the right side is `1`. The subsequent displayed identity (2.10), the remainder of Lemma 2.3, and hence Theorem 2.5 all depend on this false step. The preprint therefore cannot be imported as unconditional prime-gap evidence in its present form.
- **What it does not claim:** this is not a proof that the stated `O(log^2 p)` theorem is false, nor a proof that no repair of the manuscript is possible. It establishes only that the current v5 proof does not prove the theorem as written. The established `WI-288`--`WI-292` arithmetic endpoint therefore remains open.
- **Novelty boundary:** the Cramér-scale statement is the preprint's claim, not Mathia's. The line-local contribution is the exact proof audit of the identity on which its main bound depends and the observation that this candidate theorem, were it valid, would be decisive for the current Lambert-screening branch. Search absence of an independent validation is audit context only.

## 1. Why this preprint would be decisive if correct

`WI-288` shows that a hypothetical completely screened symmetric two-island first-crossing null mode at center `x` forces a two-sided prime-power gap on the Lambert scale. Since ordinary primes are prime powers, the neighboring ordinary primes `p_-<x<p_+` must in particular satisfy

\[
p_+-p_-
\ge 2\sqrt{x}\,W(c_0\sqrt{x})(1-o(1))
=\sqrt{x}\log x-2\sqrt{x}\log\log x+O(\sqrt{x}).
\tag{1}
\]

Thus any unconditional bound

\[
g_n\ll \log^2 p_n
\tag{2}
\]

would be far stronger than needed: for sufficiently large `x`,

\[
\log^2 x=o(\sqrt{x}\log x).
\tag{3}
\]

Wang's current arXiv v5, dated 23 July 2026, states precisely such a theorem with constant `13/3`. If Theorem 2.5 were established, (1)--(3) would close the current two-island complete-screening branch outright, with no cross-scale prime-square incidence theorem required.

That makes the proof provenance load-bearing rather than optional: importing the headline without checking the manuscript would create a false RH-path shortcut if the proof has a gap.

## 2. The load-bearing telescope in Lemma 2.3 is false

In v5, the paper defines

\[
B_n:=\sum_{k=2}^n\frac{g_k}{k-1}.
\tag{4}
\]

Lemma 2.3 then writes

\[
y_n:=B_n-B_{n-1}.
\tag{5}
\]

Equations (4)--(5) give immediately

\[
\boxed{y_n=\frac{g_n}{n-1}.}
\tag{6}
\]

Therefore the genuine telescope is

\[
\boxed{B_n-B_2=\sum_{k=3}^n y_k.}
\tag{7}
\]

The manuscript instead asserts, immediately after defining `y_n`,

\[
\boxed{
\sum_{k=3}^n\frac{k}{k-1}y_k=B_n-B_2.
}
\tag{8}
\]

But substituting (7) shows that the discrepancy is exactly

\[
\sum_{k=3}^n\left(\frac{k}{k-1}-1\right)y_k
=
\boxed{
\sum_{k=3}^n\frac{y_k}{k-1}
}
>0,
\tag{9}
\]

because every prime gap is positive. Hence (8) is not an endpoint convention or an asymptotic approximation; it is algebraically false for every `n>=3`.

There is a minimal exact countercheck. With

\[
(p_1,p_2,p_3,p_4)=(2,3,5,7),
\]

we have `g_2=g_3=2`, so

\[
B_2=2,\qquad B_3=3,\qquad y_3=1.
\]

At `n=3`, (8) reads

\[
\frac32=1.
\tag{10}
\]

Thus the displayed claim fails before any asymptotic estimate enters.

## 3. The main theorem depends on the false identity

The false equality (8) is used to derive the manuscript's displayed equation (2.10), which expresses `T_n` and then `g_n/n` in terms of the weighted `y_k` sum. The rest of Lemma 2.3 starts from that representation and eventually concludes

\[
g_n<\frac{13}{3}B_n.
\tag{11}
\]

Theorem 2.5 explicitly invokes Lemma 2.3 and then combines (11) with an upper estimate for `B_n` to obtain

\[
g_n<\frac{13}{3}\log^2 p_n.
\tag{12}
\]

Because the derivation of (11) passes through the false identity (8), (11) is not proved by the argument given, and consequently neither is (12).

There are additional transcription-level inconsistencies in this part of the manuscript -- for example a later line labels a quantity `B_{n+1}` while expanding the formula for `B_n`, and one sum drops the visible `(k-1)^{-1}` factor that the next integral requires. Those may be repairable typographical errors. They are not needed for the present audit. Equation (8) is already a decisive proof break because it changes the algebra from which Lemma 2.3 is derived.

A future revision could of course replace the argument with a valid one. The correct review posture is therefore **not** “the Cramér-scale theorem is disproved”; it is “the current v5 theorem is unestablished and cannot be used as an input.”

## 4. Prior-art and provenance audit

Primary source inspected:

- Cheng-Ting Wang, **On Maximal Prime Gaps**, arXiv:2605.14871v5, 23 July 2026, https://arxiv.org/abs/2605.14871. The arXiv record says the paper was first submitted 14 May 2026, is currently at v5, and supersedes arXiv:2510.17065. The abstract claims `g_n<(13/3) log^2 p_n`; the proof above is in Lemma 2.3 and Theorem 2.5.

The manuscript itself describes Baker--Harman--Pintz's `x^0.525` short-interval theorem as the best unconditional result known to the author. The line already records the more recent Runbo Li `x^0.52` preprint at a lower evidence tier. Neither established input comes close to (2), and neither closes (1).

Targeted searches for the current arXiv identifier, title, author, and criticism/validation found the preprint and mirrors of it but no independent proof, peer-reviewed acceptance, or correction of the Lemma 2.3 telescope. This search result is not mathematical evidence; the rejection here rests only on the exact countercalculation (6)--(10).

## Consequence for the research line

This audit prevents a superficially decisive but invalid shortcut. A genuine unconditional Cramér-scale prime-gap upper bound would annihilate the `WI-288` two-island branch immediately, so future literature watches should continue to test any such claim against the exact Lambert threshold. The current Wang v5 claim does **not** change the canonical frontier: after `WI-292`, the live problem remains the survival or exclusion of the rare `X^{1/10+o(1)}` host-localized candidate pieces under all prime-power cuts, or a different support/sign topology that bypasses complete screening.
