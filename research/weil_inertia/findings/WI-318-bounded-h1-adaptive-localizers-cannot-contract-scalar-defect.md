# WI-318 — Uniformly H1-bounded adaptive localizers cannot contract a scalar defect

**Status:** `EXACT-DERIVED + CLASSICAL-HARMONIC + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY + PRIOR-ART-AUDITED`.

**Parent findings:** WI-304, WI-311, WI-312, WI-317.

WI-317 rules out autonomous scalar defect contraction for every **fixed finite** portfolio of source-exact smooth localizations, but deliberately leaves infinite or dynamically selected families open. The finiteness there enters only once: it upgrades pointwise Riemann--Lebesgue decay of the continuous localization error to decay simultaneous over the portfolio.

For the unit-window localizers used in WI-307--WI-312, that loophole can be closed for an arbitrary infinite/adaptive family as long as its total `H^1` cost stays uniformly bounded. The derivative budget gives a uniform `O(1/|t|)` Riemann--Lebesgue estimate for the continuous source defect. Independently, compact unit support gives a **uniform first-prime autocorrelation gap**: at the shift `log 2`, the truncated translation squares to zero, so Haagerup--de la Harpe implies `R(log 2) <= 1/2` for every multiwindow family. A single common prime-phase recurrence sequence therefore defeats the whole infinite family at once.

Hence an infinite/adaptive scalar-feedback architecture can escape WI-317 only by leaving every bounded-`H^1` class (or by adding genuinely new information). In frequency language, its localization second moment must become unbounded. This turns the large-carrier degeneration observed in WI-311 from a feature of that construction into a necessary condition for any unit-window scalar-feedback escape.

## 1. Infinite-family contraction criterion

Fix an outer aperture `L>0`. Let `Q` be the source-exact Weil quadratic form on the corresponding compact-support domain. Let `mathcal R` be an arbitrary index set, finite or infinite. For every `r in mathcal R`, let

\[
\{g^{(r)}_\nu\}_{\nu=1}^{J_r}
\subset C_c^\infty((-1/2,1/2);\mathbb R)
\]

be a finite real multiwindow family satisfying

\[
\sum_{\nu=1}^{J_r}\|g^{(r)}_\nu\|_2^2=1.
\tag{1}
\]

Write its aggregate autocorrelation

\[
R_r(a)
:=
\sum_{\nu=1}^{J_r}
\int g^{(r)}_\nu(u+a)g^{(r)}_\nu(u)\,du.
\tag{2}
\]

Assume the family has a uniform Dirichlet budget

\[
\boxed{
\sup_{r\in\mathcal R}
\sum_{\nu=1}^{J_r}\|(g^{(r)}_\nu)'\|_2^2
\le M<\infty.
}
\tag{3}
\]

The exact WI-311 localization identity is

\[
Q(f)=\operatorname{Loc}_r(f)-\mathcal E_r(f).
\tag{4}
\]

Suppose, exactly as in WI-317, that the only estimate fed into every localized source term is the same scalar semibound

\[
Q(h)\ge-c\|h\|_2^2.
\tag{5}
\]

Normalization (1) gives

\[
\operatorname{Loc}_r(f)\ge-c\|f\|_2^2,
\]

hence an adaptive choice from the whole family can improve the scalar constant by a uniform `kappa>0` only if

\[
\boxed{
\inf_{r\in\mathcal R}\mathcal E_r(f)
\le-\kappa\|f\|_2^2
\quad\text{for every }f.
}
\tag{6}
\]

The claim below is that (6) is impossible under (3), even when `r` is chosen after seeing `f`.

## 2. The derivative budget gives uniform Riemann--Lebesgue decay

Bundle the windows into the vector-valued function

\[
G_r=(g^{(r)}_1,\ldots,g^{(r)}_{J_r}),
\]

extended by zero to the real line. Then

\[
\|G_r\|_2=1,
\qquad
\|G_r'\|_2^2\le M,
\qquad
R_r(a)=\langle T_aG_r,G_r\rangle.
\tag{7}
\]

For every real `a`, the translation estimate for `H^1` functions gives

\[
\|T_aG_r-G_r\|_2\le |a|\|G_r'\|_2.
\]

Therefore

\[
\boxed{
0\le1-R_r(a)
=\frac12\|T_aG_r-G_r\|_2^2
\le\frac M2a^2.
}
\tag{8}
\]

There is also a first-derivative bound with the crucial extra factor `a`. Since the windows are compactly supported,

\[
\langle G_r,G_r'\rangle=0,
\]

and integration by parts gives

\[
R_r'(a)=-\langle T_aG_r,G_r'\rangle.
\]

Thus

\[
\boxed{
|R_r'(a)|
=|\langle T_aG_r-G_r,G_r'\rangle|
\le M|a|.
}
\tag{9}
\]

Now choose a fixed real nonnegative unit vector

