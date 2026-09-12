# NB-081 — variable future depth subtracts exact screening and has a sharp outer-control threshold

**Status:** `EXACT-DERIVED + VARIABLE-HORIZON-LEDGER + HORIZON-SCREENING + MATCHED-OUTER-CONTROL + SHARP-DEPTH-THRESHOLD + METHOD-CALIBRATION`.

`NB-079` gives an exact residual-discovery-versus-screening ledger only when the future horizon is refined at the same fixed multiplicative ratio as the prefix. `NB-080` then shows that this fixed-ratio geometry has a severe false positive: even the boundedly invertible outer control

\[
D_j^{(\rho)}=(I-\rho V_m)e_j,
\qquad 0<\rho<1,
\]

has zero stable tail and a uniformly conditioned global Gram, but its fixed-ratio prediction-volume charge grows linearly in the prefix size. The mechanism is a positive-density boundary layer whose innovations are given only finitely many descendant generations.

The present finding resolves the first proposed escape from that obstruction. First, the `NB-079` ledger extends exactly to a growing future horizon by adding one new nonnegative **horizon-screening charge**. Second, on the matched outer controls of `NB-080`, the amount of future depth needed to remove the false positive can be computed sharply.

For a refinement step

\[
R^+=qR,
\qquad
\widetilde N^+=q(N+1)-1,
\qquad
N^+\ge \widetilde N^+,
\]

define

\[
\boxed{
\mathfrak H_{R^+;\widetilde N^+\to N^+}
:=
\mathfrak J_{R^+,\widetilde N^+}
-
\mathfrak J_{R^+,N^+}
\ge0.
}
\tag{1}
\]

Then the exact `NB-079` identity becomes

\[
\boxed{
\mathfrak J_{R^+,N^+}-\mathfrak J_{R,N}
=
\mathfrak P_{q;R,N}
-
\mathfrak S_{q;R,N}
-
\mathfrak H_{R^+;\widetilde N^+\to N^+}.
}
\tag{2}
\]

Thus enlarging the future beyond the descendant copy of the previous horizon is not an uncontrolled modification of the ledger. It contributes a third, explicitly nonnegative screening term.

For the stationary branch control, take an integer `m>=2`, `0<rho<=1`, and the depth-`L` horizon

\[
\boxed{
N_{R,L}=m^L R-1.
}
\tag{3}
\]

Put

\[
a_{\rho,L}
:=
\begin{cases}
\displaystyle
\frac{(1-\rho^2)\rho^{2L+2}}
{1-\rho^{2L+2}},&0<\rho<1,\\[1.2ex]
\displaystyle\frac1{L+1},&\rho=1.
\end{cases}
\tag{4}
\]

Then the complete finite prediction-volume charge satisfies the two-sided bound

\[
\boxed{
K_{m,R,L}\log(1+a_{\rho,L})
\le
\mathfrak J_{R,N_{R,L}}
\le
(R-1)\log(1+a_{\rho,L}),
}
\tag{5}
\]

where

\[
K_{m,R,L}
:=
R-1-
\left\lfloor
\frac{m^L R-1}{m^{L+1}}
\right\rfloor
\]

and therefore

\[
\frac{K_{m,R,L}}R\longrightarrow1-\frac1m
\qquad(R\to\infty)
\tag{6}
\]

uniformly in `L`. Consequently, whenever `L=L(R)->infinity`,

\[
\boxed{
\mathfrak J_{R,m^{L(R)}R-1}
\asymp_m
R\,a_{\rho,L(R)}.
}
\tag{7}
\]

For every boundedly invertible outer control `0<rho<1`, this gives the sharp depth threshold

\[
\boxed{
\mathfrak J_{R,m^LR-1}=O(1)
\iff
R\rho^{2L}=O(1),
}
\tag{8}
\]

and

\[
\boxed{
\mathfrak J_{R,m^LR-1}\to0
\iff
R\rho^{2L}\to0.
}
\tag{9}
\]

Thus logarithmically many descendant generations are sufficient and, at the level of powers, necessary. In particular, for every `epsilon>0`,

