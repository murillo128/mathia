# WP-128 — Gamma power warps have an exact Markov-versus-superpolynomial cutoff dichotomy

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + GAMMA-POWER-WARPS + CND-RIGIDITY + MARKOV-VS-CUTOFF-DICHOTOMY + FINITE-BLOCK-MATCHED-CONTROL + PRIOR-ART-CLASSICALIZATION`.

`WP-117` identifies the Prime-Circle-selected Riemann Gamma variation

\[
H_\infty(t)
=
\operatorname{Re}\psi\!\left(\frac14+\frac{it}{2}\right)
-
\psi\!\left(\frac14\right)
\tag{1}
\]

as an exact continuous conditionally negative-definite (CND) symbol and hence as the generator of a symmetric Lévy/Markov Dirichlet form. `WP-126` shows that every fixed positive spectral multiplier with a polynomial lower tail has infinite cylindrical cost on the critical finite-block prime-torus completions. `WP-127` then proves that Bernstein subordination and positive heat-scale mixing cannot sharpen the logarithmic Gamma generator enough to escape that theorem, while leaving the explicit non-Bernstein control `H_\infty^2` as a superpolynomially damped spectral possibility.

There is a sharper boundary inside the most canonical scalar warp family. For

\[
q_\alpha(t):=H_\infty(t)^\alpha,
\qquad \alpha>0,
\tag{2}
\]

and its heat-dissipation multiplier

\[
w_{\alpha,\tau}(t)
:=q_\alpha(t)e^{-\tau q_\alpha(t)},
\qquad \tau>0,
\tag{3}
\]

one has an exact phase transition at `alpha=1`:

\[
\boxed{
0<\alpha\le1
\Longrightarrow
q_\alpha\text{ is CND/Markov, but }w_{\alpha,\tau}
\text{ has at-best polynomial decay};
}
\tag{4}
\]

whereas

\[
\boxed{
\alpha>1
\Longrightarrow
w_{\alpha,\tau}\text{ has superpolynomial decay, but }
q_\alpha\text{ is not CND.}
}
\tag{5}
\]

Thus **no positive power warp of the canonical Gamma symbol simultaneously preserves the inherited Lévy/Markov sign theorem and crosses the superpolynomial high-frequency boundary required to evade `WP-126`**.

The obstruction is local and stronger than merely observing that `s^alpha` ceases to be a Bernstein function for `alpha>1`. The Gamma symbol has a nonzero quadratic germ at the origin, while every nonzero continuous even CND symbol on `R` is forbidden from vanishing faster than quadratically. For the power family this gives an elementary three-point CND violation at arbitrarily small scale.

This finding does **not** rule out arbitrary pointwise-positive operator multipliers such as `H_\infty^2 e^{-\tau H_\infty^2}`. It says that once such a warp crosses the power threshold, its sign no longer comes from the canonical Gamma Lévy/Dirichlet geometry. A surviving route must therefore derive the warp from some different Mathia-native positive theorem, or use a more subtle warp that stays linear at the Gamma origin while becoming superlinear at large Gamma energy, or leave scalar functional calculus altogether.

## 1. The canonical Gamma symbol has a strictly quadratic germ

`WP-117` gives the exact symmetric Lévy representation

\[
H_\infty(t)
=
\int_{\mathbb R}
(1-\cos ty)\,\nu_\infty(dy),
\tag{6}
\]

with

\[
\nu_\infty(dy)
=
\frac{e^{-|y|/2}}{1-e^{-2|y|}}\,dy.
\tag{7}
\]

Near zero the density is asymptotic to `1/(2|y|)`, while at infinity it decays exponentially. Therefore

\[
0<\int_{\mathbb R}y^2\,\nu_\infty(dy)<\infty.
\tag{8}
\]

Using `1-cos u <= u^2/2`, dominated convergence in (6) gives

\[
\boxed{
\frac{H_\infty(t)}{t^2}
\longrightarrow
c_\infty
:=
\frac12\int_{\mathbb R}y^2\,\nu_\infty(dy)
>0
}
\qquad(t\to0).
\tag{9}
\]

Equivalently, from the ordinary polygamma expansion,

\[
c_\infty
=-\frac18\psi^{(2)}\!\left(\frac14\right)>0.
\tag{10}
\]

Hence

\[
\boxed{
H_\infty(t)=c_\infty t^2+o(t^2).
}
\tag{11}
\]

This local scale is forced by the same positive Gamma jump measure that proves `WP-117`; no zeta-zero data or fitted cutoff enters.

## 2. Nonzero CND symbols cannot have superquadratic contact with zero

Let `q:R->R_+` be continuous, even, CND, and satisfy `q(0)=0`. The classical symmetric Lévy--Khintchine representation gives

\[
q(t)
=
a t^2
+
\int_{\mathbb R\setminus\{0\}}
(1-\cos tx)\,\nu(dx),
\qquad a\ge0,
\tag{12}
\]

where `nu` is a Lévy measure.

Divide by `t^2`. Since the integrand is nonnegative, Fatou's lemma yields

\[
\begin{aligned}
\liminf_{t\to0}\frac{q(t)}{t^2}
&\ge
 a
+
\int
\liminf_{t\to0}
\frac{1-\cos(tx)}{t^2}\,\nu(dx)\\
&=
\boxed{
a+\frac12\int x^2\,\nu(dx).}
\end{aligned}
\tag{13}
\]

The last quantity may be infinite. If `q` is nonzero, then either `a>0` or `nu` is nonzero, and because the Lévy measure lives off the origin,

\[
a+\frac12\int x^2\,\nu(dx)>0.
\tag{14}
\]

Therefore

\[
\boxed{
q\not\equiv0\text{ and CND}
\quad\Longrightarrow\quad
q(t)\ne o(t^2)\text{ as }t\to0.
}
\tag{15}
\]

This is a direct classical consequence of Lévy--Khintchine theory, not a new theorem claim.

Combining (11) and (15) gives a useful Mathia-specific composition obstruction. If a nonnegative scalar warp `Phi` obeys

\[
\Phi(0)=0,
\qquad
\Phi(s)=o(s)
\quad(s\downarrow0),
\tag{16}
\]

and `Phi(H_\infty)` is not identically zero, then

\[
\Phi(H_\infty(t))=o(t^2),
\tag{17}
\]

so

\[
\boxed{
\Phi(H_\infty)\text{ cannot be CND.}
}
\tag{18}
\]

Thus every warp that is genuinely superlinear at the **Gamma origin** destroys the fixed Gamma Markov geometry, independently of its behavior at high frequency.

## 3. Power warps have an elementary finite CND witness

For the power family (2), equation (11) gives

\[
q_\alpha(t)
=
c_\infty^\alpha |t|^{2\alpha}(1+o(1)).
\tag{19}
\]

When `alpha>1`, (15) already proves that `q_alpha` is not CND. There is also a finite three-point witness that makes the failure directly auditable.

Take the points

\[
x_1=-h,
\qquad x_2=0,
\qquad x_3=h,
\tag{20}
\]

with coefficients

\[
(c_1,c_2,c_3)=(1,-2,1),
\qquad
c_1+c_2+c_3=0.
\tag{21}
\]

For an even function with `q(0)=0`, the CND inequality requires

\[
\sum_{i,j=1}^3c_ic_jq(x_i-x_j)
=
2\bigl(q(2h)-4q(h)\bigr)
\le0.
\tag{22}
\]

But (19) implies

\[
\frac{q_\alpha(2h)}{q_\alpha(h)}
\longrightarrow
2^{2\alpha}.
\tag{23}
\]

For every `alpha>1`, `2^{2alpha}>4`. Hence for all sufficiently small nonzero `h`,

\[
q_\alpha(2h)>4q_\alpha(h),
\tag{24}
\]

and the left side of (22) is strictly positive. Therefore

\[
\boxed{
H_\infty^\alpha\text{ is not conditionally negative definite for every }\alpha>1.
}
\tag{25}
\]

This is stronger than the universal statement that `s^alpha` is not Bernstein for `alpha>1`: it rejects the power composition for this **specific** Gamma symbol by an explicit finite metric test.

## 4. The Markov side of the threshold is exactly `0<alpha<=1`

For

\[
0<\alpha\le1,
\tag{26}
\]

the scalar function `s mapsto s^alpha` is a Bernstein function. The classical Bernstein/Schoenberg composition theorem therefore sends every CND symbol to a CND symbol. Since `H_infty` is CND by `WP-117`,

\[
\boxed{
H_\infty^\alpha\text{ is CND for every }0<\alpha\le1.
}
\tag{27}
\]

Consequently the power family has a sharp Markov threshold:

\[
\boxed{
H_\infty^\alpha\text{ is CND}
\quad\Longleftrightarrow\quad
0<\alpha\le1.
}
\tag{28}
\]

The forward implication for `alpha>1` is the new exact branch-local calculation (25); the preservation for `alpha<=1` is classical Bernstein functional calculus.

As a local sanity check, (23) gives a transparent geometric boundary. For `alpha<1`, the limiting doubling ratio is below `4`; at `alpha=1` it is exactly `4`, consistent with a genuine quadratic Lévy germ; and for `alpha>1` it crosses the three-point negative-type bound.

## 5. The high-frequency cutoff threshold is the opposite one

`WP-126` controls finite-block critical completions whenever a fixed nonnegative multiplier has a polynomial lower tail. `WP-117` gives

\[
H_\infty(t)=\log|t|+O(1)
\qquad(|t|\to\infty).
\tag{29}
\]

Therefore

\[
q_\alpha(t)
=(\log|t|)^\alpha(1+o(1)),
\tag{30}
\]

and

\[
\log w_{\alpha,\tau}(t)
=
\alpha\log\log|t|
-
\tau(\log|t|)^\alpha
+o\bigl((\log|t|)^\alpha\bigr).
\tag{31}
\]

Three regimes follow.

For `0<alpha<1`, the term `(log|t|)^alpha` is sublinear in `log|t|`, so `w_{alpha,tau}` decays **slower than every power**. In particular it is eventually bounded below by `c|t|^{-rho}` for some fixed `c,rho>0`.

For `alpha=1`,

\[
w_{1,\tau}(t)
\asymp
(\log|t|)|t|^{-\tau},
\tag{32}
\]

up to fixed multiplicative constants, so it has polynomial decay.

For `alpha>1`, for every `N>0`,

\[
\boxed{
|t|^Nw_{\alpha,\tau}(t)\longrightarrow0.
}
\tag{33}
\]

Thus the heat filter is superpolynomial exactly when the power warp has already left the CND/Markov class.

Combining (27), (25), and `WP-126` gives the promised dichotomy:

\[
\boxed{
\begin{array}{c|c|c}
\text{power }\alpha & H_\infty^\alpha\text{ Markov/CND?} &
H_\infty^\alpha e^{-\tau H_\infty^\alpha}\text{ tail}\\
\hline
0<\alpha<1 & \text{yes} & \text{subpolynomial}\\
\alpha=1 & \text{yes} & \text{polynomial}\\
\alpha>1 & \text{no} & \text{superpolynomial}
\end{array}
}
\tag{34}
\]

Hence every Markov-valid power is in the multiplier class killed by `WP-126`, while every power that escapes that high-support theorem has lost the independent Gamma Markov sign theorem.

## 6. Matched controls and limits of the obstruction

**Pointwise operator positivity survives.** For `alpha>1`, the multiplier `w_{alpha,tau}` remains a nonnegative scalar function. Therefore ordinary spectral functional calculus still produces a positive operator `w_{alpha,tau}(|X|)` whenever `X` is self-adjoint. Equation (25) does not contradict that. It says only that `H_infty^alpha` is not itself the symbol of a symmetric Lévy/Markov Dirichlet form, so the positivity can no longer be attributed to the canonical Gamma jump geometry of `WP-117`.

**The square control from `WP-127` is now classified exactly.** The explicit escape

\[
H_\infty(t)^2e^{-\tau H_\infty(t)^2}
\tag{35}
\]

really does cross the `WP-126` high-frequency boundary, but its generator `H_infty^2` violates CND already on the infinitesimal three-point configuration (20). It is therefore an additional positive spectral choice, not a sharper Gamma Markov energy.

**Linear-at-origin, superlinear-at-infinity warps remain open.** The present local theorem deliberately does not cover, for example,

\[
\Phi(s)=s+s^2.
\tag{36}
\]

Such a warp satisfies `Phi(H_infty(t))~H_infty(t)` at the origin, so (15) does not reject it, while its large-`s` growth could generate a superpolynomial heat cutoff. `Phi` is not Bernstein and therefore has no universal subordination theorem, but it is not proved here that the specific composition `Phi(H_infty)` fails CND. This is the precise scalar-functional-calculus boundary left by the finding.

**Finite-block hypothesis remains on the arithmetic side.** The implication from polynomial tail to divergent critical cost uses `WP-126` and therefore its finite-block correlated completion class. An arbitrary non-block completion may alter the high-support Fourier mass. The local CND obstruction (15), by contrast, is independent of the finite-prime architecture.

**No global Weil form has been produced.** Even a hypothetical CND warp surviving the remaining boundary would still need a canonical finite--archimedean coupling, the exact finite-prime and archimedean/polar terms, and a sign theorem for the assembled global form. No RH-equivalent kernel or zero data is used here.

## 7. Prior-art and novelty audit

The harmonic-analysis ingredients are classical. The Lévy--Khintchine representation of continuous negative-definite functions on locally compact abelian groups is standard; see Christian Berg and Gunnar Forst, *Potential Theory on Locally Compact Abelian Groups*, Springer, 1975, especially the chapters on negative-definite functions and convolution semigroups. René L. Schilling, *An Introduction to Lévy and Feller Processes*, Birkhäuser, 2017 (arXiv:`1603.00251`), is a modern Lévy-process reference already used by this research line.

The Bernstein-function composition theorem, the fact that `s^alpha` is Bernstein for `0<alpha<=1`, and Bochner subordination are standard; see René L. Schilling, Renming Song, and Zoran Vondraček, *Bernstein Functions: Theory and Applications*, 2nd ed., De Gruyter, 2012, DOI `10.1515/9783110269338`, particularly the chapters on positive/negative definite functions and subordination. `WP-127` already audits this functional-calculus boundary.

A targeted literature search over negative-definite functions, Bernstein composition, powers, Lévy--Khintchine small-frequency behavior, and digamma/Gamma complete-monotonicity literature found the standard abstract ingredients but no source treating the Mathia-specific combination

\[
\text{Prime-Circle-selected Riemann Gamma CND symbol}
+
\text{exact power-warp threshold}
+
\text{critical finite-block superpolynomial Fourier-mass boundary}.
\tag{37}
\]

No theorem-level historical novelty is claimed for the general CND lemma (15) or for Bernstein power preservation. The durable branch-local content is the exact incompatibility obtained after applying those classical facts to the intrinsically selected `H_infty` and matching the result against `WP-126`.

## Research consequence

`WP-127` left `H_infty^2` as the cleanest demonstration that a non-Markov superlinear transform can in principle create the superpolynomial spectral cutoff missing from all Bernstein-subordinate Gamma forms. The present finding shows that this is not a mild extension of the same geometry: the square, and indeed every power `alpha>1`, fails the defining negative-type inequality of the Gamma Markov category at arbitrarily small scale.

Within the canonical power family there is therefore no compromise parameter. Powers at or below one retain the independently derived Gamma Dirichlet sign but are too spectrally soft for the finite-block critical mass; powers above one become spectrally sharp enough but lose that sign mechanism.

The next admissible scalar escape is correspondingly narrow: a warp would have to remain effectively linear at the Gamma origin while becoming superlinear at large Gamma energy, and its CND/positive theorem would have to be proved for the specific Mathia-selected symbol rather than inherited from Bernstein subordination. Alternatively the construction must move to the more structural routes already identified by the branch: nonseparable finite--archimedean coupling, singular/frequency-dependent matrix geometry, a domain-changing quotient, or a genuinely higher-cohomological sign mechanism before final positivity is formed.