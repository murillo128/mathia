# NB-112 — zero-counting symmetry eliminates the one-zero multiplicity rescue

**Status:** `LITERATURE+DERIVED + SOURCE-SPECIFIC + TRUE-MULTIPLICITY + FULL-EARLY-CELL-BACKFILL + TARGET-AWARE-STATE-SUBSPACE + DECISIVE-NEGATIVE/ONE-ZERO-BRANCH`.

`NB-111` proves a uniform target-poorness theorem for a one-zero confluent/Jordan packet whenever its rank lies strictly below `(1/8) log G`, and leaves open a source-specific escape: perhaps a genuine off-critical zeta zero could have multiplicity large enough to cross that logarithmic window. The explicit zero-counting estimate of Bellotti--Wong closes that escape once one uses the functional-equation symmetry of an off-critical zero at the **same ordinate**.

Let

\[
\rho_j=\frac12+a_j+iG_j,
\qquad 0<a_j<\frac12,
\qquad G_j\to\infty,
\]

be genuine nontrivial zeros of `zeta`, and let

\[
d_j:=\operatorname{mult}(\rho_j).
\tag{1}
\]

Retain the terminal-band hypotheses and notation of `NB-111`:

\[
m_j=\lceil G_j\rceil,
\qquad R_j=m_jq_j,
\qquad 2a_j\log q_j\to L\in(0,\infty),
\tag{2}
\]

with fixed `r>=1`, derivative-state space

\[
S_j^{(d_j)}
=\operatorname{span}\{w_{0,j},\ldots,w_{d_j-1,j}\},
\qquad
e_j=\sum_{n=r}^{R_j-1}\phi_n,
\tag{3}
\]

and target fraction

\[
\delta_j^2
:=
\frac{\|P_{S_j^{(d_j)}}e_j\|_2^2}{\|e_j\|_2^2}.
\tag{4}
\]

Then

\[
\boxed{\delta_j\longrightarrow0.}
\tag{5}
\]

Thus the **entire derivative packet actually supplied by the true multiplicity of one off-critical zeta zero** is asymptotically target-poor after the full early-cell backfill of `NB-111`. Every smaller packet from that same zero is target-poor as well.

The conclusion is uniform in the horizontal location `a_j in (0,1/2)`. No simplicity hypothesis, RH assumption, zero-free region, or lower bound on the distance from the critical line is used.

## 1. An off-critical zero spends multiplicity twice in one zero-counting jump

Bellotti and Wong, with an appendix by Andrew Fiori in the accepted/journal version, prove that for every `T>=e`,

\[
\left|
N(T)-\frac{T}{2\pi}\log\frac{T}{2\pi e}
\right|
\le E(T),
\tag{6}
\]

where

\[
E(T)
:=0.10076\log T
+0.24460\log\log T
+8.08344,
\tag{7}
\]

and `N(T)` counts nontrivial zeros with multiplicity and ordinates in `(0,T]`.

Fix one off-critical zero

\[
\rho=\beta+i\gamma,
\qquad \beta>\frac12,
\qquad d=\operatorname{mult}(\rho).
\tag{8}
\]

The completed zeta functional equation and Schwarz symmetry send it to

\[
\rho^*=1-\overline\rho
=(1-\beta)+i\gamma.
\tag{9}
\]

Because `beta>1/2`, the two zeros are distinct. Both symmetries preserve order of vanishing, so `rho^*` has the same multiplicity `d`. Therefore the jump of `N` at the common ordinate `gamma`,

\[
J(\gamma):=N(\gamma)-N(\gamma^-),
\tag{10}
\]

satisfies

\[
J(\gamma)\ge 2d.
\tag{11}
\]

Write the continuous main term in `(6)` as

\[
M(T)=\frac{T}{2\pi}\log\frac{T}{2\pi e}.
\]

Since `M` is continuous, `(6)` at `T=gamma` and along `T\uparrow gamma` gives

\[
J(\gamma)
=\bigl(N(\gamma)-M(\gamma)\bigr)
 -\bigl(N(\gamma^-)-M(\gamma)\bigr)
\le 2E(\gamma).
\tag{12}
\]

Combining `(11)` and `(12)` cancels the factor two:

\[
\boxed{
\operatorname{mult}(\beta+i\gamma)
\le
0.10076\log\gamma
+0.24460\log\log\gamma
+8.08344
}
\tag{13}
\]

