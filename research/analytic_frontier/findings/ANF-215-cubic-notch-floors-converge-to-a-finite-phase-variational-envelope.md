# ANF-215 — Cubic notch floors converge to a finite-phase variational envelope

**Status:** EXACT-DERIVED + ALL-REAL-MULTISETS + SMALL-WIDTH-LIMIT.
For each fixed `lambda>0`, the unrestricted real triangular-notch floor
at removed height `a=lambda eta^3` has an expansion
`q_eta=1+c(lambda) eta^4+o(eta^4)`. The coefficient is finite and is the
infimum of an explicit family of finite quadratic phase problems,
together with the collapsed-pair value `-2 lambda`. The same statement
holds at each fixed total-cardinality cap. ANF-214's width-uniform
approximation then justifies exchanging the shrinking-width and
increasing-cardinality limits. No minimizing cardinality, geometry,
exact transition coefficient or complex-zero consequence is asserted.

## Object and variational formula

Use the Fourier convention `f_hat(x)=int f(u) exp(-2 pi iux) du` and set
\[
g(u)=\frac{\cos(\sqrt2u)}{\sqrt2\sin(1/\sqrt2)}
\mathbf1_{[-1/2,1/2]}(u),\qquad F=\widehat g^{\,2}=K^2,
\]
\[
K(x)=\frac{\cos(\pi x)-b x\sin(\pi x)}{1-dx^2},\qquad
b=\sqrt2\pi\cot(1/\sqrt2),\qquad d=2\pi^2,
\tag{1}
\]
with removable values continued. For `sinc(t)=sin(pi t)/(pi t)`,
continuously at zero, put
\[
V_\eta(x)=F(x)-\lambda\eta^4\operatorname{sinc}^2(\eta x).
\tag{2}
\]
This is the Fourier transform of `g*g-lambda eta^3 tau_eta`, where
`tau_eta(u)=(1-|u|/eta)_+`. For distinct real sites `x_i` of positive
integer multiplicity `m_i`, define
\[
N=\sum_i m_i,\quad L=\sum_i\ell(m_i),\qquad
\ell(1)=1,\quad \ell(m)=2m\quad(m\ge2),
\]
\[
Q_\eta(W)=\frac{\sum_{i,j}m_im_jV_\eta(x_i-x_j)}{L},\qquad
q_\eta=\inf_{W\ne\varnothing}Q_\eta(W),\qquad
q_{\eta,M}=\inf_{0<N(W)\le M}Q_\eta(W).
\tag{3}
\]
There is no span, separation or density restriction.

For a finite ordered scaled geometry `p_1=0<p_2<...<p_k`, weights
`m_i in {1,2}`, and real phases `y_1=0,y_2,...,y_k`, write
`r_ij=p_j-p_i`, `L_m=sum_i m_i^2`, and
\[
\mathcal C(p,m,y)=\frac{2}{d^2L_m}\sum_{i<j}m_im_j
\left(\frac{y_j-y_i}{r_{ij}}-\frac1{r_{ij}^2}\right)^2,
\]
\[
\mathcal H(p,m)=1+\frac2{L_m}\sum_{i<j}m_im_j
\operatorname{sinc}^2(r_{ij}),\qquad
\mathcal G_\lambda=\mathcal C-\lambda\mathcal H.
\tag{4}
\]
For each integer `M>=2`, let
\[
c_M(\lambda)=\min\left\{-2\lambda,
\inf_{\substack{k\ge3,\ m_i\in\{1,2\},\ \sum_i m_i\le M\\
0=p_1<\cdots<p_k,\ y_1=0,\ y_i\in\mathbb R}}
\mathcal G_\lambda(p,m,y)\right\},
\tag{5}
\]
where an empty infimum is `+infinity`. Then
\[
\boxed{\lim_{\eta\downarrow0}\frac{q_{\eta,M}-1}{\eta^4}
=c_M(\lambda).}
\tag{6}
\]
Moreover, with `c(lambda)=inf_(M>=2)c_M(lambda)`,
\[
\boxed{-\infty<c(\lambda)\le-2\lambda,\qquad
\lim_{\eta\downarrow0}\frac{q_\eta-1}{\eta^4}=c(\lambda).}
\tag{7}
\]
Thus (5) with no cardinality cap gives an exact variational formula
for the unrestricted coefficient. It is a family of finite problems,
not an assertion that one fixed member attains the infimum.