\[
\phi\in C_c^\infty((-L,L))
\]

and define

\[
h(a):=\int\phi(u+a)\phi(u)\,du.
\tag{10}
\]

For the high-frequency modulation

\[
f_t(u)=e^{itu}\phi(u),
\tag{11}
\]

we have

\[
H_{f_t}(a)=h(a)\cos(ta).
\tag{12}
\]

The continuous part of the exact source defect is

\[
\mathcal C_r(f_t)
=
\int_0^{2L}
(1-R_r(a))\,\kappa(a)\,h(a)\cos(ta)\,da,
\tag{13}
\]

where

\[
\kappa(a)
=
\frac{2e^{-a/2}}{1-e^{-2a}}
-4\cosh(a/2).
\tag{14}
\]

The apparent singularity is only simple: `a kappa(a)` extends smoothly to `a=0` with value `1`, and `a^2 kappa'(a)` stays bounded on `(0,2L]`. Put

\[
b_r(a):=(1-R_r(a))\kappa(a)h(a).
\tag{15}
\]

Equations (8)--(9), together with the boundedness of `a kappa(a)`, `a^2 kappa'(a)`, `h`, and `h'`, give a constant `C=C(L,phi,M)` independent of `r` such that

\[
\|b_r'\|_{L^1(0,2L)}+\|b_r\|_\infty\le C.
\tag{16}
\]

Moreover `b_r(0)=0`, and `h` vanishes near `2L` because `phi` is compactly supported strictly inside `(-L,L)`. Integration by parts in (13) therefore yields the uniform estimate

\[
\boxed{
\sup_{r\in\mathcal R}
|\mathcal C_r(f_t)|
\le\frac{C}{|t|}
\longrightarrow0.
}
\tag{17}
\]

This is the exact point where bounded `H^1` replaces the finiteness assumption of WI-317. No compactness extraction and no choice of a finite subportfolio are needed.

## 3. Unit support forces a uniform first-prime loss

Assume now that the first prime is active,

\[
\log2<2L.
\tag{18}
\]

For every `r`, regard translation by

\[
a_2:=\log2
\]

as the truncated translation on

\[
L^2((-1/2,1/2);\mathbb R^{J_r}).
\]

Because

\[
2\log2>1,
\]

this contraction satisfies

\[
T_{a_2}^2=0.
\tag{19}
\]

The sharp Haagerup--de la Harpe numerical-radius inequality for a square-zero contraction gives

\[
w(T_{a_2})\le\cos\frac\pi3=\frac12.
\tag{20}
\]

Consequently, uniformly over the entire family,

\[
\boxed{
R_r(\log2)
=\langle T_{a_2}G_r,G_r\rangle
\le\frac12.
}
\tag{21}
\]

In the source-exact defect, the coefficient of the `n=2` atom is

\[
\alpha_{r,2}
=
\frac{2\log2}{\sqrt2}
\bigl(1-R_r(\log2)\bigr).
\]

Equation (21) therefore gives the family-independent floor

\[
\boxed{
\alpha_{r,2}
\ge\frac{\log2}{\sqrt2}
\qquad(r\in\mathcal R).
}
\tag{22}
\]

This is stronger than the pointwise strict inequality used in WI-317. There, finiteness was needed because the individual gaps `1-R_r(log 2)` could a priori approach zero across the portfolio. Unit support shows that this cannot happen at the first-prime shift.

More generally, the same argument gives

\[
R_r(a)
\le
\cos\!\left(
\frac{\pi}{\lceil1/a\rceil+1}
\right)
\qquad(0<a<1),
\tag{23}
\]

by applying the nilpotent numerical-radius theorem to the truncated translation, but only the square-zero `a=log 2` case is needed below.

## 4. One recurrence sequence defeats the whole infinite family

There are only finitely many active prime powers with

\[
\log n<2L.
\]

Choose `phi` in (10) positive on a sufficiently long interval that

\[
h(\log n)>0
\tag{24}
\]

for every active prime power. This is possible because the largest active shift is strictly smaller than `2L`.

For every `r`, the arithmetic part of the source defect is

\[
\mathcal P_r(f_t)
=
\sum_{\log n<2L}
\alpha_{r,n}h(\log n)\cos(t\log n),
\tag{25}
\]

with

\[
\alpha_{r,n}
=
\frac{2\Lambda(n)}{\sqrt n}
\bigl(1-R_r(\log n)\bigr)\ge0.
\tag{26}
\]

Also `|R_r(a)|<=1`, so all coefficients in the finite active set are uniformly bounded.

Simultaneous Dirichlet/Kronecker recurrence supplies an unbounded sequence `t_k` depending only on the finite set of active shifts such that

\[
\cos(t_k\log n)\longrightarrow1
\]

for every active prime power at once. In particular, for all sufficiently large `k`, every cosine in (25) is nonnegative and