for every off-critical zero with `beta>1/2` and sufficiently large positive ordinate; in fact `(13)` applies whenever the Bellotti--Wong estimate applies.

Consequently,

\[
\frac{d}{\log\gamma}
\le 0.10076+o(1).
\tag{14}
\]

This is the source-specific multiplicity input that `NB-111` left open.

## 2. The zero-counting constant falls strictly inside the Laguerre window

The numerical comparison is strict:

\[
\frac18-0.10076
=0.02424>0.
\tag{15}
\]

Choose any fixed

\[
0<\varepsilon<0.02424.
\tag{16}
\]

By `(14)`, every sufficiently high off-critical zero satisfies

\[
d
\le
\left(\frac18-\varepsilon\right)\log\gamma.
\tag{17}
\]

For the sequence `(1)` this is exactly the uniform rank hypothesis in `NB-111`. Applying its target-aware theorem with `G_j=gamma_j` and the **full true multiplicity** `d_j` proves `(5)`.

The argument needs no estimate for `a_j`: the uniform `(1/8-epsilon) log G` consequence of `NB-111` was designed precisely to remove that dependence. The source input and the state-space input therefore meet without an additional horizontal-zero hypothesis.

## 3. Stress tests: the off-critical symmetry is load-bearing

The factor-of-two gain is not cosmetic. If one used only the zero-counting jump without the distinct same-ordinate partner `(9)`, then `(12)` would give merely

\[
d\le 2E(\gamma)
=(0.20152+o(1))\log\gamma,
\tag{18}
\]

and

\[
0.20152>\frac18.
\]

That estimate would **not** enter the `NB-111` window. Hence the closure of the branch comes specifically from combining the explicit zero-counting constant with the exact off-critical functional-equation pairing; neither input alone is sufficient at the present constants.

This also marks the critical-line boundary correctly. If `beta=1/2`, then `rho^*=rho`, so `(11)` need not contain `2d`; the present argument then falls back to `(18)` and does not control a critical-line multiplicity packet by `NB-111`. That is not a defect for the false-RH obstruction studied here: the one-zero rescue requiring elimination is an off-critical zero with `beta>1/2`.

A reusable threshold statement is therefore:

> Any bound `|N(T)-M(T)| <= c log T + o(log T)` with continuous `M`, together with same-ordinate off-critical symmetry, gives `mult(rho) <= c log gamma + o(log gamma)`. Any `c<1/8` closes the one-zero true-multiplicity escape through `NB-111`.

Bellotti--Wong supply `c=0.10076`.

## 4. Boundaries and prior-art position

The zero-counting estimate is external literature, and functional-equation/conjugation symmetry of zeta zeros is classical. No novelty is claimed for either ingredient or for the general fact that multiplicity matters in quantitative Nyman--Beurling bounds; Burnol's lower-bound work is an established neighboring boundary where zero multiplicities already enter explicitly.

The line-local derived content is the threshold bridge `(11)`--`(17)`: an off-critical zero pays its multiplicity twice in a single ordinate jump, which reduces the best current explicit zero-counting coefficient below the independently derived `NB-111` Laguerre target-poorness threshold. A targeted prior-art check did not locate this particular comparison as an existing Nyman--Beurling theorem, but the claim here is the mathematical implication, not a broad novelty assertion about zero multiplicity.

The result inherits the geometric hypotheses of `NB-111`, in particular the terminal-band regime `(2)` and fixed early endpoint `r`. It does **not** prove target-poorness for an arbitrary state construction outside that regime.

Most importantly, it says nothing comparable about a growing packet built from **several distinct zeros**. Zero counting controls the multiplicity of one ordinate pair; it does not prevent many distinct off-critical zeros from supplying a genuinely multi-center growing-rank state space.

## Consequence for the research line

The alternative left open by `NB-111` — that source-specific zeta multiplicity might cross the explicit one-zero logarithmic window — is now eliminated for every genuine off-critical zero. There is therefore no need to improve the `1/8` Laguerre constant merely to defeat the **one-zero true-multiplicity** rescue.

The surviving zero-state frontier is structurally different: it must use growing rank from several distinct zeros, or leave the terminal-band/full-backfill geometry to which `NB-111` applies. That redirects the next source-sensitive test away from ever-higher derivatives of one zero and toward multi-center target geometry.