For fixed `(p,m)`, phase minimization is ordinary weighted least
squares. Its quadratic part is
`sum_(i<j) m_i m_j (y_j-y_i)^2/r_ij^2`, positive definite after
`y_1=0`, so the phase minimum exists and is unique in that gauge.
The nontrivial remaining optimization is over geometry, multiplicity
patterns and cardinality. The constant `b` is absorbed in the phase
coordinates, not discarded from the physical kernel.

## Every finite phase state has a recovery family at all small widths

Fix one admissible `(p,m,y)` in (5). Choose
\[
x_i(\eta)=\left\lfloor\frac{p_i}{\eta}\right\rfloor
+\frac{\eta y_i}{b\pi}.
\tag{8}
\]
The sites are distinct and ordered for every sufficiently small width.
For `n_ij=floor(p_j/eta)-floor(p_i/eta)`, Taylor expansion of (1)
gives
\[
\eta(x_j-x_i)\longrightarrow r_{ij},\qquad
\frac{(-1)^{n_{ij}}K(x_j-x_i)}{\eta^2}
\longrightarrow\frac1d
\left(\frac{y_j-y_i}{r_{ij}}-\frac1{r_{ij}^2}\right).
\tag{9}
\]
Indeed the numerator after removing its parity has limit
`1-r_ij(y_j-y_i)` and the denominator times `eta^2` tends to
`-d r_ij^2`. Because `m_i in {1,2}`, the diagonal identity
`sum m_i^2=L` is exact. Hence
\[
\frac{Q_\eta(W_\eta)-1}{\eta^4}
\longrightarrow\mathcal G_\lambda(p,m,y).
\tag{10}
\]
No commensurability of the `p_i`, restriction to reciprocal-integer
widths or parity subsequence is needed: the signs disappear in `F=K^2`.

A simple pair at a fixed positive zero `r_*` of `K` gives
\[
Q_\eta(\{0,r_*\})
=1-\lambda\eta^4\{1+\operatorname{sinc}^2(\eta r_*)\}
=1-2\lambda\eta^4+O_\lambda(\eta^6).
\tag{11}
\]
Such a zero exists between `1` and `3/2`, by opposite signs in
(1) and no pole on that interval. Equations (10)--(11) give the
upper bound in (6), including when the infimum in (5) is not attained.

## Bounded-cardinality low energy allows only two kinds of component

Fix `M>=2`. Choose any sequence of widths tending to zero and
configurations satisfying
\[
N(W)\le M,\qquad Q_\eta(W)\le1+O(\eta^4).
\tag{12}
\]
For the lower-bound proof it suffices to use approximate minimizers
with error `o(eta^4)`, since (11) supplies (12).
ANF-213 permits replacement by a submultiset with no larger quotient
and `m_i in {1,2}` once `lambda eta^3<=1/100`. The cardinality cap
is preserved. The replaced approximate minimizers still lie above
`q_(eta,M)` and within the same error. Take a subsequence with the
number of distinct sites and all multiplicities fixed.

For these reduced configurations the exact identity is
\[
\frac{Q_\eta-1}{\eta^4}
=\frac2L\sum_{i<j}m_im_j\frac{F(x_j-x_i)}{\eta^4}
-\lambda\left\{1+\frac2L\sum_{i<j}m_im_j
\operatorname{sinc}^2(\eta(x_j-x_i))\right\}.
\tag{13}
\]
The expression in braces is at most `N^2/L<=M`. Positivity of
each source pair therefore gives, individually,
\[
K(x_j-x_i)=O(\eta^2)\qquad(i<j).
\tag{14}
\]
Pass to a further subsequence on which each consecutive scaled gap
`eta(x_(i+1)-x_i)` has a limit in `[0,infinity]`. Split the ordered
sites at gaps with infinite limit. Each remaining component has
bounded scaled span. Between components the notch terms tend to
zero in (13), while source terms are nonnegative. Since `L` is
additive over components, the full scaled energy is bounded below
by the `L`-weighted average of the component scaled energies, up to
`o(1)`. Dropping source cross terms is one-sided; their convergence
to zero is neither needed nor claimed.

