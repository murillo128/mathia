# AF-248 — Periodic completeness fails for Li-symmetric transcendental modes

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `OUTPUT-SAMPLING`, `DIOPHANTINE-FIDELITY`, `LI-DOMINANT-MODE-CONTROL`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-247 shows that periodic completeness is the exact universal root-observability criterion for **algebraic** finite unit-circle modes. That conclusion does not extend to the elementary phase structure forced on a dominant off-RH Keiper--Li contribution.

There exist an irrational `alpha` and a strictly increasing set

\[
S=\{n_1<n_2<\cdots\}\subset\mathbb N
\tag{1}
\]

such that

\[
\forall q\ge1,\ \forall r\in\mathbb Z/q\mathbb Z,
\qquad |S\cap(r+q\mathbb Z)|=\infty,
\tag{2}
\]

but for the conjugate two-mode trigonometric polynomial

\[
F(n)
=-\left(u^n+\bar u^n\right)
=-2\cos(\pi n\alpha),
\qquad
u=e^{\pi i\alpha},
\tag{3}
\]

one has the much stronger failure

\[
\boxed{
\limsup_{\substack{n\to\infty\\n\in S}}
|F(n)|^{1/n}=0.
}
\tag{4}
\]

The coefficients in `(3)` have the common sign and integer multiplicity pattern arising from a simple conjugate pair of dominant Keiper--Li poles. Moreover, for every `0<r_0<1`, `alpha` can be chosen in `(1/2,5/8)` so that the same phase pair is compatible with the elementary functional-equation/conjugation geometry of an off-critical zero quartet. Put

\[
a=r_0e^{-\pi i\alpha},
\qquad
\rho=\frac1{1-a}.
\tag{5}
\]

Then

\[
\frac12<\Re\rho<1,
\qquad
1-\frac1\rho=a,
\tag{6}
\]

and the quartet

\[
\rho,\ \bar\rho,\ 1-\rho,\ 1-\bar\rho
\tag{7}
\]

has Keiper conformal images

\[
a,\ \bar a,\ a^{-1},\ \bar a^{-1}.
\tag{8}
\]

The two interior images `a,\bar a` have common modulus `r_0`, and after the AF-244 normalization their phases are exactly `u,\bar u`; a simple pair therefore contributes the normalized mode `(3)` up to the irrelevant common sign.

Thus **periodic completeness, conjugate pairing, positive integer multiplicity, and the elementary zero symmetries are jointly insufficient to guarantee Li root-rate fidelity**. Any attempt to transfer AF-247 from algebraic modes to the actual zeta-derived dominant modes needs genuinely quantitative Diophantine information about those phases, not only profinite coverage or functional-equation symmetry.

By AF-247, the phase `u` produced here cannot be algebraic. The obstruction is therefore exactly on the transcendental side of the algebraic/transcendental boundary isolated there.

## Why it matters

AF-245--AF-246 replaced output density by phase recurrence and then by the exact shrinking-target exponent consumed by the root-rate decoder. AF-247 showed that algebraic recurrence rigidity collapses this quantitative condition to the purely periodic requirement `(2)`. A tempting next step would be to hope that the special real/conjugate structure of Li's dominant mode supplies enough extra rigidity to make the same reduction for zeta.

The present control rules that out. The simplest Li-shaped mode already supports an arbitrarily severe shrinking-target defect on a periodically complete retained set. The missing ingredient cannot be merely that Li coefficients are real, that conjugate zeros occur together, that their residues are integer multiplicities, or that the functional equation supplies the reciprocal exterior partners.

This sharpens the output-side frontier: for a retained set substantially weaker than AF-244 thickness, a source-specific theorem must control how the **actual zero-derived phase orbit approaches the zero loci of its finite trigonometric combinations**. Without such a theorem, periodic completeness can preserve every finite-order alias and still erase the off-RH exponential rate completely.

## Exact construction

### 1. Force exponentially shrinking half-integer targets in every residue class

Choose a sequence of residue constraints

\[
(q_j,r_j),\qquad q_j\ge1,\quad 0\le r_j<q_j,
\tag{9}
\]

in which every pair `(q,r)` occurs infinitely many times. We construct increasing rational approximants

\[
\alpha_j=\frac{p_j}{2n_j}
\tag{10}
\]

with `p_j` odd and

\[
n_j\equiv r_j\pmod{q_j}.
\tag{11}
\]

Start from `\alpha_0=1/2`. Having chosen `\alpha_{j-1}` and `n_{j-1}`, choose `n_j` in the required residue class, larger than all previous indices, and so large that

\[
\frac1{n_j}\le 2^{-j-3},
\tag{12}
\]

and, for `j>1`,

\[
\frac1{n_j}
\le \frac14\varepsilon_{j-1},
\qquad
\varepsilon_{j-1}:=
\frac{e^{-n_{j-1}^2}}{8n_{j-1}},
\tag{13}
\]

