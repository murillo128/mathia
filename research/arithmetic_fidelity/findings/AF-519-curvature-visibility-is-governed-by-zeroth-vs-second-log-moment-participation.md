# AF-519 — Curvature visibility is governed by zeroth-versus-second log-moment participation

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `DIRICHLET-SOURCE` · `SCALE-DEPENDENT-PARTICIPATION` · `MESOSCOPIC-CURVATURE` · `MOMENT-PROFILE` · `NO-NOVELTY-CLAIM`

## Claim

Let

\[
P(s)=\sum_{p\in\mathbb P}p^{-s},
\qquad
\kappa_P(s)=\frac{d^2}{ds^2}\log P(s),
\qquad s>1.
\tag{1}
\]

Fix an integer `c\ge2`, and put

\[
\beta(s)=1-c^{-s},
\qquad
\beta_0=\beta(1)=1-\frac1c.
\tag{2}
\]

For each cutoff `A`, choose an arbitrary scale-dependent selected set

\[
E_A\subseteq\{p\in\mathbb P:p>A\}
\tag{3}
\]

and move each selected prime `p\in E_A` to the composite atom `cp`, leaving every other prime unchanged. Define

\[
T_A(s)=\sum_{p\in E_A}p^{-s}
\tag{4}
\]

and

\[
Q_A(s)=P(s)-\beta(s)T_A(s),
\qquad
\kappa_A(s)=\frac{d^2}{ds^2}\log Q_A(s).
\tag{5}
\]

Let `t_A\downarrow0`, `s_A=1+t_A`. Suppose the selected family has limiting zeroth and second logarithmic moment participation

\[
\frac{T_A(s_A)}{P(s_A)}\longrightarrow\alpha_0,
\qquad
\frac{T_A''(s_A)}{P''(s_A)}\longrightarrow\alpha_2.
\tag{6}
\]

Because `E_A` is a subset of the primes, `0\le\alpha_0,\alpha_2\le1` whenever the limits exist. Then

\[
\boxed{
\frac{\kappa_A(s_A)}{\kappa_P(s_A)}
\longrightarrow
\frac{1-\beta_0\alpha_2}{1-\beta_0\alpha_0}
}
\tag{7}
\]

and hence

\[
\boxed{
\frac{\kappa_A(s_A)-\kappa_P(s_A)}{\kappa_P(s_A)}
\longrightarrow
\frac{\beta_0(\alpha_0-\alpha_2)}
{1-\beta_0\alpha_0}.
}
\tag{8}
\]

Thus the leading curvature response is not controlled by selected counting density alone. At a given boundary scale it is controlled by the mismatch between **Dirichlet-value participation** `\alpha_0` and **second logarithmic-moment participation** `\alpha_2`. The first logarithmic moment does not enter the leading curvature ratio.

In particular, there are scale-dependent selections with

\[
\alpha_0=0,
\qquad
\alpha_2>0,
\tag{9}
\]

so a perturbation may carry a vanishing fraction of the prime-zeta value while remaining macroscopically visible to logarithmic curvature.

A concrete family is obtained as follows. Fix

\[
0<a<b<\infty,
\qquad
k>1,
\tag{10}
\]

and set

\[
t_A=(\log A)^{-k}.
\tag{11}
\]

Select the moving logarithmic shell

\[
E_A
=
\left\{
 p\in\mathbb P:
 \exp(a/t_A)<p\le \exp(b/t_A)
\right\}.
\tag{12}
\]

Since `k>1`, the lower edge `\exp(a/t_A)=\exp(a(\log A)^k)` eventually exceeds `A`, so `(12)` is an admissible tail selection. Define

\[
I_2(a,b)
=
\int_a^b u e^{-u}\,du
=
(a+1)e^{-a}-(b+1)e^{-b}.
\tag{13}
\]

Then

\[
\frac{T_A(s_A)}{P(s_A)}\longrightarrow0,
\qquad
\frac{T_A''(s_A)}{P''(s_A)}\longrightarrow I_2(a,b),
\tag{14}
\]

and therefore

\[
\boxed{
\frac{\kappa_A(s_A)}{\kappa_P(s_A)}
\longrightarrow
1-\left(1-\frac1c\right)I_2(a,b)
}
\tag{15}
\]