\[
\cos(t_k\log2)\ge\frac12.
\tag{27}
\]

Using (22), (24), and (27), while simply discarding the other nonnegative prime-power terms, gives

\[
\boxed{
\inf_{r\in\mathcal R}
\mathcal P_r(f_{t_k})
\ge
\frac{\log2}{2\sqrt2}
\,h(\log2)
>0
}
\tag{28}
\]

for all sufficiently large `k`. Combining (17) and (28) yields

\[
\boxed{
\inf_{r\in\mathcal R}
\mathcal E_r(f_{t_k})>0
}
\tag{29}
\]

for all sufficiently large `k`.

Equation (29) contradicts the necessary contraction condition (6) for every `kappa>0`. The localizer may be selected after seeing `f_{t_k}`; the conclusion already takes the infimum over the entire infinite family.

If instead

\[
2L\le\log2,
\tag{30}
\]

there are no active prime-power terms because the source cutoff is strict. Equation (17) then gives

\[
\sup_{r\in\mathcal R}|\mathcal E_r(f_t)|\to0.
\tag{31}
\]

For every `kappa>0`, sufficiently large `|t|` has

\[
\inf_r\mathcal E_r(f_t)>-\kappa,
\]

so (6) again fails. Thus at every fixed aperture,

\[
\boxed{
\text{an arbitrary unit-window localization family with bounded total }H^1
\text{ cost cannot autonomously contract a reused scalar Weil defect.}
}
\tag{32}
\]

## 5. Escape requires unbounded frequency second moment or new information

For the Fourier convention of WI-311, Plancherel identifies the total derivative energy with the second moment of the aggregate frequency-energy law, up to the fixed convention factor. Therefore (3) is exactly a uniform frequency-second-moment bound.

The contrapositive of (32) is useful operationally. Any infinite/adaptive unit-window architecture that genuinely escapes WI-317 while still feeding only the same scalar semibound into every localized piece must contain a sequence with

\[
\boxed{
\sum_\nu\|(g_\nu)'\|_2^2\longrightarrow\infty.
}
\tag{33}
\]

Equivalently, its aggregate frequency second moment must diverge. It is not enough merely to have infinitely many windows or to choose them dynamically; the family has to become spectrally noncompact.

This connects two previously separate observations. WI-311 constructs increasingly high carrier frequencies to flatten the capped tail, and WI-312 shows that a particular anti-concentrating tail-flattening limit forces archimedean Hilbert--Schmidt blow-up. Equation (33) is more basic and does not assume tail flattening: **unbounded modulation/derivative complexity is already necessary before an infinite scalar-feedback family can evade the common recurrence obstruction at all.**

The result does not say that unbounded `H^1` is sufficient. The WI-311/WI-312 chain is evidence in the opposite direction: moving to high carriers transfers complexity elsewhere. Nor does (32) cover an architecture that supplies stronger localized arithmetic estimates, tracks mode- or prime-dependent information, uses matrix/vector invariants rather than the scalar bottom, changes the support geometry, or otherwise injects information absent from premise (5).

## 6. Prior-art and novelty audit

The ingredients are classical separately. The localization algebra is the standard IMS-type pattern already source-audited in WI-317. Uniform high-frequency decay under a derivative/variation budget is a standard strengthening of the Riemann--Lebesgue mechanism; here (8)--(17) give the required estimate directly rather than importing a black-box compactness theorem. Simultaneous phase recurrence is classical Dirichlet/Kronecker approximation. The sharp numerical-radius estimate

\[
w(T)\le\|T\|\cos\frac\pi{N+1}
\quad(T^N=0)
\]

is due to Uffe Haagerup and Pierre de la Harpe, **The numerical radius of a nilpotent operator on a Hilbert space**, *Proceedings of the American Mathematical Society* **115** (1992), 371--379, DOI `10.1090/S0002-9939-1992-1072339-6`; it was already imported into this line in WI-276.

A targeted prior-art audit around IMS/localization semibounds, uniform Riemann--Lebesgue estimates for compact or Sobolev-bounded families, nilpotent translation numerical-radius bounds, and source-exact Weil localization found these ingredients individually but no source stating the adaptive infinite-family obstruction (32) or the necessary unbounded-frequency conclusion (33) for this Weil-form scalar-feedback architecture. No priority claim is made.

### Validation boundary

The theorem is exact for the source-exact **unit-window** smooth multiwindow identities of WI-311 at a fixed outer aperture and for arbitrary finite or infinite collections satisfying the uniform derivative budget (3). It assumes only that the same scalar semibound is recycled into every localized source term. The first-prime argument uses the strict source cutoff and the fact `log 2<1`, so the square-zero translation bound is specific to the unit-window normalization used here. The result does not exclude non-unit support families, unbounded-`H^1` adaptive families, stronger localized source estimates, or non-scalar bootstraps. It proves a necessary complexity escape condition, not RH and not a new zero-density statement.