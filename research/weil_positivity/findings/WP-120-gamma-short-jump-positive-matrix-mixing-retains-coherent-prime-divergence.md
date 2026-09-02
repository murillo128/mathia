# WP-120 — Gamma short-jump positive matrix mixing retains coherent prime divergence

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + NONREFLECTION-MATRIX-GRAM + PRIME-CIRCLE-BRIDGE + SHARP-THRESHOLD + MATCHED-CONTROL + PRIOR-ART-AUDITED` for bounded jump-local positive matrix couplings of the canonical even/odd Gamma–Schoenberg channels.

`WP-119` shows that the two reflection-parity sectors of the Prime-Circle-selected Gamma Schoenberg space each retain the coherent prime divergence of `WP-118`. Its explicit scope boundary leaves open a positive matrix coupling between those sectors, including a coupling that breaks reflection equivariance and therefore can create negative even--odd cross terms.

That escape still fails for the natural class of **jump-local** positive matrix couplings. Put the even and odd Gamma increments into the real two-channel vector

\[
u_t(y)
:=
\begin{pmatrix}
\cos(ty)-1\\
\sin(ty)
\end{pmatrix},
\qquad y>0,
\tag{1}
\]

and let `M(y)` be any bounded measurable `2 x 2` real positive-semidefinite matrix weight with a finite nonzero short-jump limit

\[
M(y)\longrightarrow M_0\succeq0,
\qquad
M_0\ne0
\quad(y\downarrow0).
\tag{2}
\]

The resulting local matrix energy is independently nonnegative pointwise. Nevertheless, for the dyadic prime shell with exact matched amplitudes `(log p)/p^sigma`, its energy has the universal asymptotic

\[
\boxed{
\mathcal E_M(F_{X,\sigma})
=
A_{X,\sigma}^2
\left(
q(M_0)\log\log X+o(\log\log X)
\right),
}
\tag{3}
\]

where

\[
A_{X,\sigma}
:=
\sum_{X<p\le2X}\frac{\log p}{p^\sigma},
\qquad
q(M_0)
=
\frac32(M_0)_{11}
+\frac12(M_0)_{22}
>0.
\tag{4}
\]

Thus every such positive matrix coupling still diverges for `0<sigma<=1`, including the Weil value `sigma=1/2`; for `sigma>1` the global prime series converges absolutely in the corresponding Hilbert seminorm. The coherent threshold remains exactly `sigma=1`.

The mechanism is stronger than pairwise acuteness. A non-reflection-equivariant matrix is allowed to alter the signs of pairwise even--odd cross contributions; the proof does not assume pairwise acuteness. That freedom does not help on a dyadic shell: all frequencies `log p` differ from the common shell frequency `log X` by at most `log 2`, so after positive same-sign weighting the entire shell is, in the short-jump Hilbert geometry, a bounded perturbation of **one** high-frequency Gamma increment multiplied by the total shell mass. The singular Gamma density `dy/y` at short jumps then forces the `log log X` cost.

Consequently, a local positive parity/matrix repair can evade `WP-118`--`WP-119` only by becoming asymptotically blind or nonconvergent at the short-jump endpoint, or by leaving the jump-local matrix class altogether. This is a substantive restriction because the same short-jump singularity is precisely what produces the logarithmic high-frequency growth of the Riemann Gamma response.

This finding does **not** exclude frequency-dependent matrices acting on prime frequency rather than jump position, nonlocal integral intertwiners, singular endpoint quotients, cohomological primitive sectors, or a genuinely different finite--archimedean geometry. It does not prove Weil positivity or RH.

## 1. The Gamma Schoenberg space is a two-channel short-jump geometry

`WP-117` gives the exact Riemann Gamma Lévy density on the full line,

\[
\nu_\infty(dy)
=
\frac{e^{-|y|/2}}{1-e^{-2|y|}}\,dy,
\tag{5}
\]

and the Schoenberg increment

\[
\Phi(t)(y)=e^{ity}-1.
\tag{6}
\]

Because the measure is symmetric, restriction to the positive half-line identifies the real even/odd decomposition with the vector (1). The positive-half density is

\[
\boxed{
\rho(y)
:=
2\frac{e^{-y/2}}{1-e^{-2y}},
\qquad y>0.
}
\tag{7}
\]

Its decisive endpoint behavior is

\[
\boxed{
\rho(y)=\frac1y+O(1)
\qquad(y\downarrow0).
}
\tag{8}
\]

Moreover,

\[
\int_0^\infty |u_t(y)|^2\rho(y)\,dy
=
2H_\infty(t),
\tag{9}
\]

where `H_infty` is the positive Gamma symbol of `WP-117`, and

\[
H_\infty(t)=\log t+O(1)
\qquad(t\to+\infty).
\tag{10}
\]

Now grant the broad local matrix deformation (2). Define

\[
\boxed{
\mathcal E_M(g)
:=
\int_0^\infty
g(y)^TM(y)g(y)\rho(y)\,dy.
}
\tag{11}
\]

Since `M(y)` is positive semidefinite almost everywhere,

\[
\boxed{
\mathcal E_M(g)\ge0
}
\tag{12}
\]

for every vector-valued `g` in the form domain. This sign is independent of zeta zeros, RH, or the desired Weil functional. Constant diagonal `M` recovers the reflection-equivariant positive block weights treated in `WP-119`; constant off-diagonal `M` already allows fixed reflection-breaking parity mixing, and variable `M(y)` allows a bounded local deformation along the Gamma jump coordinate.

The hypothesis `M_0 != 0` is the precise nondegeneracy condition tested below. No lower bound `M_0 >= cI` is assumed: rank-one endpoint matrices are allowed.

## 2. Every nonzero short-jump matrix has a positive logarithmic coefficient

First freeze the frequency at `t=L`. For a constant symmetric matrix

\[
M_0=
\begin{pmatrix}
a&c\\
c&b
\end{pmatrix},
\tag{13}
\]

the periodic scalar function

\[
f_{M_0}(z)
:=
u_1(z)^TM_0u_1(z)
\tag{14}
\]

has period `2pi`. Its mean is exact:

\[
\begin{aligned}
\frac1{2\pi}\int_0^{2\pi}(\cos z-1)^2\,dz&=\frac32,\\
\frac1{2\pi}\int_0^{2\pi}\sin^2z\,dz&=\frac12,\\
\frac1{2\pi}\int_0^{2\pi}(\cos z-1)\sin z\,dz&=0.
\end{aligned}
\tag{15}
\]

Hence

\[
\boxed{
\langle f_{M_0}\rangle
=
q(M_0)
=
\frac{3a+b}{2}.
}
\tag{16}
\]

If `M_0` is positive semidefinite and nonzero, then `a,b>=0`, and `a=b=0` would force `c=0`. Therefore

\[
\boxed{
M_0\succeq0,\ M_0\ne0
\quad\Longrightarrow\quad
q(M_0)>0.
}
\tag{17}
\]

A periodic function with mean `q` obeys the elementary logarithmic Cesàro asymptotic

\[
\int_1^R\frac{f(z)}{z}\,dz
=
q\log R+O(1)
\tag{18}
\]

when its zero-mean part is a finite trigonometric polynomial; the oscillatory terms have bounded sine/cosine-integral primitives. Applying this to (14), using (8), boundedness of `M`, and the convergence `M(y)->M_0`, gives

\[
\boxed{
\mathcal E_M(u_L)
=
q(M_0)\log L+o(\log L).
}
\tag{19}
\]

For completeness, the endpoint replacement is robust. On a sufficiently small fixed interval,

\[
M(y)=M_0+o(1),
\qquad
\rho(y)=y^{-1}+O(1),
\tag{20}
\]

and `u_L` is uniformly bounded. The `o(1)` matrix error contributes `o(log L)` by splitting first at a fixed small endpoint and then letting that endpoint shrink. The `O(1)` density error contributes only `O(1)`. Outside any fixed small endpoint interval, the Gamma density is integrable and the contribution is `O(1)`. Thus the logarithm in (19) is forced entirely by the short-jump singularity.

Equation (19) also explains why a fixed off-diagonal parity coupling cannot cancel the leading divergence: its coefficient `c` disappears from the logarithmic mean. The even--odd mixed trigonometric term has zero average, while the two diagonal means are strictly positive.

## 3. A dyadic prime shell collapses to one high-frequency increment

Fix

\[
L:=\log X,
\qquad
d:=\log2,
\tag{21}
\]

and for `X<p<=2X` write

\[
t_p:=\log p=L+\delta_p,
\qquad
0<\delta_p\le d.
\tag{22}
\]

For `sigma>0`, set

\[
a_{p,\sigma}:=\frac{\log p}{p^\sigma}>0,
\qquad
A_{X,\sigma}:=\sum_{X<p\le2X}a_{p,\sigma},
\tag{23}
\]

and form the coherent shell vector

\[
\boxed{
F_{X,\sigma}(y)
:=
\sum_{X<p\le2X}
a_{p,\sigma}u_{t_p}(y).
}
\tag{24}
\]

Normalize by the positive shell mass:

\[
\overline u_{X,\sigma}(y)
:=
\frac{F_{X,\sigma}(y)}{A_{X,\sigma}}.
\tag{25}
\]

The key estimate is deterministic and uses no number theory. Since

\[
\left\|
\frac{\partial}{\partial t}u_t(y)
\right\|
=
y,
\tag{26}
\]

the mean-value theorem and positivity of the weights imply

\[
\boxed{
\|\overline u_{X,\sigma}(y)-u_L(y)\|
\le d\,y
\qquad(y>0).
}
\tag{27}
\]

Thus the entire prime shell is geometrically indistinguishable, to bounded error in the short-jump form, from one frequency `L`.

Indeed, let

\[
r_X:=\overline u_{X,\sigma}-u_L.
\tag{28}
\]

By (27), boundedness of `M`, the endpoint estimate `rho(y)=O(1/y)` near zero, and exponential decay of `rho` at infinity,

\[
\int_0^\infty r_X(y)^TM(y)r_X(y)\rho(y)\,dy
=O(1).
\tag{29}
\]

The mixed term is also uniformly bounded. Use

\[
\|u_L(y)\|
\ll \min(Ly,1),
\tag{30}
\]

split at `y=1/L`, and combine (27) with (8); this gives

\[
\int_0^\infty
\bigl|u_L(y)^TM(y)r_X(y)\bigr|
\rho(y)\,dy
=O(1).
\tag{31}
\]

Therefore

\[
\boxed{
\mathcal E_M(\overline u_{X,\sigma})
=
\mathcal E_M(u_L)+O(1),
}
\tag{32}
\]

uniformly in the positive shell weights. Combining (19), (21), (25), and (32),

\[
\begin{aligned}
\mathcal E_M(F_{X,\sigma})
&=
A_{X,\sigma}^2
\mathcal E_M(\overline u_{X,\sigma})\\
&=
\boxed{
A_{X,\sigma}^2
\left(
q(M_0)\log\log X+o(\log\log X)
\right).
}
\end{aligned}
\tag{33}
\]

This proves the announced asymptotic (3).

The argument does **not** require the pairwise matrix-weighted Gram kernel to be acute. The matrix-weighted pairwise kernel is not assumed positive entrywise. On a multiplicative dyadic shell, however, the logarithmic frequencies are an additive `O(1)` cluster around `L`, while the Gamma endpoint sees the common frequency on an expanding logarithmic range. Same-sign arithmetic amplitudes therefore coalesce before the final positive norm.

## 4. The coherent threshold remains exactly sigma equals one

The prime number theorem with partial summation gives

\[
A_{X,\sigma}
\asymp_\sigma
X^{1-\sigma}
\qquad(0<\sigma<1),
\tag{34}
\]

and at the endpoint

\[
\boxed{
A_{X,1}
=
\sum_{X<p\le2X}\frac{\log p}{p}
\longrightarrow\log2.
}
\tag{35}
\]

Since `q(M_0)>0`, equation (33) yields

\[
\boxed{
\mathcal E_M(F_{X,\sigma})
\longrightarrow+\infty
\qquad(0<\sigma\le1).
}
\tag{36}
\]

At `sigma=1` the divergence is already asymptotic to a positive constant times `log log X`; below `1` it is amplified by the polynomial shell mass.

This rules out convergence of the global coherent prime series for every `sigma<=1`: convergence in the Hilbert/seminorm completion would force the norm of every dyadic tail block to tend to zero, whereas (36) makes those block norms unbounded.

The opposite direction is a matched control. From boundedness of `M` and (9)--(10),

\[
\mathcal E_M(u_{\log p})^{1/2}
\ll
\sqrt{\log\log p}.
\tag{37}
\]

Therefore, for every `sigma>1`,

\[
\sum_p
\frac{\log p}{p^\sigma}
\mathcal E_M(u_{\log p})^{1/2}
<\infty,
\tag{38}
\]

so the coherent series converges absolutely in the form seminorm. Hence, for every bounded local positive matrix deformation satisfying (2),

\[
\boxed{
\sum_p
\frac{\log p}{p^\sigma}u_{\log p}
\text{ converges in }\mathcal E_M
\iff
\sigma>1.
}
\tag{39}
\]

The exact same threshold found in `WP-118` and `WP-119` survives fixed off-diagonal parity mixing and, more generally, every bounded short-jump-continuous local positive matrix weight with nonzero endpoint response.

## 5. What a surviving matrix mechanism would have to change

The theorem isolates the endpoint responsible for the failure. If a bounded jump-local positive matrix weight has a nonzero limit at `y=0`, its logarithmic coefficient is the strictly positive number (16). Therefore no such deformation can regularize the exact critical prime amplitudes.

A jump-local positive weight can escape the theorem only by violating the nondegenerate endpoint hypothesis — for example by tending to zero, oscillating without a limiting endpoint geometry, or otherwise suppressing the short-jump channel. But that is not a harmless reweighting of the canonical Gamma geometry: equations (8) and (19) show that the short-jump `dy/y` sector is exactly the source of the `log t` high-frequency behavior of `H_infty`. Any successful endpoint-degenerate proposal must therefore re-derive why the altered form still represents the required archimedean Gamma contribution rather than merely discarding the part that causes the obstruction.

Other genuine escapes remain outside the result:

1. a matrix depending on the **prime/frequency variable** rather than only on the local jump coordinate;
2. a nonlocal integral operator intertwining different jump scales;
3. an unbounded or singular endpoint construction with a separately proved closed positive form;
4. a quotient/compression or primitive cohomological sector formed before the Gamma norm;
5. a finite--archimedean geometry not represented by a local matrix deformation of the Schoenberg jump space.

These are real scope boundaries, not invitations to insert a cancelling phase by hand. Any survivor must still derive its sign independently and match the finite-prime, Gamma, and polar terms of the Weil explicit formula in one canonical architecture.

## 6. Matched controls and falsification surface

The harmonic part of the argument is not arithmetic-specific. Replace the primes in one dyadic shell by any finite family of positive frequencies contained in `[L,L+d]` with positive coefficients of total mass `A_L`. Equations (26)--(33) give

\[
\mathcal E_M\!\left(\sum_j a_j u_{t_j}\right)
=
A_L^2
\left(
q(M_0)\log L+o(\log L)
\right).
\tag{40}
\]

Primality enters only when the prime number theorem evaluates the shell mass in (34)--(35). Thus the matrix obstruction is a generic short-jump/coherent-cluster mechanism, not hidden evidence for RH.

The finding is falsified if any of the following fails:

1. the positive-half Gamma density (7) has endpoint coefficient different from `1/y`;
2. the periodic mean in (15)--(16) is not `(3a+b)/2`;
3. there exists a nonzero `M_0>=0` for which that mean vanishes;
4. the shell approximation (27) fails for frequencies in `[L,L+log 2]`;
5. the errors in (29)--(32) can grow at logarithmic order despite bounded `M`;
6. the PNT shell mass in (35) tends to zero;
7. a convergent Hilbert series can have dyadic tail blocks whose norms diverge.

Items 1--5 are direct analytic identities/estimates; item 6 is the classical PNT with partial summation; item 7 is a basic necessary condition for convergence. No numerical evidence, zeta zero data, or RH assumption is load-bearing.

## 7. Prior-art and novelty audit

No novelty is claimed for matrix-valued positive kernels, Schoenberg theory, logarithmic trigonometric integrals, the sine/cosine integral asymptotics, or the prime number theorem.

The directed matrix-valued audit found the established multivariate Schoenberg/variogram literature, including Christopher Dörr and Martin Schlather, *Characterization theorems for pseudo cross-variograms*, Journal of Applied Probability **60** (2023), no. 4, DOI `10.1017/jpr.2022.133`, and V. P. Zastavnyi, *Analog of Schoenberg's Theorem for a-Conditionally Negative Definite Matrix-Valued Kernels*, Mathematical Notes **114** (2023), 66--76, DOI `10.1134/S0001434623070064`. Those works address matrix-valued positive/conditionally negative-definite kernel structure; they do not identify the Mathia-specific Gamma short-jump endpoint with the critical same-sign prime-shell summability problem.

The logarithmic coefficient in (19) is classical harmonic analysis: after scaling, it is the mean of a finite trigonometric polynomial against `dz/z`, with the oscillatory remainders controlled by the standard sine/cosine integrals. NIST DLMF Chapter 6, especially §§6.7 and 6.12, is a convenient reference for those integral representations and asymptotics.

The Mathia-specific durable content is therefore the exact composition:

\[
\boxed{
\text{Prime-Circle }q=2\text{ Gamma selector}
\to
\text{Gamma }dy/y\text{ short-jump endpoint}
\to
\text{arbitrary bounded local PSD parity matrix}
\to
\text{dyadic prime-frequency clustering}
\to
\text{unavoidable }A_X^2\log\log X\text{ energy}.
}
\tag{41}
\]

This is a strict extension of `WP-119`: it no longer requires reflection equivariance or positive pairwise cross-prime Gram entries.

## Research consequence

`WP-118` showed that the raw shared Gamma Schoenberg space is too coherently positive. `WP-119` showed that each canonical reflection parity remains too coherent. The present result closes the next local matrix escape: **even allowing positive off-diagonal parity mixing, including bounded jump-dependent mixing that breaks reflection symmetry, does not alter the coherent threshold as long as the short-jump geometry remains nondegenerate.**

The obstruction is now localized to the same feature that carries the archimedean logarithmic scale. The Gamma jump density behaves as `dy/y`; a dyadic prime shell has logarithmic frequencies packed into a bounded interval; and every nonzero local PSD endpoint matrix assigns a strictly positive mean-square cost to the resulting high-frequency two-channel oscillation. At the critical prime amplitudes this produces divergent shell energy before any polar counterterm or Weil autocorrelation is assembled.

A surviving Mathia-native route must therefore do more than choose a better fixed grading or positive local matrix. It must alter the endpoint architecture nonlocally or frequency-dependently, pass to a genuinely new quotient/cohomological sector before positivity, or discover a different geometric object whose independent sign theorem assembles the finite and archimedean terms without paying this short-jump coherent cost.