Within a component with at least three distinct sites, all limiting
scaled gaps are strictly positive. There are two possible failures
to exclude.

**An entirely collapsed component cannot have three sites.** The
coarse triple gap from ANF-114 states that any three sites of span
`h` satisfy
\[
\sum_{\text{three pairs}}F(x_j-x_i)
\ge\frac1{16(1+dh^2)^2}.
\tag{15}
\]
If `eta h->0`, the right side divided by `eta^4` tends to infinity,
contradicting (14). The identity
`eta^4(1+dh^2)^2=(eta^2+d(eta h)^2)^2` covers bounded as well as
unbounded physical spans.

**A collapsed subcluster cannot coexist with another scaled site.**
If two sites in one limiting scaled cluster coexist with a site at
positive finite scaled distance, choose three ordered sites with
one gap `u=o(1/eta)` and the other `v` satisfying `eta v->p>0`;
reflection handles either ordering. Equation (1) gives, for large `z`,
\[
zK(z)=\frac bd\sin(\pi z)+O(z^{-1}).
\tag{16}
\]
Apply (14) and (16) at `v` and `u+v`. Both sines are `O(eta)`;
the angle subtraction formula gives `sin(pi u)=O(eta)`. Therefore
`|cos(pi u)|->1` and `bu sin(pi u)->0`. In contrast,
\[
\cos(\pi u)-bu\sin(\pi u)=(1-du^2)K(u)
=O\bigl(\eta^2(1+u^2)\bigr)=o(1),
\tag{17}
\]
a contradiction. This is ANF-210's short-gap exclusion applied to
an arbitrary triple inside the component. It includes bounded,
shrinking and mesoscopically growing short gaps, and uses the
numerator identity without division at removable points.

These two arguments exclude every repeated scaled position in a
component of at least three sites. Such a component consequently
has a strictly ordered finite limiting geometry `p`.

## The component lower bound recovers exactly the phase problem

Translate a component of at least three sites so its first site is
zero. For each other site, (14), (16) and `eta x_i->p_i>0` imply
`sin(pi x_i)=O(eta)`. If `n_i` is its nearest integer, then
`x_i-n_i=O(eta)`. After another subsequence,
\[
y_i:=\lim\frac{b\pi(x_i-n_i)}\eta
\quad\hbox{exists in }\mathbb R,\qquad y_1=0.
\tag{18}
\]
For differences the offsets subtract exactly; independent edge
phases are not permitted. The same expansion as (9) now applies
to every edge of this component. Thus its scaled energy converges
to `G_lambda(p,m,y)`, which is at least `c_M(lambda)` because its
total multiplicity is at most `M`.

A component of one site has scaled energy `-lambda`. For two sites
of multiplicities `m,k in {1,2}`, positivity gives for every separation
\[
\frac{Q_\eta-1}{\eta^4}
\ge-\lambda\left(1+\frac{2mk}{m^2+k^2}\right)
\ge-2\lambda.
\tag{19}
\]
This handles their bounded, collapsed and positive scaled-gap
regimes without assigning an artificial multiplicity to a limiting
collision. In particular, merging sites in the limit would change
`L` and is not a legitimate substitute for (19).

All components therefore have limiting lower energy at least
`c_M(lambda)`. Their denominator-weighted average has the same lower
bound. Every subsequence realizing a putative lower limit of the
capped infimum admits the preceding extraction. This proves the
lower bound in (6). The elementary estimate from (13),
`(Q_eta-1)/eta^4>=-lambda M`, also ensures finiteness at each cap.

## Width-uniform localization closes the unrestricted limit