with the nonzero relative defect

\[
\boxed{
\frac{\kappa_A(s_A)-\kappa_P(s_A)}{\kappa_P(s_A)}
\longrightarrow
-\left(1-\frac1c\right)I_2(a,b).
}
\tag{16}
\]

Because `u e^{-u}` is positive and has total mass `1` on `(0,\infty)`, every proper shell `0<a<b<\infty` has

\[
0<I_2(a,b)<1.
\tag{17}
\]

Equation `(16)` is therefore a genuine order-one curvature witness despite the vanishing value participation in `(14)`.

## Derivation

### 1. Prime-zeta curvature has one dominant derivative scale

As `t\downarrow0`, the classical singular expansion of the prime zeta function at `s=1` gives

\[
P(1+t)
=
\log\frac1t+O(1),
\tag{18}
\]

\[
P'(1+t)
=
-\frac1t+O(1),
\qquad
P''(1+t)
=
\frac1{t^2}+O(1).
\tag{19}
\]

Writing

\[
L_t=\log\frac1t,
\tag{20}
\]

one obtains

\[
\kappa_P(1+t)
=
\frac{P''}{P}
-
\left(\frac{P'}P\right)^2
\sim
\frac1{t^2L_t},
\tag{21}
\]

because the squared logarithmic derivative is smaller by one factor of `L_t`:

\[
\left(\frac{P'}P\right)^2
=
O\!\left(\frac1{t^2L_t^2}\right).
\tag{22}
\]

This is the same boundary carrier used in AF-512--AF-518.

### 2. Two selected moments determine the leading transformed curvature

At `s_A=1+t_A`, equation `(6)` gives

\[
T_A(s_A)
=
\alpha_0 P(s_A)+o(P(s_A)),
\tag{23}
\]

\[
T_A''(s_A)
=
\alpha_2 P''(s_A)+o(P''(s_A)).
\tag{24}
\]

Since all summands are positive after taking absolute values of derivatives,

\[
|T_A'(s_A)|
=
\sum_{p\in E_A}(\log p)p^{-s_A}
\le
\sum_p(\log p)p^{-s_A}
=
|P'(s_A)|.
\tag{25}
\]

Thus no separate first-moment convergence hypothesis is needed.

From `(5)`,

\[
Q_A=P-\beta T_A,
\tag{26}
\]

so `(23)` and `\beta(s_A)\to\beta_0` imply

\[
\frac{Q_A(s_A)}{P(s_A)}
\longrightarrow
1-\beta_0\alpha_0.
\tag{27}
\]

The denominator remains strictly positive because

\[
1-\beta_0\alpha_0
\ge
1-\beta_0
=
\frac1c.
\tag{28}
\]

Differentiating twice,

\[
Q_A''
=
P''-\beta''T_A-2\beta'T_A'-\beta T_A''.
\tag{29}
\]

The functions `\beta'` and `\beta''` are bounded near `s=1`. By `(18)`, `(19)`, `(23)`, and `(25)`,

\[
\beta''T_A=O(L_{t_A})=o(t_A^{-2}),
\qquad
\beta'T_A'=O(t_A^{-1})=o(t_A^{-2}).
\tag{30}
\]

Hence `(24)` and `(29)` give

\[
\frac{Q_A''(s_A)}{P''(s_A)}
\longrightarrow
1-\beta_0\alpha_2.
\tag{31}
\]

Similarly `Q_A'(s_A)=O(t_A^{-1})`, while `(27)` gives `Q_A(s_A)\asymp L_{t_A}`. Therefore

\[
\left(\frac{Q_A'}{Q_A}\right)^2(s_A)
=
O\!\left(\frac1{t_A^2L_{t_A}^2}\right),
\tag{32}
\]

again lower order than the curvature scale `t_A^{-2}/L_{t_A}`. Combining `(21)`, `(27)`, `(31)`, and `(32)` proves `(7)`, and subtracting one proves `(8)`.

The key point is structural: the first logarithmic moment affects `Q_A'`, but the entire square `(Q_A'/Q_A)^2` is asymptotically suppressed by one extra logarithm. The leading curvature therefore compares only the value layer and the second-log-moment layer.

### 3. A moving logarithmic shell has zero value share but positive curvature share

For the shell `(12)`, the prime number theorem and partial summation turn prime sums over the moving interval into Laplace-window integrals. With `t=t_A`, write `x=e^y` and then `u=ty`. Uniformly on the fixed window `u\in[a,b]`, the PNT gives the standard replacement

\[
d\pi(x)
\sim
\frac{dx}{\log x}.
\tag{33}
\]

For the zeroth moment,

\[
T_A(1+t)
=
\sum_{e^{a/t}<p\le e^{b/t}}p^{-1-t}
\longrightarrow
I_0(a,b),
\tag{34}
\]

where

\[
I_0(a,b)
=
\int_a^b\frac{e^{-u}}u\,du.
\tag{35}
\]

Since `P(1+t)\sim\log(1/t)\to\infty`, equation `(34)` gives

\[
\frac{T_A(1+t)}{P(1+t)}\longrightarrow0.
\tag{36}
\]

For the first logarithmic moment,

\[
-t\,T_A'(1+t)
\longrightarrow
I_1(a,b)
:=
\int_a^b e^{-u}\,du
=
e^{-a}-e^{-b}.
\tag{37}
\]

For the second logarithmic moment,

\[
t^2T_A''(1+t)
\longrightarrow
I_2(a,b)
:=
\int_a^b u e^{-u}\,du.
\tag{38}
\]

Since `t^2P''(1+t)\to1`, equation `(38)` gives

\[
\frac{T_A''(1+t)}{P''(1+t)}
\longrightarrow
I_2(a,b).
\tag{39}
\]

Thus the shell has the moment profile

\[
(\alpha_0,\alpha_2)
=
(0,I_2(a,b)),
\tag{40}
\]

and `(15)`--`(16)` follow immediately from the general response law.

The phenomenon is not a contradiction with `(34)`. The value kernel weighs logarithmic location by `e^{-u}/u`, whereas the second derivative weighs it by `u e^{-u}` after normalization. A shell at `\log p\asymp1/t` therefore contributes only `O(1)` to a total value of order `\log(1/t)`, yet contributes an order-one fraction of the normalized second logarithmic moment.

### 4. AF-517 is the regular-density specialization of the same moment law

For the fixed PNT-density family in AF-517, with density `\delta` and the same scale

\[
t_A=(\log A)^{-k},
\qquad k>1,
\tag{41}
\]

the selected tail satisfies

\[
\frac{T_A(s_A)}{P(s_A)}
\longrightarrow
\delta\frac{k-1}{k},
\qquad
\frac{T_A''(s_A)}{P''(s_A)}
\longrightarrow
\delta.
\tag{42}
\]

Thus

\[
\alpha_0=\delta\frac{k-1}{k},
\qquad
\alpha_2=\delta.
\tag{43}
\]

Substitution into `(8)` gives

\[
\frac{\kappa_A(s_A)-\kappa_P(s_A)}{\kappa_P(s_A)}
\longrightarrow
-
\frac{\beta_0\delta/k}
{1-\beta_0\delta(k-1)/k}.
\tag{44}
\]

Writing `r=\beta_0\delta`, equation `(44)` is exactly

\[
-\frac{r}{k-r(k-1)},
\tag{45}
\]

which recovers AF-517. The previous density law is therefore not a separate mechanism: it is one regular family whose zeroth and second moment shares happen to be locked together by PNT density.

## Fidelity and matched-control audit

The transformed atoms are ordinary composites when `c\ge2` is an integer. The map `p\mapsto cp` is injective, and no moved atom can collide with an unmoved prime. Thus `(5)` is an exact matched source perturbation rather than a formal change of coefficients.

AF-517 showed that every fixed positive PNT-density selected tail is visible at the cutoff-adapted boundary scale and that fixed PNT density zero removes its leading density-controlled witness. AF-519 shows why that statement cannot be promoted to a general sparse-selection criterion: a selection may have negligible **value participation** while concentrating on the logarithmic region that dominates `P''`.

The correct leading statistic for this curvature carrier is therefore the moment pair

\[
(\alpha_0,\alpha_2),
\tag{46}
\]

or, more precisely, their mismatch under `(8)`. Equality `\alpha_0=\alpha_2` makes the leading relative curvature defect vanish even if both are positive. Conversely `\alpha_0=0<\alpha_2` produces an order-one defect. Counting density is sufficient only in regular families where it determines both moments.

The shell `(12)` should not be described as a fixed zero-PNT-density subset of the primes. It depends on `A` and on the observation scale `t_A`. What vanishes is its normalized Dirichlet-value participation at that scale. This distinction is essential: AF-519 concerns **scale-dependent participation**, precisely the regime left open by AF-517.

## Representation audit

The carrier remains the unmarked logarithmic curvature of a positive Dirichlet source. No side channel, prime labels, or external arithmetic metadata are added.

The new invariant is not another representation of the selected set. It is a classification of what this compression can see at leading order: once a perturbation is summarized by its contributions to `P` and `P''` at the probed boundary scale, the first derivative is asymptotically demoted and the curvature response is forced by `(7)`.

This gives a sharper instance of the line's general question about survival under compression. The same perturbation can be negligible in one normalized layer and visible in another; therefore statements such as “the perturbation has vanishing mass” are incomplete until the relevant compression kernel and moment scale are specified.

## Prior art and novelty assessment

No novelty is claimed for the analytic-number-theory or Tauberian ingredients.

- C.-E. Fröberg, **“On the prime zeta function,”** *BIT* 8 (1968), 187--202, DOI `10.1007/BF01933420`, is the classical prime-zeta reference underlying the boundary expansion at `s=1`.
- Hugh L. Montgomery and Robert C. Vaughan, ***Multiplicative Number Theory I: Classical Theory***, Cambridge University Press (2006), provides standard prime-number-theorem and partial-summation machinery for weighted prime sums.
- N. H. Bingham, C. M. Goldie, and J. L. Teugels, ***Regular Variation***, Cambridge University Press (1987), gives the classical Karamata/Laplace--Stieltjes framework in which moment-weighted boundary asymptotics such as `(34)`--`(38)` naturally sit.
- AF-515--AF-518 provide the immediately preceding Mathia transport results: full proportional dilation, stability under sublinear rounding, fixed PNT-density participation, and uniform vanishing-relative transport.

A focused literature search did not identify a standard theorem stated specifically as `(7)`--`(8)` for prime-zeta logarithmic curvature under scale-dependent proportional tail selection, nor the moving-shell specialization `(15)`--`(16)`. These formulas are therefore recorded as exact derived specializations and a structural classification internal to Arithmetic Fidelity, with `NO-NOVELTY-CLAIM` retained.

## Boundaries and failure modes

1. **The theorem is pointwise along the chosen boundary scale.** It does not establish uniform control of the relative-curvature supremum over all `s>1` for an arbitrary scale-dependent family.
2. **The moment limits are hypotheses in the general statement.** Families for which `T_A/P` or `T_A''/P''` oscillate need subsequence or limsup/liminf analysis rather than `(7)`.
3. **The displacement is proportional.** Nonproportional transport introduces a distribution of displacement amplitudes and need not reduce to one scalar `\beta_0`.
4. **The shell is scale-dependent.** Equation `(12)` is not evidence that a single fixed zero-density subset has the same response.
5. **Curvature visibility is not arithmetic identification.** A nonzero defect distinguishes the transformed matched control from the rational-prime source for this carrier and scale; it does not identify primes uniquely among all possible controls and is not evidence for RH.
6. **Moment equality is only a leading-order invisibility condition.** If `\alpha_0=\alpha_2`, lower-order terms may still distinguish the sources.

## Research consequence

The sparse/blockwise frontier can now be formulated more precisely. For proportional transport, the leading mesoscopic curvature question is not “what fraction of primes was moved?” but “what normalized log-moment profile does the moved family present to the boundary kernel?”

The next unresolved regime is therefore to replace the two-number limit `(\alpha_0,\alpha_2)` by a scale-dependent measure profile and determine which nonproportional, oscillatory, or mixed-direction transports are classified by finitely many moments and which require genuinely distributional information.