while also

\[
\varepsilon_j:=\frac{e^{-n_j^2}}{8n_j}
\le \frac12\varepsilon_{j-1}.
\tag{14}
\]

Every residue class contains arbitrarily large integers, so these requirements are compatible.

The numbers with odd numerator and denominator `2n_j` form a grid of spacing `1/n_j`. Hence one can choose an odd `p_j` so that

\[
0<\alpha_j-\alpha_{j-1}\le\frac1{n_j}.
\tag{15}
\]

The sequence `\alpha_j` is strictly increasing. By `(12)`,

\[
0<\alpha_j-\frac12
<\sum_{k\ge1}2^{-k-3}
=\frac18,
\tag{16}
\]

so it converges to some

\[
\alpha\in\left(\frac12,\frac58\right).
\tag{17}
\]

For fixed `j`, `(13)`--`(14)` give a geometric tail bound:

\[
0<\alpha-\alpha_j
\le\sum_{k>j}\frac1{n_k}
\le\frac12\varepsilon_j
=\frac{e^{-n_j^2}}{16n_j}.
\tag{18}
\]

Since `p_j` is odd,

\[
n_j\alpha_j=\frac{p_j}{2}\in\mathbb Z+\frac12.
\tag{19}
\]

Therefore

\[
\operatorname{dist}
\left(n_j\alpha,\mathbb Z+\frac12\right)
\le\frac1{16}e^{-n_j^2}.
\tag{20}
\]

Because every residue constraint occurs infinitely often, `(11)` makes `S={n_j}` periodically complete exactly as in `(2)`.

### 2. The limiting phase is irrational and has no exact periodic alias

Suppose `\alpha=A/B` were rational in lowest terms. Since `\alpha_j<\alpha` for every `j`, rational separation gives

\[
\alpha-\alpha_j
=\left|\frac AB-\frac{p_j}{2n_j}\right|
\ge\frac1{2Bn_j}.
\tag{21}
\]

But `(18)` is smaller than `1/(2Bn_j)` for all sufficiently large `j`, a contradiction. Thus `\alpha` is irrational.

Consequently `n\alpha` is never a half-integer for an integer `n>0`, so the mode `(3)` has no exact zeros at all. The failure below is therefore a pure near-cancellation phenomenon, not a Skolem--Mahler--Lech periodic zero class.

### 3. Every retained value is superexponentially small

Using `(19)`--`(20)`,

\[
|F(n_j)|
=2|\cos(\pi n_j\alpha)|
=2\left|\sin\!\left(\pi n_j(\alpha-\alpha_j)\right)\right|
\le 2\pi n_j|\alpha-\alpha_j|.
\tag{22}
\]

Hence

\[
|F(n_j)|
\le \frac\pi8 e^{-n_j^2}.
\tag{23}
\]

Taking `n_j`th roots yields

\[
|F(n_j)|^{1/n_j}
\le
\left(\frac\pi8\right)^{1/n_j}e^{-n_j}
\longrightarrow0,
\tag{24}
\]

which proves `(4)`. In AF-246 notation, this example has

\[
\tau_F(S)=+\infty
\tag{25}
\]

despite periodic completeness and the absence of exact zeros.

### 4. The mode satisfies the elementary off-RH Li symmetry constraints

Let `theta=\pi\alpha`, so by `(17)`

\[
\frac\pi2<\theta<\frac{5\pi}{8}
\qquad\Longrightarrow\qquad
\cos\theta<0.
\tag{26}
\]

Fix any `0<r_0<1`, put `a=r_0e^{-i\theta}`, and define `\rho` by `(5)`. Writing

\[
D=|1-a|^2=1+r_0^2-2r_0\cos\theta,
\tag{27}
\]

one has

\[
\Re\rho
=\frac{1-r_0\cos\theta}{D}.
\tag{28}
\]

The inequality `\Re\rho>1/2` is equivalent to `1>r_0^2`, while `\Re\rho<1` is equivalent to `\cos\theta<r_0`. Both hold by construction. Thus `(6)` is exact.

For the reflected point,

\[
1-\frac1{1-\rho}
=\frac{\rho}{\rho-1}
=\left(1-\frac1\rho\right)^{-1}
=a^{-1},
\tag{29}
\]

and conjugation gives the other two identities in `(8)`.

AF-244 shows that, if an actual off-RH conjugate pair supplied the innermost Keiper poles `a,\bar a`, writing

\[
a=r_0\omega,
\qquad \omega=e^{-i\theta},
\tag{30}
\]

would produce normalized unit phases `\omega^{-1}=u` and `\bar\omega^{-1}=\bar u`, with coefficients equal to minus the zero multiplicities. For a simple pair the normalized dominant mode is exactly `(3)`.

This construction is **not** a claim that the Riemann xi function has such a zero quartet. It is a matched control showing that the strip location, conjugation, reflection symmetry, and integer-residue structure used in the standard Li asymptotic do not by themselves prevent the shrinking-target failure.

