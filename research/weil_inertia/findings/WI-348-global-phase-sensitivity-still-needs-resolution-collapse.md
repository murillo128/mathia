# WI-348 — global-phase sensitivity still needs resolution collapse

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + CLASSICAL-MECHANISM + PRIOR-ART-AUDITED + STRUCTURAL-RIGIDITY + NON-RH`.

## Claim

WI-347 leaves essential sensitivity to the globally removable carrier phase as one possible escape from its projective-continuity obstruction. That escape is narrower than it first appears. At fixed bow aperture, **global-phase sensitivity by itself cannot produce extensive scale-preserving height rank if the normalized feature map has a `T`-uniform ordinary Hilbert-space modulus of continuity on the phase-saturated carrier set**.

Let `S_T` be finite with

\[
\log n\in[x_c-\Delta/2,x_c+\Delta/2],
\qquad n\in S_T,
\tag{1}
\]

and let

\[
w_U(n)=\frac{a_n n^{iU}}{\|a\|_2},
\qquad |U-U_c|\le H/2,
\qquad \|w_U\|=1.
\tag{2}
\]

Center the carrier by

\[
z_U:=e^{-iUx_c}w_U.
\tag{3}
\]

Define its phase saturation

\[
\mathcal K_T
:=
\{e^{i\phi}z_U:\phi\in\mathbf R,\ |U-U_c|\le H/2\}.
\tag{4}
\]

The physical carrier `w_U` belongs to `K_T` for every `U`. For `0<rho<=1`, `K_T` has a Hilbert-norm `rho`-net of cardinality at most

\[
\boxed{
N_{\rm in}(\rho)
:=
\left\lceil\frac{2\pi}{\rho}\right\rceil
\left(1+\left\lceil\frac{H\Delta}{2\rho}\right\rceil\right).
}
\tag{5}
\]

In particular, at natural bow/Gallagher aperture `H Delta<=1`,

\[
\boxed{N_{\rm in}(\rho)\le \frac{20}{\rho^2}.}
\tag{6}
\]

Now let `F_T` be any height-independent feature map defined on `K_T`, with nonzero outputs there, and normalize

\[
h_T(x):=\frac{F_T(x)}{\|F_T(x)\|}.
\tag{7}
\]

No phase equivariance, linearity, polynomial structure, differentiability, or analyticity is assumed. Fix `epsilon>0`. Suppose there is `rho_epsilon>0`, independent of `T`, such that

\[
\|x-y\|\le\rho_\varepsilon,
\quad x,y\in\mathcal K_T
\quad\Longrightarrow\quad
 d_{\mathbb P}(h_T(x),h_T(y))\le\varepsilon.
\tag{8}
\]

For arbitrary sampled heights `U_1,...,U_m`, let `G` be the Gram matrix of `h_T(w_{U_j})`. Then

\[
\boxed{
\sum_{j>N_{\rm in}(\min(1,\rho_\varepsilon))}
\lambda_j(G)
\le m\varepsilon^2.
}
\tag{9}
\]

Consequently, when `H Delta<=1`, every phase-sensitive feature family with a `T`-uniform ordinary continuity radius at fixed output tolerance still has bounded normalized Gram effective dimension. If for fixed `tau in (0,1)` the spectral-tail rank

\[
r_\tau(G)
:=
\min\left\{r:\sum_{j>r}\lambda_j(G)\le\tau m\right\}
\tag{10}
\]

tends to infinity, then any ordinary continuity radius at output tolerance `sqrt(tau)` must collapse. More quantitatively, once `r_tau(G)>20`,

\[
\boxed{
\rho_{\sqrt\tau}
\le
\sqrt{\frac{20}{r_\tau(G)}}.
}
\tag{11}
\]

Thus the nonprojective escape listed in WI-347 cannot be realized merely by a smooth dependence on absolute carrier phase. It must pay a growing source-resolution cost (or lose transmission), just as the projective routes do. The cost is weaker here, `rho=O(r^{-1/2})` rather than WI-347's projective `O(r^{-1})`, because the phase-saturated source set is a two-parameter cylinder rather than a one-parameter projective arc.

## 1. The raw phase-saturated carrier has bounded metric entropy

For `n in S_T`, put

\[
\xi_n:=\log n-x_c,
\qquad |\xi_n|\le\Delta/2.
\tag{12}
\]

Then

\[
z_U(n)=\frac{a_n}{\|a\|_2}e^{iU\xi_n}.
\tag{13}
\]

Using `|e^{it}-1|<=|t|`,

\[
\begin{aligned}
\|z_U-z_V\|^2
&=
\sum_n\frac{|a_n|^2}{\|a\|_2^2}
\left|e^{i(U-V)\xi_n}-1\right|^2\\
&\le
|U-V|^2
\sum_n\frac{|a_n|^2}{\|a\|_2^2}\xi_n^2\\
&\le
\frac{\Delta^2}{4}|U-V|^2.
\end{aligned}
\tag{14}
\]

Hence

\[
\boxed{\|z_U-z_V\|\le\frac\Delta2|U-V|.}
\tag{15}
\]

Take `M_phi=ceil(2 pi/rho)` equally spaced phases on the unit circle. Every phase lies within angular distance at most `pi/M_phi<=rho/2` of one mesh phase, and therefore within chordal distance at most `rho/2`.

Next choose

\[
M_U:=1+\left\lceil\frac{H\Delta}{2\rho}\right\rceil
\tag{16}
\]

mesh points across the height interval. Their maximum gap is at most `2 rho/Delta`, so every `U` is within `rho/Delta` of one mesh point. Equation (15) then gives centered-carrier error at most `rho/2`.

For any `e^{i phi}z_U in K_T`, choose both nearest mesh coordinates. The triangle inequality gives input error at most `rho`. This proves (5). If `H Delta<=1` and `rho<=1`, then

\[
\left\lceil\frac{2\pi}{\rho}\right\rceil
\le \frac{2\pi+1}{\rho}<\frac8\rho,
\tag{17}
\]

while

\[
1+\left\lceil\frac{H\Delta}{2\rho}\right\rceil
\le 2+\frac1{2\rho}
\le\frac{5}{2\rho}.
\tag{18}
\]

Multiplication gives (6).

The key point is that the rapid physical phase `e^{iUx_c}` may wind around the circle arbitrarily many times as height grows, but repeated winding does not create new fixed-resolution source information. The phase coordinate lives on one compact circle, while the centered carrier traverses a path of total Hilbert length at most `H Delta/2`. At `H Delta<=1` their product has a `T`-uniform fixed-resolution cover.

## 2. A bounded input cover forces a bounded Gram tail after every uniformly continuous feature

Let `x_1,...,x_N` be the input net from (5), with `N=N_in(rho_epsilon)` after capping the radius at one. By (8), every physical normalized output `h_T(w_U)` is projectively within `epsilon` of one of the `h_T(x_k)`.

Let

\[
V_\varepsilon:=\operatorname{span}\{h_T(x_1),\ldots,h_T(x_N)\}.
\tag{19}
\]

Projective closeness means that after multiplying the chosen center by a scalar phase, which does not leave `V_epsilon`,

\[
\operatorname{dist}(h_T(w_U),V_\varepsilon)\le\varepsilon.
\tag{20}
\]

For sampled outputs `h_j=h_T(w_{U_j})`, define the covariance operator

\[
C:=\sum_{j=1}^m h_jh_j^*.
\tag{21}
\]

If `P` is orthogonal projection onto `V_epsilon`, then

\[
\operatorname{tr}((I-P)C)
=
\sum_{j=1}^m\|(I-P)h_j\|^2
\le m\varepsilon^2.
\tag{22}
\]

The nonzero eigenvalues of `C` are those of the Gram matrix `G`. Ky Fan/min--max therefore gives (9).

For `epsilon=sqrt(tau)`, equation (9) says `r_tau(G)<=N_in(rho_sqrt(tau))`. Under `H Delta<=1`, (6) gives

\[
r_\tau(G)\le\frac{20}{\rho_{\sqrt\tau}^2}
\tag{23}
\]

whenever the useful radius is at most one. If a radius larger than one were admissible, radius one would be admissible and (6) would already give `r_tau<=20`. Thus `r_tau>20` forces (11).

## 3. Lipschitz features pay an explicit sensitivity/transmission cost

A useful raw-feature specialization makes the escape cost explicit. Suppose on `K_T`

\[
\|F_T(x)-F_T(y)\|\le L\|x-y\|,
\qquad
\|F_T(x)\|\ge\mu>0,
\tag{24}
\]

with `L` and `mu` independent of `T`. For nonzero vectors,

\[
\left\|
\frac{x}{\|x\|}-\frac{y}{\|y\|}
\right\|
\le
\frac{2\|x-y\|}{\min(\|x\|,\|y\|)}.
\tag{25}
\]

Therefore

\[
\|h_T(x)-h_T(y)\|
\le\frac{2L}{\mu}\|x-y\|.
\tag{26}
\]

At `H Delta<=1`, taking output tolerance `sqrt(tau)` yields

\[
\boxed{
r_\tau(G)
\le
20\max\left\{1,\frac{4L^2}{\mu^2\tau}\right\}.
}
\tag{27}
\]

In particular, if `r_tau(G)>20`,

\[
\boxed{
\frac{L}{\mu}
\ge
\sqrt{\frac{\tau\,r_\tau(G)}{80}}.
}
\tag{28}
\]

Thus a smooth phase-sensitive feature can evade fixed-rank compression only by becoming increasingly ill-conditioned: its ordinary source sensitivity relative to transmitted scale must diverge at least like the square root of the desired effective rank under this coarse two-dimensional cover.

This includes smooth feature maps that explicitly compare the carrier to a fixed phase reference, mix several `U(1)` charge sectors, or otherwise fail the projective-equivariance hypotheses discussed in WI-345--WI-347. It does not include a hard phase quantizer, a feature whose oscillation count grows with `T`, a map with `L/mu -> infinity`, explicit height-dependent feature injection, or a construction not controlled on the phase-saturated source set.

## 4. Relation to WI-195 and the live bow clue

WI-195 rewrites the localized source square exactly as the positive Gallagher/Fejer quantity

\[
\int
\left|\sum_{e^y<n\le e^{y+1/H}}b_n\right|^2dy,
\tag{29}
\]

and identifies the missing source theorem as a diagonal-scale `L^2` cancellation statement. WI-343--WI-347 then show that one fixed natural source aperture cannot manufacture an extensive portfolio of scale-preserving height directions through linear, fixed-degree, uniformly analytic, or uniformly projectively continuous feature processing.

WI-347 deliberately left absolute/global phase sensitivity outside its theorem because projective distance quotients that phase out. The present finding shows that **ordinary smooth access to that phase is still not enough**. Once the whole phase orbit is included, the raw source family has only bounded fixed-resolution metric entropy, and a uniformly continuous height-independent map cannot turn it into an extensive Gram tail.

This does not prove the signed `Lambda-Lambda^sharp` covariance requested by `CLUE-bow-distinguished-twist-offdiagonal-cancellation`, and it does not exclude a deliberately `T`-sensitive phase detector. Rather, it removes the interpretation that merely retaining absolute phase provides a cheap smooth escape from the fixed-aperture obstruction. A successful phase-based route must explain where its growing phase resolution comes from and how that sensitivity survives normalization and feeds the source-justified covariance sign.

## 5. Prior art and novelty boundary

The covering argument is classical metric entropy, not new approximation theory. Kolmogorov and Tikhomirov introduced `epsilon`-entropy/covering-number methods for compact metric sets:

- A. N. Kolmogorov and V. M. Tikhomirov, **epsilon-entropy and epsilon-capacity of sets in functional spaces**, *Uspekhi Mat. Nauk* 14:2 (1959), 3--86; English translation, *AMS Translations*, Series 2, 17 (1961), 277--364.

The broader approximation viewpoint is also standard; WI-347 already anchors Allan Pinkus, *n-Widths in Approximation Theory* (Springer, 1985), and Bernd Carl--Irmtraud Stephani, *Entropy, Compactness and the Approximation of Operators* (Cambridge, 1990).

The line-local novelty audit is decisive about the boundary. WI-343 already proves bounded approximation dimension for the raw one-window carrier. WI-345 treats finitely many mixed `U(1)` charge sectors through fixed-degree polynomial/tensor lifts. WI-347 removes representation assumptions for **projectively** uniformly continuous features but explicitly leaves essential global-phase sensitivity outside its hypotheses. The durable delta here is the phase-saturated product cover (5)--(6) and its consequence (9)--(11): even arbitrary nonprojective phase-sensitive features remain compressed when their ordinary normalized modulus is uniform. No external priority claim is made for the generic entropy argument.

## Research consequence

Refine the post-WI-347 frontier as follows: `global phase sensitivity` is not by itself a viable escape. At fixed natural aperture, a phase-sensitive source feature must also exhibit **ordinary resolution collapse**, vanishing transmission, explicit height dependence, growing aperture, or some other new structure. In the smooth/nonvanishing case the required conditioning cost is quantified by (28).

This strengthens the case for the accepted distinguished-twist clue. Generic feature enrichment now has to pay a measurable projective or ordinary resolution cost; the cleaner remaining route is still a source-specific arithmetic identity that forces the needed signed off-diagonal covariance directly rather than trying to manufacture extensive height rank from one fixed Gallagher aperture.