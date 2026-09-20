# PC-364 — supercritical scalar raising spectrum fills the complex plane

- **Finding ID:** `PC-364`
- **Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE`
- **Workflow:** `DERIVED + PRIOR-ART AUDIT + ADVERSARIAL CONTROL`
- **Research line:** `prime_circle`
- **Result type:** exact supercritical-domain / residual-spectrum classification
- **Scope:** completes the canonical one-sided weighted-shift family left only partially classified by PC-362--PC-363. Once the scalar raising coefficient crosses the critical modulus, the operator does not acquire a richer arithmetic spectrum: its resolvent set disappears and the entire complex plane becomes residual spectrum.
- **RH relevance:** high as a negative control. Together with PC-362 and PC-363 this gives an exact three-regime phase diagram for the simplest all-depth one-sided spectralization. The subcritical regime keeps only bare grades, the critical regime produces a universal half-plane with a `1/2` edge, and the supercritical regime produces all of `C`. None of these transitions selects zeta zeros or retains Prime-Circle arithmetic.

## Claim

On `ell^2(N_0)` let

\[
N e_n=n e_n,
\qquad
Q_c e_n=c(n+1)e_{n+1},
\qquad
H_c=N+Q_c
\]

with domain `D(N)`, where `c in C`. PC-362 proves the subcritical case `|c|<1`; PC-363 resolves `|c|=1`. For the remaining supercritical regime,

\[
\boxed{|c|>1\quad\Longrightarrow\quad \sigma(H_c)=\mathbb C.}
\tag{1}
\]

More sharply,

\[
\boxed{\sigma_p(H_c)=\varnothing,}
\qquad
\boxed{\sigma_p(H_c^*)=\mathbb C,}
\tag{2}
\]

and for every `lambda in C`,

\[
\boxed{
\dim\ker(H_c^*-\overline\lambda)=1,
\qquad
\operatorname{codim}\overline{\operatorname{Ran}(H_c-\lambda)}=1.
}
\tag{3}
\]

Thus every complex number is residual/compression spectrum: `H_c-lambda` is injective but its range is not dense.

Combining PC-362--PC-364 gives the exact scalar-amplitude phase diagram

\[
\boxed{
\begin{array}{c|c}
|c|<1 & \sigma(H_c)=\mathbb N_0 \\
|c|=1 & \sigma(H_c)=\{\lambda:\operatorname{Re}\lambda\ge-\tfrac12\} \\ 
|c|>1 & \sigma(H_c)=\mathbb C.
\end{array}}
\tag{4}
\]

The middle formula is understood after the harmless diagonal phase conjugation described below, so the spectrum depends only on `|c|`.

## 1. The phase of `c` is unitary gauge

For `c=re^{i theta}`, define

\[
D_\theta e_n=e^{-in\theta}e_n.
\]

Then `D_theta` commutes with `N` and rotates the unilateral shift so that

\[
D_\theta H_cD_\theta^*=H_r.
\tag{5}
\]

Hence only `r=|c|` matters. We may assume `c=r>1`.

As in PC-363, conjugate once more by the alternating unitary `Ue_n=(-1)^n e_n`. The resulting operator

\[
B_r:=UH_rU
\]

has coordinate form

\[
(B_r x)_n=n(x_n-rx_{n-1}),
\qquad x_{-1}=0,
\tag{6}
\]

on `D(N)`.

For `r>1`, this operator is closed. Indeed,

\[
B_r=(I-rS)N-rS,
\tag{7}
\]

and the bounded factor `I-rS` is bounded below because

\[
\|(I-rS)x\|\ge(r-1)\|x\|.
\tag{8}
\]

Consequently the graph norm of `B_r` is equivalent to the graph norm of `N`; in particular finite sequences form a core.

## 2. The adjoint has an eigenvector for every complex spectral parameter

Because finite sequences are a core, the adjoint is the maximal backward bidiagonal operator

\[
(B_r^*y)_n
=n y_n-r(n+1)y_{n+1}
\tag{9}
\]

on the maximal domain for which the right-hand side lies in `ell^2`.

Solving

\[
B_r^*y=\overline\lambda y
\]

gives the first-order recurrence

\[
y_{n+1}
=\frac{n-\overline\lambda}{r(n+1)}y_n.
\tag{10}
\]

If `lambda` is not a nonnegative integer,

\[
y_n
=r^{-n}
\frac{\Gamma(n-\overline\lambda)}
{\Gamma(-\overline\lambda)\,n!}
y_0,
\tag{11}
\]

so Stirling's formula gives

\[
|y_n|\asymp
r^{-n}n^{-\operatorname{Re}\lambda-1}.
\tag{12}
\]

The exponential factor `r^{-n}` makes this sequence square-summable for **every** `lambda in C`. If `lambda=m in N_0`, the recurrence terminates at `n=m` and gives a nonzero finite-support vector. In either case the formal image in (9) equals `overline(lambda)y`, so the vector lies in `D(B_r^*)`.

Therefore

\[
\boxed{
\ker(B_r^*-\overline\lambda)\ne0
\quad\text{for every }\lambda\in\mathbb C.
}
\tag{13}
\]

The recurrence is determined uniquely by `y_0`, so every such eigenspace is one-dimensional.

Using

\[
\overline{\operatorname{Ran}(B_r-\lambda)}^\perp
=
\ker(B_r^*-\overline\lambda),
\tag{14}
\]

we obtain

\[
\boxed{
\operatorname{codim}
\overline{\operatorname{Ran}(B_r-\lambda)}=1
\quad\text{for every }\lambda\in\mathbb C.
}
\tag{15}
\]

Thus the resolvent set is empty.

## 3. The original operator still has no eigenvalues

For completeness, the supercritical point-spectrum obstruction from PC-362 can be seen directly in (6). Suppose

\[
B_r x=\lambda x.
\]

At coordinate zero, `0=lambda x_0`. If `lambda` is not a nonnegative integer, the forward recurrence forces every coordinate to vanish. If `lambda=m in N_0`, the first possible free coefficient occurs at grade `m`; thereafter

\[
x_{m+k}
=r^k\binom{m+k}{k}x_m.
\tag{16}
\]

For `r>1` this grows exponentially and cannot belong to `ell^2` unless `x_m=0`. The case `m=0` is the same recurrence starting from `x_0`.

Hence

\[
\boxed{\sigma_p(B_r)=\varnothing.}
\tag{17}
\]

Together with (13)--(15), every `lambda` is residual spectrum, proving (1)--(3).

## 4. Hardy-space form exposes the universal threshold

Under the standard identification

\[
\ell^2(\mathbb N_0)\simeq H^2(\mathbb D),
\qquad
x\longleftrightarrow f(z)=\sum_{n\ge0}x_nz^n,
\]

(6) becomes

\[
\boxed{
B_r f(z)=z(1-rz)f'(z)-rzf(z).
}
\tag{18}
\]

The same scalar threshold has an immediate analytic interpretation. The second zero of the derivative coefficient `z(1-rz)` is

\[
z=1/r.
\]

For `r<1` it lies outside the unit disk; at `r=1` it reaches the Hardy boundary; for `r>1` it lies strictly inside the disk. Exactly the same crossing is reflected by the adjoint solution:

\[
r^{-n}n^{-\lambda-1}.
\tag{19}
\]

Below threshold the exponential factor grows and only terminating sequences survive; at threshold square summability is controlled by the polynomial exponent and produces the `-1/2` boundary of PC-363; above threshold exponential decay makes **every** spectral parameter admissible to the adjoint.

This is a universal Hardy/domain transition. No cyclotomic shell, Ramanujan mode, resultant, von Mangoldt weight, old/new coupling, or other Prime-Circle datum enters it.

## 5. Consequence for the live Prime-Circle operator route

The canonical scalar one-sided raising family is now completely classified:

\[
\text{subcritical}
\longrightarrow
\text{bare grade spectrum},
\qquad
\text{critical}
\longrightarrow
\text{universal half-plane},
\qquad
\text{supercritical}
\longrightarrow
\text{entire complex plane}.
\tag{20}
\]

Increasing the one-sided raising amplitude therefore does not create progressively sharper arithmetic spectral data. It does the opposite: after the critical completion transition, spectral localization is destroyed completely.

This closes the simplest remaining escape in PC-363: **a scalar supercritical rescaling of the canonical strictly raising term cannot be an RH mechanism**. It does not close genuinely source-dependent supercritical domains, same-grade/backward/two-sided couplings, or non-eigenvalue observables. Those remain separate questions and would need an intrinsic Prime-Circle coupling that survives the line's matched-control and prior-art tests.

## Prior-art and novelty audit

No operator-theory novelty is claimed. The Hardy-space differential form (18) belongs to the classical class `Af=G f'+g f` studied for generators and weighted-composition dynamics; PC-363 already records the nearby literature boundary, including Gallardo-Gutiérrez, Siskakis and Yakubovich, *Generators of C0-semigroups of weighted composition operators* (Israel Journal of Mathematics, 2023; arXiv:2110.05247), and earlier composition-semigroup work of Siskakis. The present proof uses only the explicit bidiagonal adjoint recurrence, standard gamma-ratio asymptotics, and the Hilbert-space identity `(Ran T)^perp=ker T*`.

Targeted searches for the exact matrix `N+cS(N+I)`, its Hardy differential form `z(1-cz)f'-czf`, unbounded bidiagonal spectra, and whole-plane residual spectra did not locate a publication stating precisely the phase diagram (4) for this normalization. That absence is not treated as evidence of novelty. The durable contribution here is line-local and negative: it completes the exact control family generated by PC-362--PC-363 and shows that the supercritical scalar branch loses all spectral selectivity rather than revealing a hidden zeta spectrum.

## Audit / falsification checks

The conclusion depends on the canonical one-sided scalar family and on the common domain `D(N)` for `r>1`. It would not automatically apply to a source-dependent closed extension, a coefficient sequence `c_n` carrying arithmetic data, a backward or two-sided coupling, or a nontriangular block operator. Those changes are not cosmetic: they alter the recurrence or its admissible domain and require a fresh analysis.

The decisive check is (10)--(12). Any counterexample to (1) would need a complex `lambda` for which the adjoint recurrence fails to define a nonzero vector in `D(B_r^*)`; for `r>1`, the explicit exponential decay rules this out for every `lambda`.