## Consequence for an off-RH root-rate detector

Suppose abstractly that a Li-type sequence has the AF-244 dominant decomposition

\[
a_n=q^nF(n)+r_n,
\qquad q=r_0^{-1}>1,
\qquad
\limsup_{n\to\infty}|r_n|^{1/n}<q,
\tag{31}
\]

with the two-mode `F` constructed above. Along `S`, the dominant term has restricted root rate zero by `(4)`, while the remainder has root rate strictly below `q`. Therefore

\[
\limsup_{\substack{n\to\infty\\n\in S}}|a_n|^{1/n}<q.
\tag{32}
\]

So the retained set can visit **every finite residue class infinitely often** and nevertheless fail to observe the true off-critical exponential scale.

The result does not weaken AF-244: a thick retained set contains arbitrarily long consecutive blocks and is uniformly observable for every fixed finite mode. Nor does it weaken AF-247: algebraic finite modes cannot realize `(23)`. It isolates the exact gap between them.

## Prior-art audit

The Keiper--Li conformal map and the off-RH exponentially growing oscillatory asymptotics are classical. André Voros, **“Sharpenings of Li's Criterion for the Riemann Hypothesis,”** *Mathematical Physics, Analysis and Geometry* 9 (2006), 53--63, DOI `10.1007/s11040-005-9002-8`, analyzes the transformed zero singularities and the non-tempered oscillatory alternative when RH fails. AF-244 already records this source and derives the finite dominant-mode decomposition used here.

Exceptional inhomogeneous approximation and shrinking-target questions for rotations belong to classical Diophantine approximation/dynamical-systems territory. As modern context, Dmitry Kleinbock and Nick Wadleigh, **“An inhomogeneous Dirichlet theorem via shrinking targets,”** *Compositio Mathematica* 155(7) (2019), 1402--1423, DOI `10.1112/S0010437X1900719X`, studies inhomogeneous approximation through shrinking-target methods. The nested rational construction above is elementary and deliberately exceptional; no novelty is claimed for the general possibility of Liouville-type superfast approximation.

AF-246 already established that arbitrary irrational phase modes can suffer exponential shrinking-target defects, and AF-247 established that algebraic finite modes cannot. The derived contribution of AF-248 is narrower: it intersects that classical exceptional approximation mechanism simultaneously with **periodic completeness** and with the exact two-mode conjugation/multiplicity shape of a dominant Li pair, showing that the obvious zeta symmetries do not close the algebraic-to-zeta gap.

A targeted search did not identify a standard Li-coefficient statement formulated as this periodic-complete/symmetry-admissible control, but no broad novelty claim is made. The mathematical value here is the falsification boundary it imposes on the current Arithmetic Fidelity route.

## Boundaries

**The constructed quartet is a symmetry-admissible control, not a zeta zero theorem.** Actual Riemann zeros satisfy much more than strip membership and functional-equation symmetry. The whole point is that some additional property would have to do the work.

**The result is output sampling only.** It says nothing about the source depth needed to form a retained Li coefficient. AF-238--AF-243's cancellation-coherent source-access obstruction remains independent.

**Periodic completeness is intentionally weak.** AF-244 thickness remains a universal sufficient condition for arbitrary fixed finite modes, while AF-245--AF-246 give stronger phase-space criteria. AF-248 only kills the hope that profinite residue coverage becomes sufficient once the elementary Li symmetries are imposed.

**The phase is necessarily outside the AF-247 algebraic category.** Since `(2)` holds while `(4)` fails, AF-247 itself implies that `u=e^{\pi i\alpha}` is not algebraic. No independent transcendence classification of the angle is required for the argument.

**No statement about the actual dominant zeta phases is proved.** In particular, the finding neither proves nor disproves any algebraicity, transcendence, irrationality measure, simultaneous Diophantine condition, or shrinking-target exponent for phases determined by Riemann zeros.

## Research consequence

The live output-side problem is now sharper. To justify a sparse Li sampling set weaker than the universal observability regimes already known, one must prove an arithmetic/analytic property of the **actual finite dominant zero-phase families** that forces

\[
\tau_F(S)=0
\tag{33}
\]

for every mode that can arise from innermost off-RH Keiper poles.

Functional-equation symmetry, conjugation, integer multiplicity, and periodic completeness are not such a property. A productive next theorem must instead control a quantitative Diophantine resource: irrationality/approximation exponents, simultaneous phase recurrence, a zero-separation consequence strong enough to bound trigonometric cancellation, or another source-specific mechanism that rules out exponential approach to the relevant zero loci.

Until such an input is proved, the safe positive statement remains the structural one already supplied by AF-244--AF-246: choose a sampling geometry whose observability is robust for the entire admissible phase class rather than assuming the zeta phases are automatically tame.