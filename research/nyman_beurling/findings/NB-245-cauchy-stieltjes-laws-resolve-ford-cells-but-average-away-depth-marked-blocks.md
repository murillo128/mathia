# NB-245 — Cauchy Stieltjes laws resolve Ford cells but average away depth-marked blocks

**Date:** 2026-09-20  
**Status:** `FRESH-LITERATURE + EXACT-SCALE-AUDIT + REPRESENTATION/METHOD-BOUNDARY + DEPTH-MARKED-PAIR-ENERGY + NB-243-FRONTIER + SOURCE-ONLY`.

A fresh result of Najnudel and Nikeghbali, [*Cauchy laws for zeta logarithmic derivatives and stationary Stieltjes transforms*](https://arxiv.org/abs/2609.15862) (submitted 14 September 2026), is unusually close to the source-side object isolated in `NB-237` and `NB-243`: it studies Stieltjes transforms of zeta zeros and a normalized logarithmic derivative of `zeta` at a randomly selected height.

The first scale audit is encouraging. Their zero process is normalized at the mean-zero-spacing scale `1/log T`, which is **finer** than the Ford carrier scale `1/R`; the whole Ford block also lies far inside their stated symmetric Stieltjes truncation. So, unlike the clustering theorems audited in `NB-238` and `NB-244`, this result does not fail because its vertical resolution is too coarse.

The obstruction is different and more structural. The unconditional theorem first **projects away every horizontal coordinate `beta`**, and the logarithmic-derivative comparison retains horizontal information only through one global first moment. In addition, the theorem is a convergence-in-distribution statement for a height chosen uniformly from a long interval. Neither output controls the deterministic, near-one, depth-marked carrier pair energy required by `NB-243`.

There is an exact representation-level reason not to expect the Cauchy law itself to do so. The paper's finite/periodic input proves a Cauchy law under a uniform translation **conditionally on an arbitrary periodic atom configuration**. Hence a configuration may contain a perfectly carrier-coherent block and still have exactly the same normalized Cauchy Stieltjes law after random translation. The distributional law is therefore compatible, by construction, with the kind of exceptional deterministic block that the Ford argument must exclude.

The useful route consequence is narrower than a rejection of the paper's machinery: its local Hadamard factorization, truncation estimates, or stationary-measure technology may still be adaptable. What cannot close the current frontier is the stated projected/random-height Cauchy output by itself. A successful adaptation would have to keep the Ford depth mark and replace random-height distributional convergence by a deterministic or sufficiently uniform estimate for the carrier pair energy.

## 1. The fresh theorem and its native coordinate

Let `T` be the height parameter in Najnudel--Nikeghbali and write

\[
L_T:=\log T.
\tag{1}
\]

They choose `t_T` uniformly on `[T/L_T,T]` and attach to every nontrivial zero `rho=beta+i gamma` the projected ordinate

\[
u_{\rho,T}
:=
\frac{(\gamma-t_T)L_T}{2\pi}.
\tag{2}
\]

Their unconditional arithmetic statement is

\[
P_T
:=-\frac1\pi
\sum_{0<|u_{\rho,T}|\le L_T^2}
\frac{m(\rho)}{u_{\rho,T}}
\Longrightarrow
\operatorname{Cauchy}(0,1).
\tag{3}
\]

Crucially, equation (3) contains `gamma` and multiplicity but no `beta`: the zero set has been horizontally projected before the Stieltjes transform is formed.

They also define the horizontal first moment

\[
\mathcal H(T)
:=
\sum_{\substack{0<\gamma\le2T\\ \beta>1/2}}
 m(\rho)(\beta-1/2).
\tag{4}
\]

Under the additional assumption

\[
\mathcal H(T)=o(T),
\tag{5}
\]

they prove

\[
A_T
:=
\frac{2i}{L_T}
\frac{\zeta'}{\zeta}\!\left(\frac12+it_T\right)+i
\Longrightarrow
\operatorname{Cauchy}(0,1),
\tag{6}
\]

with the quantitative comparison

\[
d_{\rm BL}(\operatorname{Law}(A_T),\operatorname{Law}(P_T))
\le
C\sqrt{\frac{\mathcal H(T)}T}
+
\frac{C}{\log T}.
\tag{7}
\]

These are exactly the features relevant to the Ford audit: microscopic vertical information is retained, horizontal information is collapsed to an aggregate moment for the comparison, and the observation height is randomized.

## 2. Vertical resolution is not the missing ingredient

Return to the Ford variables stabilized in `NB-230`--`NB-244`:

\[
Q:=\log(10+|t|),
\qquad
R:=Q^{2/3}(\log Q)^{1/3},
\qquad
X:=YR,
\qquad
J:=\frac RH,
\tag{8}
\]

where `Y asymp 1` and

\[
1\ll J\le\log Q.
\tag{9}
\]

At comparable heights `T asymp t`,

\[
L_T=Q+o(Q).
\tag{10}
\]

One Ford carrier cell has vertical width

\[
\Delta_F\asymp\frac1X\asymp\frac1R.
\tag{11}
\]

In the coordinate (2), such a cell has width

\[
\Delta u_F
\asymp
\frac{Q}{R}
=
\left(\frac{Q}{\log Q}\right)^{1/3}
\longrightarrow\infty.
\tag{12}
\]

Thus the Najnudel--Nikeghbali microscopic coordinate is actually much finer than the Ford carrier: a single Ford cell contains a growing number of mean-spacing units.

The complete Ford window has width

\[
W_F:=\frac JR,
\tag{13}
\]

and hence occupies

\[
U_F
\asymp
\frac{JQ}{R}
\le
Q^{1/3}(\log Q)^{2/3}
=o(Q^2)
\tag{14}
\]

units in (2). Their truncation `|u|<=L_T^2` therefore contains the entire Ford block with enormous room to spare.

This distinguishes the present audit from `NB-238` and `NB-244`. The fresh theorem reaches a vertical resolution finer than we need. **The failure is not a scale-resolution failure.**

## 3. Horizontal projection deletes the Ford mark

The live energy from `NB-243` is

\[
|\mathcal R_J|^2
=
\frac{e^{-2r}}{J^2}
\sum_{j,k}
 b_{j,J}\overline{b_{k,J}}
 e^{iX(\gamma_j-\gamma_k)},
\tag{15}
\]

where the mark contains, among other bounded profile factors,

\[
 d_j:=X(1-\beta_j)-\log J,
\qquad
b_{j,J}\supset e^{-d_j}\chi(d_j).
\tag{16}
\]

Equation (3) cannot distinguish two zero configurations with the same projected ordinates and multiplicities but different `beta` coordinates. Such configurations can have the same `P_T` and radically different Ford energy because (16) can either retain or suppress the corresponding atoms.

The comparison theorem (6)--(7) does not restore this missing local information. Its entire off-critical input is the single global positive moment (4). That moment is suitable for proving that horizontal projection is harmless **on average for the normalized critical-line logarithmic derivative**; it is not a local depth selector near `beta=1`.

Indeed a zero in the critical Ford layer satisfies

\[
1-\beta
=
\frac{\log J+O(1)}X=o(1),
\tag{17}
\]

so

\[
\beta-\frac12
=
\frac12-o(1).
\tag{18}
\]

A coherent Ford packet with `M asymp J` such zeros contributes only `Theta(J)` to `mathcal H(T)`. Therefore condition (5) is compatible with any sparse family of dangerous packets whose total number of atoms below height `2T` is `o(T)`. In particular, it is compatible with an exceptional deterministic sequence of Ford blocks, while each selected block can still have the order-one residue constructed in `NB-231`.

So the horizontal condition needed for the Cauchy comparison is far too integrated to imply the depth-marked local estimate (15).

## 4. Random translation makes the Cauchy law configuration-blind

The strongest representation audit comes from the paper itself. Before treating zeta, Najnudel--Nikeghbali prove a periodic-measure identity. Let

\[
M
=
KB\sum_{j=1}^n w_j
\sum_{m\in\mathbb Z}
\delta_{B(m+\theta_j/\pi)},
\qquad
w_j\ge0,
\qquad
\sum_jw_j=1,
\tag{19}
\]

be an arbitrary nonzero positive `B`-periodic atomic measure. For a point `S` chosen uniformly from one period, its symmetric Stieltjes transform satisfies exactly

\[
\boxed{
\frac{F_M(S)}{\pi K}
\sim
\operatorname{Cauchy}(0,1),
}
\tag{20}
\]

**conditionally on the entire periodic atom configuration**. The proof is the weighted cotangent identity; no generic spacing or pair decorrelation is required.

This is an exact adversarial control for the intended inference. Choose the atoms inside one period so that one subblock is carrier coherent at the Ford frequency. The internal block can have order-one normalized carrier pair energy. Equation (20) remains exactly Cauchy after uniform translation because its law is independent of that internal arrangement.

Consequently,

\[
\boxed{
\text{Cauchy Stieltjes law under random translation}
\not\Rightarrow
\text{small deterministic carrier pair energy}.
}
\tag{21}
\]

This is stronger than merely observing that convergence in distribution is an average statement. At the abstract periodic level, the Cauchy law is deliberately universal across configurations. It therefore cannot, by itself, certify the intra-window decorrelation demanded by (15).

## 5. Random-height convergence also permits exceptional Ford blocks

For the actual zeta theorem, `t_T` is uniform on an interval of length comparable to `T`. A Ford window has length only

\[
W_F=\frac JR=o(1).
\tag{22}
\]

Hence even a sequence of completely bad deterministic Ford windows can occupy vanishing relative measure in the sampling interval. Convergence in distribution of `P_T` or `A_T` does not exclude them.

More generally, suppose a collection of bad windows below height `T` has total length `o(T)`. Altering the observable arbitrarily on their union is invisible to weak convergence under a uniform height sample. But the Nyman source problem does not sample `t`: its bound must survive the particular height selected by the Mellin/Ford construction. That quantifier difference is exactly the one already exposed for averaged pair correlation in `NB-232` and `NB-240`.

Thus the fresh theorem clears one concern -- vertical resolution -- but retains both live obstructions:

1. the critical Ford depth mark is not present in the projected statistic; and
2. random-height distributional convergence does not give deterministic control of the selected block.

These are logically independent. Fixing only one would still leave the other.

## 6. What remains reusable from the new paper

This finding is a boundary on the **stated Cauchy-law outputs**, not on the machinery of Najnudel--Nikeghbali. Several ingredients are structurally closer to the current frontier than the older clustering theorems:

- their local zero coordinate resolves scales finer than `1/R`;
- their Stieltjes-transform formalism is directly related to logarithmic derivatives, hence to the `NB-237` representation;
- their quantitative truncation and local-factorization estimates are designed to transfer between zero measures and `zeta'/zeta`.

A useful adaptation would therefore have to change the observable rather than merely sharpen the convergence rate. The target suggested by `NB-243` remains a **depth-marked, carrier-frequency two-point energy in the deterministic Ford window**,

\[
\frac1{J^2}
\sum_{j\ne k}
 b_{j,J}\overline{b_{k,J}}
 e^{iX(\gamma_j-\gamma_k)}
=o(1),
\tag{23}
\]

or an equivalent deterministic estimate for the local logarithmic-derivative representation.

The fresh paper suggests that Stieltjes/local-factorization technology may be a viable language for such a theorem. It does not supply the theorem because both the horizontal marking and the deterministic-window quantifier have been removed before the Cauchy limit is taken.

## 7. Prior-art and adversarial audit

The source statement used here is Theorem 1.1 and the periodic weighted-cotangent mechanism in Proposition 2.1/Theorem 2.2 of Joseph Najnudel and Ashkan Nikeghbali, *Cauchy laws for zeta logarithmic derivatives and stationary Stieltjes transforms*, arXiv:2609.15862v1 (submitted 14 September 2026). No claim is made that their Cauchy law is new to this line; it is fresh external prior art being tested against the current Ford frontier.

The derived scale comparison (12)--(14), the depth audit (17)--(18), and the inference boundary (21) are line-local consequences. The finding does **not** claim that actual zeta zeros contain carrier-coherent Ford packets, that the paper's stationary-measure methods cannot be adapted, or that every probabilistic zero theorem is irrelevant. It only shows that the published projected/random-height Cauchy conclusions do not imply the deterministic marked pair-energy decay required by `NB-243`.

The periodic construction is an abstract representation control, not a zeta counterexample. Its role is to show that a Cauchy Stieltjes law under translation contains insufficient information about internal carrier coherence. Likewise, the compatibility of sparse Ford packets with `mathcal H(T)=o(T)` is a quantifier check, not an existence assertion about the real zero set.

Finally, this finding does not update the Nyman--Beurling distance bridge. It is `SOURCE-ONLY`: it identifies which information survives, and which information is deliberately averaged away, in a newly available theorem sitting unusually close to the current source observable.