The limit in (6) alone would not justify (7). The load-bearing
additional statement is ANF-214: for each fixed `lambda` there are
`eta_lambda>0`, integers `M_R->infinity` and numbers
`Gamma_lambda(R)->0` such that
\[
0\le\frac{q_{\eta,M_R}-q_\eta}{\eta^4}
\le\Gamma_\lambda(R)
\qquad(0<\eta\le\eta_\lambda).
\tag{20}
\]
Its explicit choices are `M_R=ceil(4 B_lambda R)` and
`Gamma_lambda(R)=6 lambda B_lambda(1+log R)/R`, with `B_lambda`
as defined in ANF-214. The same finding supplies
`q_eta>=1-D_lambda eta^4` with finite `D_lambda`. Hence all `c_M`
are at least `-D_lambda`; they decrease with `M`, so their infimum
`c(lambda)` is finite.

First fix `R` and take the shrinking-width limit using (6). Equation
(20) gives
\[
\liminf_{\eta\downarrow0}\frac{q_\eta-1}{\eta^4}
\ge c_{M_R}(\lambda)-\Gamma_\lambda(R)
\ge c(\lambda)-\Gamma_\lambda(R).
\tag{21}
\]
Conversely `q_eta<=q_(eta,M)` for every fixed `M`, so the upper
limit is at most every `c_M`, and hence at most `c`. Sending `R`
to infinity in (21) proves (7). It also proves the quantitative
coefficient approximation
\[
\boxed{0\le c_{M_R}(\lambda)-c(\lambda)
\le\Gamma_\lambda(R).}
\tag{22}
\]
The order of limits is essential. Neither a fixed geometry expansion
nor a cardinality cap chosen separately at each width proves this
uniform conclusion.

## Prior art, validation and research boundary

The variational method is classical. [Andrea Braides, *Local
minimization, variational evolution and Gamma-convergence*, author
lecture-note version, sections 1.1--1.5](https://cvgmt.sns.it/media/doc/paper/2094/Corso2013LN.pdf),
develops lower bounds, recovery sequences, compactness and higher-order
energy limits. No general Gamma-convergence theorem is invoked here:
(14)--(19) check the possible degenerations explicitly, and (20)
replaces an assumed global compactness statement. In particular,
this finding proves convergence of infimum values, not a theorem on
convergence of minimizers in a specified configuration topology.

[Wang, Lemma 3.2](https://arxiv.org/html/2609.24167v1#S3)
provides the neighboring three-point numerator obstruction;
ANF-114 and ANF-210 give the exact local versions used above.
[Knausgård, sections 7.1--7.2](https://arxiv.org/html/2610.08965v1#S7.SS1)
studies simple/double pair energies, constrained density and periodic
trial states. Those are prior art for the particle interpretation,
not a shrinking-notch free-span limit. The exact cubic variational
formula (4)--(7) was not identified in the targeted literature check;
no exhaustive novelty claim is made. Weighted least squares,
subsequence extraction and recovery sequences are standard tools.

Locally, ANF-210 and ANF-212 establish the phase reduction for triples;
ANF-213 removes higher site multiplicities exactly. The additional
result here is that every fixed-cardinality low-energy sequence,
including collisions and infinitely separated components, is covered
by (5), and ANF-214 makes this description sufficient for the full
coefficient limit. A three-site or periodic ansatz is not assumed.

The decisive analytic checks are the bounded-cardinality implication
(14), the exhaustive two collision cases, the common vertex phases
in (18), the exact denominator average over components, and the
width-uniform error in (20). Scratch evaluation at 80 decimal digits
checked 24 mixed-weight geometries of three through eight sites at
three decreasing widths, using the weighted normal equations and (8).
The largest final error in the scaled coefficient at `eta=10^-8`
was below `1.11e-8`. A fixed-zero pair separately checked (11).
These are diagnostics of normalization and recovery, not a proof of
optimization or the lower bound. Integer rounding need not give
monotone recovery errors. No Lean verification is claimed.

The limiting coefficient now exists, but its value and optimizing
geometry remain open beyond already certified regimes. ANF-209's
small-coefficient two-site window and ANF-211--ANF-212's descending
witnesses remain compatible with (5); this result does not certify
any additional numerical transition. Arbitrarily large cardinality
may still be needed as approximation error tends to zero. Neither
finite attainment at positive width nor attainment of (5) is proved.
The real positivity of `F` is used in both component splitting and
(14), so this does not extend to nonreal sites. No improved zeta-zero
proportion, zero-density estimate or exclusion of off-critical zeros
follows without an additional analytic bridge.
