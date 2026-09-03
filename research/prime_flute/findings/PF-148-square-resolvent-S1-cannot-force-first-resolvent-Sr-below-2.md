# PF-148 — the PF-147 `S_2` conclusion is abstractly sharp

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + BOUNDARY`. PF-147 proves the classical conditional implication

\[
R_1^2-R_0^2\in\mathcal S_1
\quad\Longrightarrow\quad
R_1-R_0\in\mathcal S_2
\]

for positive Laplace resolvents. The present finding shows that exponent `2` cannot be improved by any argument using only positivity/self-adjointness, genuine resolvent realization, and trace class of the squared-resolvent difference. There are nonnegative self-adjoint operators with compact resolvent for which the squared-resolvent difference is trace class while the first-resolvent difference fails to lie in `S_r` for **every** `1 <= r < 2`. Thus the still-open prime/shift question for `1<r<2` can only be settled by extra prime-flute geometry or operator structure; it cannot follow abstractly from the PF-146/PF-147 square gate. This does not prove any lower-Schatten failure for the actual prime flute and its all-composite shift clone.

## Claim

There exist nonnegative self-adjoint operators `H_0,H_1` on a separable Hilbert space, each with compact resolvent, such that with

\[
R_i=(H_i+1)^{-1},
\qquad i=0,1,
\]

one has

\[
\boxed{R_1^2-R_0^2\in\mathcal S_1,}
\tag{1}
\]

but

\[
\boxed{R_1-R_0\in\mathcal S_2
\quad\text{and}\quad
R_1-R_0\notin\mathcal S_r\ \text{for every }1\le r<2.}
\tag{2}
\]

Consequently there is no general implication, even inside the class of positive compact resolvents,

\[
R_1^2-R_0^2\in\mathcal S_1
\quad\Longrightarrow\quad
R_1-R_0\in\mathcal S_r
\qquad (r<2).
\tag{3}
\]

The `S_2` endpoint supplied by Powers--Størmer/Birman--Koplienko--Solomyak in PF-147 is therefore sharp at this level of abstraction.

## 1. Explicit diagonal resolvent pair

Work on

\[
\mathcal H=\ell^2(\{n\ge2\}).
\]

Fix, for example, `c=1/4` and put

\[
a_n=\frac{c}{\sqrt n\,\log n},
\qquad
b_n=\frac{a_n}{2}.
\tag{4}
\]

Both sequences are strictly positive, bounded by `1`, and tend to zero. Define positive compact diagonal operators

\[
A=\operatorname{diag}(a_n),
\qquad
B=\operatorname{diag}(b_n).
\tag{5}
\]

Because every diagonal entry lies in `(0,1]`, set

\[
H_A=\operatorname{diag}(a_n^{-1}-1),
\qquad
H_B=\operatorname{diag}(b_n^{-1}-1)
\tag{6}
\]

on their natural maximal diagonal domains. These are nonnegative self-adjoint operators, their eigenvalues tend to `+infinity`, and hence they have compact resolvent. Moreover

\[
(H_A+1)^{-1}=A,
\qquad
(H_B+1)^{-1}=B.
\tag{7}
\]

Thus `A,B` are not arbitrary positive contractions inserted after the fact: they are genuine resolvents of nonnegative self-adjoint operators of the same abstract type used in PF-147.

## 2. The squared-resolvent difference is trace class

Since `B=A/2`,

\[
A^2-B^2
=
\frac34 A^2
=
\frac34\operatorname{diag}(a_n^2).
\tag{8}
\]

The trace norm is therefore

\[
\|A^2-B^2\|_{\mathcal S_1}
=
\frac34\sum_{n\ge2} a_n^2
=
\frac{3c^2}{4}\sum_{n\ge2}\frac{1}{n(\log n)^2}.
\tag{9}
\]

The last series converges by the integral test. Hence

\[
\boxed{A^2-B^2\in\mathcal S_1.}
\tag{10}
\]

This is exactly the abstract hypothesis appearing in PF-147.

## 3. The first-resolvent difference has exact threshold `2`

Again because `B=A/2`,

\[
A-B
=
\frac12 A
=
\frac12\operatorname{diag}(a_n).
\tag{11}
\]

For `r>0`, diagonal Schatten membership is equivalent to summability of the `r`th powers of the diagonal entries:

\[
A-B\in\mathcal S_r
\quad\Longleftrightarrow\quad
\sum_{n\ge2} a_n^r<\infty.
\tag{12}
\]

At `r=2`, equation (9) already gives convergence. Thus

\[
A-B\in\mathcal S_2.
\tag{13}
\]

Now fix `1<=r<2`. Then

\[
\sum_{n\ge2} a_n^r
=
c^r\sum_{n\ge2}
\frac{1}{n^{r/2}(\log n)^r}.
\tag{14}
\]

Let

\[
\varepsilon=\frac{1-r/2}{2}>0.
\]

For sufficiently large `n`, `(\log n)^r <= n^\varepsilon`. Therefore the summand in (14) obeys

\[
\frac{1}{n^{r/2}(\log n)^r}
\ge
\frac{1}{n^{r/2+\varepsilon}}.
\tag{15}
\]

But

\[
r/2+\varepsilon
=
\frac12+\frac r4
<1,
\tag{16}
\]

so the comparison series diverges. Hence

\[
\boxed{A-B\notin\mathcal S_r\quad(1\le r<2).}
\tag{17}
\]

Taking `(R_1,R_0)=(A,B)` proves (1)--(2).

## 4. What this closes in the prime-flute program

PF-146 asks whether the **actual** prime-flute/all-composite-shift pair satisfies the still-open global gate

\[
(\Delta_{g_+}+1)^{-2}-(\Delta_g+1)^{-2}\in\mathcal S_1.
\tag{18}
\]

PF-147 shows that (18), if established, forces

\[
(\Delta_{g_+}+1)^{-1}-(\Delta_g+1)^{-1}\in\mathcal S_2.
\tag{19}
\]

A tempting next step would be to search for a stronger general functional-calculus theorem that pushes (19) automatically to `S_r`, `1<r<2`. The diagonal pair above rules out that route under precisely the abstract data available in PF-147. Even requiring that both positive operators be genuine compact resolvents of nonnegative self-adjoint operators does not improve the exponent.

Therefore the accepted sharp-Schatten question is now split cleanly:

- `r>=2`: conditionally controlled by the still-open global PF-146 gate via PF-147;
- `1<r<2`: **cannot** be obtained from that gate by abstract square-root ideal theory alone.

Any proof below exponent `2` must use additional structure specific to the prime/shift surfaces: geometric localization, a stronger factorization of the resolvent identity, singular-value estimates for the actual metric defect, boundary-coherent pants/collar assembly, heat-kernel/gradient factors, cancellation, or some other surface-specific mechanism. Conversely, failure of such geometric mechanisms could still show that the actual pair has threshold `2`; PF-148 does not decide that question.

## 5. Prior art and novelty audit

No novelty is claimed for the general operator-theoretic sharpness phenomenon. PF-147 already records the classical Powers--Størmer square-root inequality and the Birman--Koplienko--Solomyak fractional-power ideal estimates that produce the `S_2` endpoint. Directed searches for sharp fractional-power/Schatten exponents did not expose a need for an additional specialized theorem here: the commuting diagonal construction above is an elementary exact counterexample and independently certifies the project boundary.

The durable Mathia contribution is therefore deliberately narrow. It is not a new Schatten theorem; it is the explicit falsification of a specific escape route left open by PF-147:

\[
\boxed{
\text{global square-resolvent }\mathcal S_1
\not\Longrightarrow
\text{first-resolvent }\mathcal S_r\text{ for any }r<2
\text{ by abstract resolvent theory alone}.}
\tag{20}
\]

The classical sources supporting the positive `S_2` implication are already anchored in `SOURCES.md` for PF-147. No new external theorem is imported by the counterexample.

## 6. Boundary conditions and adversarial controls

The construction is intentionally **not** a hyperbolic surface and does not imitate the prime sequence. That is a feature of the obstruction: it proves only that the PF-147 hypotheses are insufficient by themselves. It does not establish

\[
(\Delta_{g_+}+1)^{-1}-(\Delta_g+1)^{-1}\notin\mathcal S_r
\]

for any `r>1` on the actual prime/shift pair.

Nor does PF-148 weaken PF-147. The example lies in `S_2` exactly as Powers--Størmer predicts. It demonstrates that the exponent cannot be uniformly lowered without extra assumptions. It also leaves PF-112's geometric non-`S_1` theorem untouched: here non-`S_1` follows merely from the chosen diagonal decay, whereas PF-112 derives the trace obstruction intrinsically from the nonzero order-`-2` local principal symbol of a non-isometric two-dimensional metric pair.

The example uses compact resolvents whereas the prime-flute Laplacians live on a noncompact infinite-type surface. Compactness of the model therefore cannot be cited as evidence for the surface pair; it only strengthens the abstract negative by showing that even a spectrally simpler resolvent setting does not improve the exponent.

## 7. Audit / falsification core

A later adversary can check the entire new claim without external machinery:

1. verify `0<a_n,b_n<=1`, `a_n,b_n->0`, and therefore the self-adjoint nonnegative diagonal realizations (6)--(7);
2. verify convergence of `sum 1/(n log^2 n)`, which gives (10) and `A-B in S_2`;
3. for every fixed `r<2`, use `(log n)^r=o(n^epsilon)` with `epsilon=(1-r/2)/2` to obtain the divergent lower comparison (15)--(16);
4. conclude that the same genuine-resolvent pair satisfies the PF-147 square hypothesis but fails every Schatten class below `2`.

A refutation must identify an error in one of these elementary series or in the diagonal resolvent realization. Additional geometric hypotheses satisfied by the prime flute do not refute PF-148; they would instead be exactly the extra input required to escape its abstract obstruction.

## Research consequence

PF-147's Hilbert--Schmidt endpoint is the strongest conclusion available from its abstract square-resolvent premise alone. The live `1<r<2` part of `CLUE-shift-clone-sharp-schatten-threshold.md` is therefore a genuinely **prime-flute-specific operator problem**, not a missing generic functional-calculus corollary. This removes a natural but unproductive branch of the search and focuses subsequent work on the geometry and infinite assembly of the exact prime/shift pair.