\[
L(R)
=
\left\lceil
\frac{(1+\epsilon)\log R}{2\log(1/\rho)}
\right\rceil
\tag{10}
\]

forces `mathfrak J -> 0`, while the critical depth

\[
L(R)
=
\frac{\log R}{2\log(1/\rho)}+O(1)
\tag{11}
\]

leaves a bounded order-one charge. Equivalently, a polynomial future horizon already removes the `NB-080` false positive for every fixed quantitatively invertible outer control.

At the outer but noninvertible endpoint `rho=1`, the threshold changes qualitatively:

\[
\boxed{
\mathfrak J_{R,m^LR-1}
\asymp_m
\frac{R}{L+1}.
}
\tag{12}
\]

Hence boundedness requires `L` of order at least `R`, and vanishing requires `L/R -> infinity`. Qualitative outerness alone therefore does **not** guarantee that a modestly growing future horizon removes the benign boundary layer. The speed is controlled by quantitative outer invertibility.

This is a strict calibration, not a theorem about the arithmetic Nyman source. It shows that the variable-horizon option left open by `NB-080` is mathematically viable and identifies the exact screening scale on the strongest matched outer controls. A source-facing proof must now either obtain comparable quantitative future synthesis from the actual Nyman innovations, renormalize the finite-depth layer, or use a target/stable-mode-sensitive certificate. Merely invoking outerness remains too weak because the endpoint `rho=1` can demand descendant depth comparable with the prefix size.

## 1. Future enlargement is an exact nonnegative screening charge

Recall from `NB-074` that

\[
\mathfrak J_{R,N}
=
\sum_{j<R}
\log
\frac{\Pi_{j,N}^2}{\widehat\Pi_{j,R}^2},
\tag{13}
\]

where `Pi_(j,N)` is the global prediction error using innovations through `N`, while `widehat Pi_(j,R)` is the error visible before the cutoff `R`.

For fixed `R`, enlarging the future can only improve prediction:

\[
N'\ge N
\quad\Longrightarrow\quad
\Pi_{j,N'}\le\Pi_{j,N}.
\tag{14}
\]

Therefore

\[
\boxed{
\mathfrak J_{R,N}-\mathfrak J_{R,N'}
=
\sum_{j<R}
\log\frac{\Pi_{j,N}^2}{\Pi_{j,N'}^2}
\ge0.
}
\tag{15}
\]

This proves (1), with the additional exact representation

\[
\boxed{
\mathfrak H_{R^+;\widetilde N^+\to N^+}
=
\sum_{j<R^+}
\log
\frac{\Pi_{j,\widetilde N^+}^2}
{\Pi_{j,N^+}^2}.
}
\tag{16}
\]

`NB-079` already proves

\[
\mathfrak J_{R^+,\widetilde N^+}
-
\mathfrak J_{R,N}
=
\mathfrak P_{q;R,N}-\mathfrak S_{q;R,N}.
\tag{17}
\]

Subtracting (1) gives (2). No new determinant inequality is needed: variable future depth is exactly fixed-ratio refinement followed by an additional finite Schur elimination.

Along an exact `q`-adic prefix ray `R_r=q^rR_0`, let `N_r` be any finite horizon schedule satisfying

\[
N_{r+1}\ge q(N_r+1)-1.
\tag{18}
\]

Then (2) telescopes as

\[
\boxed{
\mathfrak J_{R_m,N_m}
=
\mathfrak J_{R_0,N_0}
+
\sum_{r=0}^{m-1}
\bigl(\mathfrak P_r-\mathfrak S_r-\mathfrak H_r\bigr).
}
\tag{19}
\]

By `NB-074`, a nonzero stable tail still forces the left side to diverge for **every** such finite schedule. Conversely, boundedness on one unbounded variable-depth schedule still kills the stable tail. The extra term `mathfrak H_r` therefore records exactly the screening resource that a fixed-ratio ledger was withholding.

## 2. The visible prediction errors of the matched outer control are exactly one

Work in the scalar branch sector of `NB-071/072`. The branching isometry is

\[
V_me_j
=
\frac1{\sqrt m}
\sum_{k=mj}^{m(j+1)-1}e_k,
\tag{20}
\]

and

\[
D_j=(I-\rho V_m)e_j.
\tag{21}
\]

Because every child index of `j` is strictly larger than `j`, the finite visible synthesis matrix

\[
P_{<R}(I-\rho V_m)P_{<R}
\tag{22}
\]

is triangular with unit diagonal in the natural integer order. For every `j<R`, the visible innovation `J_RD_j` has coefficient one on `e_j`, while every later visible innovation has zero `e_j` coefficient. Conversely, backward substitution through the unit triangular suffix cancels all later visible coordinates. Hence

\[
\boxed{
\widehat\Pi_{j,R}^2=1
\qquad(1\le j<R).
}
\tag{23}
\]

This also gives `det A_R=1` for the control. The entire charge is therefore the finite-future excess above the unit causal feedthrough:

\[
\mathfrak J_{R,N}
=
\sum_{j<R}\log\Pi_{j,N}^2.
\tag{24}
\]

## 3. A depth-L horizon gives a uniform upper bound

Fix `j<R` and put

\[
f_r:=V_m^re_j.
\tag{25}
\]

The vectors `f_r` are orthonormal. Exact branching gives the radial descendant innovations

\[
d_r:=f_r-\rho f_{r+1}
=V_m^rD_j,
\qquad r\ge1.
\tag{26}
\]

For `N=m^LR-1`, every descendant generation of every `j<R` through depth `L` lies in the admitted future, because

\[
m^L(j+1)-1
\le
m^LR-1=N.
\tag{27}
\]

Thus `d_1,...,d_L` belong to the available future span. The radial computation of `NB-080` gives

\[
\operatorname{dist}\!\left(
D_j,
\operatorname{span}\{d_1,\ldots,d_L\}
\right)^2
=
1+a_{\rho,L}.
\tag{28}
\]

The full finite future can only improve on this admissible radial predictor, so

\[
\boxed{
1\le\Pi_{j,N}^2\le1+a_{\rho,L}
\qquad(j<R).
}
\tag{29}
\]

Summing (24) proves the upper bound in (5).

For completeness, (28) follows from the one-dimensional orthogonal complement already isolated in `NB-080`. For `0<rho<1`,

\[
\operatorname{dist}\!\left(
 f_1,
 \operatorname{span}\{d_1,\ldots,d_L\}
\right)^2
=
\frac{\rho^{2L}}{\sum_{s=0}^L\rho^{2s}},
\tag{30}
\]

and the coefficient `rho^2` in `D_j=f_0-rho f_1` gives (4). At `rho=1`, the same expression is `1/(L+1)`.

## 4. A positive-density boundary layer attains the depth-L penalty exactly

The upper estimate is sharp in order. Consider the indices

\[
\frac{N}{m^{L+1}}<j<R,
\qquad N=m^LR-1.
\tag{31}
\]

For every such `j`, three facts hold simultaneously:

\[
mj\ge R,
\tag{32}
\]

so none of the children is visible before the cutoff;

\[
m^L(j+1)-1\le N,
\tag{33}
\]

so the first `L` complete descendant generations are admitted; and

\[
m^{L+1}j>N,
\tag{34}
\]

so generation `L+1` lies completely beyond the horizon. These are exactly the hypotheses of the finite-depth calculation in `NB-080`, hence

\[
\boxed{
\Pi_{j,N}^2=1+a_{\rho,L}.
}
\tag{35}
\]

The number of such indices is `K_(m,R,L)`, so retaining only them in the nonnegative sum (24) proves the lower bound in (5). Since

\[
\frac{N}{m^{L+1}}
=
\frac Rm-rac1{m^{L+1}},
\tag{36}
\]

(6) follows. The boundary layer remains a fixed positive fraction of the prefix no matter how large `L` is; what changes with `L` is the cost paid by each boundary innovation.

## 5. The screening threshold is logarithmic for invertible outers and linear at the boundary

For fixed `0<rho<1`,

\[
a_{\rho,L}
=
\frac{(1-\rho^2)\rho^{2L+2}}
{1-\rho^{2L+2}}
\sim
(1-\rho^2)\rho^{2L+2}.
\tag{37}
\]

When `L->infinity`, `log(1+a_(rho,L))~a_(rho,L)`. The two-sided estimate (5) and the positive-density limit (6) therefore give

\[
\mathfrak J_{R,m^LR-1}
\asymp_{m,\rho}
R\rho^{2L},
\tag{38}
\]

which proves (8)--(11). The corresponding horizon obeys

\[
N+1=m^LR
=R^{1+\frac{L\log m}{\log R}},
\tag{39}
\]

so (10) requires only a fixed polynomial power of `R` for every fixed `rho<1`.

At `rho=1`,

\[
a_{1,L}=\frac1{L+1},
\tag{40}
\]

and (5) gives

\[
\mathfrak J_{R,m^LR-1}
\asymp_m
R\log\!\left(1+\frac1{L+1}\right)
\asymp_m
\frac R{L+1},
\tag{41}
\]

proving (12). This endpoint is outer and has zero stable tail by `NB-072`, but it is not boundedly invertible. The enormous difference between (38) and (41) is therefore a quantitative conditioning-of-the-outer-inverse effect, not an inner-factor effect.

The result also recovers `NB-080` as the special case of fixed `L`: then `a_(rho,L)>0` is constant and (5) gives `mathfrak J=Theta(R)`.

## 6. Stress tests, prior-art boundary, and consequence for the line

The unit-outer limit `rho=0` has `a_(0,L)=0`; (5) collapses to `mathfrak J=0`, matching the flat calibration in `NB-074/079`.

For every fixed `0<rho<1`, the control has the global Riesz bounds

\[
(1-\rho)^2I
\preceq H_\rho\preceq
(1+\rho)^2I
\]

from `NB-080`. Equation (38) shows that this good conditioning is exactly enough to make the benign finite-depth cost exponentially small in descendant depth, but it does **not** make a fixed depth sufficient. The boundary `rho=1` confirms that qualitative outer cyclicity without a bounded inverse gives no comparable logarithmic-depth guarantee.

No converse for the actual Nyman innovations is asserted. In particular, (5) is a theorem for the matched branch control, not an estimate of the arithmetic `mathfrak J_(R,N)`. Nor does bounded charge on a control prove any approximation rate for the canonical target. The valid implication retained from `NB-074` is only that a bounded arithmetic charge on one unbounded finite-horizon schedule would exclude the stable tail considered in `NB-066`--`NB-080`.

The horizon-screening identity (2) uses only finite prediction monotonicity and the exact `NB-079` refinement identity. The radial finite-depth computation is elementary Hardy/Wold prediction theory specialized to the explicit filter `1-rho z`; no novelty is claimed for those classical ingredients. A targeted prior-art audit checked the recent Nyman Gram programs of Werner Ehm (*On certain Gram matrices and their associated series*, arXiv:2405.06349) and Hugh Carvill (*Beurling Nyman Geometry and Gram Matrix Structure, Ladder Density and Polynomial Decay via Mellin Smoothing*, arXiv:2510.18132), together with the 2026 Friedrichs-angle work already anchored in this line. The search did not locate the present specialization: an exact variable-horizon correction to the `NB-079` branch-refinement ledger together with the sharp `R rho^(2L)` / `R/L` false-positive threshold for the matched outer controls. No priority claim is made, and no external estimate is load-bearing, so `SOURCES.md` remains unchanged.

The methodological frontier is now sharper than after `NB-080`. Growing the future is not merely a plausible fix: it contributes an exact nonnegative screening budget, and the benchmark controls quantify how much is needed. For a quantitatively invertible outer mode, logarithmic descendant depth is enough. For a merely outer boundary mode, it may take depth comparable with the whole prefix. Any arithmetic theorem using variable horizons must therefore expose a **quantitative future-synthesis rate** of the actual Nyman source, or else subtract the finite-depth outer layer before interpreting residual prediction volume as a stable-tail signal.