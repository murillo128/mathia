# FD-048 — all-short-interval Möbius cancellation transfers to the shell source but does not prevent critical occupation escape

**Status:** `LITERATURE-DERIVED + EXACT-DERIVED + NEGATIVE/OBSTRUCTION + SHORT-INTERVAL-MOBIUS-TRANSFER + NEAR-HALF-POWER-SMOOTH-CONTROL + CRITICAL-POWER-MATCHED + JOINT-NONSQUAREFREE-OCCUPATION-BOUNDARY`.

`FD-039` proves that one-Lipschitz shell regularity and divergent critical energy do not force a positive nonsquarefree Jordan occupation fraction: sparse triangular shell spikes can make one fixed squarefree row dominate selected horizons. The natural source-specific response is to use cancellation in the actual coefficient sequence rather than the trivial bound `|Delta mathcal H|<=1`.

That response is available unconditionally. Matomäki--Teräväinen prove cancellation for the Möbius function in every interval of length at least `x^theta`, for any fixed `theta>0.55`, with a logarithmic saving. Because the physical shell coefficient is the Dirichlet convolution of `mu` with `n -> 1/n`, their theorem transfers directly to `mathcal H`. For every fixed `beta>0.55` and `0<eta<1/3`,

\[
\boxed{
\mathcal H(x+h)-\mathcal H(x)
\ll_{\beta,\eta}
\frac{h}{(\log x)^{1/3-\eta}}
\qquad
(x^\beta\le h\le x).
}
\tag{1}
\]

This genuinely excludes the unit-slope tents used in `FD-039`.

However, (1) is still far below the information needed for the joint-occupation clue. There is a single nonnegative synthetic shell profile `F` with

\[
\boxed{
|F(n+1)-F(n)|
\ll_\delta n^{-\delta}
\qquad\text{for every fixed }0<\delta<\frac12,
}
\tag{2}
\]

and therefore much stronger short-interval endpoint regularity than (1), while its critical square norm diverges, both its total and nonsquarefree Jordan energies have polynomial limsup exponent exactly `1`, and nevertheless

\[
\boxed{
\frac{U^F_{H_j,D}}{E^F_{H_j,D}}\longrightarrow0
}
\tag{3}
\]

along an unbounded sequence.

Thus **all-short-interval cancellation, even strengthened abstractly to an almost half-power pointwise smoothing law, does not by itself prevent hyperbola-sampling amplification**. The surviving theorem must use the arithmetic placement of the physical increments

\[
\Delta\mathcal H(n)
=
\frac{\mu(\operatorname{rad}n)\varphi(\operatorname{rad}n)}n,
\]

or an equivalent multiplicative/divisibility coupling, rather than only their aggregate short-interval cancellation.

## 1. Matomäki--Teräväinen cancellation transfers to the physical shell source

Write

\[
c(n):=\Delta\mathcal H(n)
=\frac{\mu(\operatorname{rad}n)\varphi(\operatorname{rad}n)}n.
\tag{4}
\]

The coefficient Dirichlet series from `FD-033` is

\[
\sum_{n\ge1}\frac{c(n)}{n^s}
=
\frac{\zeta(s+1)}{\zeta(s)}.
\tag{5}
\]

Equivalently, if `u(d)=1/d`, then

\[
\boxed{c=u*\mu,}
\tag{6}
\]

because

\[
c(n)=\sum_{dm=n}\frac{\mu(m)}d.
\tag{7}
\]

Hence for integers `x,h>=1`,

\[
\mathcal H(x+h)-\mathcal H(x)
=
\sum_{d\le x+h}\frac1d
\sum_{x/d<m\le(x+h)/d}\mu(m).
\tag{8}
\]

Matomäki--Teräväinen's Theorem 1.1 states that for fixed `theta>0.55` and `0<eta<1/3`, uniformly for sufficiently large `X` and `H>=X^theta`,

\[
\sum_{X<n\le X+H}\mu(n)
\ll_{\theta,\eta}
\frac{H}{(\log X)^{1/3-\eta}}.
\tag{9}
\]

Fix `beta>0.55`, choose `theta` with `0.55<theta<beta`, and then choose

\[
0<\delta_0<
\frac{\beta-\theta}{1-\theta}.
\tag{10}
\]

Split (8) at `d=x^{\delta_0}`. For `d<=x^{\delta_0}` and `x^\beta<=h<=x`,

\[
\frac hd
\ge
\left(\frac xd\right)^\theta
x^{\beta-\theta-\delta_0(1-\theta)},
\tag{11}
\]

so after harmless endpoint rounding the inner Möbius sum lies in the range of (9). Since `log(x/d) asymp log x` uniformly there,

\[
\sum_{d\le x^{\delta_0}}
\frac1d
\left|
\sum_{x/d<m\le(x+h)/d}\mu(m)
\right|
\ll
\frac{h}{(\log x)^{1/3-\eta}}
\sum_{d\ge1}\frac1{d^2}.
\tag{12}
\]

For `d>x^{\delta_0}`, the trivial estimate for the number of integers in the inner interval gives

\[
\sum_{d>x^{\delta_0}}\frac1d
\left(\frac hd+1\right)
\ll
hx^{-\delta_0}+\log x
=
o\!\left(
\frac{h}{(\log x)^{1/3-\eta}}
\right).
\tag{13}
\]

Equations (8)--(13) prove (1). No RH input is used.

## 2. A near-half-power-smooth matched control

Fix `D>=1` and choose a prime `r_0>D`. Choose integers

\[
K_1<K_2<\cdots
\]

so rapidly that

\[
K_{j+1}\ge K_j^4
\tag{14}
\]

and `sqrt(log K_j)` dominates `j`; enlarging the `K_j` recursively makes both requirements automatic.

Put

\[
L_j:=\log K_j,
\qquad
\sigma_j:=K_j^{-1/2}e^{\sqrt{L_j}},
\tag{15}
\]

\[
W_j:=
\left\lfloor
K_j e^{-\frac23\sqrt{L_j}}
\right\rfloor,
\qquad
A_j:=\sigma_jW_j.
\tag{16}
\]

Since `W_j/K_j -> 0`, the supports below are disjoint after enlarging `K_1`. Define

\[
T_j(k):=
\sigma_j\bigl(W_j-|k-K_j|\bigr)_+,
\tag{17}
\]

and

\[
F(0)=0,
\qquad
F(k)=\mathbf 1_{\{k=1\}}+\sum_{j\ge1}T_j(k).
\tag{18}
\]

This is the same sparse hyperbola-sampling architecture as `FD-039`, but the tents are now extremely flat and wide.

If `T_j(n)` or `T_j(n+1)` is nonzero, then `n=K_j(1+o(1))` and

\[
|F(n+1)-F(n)|\le\sigma_j
=
K_j^{-1/2}e^{\sqrt{\log K_j}}.
\tag{19}
\]

For every fixed `0<delta<1/2`,

\[
K_j^{-1/2}e^{\sqrt{\log K_j}}
=o(K_j^{-\delta}),
\tag{20}
\]

so (2) follows. In fact, for every fixed `0<delta<1/2` and all large `x<=y<=2x`,

\[
\boxed{
|F(y)-F(x)|
\ll_\delta
(y-x)x^{-\delta}.
}
\tag{21}
\]

This is obtained by summing the pointwise increments. It is much stronger than (1): for every fixed `A>0`, the right side of (21) is `o((y-x)/log^A x)` after choosing any fixed `0<delta<1/2`.

The profile is simultaneously critical in size. At the center of the `j`-th tent,

\[
A_j
=
(1+o(1))
K_j^{1/2}e^{\frac13\sqrt{L_j}},
\tag{22}
\]

so for every `epsilon>0`,

\[
\boxed{F(n)\ll_\epsilon n^{1/2+\epsilon}.}
\tag{23}
\]

Thus this control is at the same polynomial shell-growth exponent as the RH-scale physical source, while retaining enough subpower room for sparse amplification.

## 3. Every flattened tent still contributes constant critical energy

Let

\[
Q_F(K)
:=
\sum_{k\le K}
\frac{F(k)^2}{k(k+1)}.
\tag{24}
\]

The `j`-th tent contributes

\[
q_j
=
\sum_{|m|<W_j}
\frac{\sigma_j^2(W_j-|m|)^2}
{(K_j+m)(K_j+m+1)}.
\tag{25}
\]

Because `W_j/K_j->0`, the denominator is `K_j^2(1+o(1))` uniformly. The exact numerator identity

\[
\sum_{|m|<W}(W-|m|)^2
=
\frac{2W^3+W}{3}
\tag{26}
\]

therefore gives

\[
q_j
=
\left(\frac23+o(1)\right)
\frac{\sigma_j^2W_j^3}{K_j^2}.
\tag{27}
\]

But (15)--(16) were chosen so that

\[
\frac{\sigma_j^2W_j^3}{K_j^2}
=
1+o(1).
\tag{28}
\]

Hence

\[
\boxed{q_j=\frac23+o(1),}
\tag{29}
\]

and consequently

\[
\boxed{Q_F(K)\longrightarrow\infty.}
\tag{30}
\]

Flattening the tents to near-half-power slope therefore does not remove the critical square mass; it merely trades slope for width.

## 4. The synthetic Jordan energies have exactly the critical polynomial exponent

Define, with the same Jordan weight as the physical problem,

\[
w(r)=\frac{J_2(r)}{r^2},
\tag{31}
\]

\[
E^F_{H,D}
=
\sum_{D<r\le H}
w(r)F(\lfloor H/r\rfloor)^2,
\tag{32}
\]

\[
U^F_{H,D}
=
\sum_{\substack{D<r\le H\\\mu(r)=0}}
w(r)F(\lfloor H/r\rfloor)^2.
\tag{33}
\]

As in `FD-039`, `w(r)>=1/zeta(2)` and quotient-block counting give, for every fixed `K`,

\[
\liminf_{H\to\infty}\frac{E^F_{H,D}}H
\ge
\frac1{\zeta(2)}
\sum_{k\le K}\frac{F(k)^2}{k(k+1)}.
\tag{34}
\]

Letting `K->infinity` and using (30),

\[
\boxed{\frac{E^F_{H,D}}H\longrightarrow\infty.}
\tag{35}
\]

On the other hand, (23) gives for every `epsilon>0`

\[
E^F_{H,D}
\ll_{\epsilon,D}
H^{1+2\epsilon}
\sum_{r>D}r^{-1-2\epsilon}
\ll_{\epsilon,D}H^{1+2\epsilon}.
\tag{36}
\]

At the selected horizons below, one fixed row contributes

\[
\asymp
K_j e^{\frac23\sqrt{L_j}},
\tag{37}
\]

whose logarithmic power exponent is `1`. Therefore

\[
\boxed{
\limsup_{H\to\infty}
\frac{\log(1+E^F_{H,D})}{\log H}
=1.
}
\tag{38}
\]

The nonsquarefree energy has the same exponent. Indeed `U^F<=E^F` gives the upper bound, while for any fixed nonsquarefree `q>D`, the horizons `H=qK_j` contain the single nonsquarefree row `q` with contribution `w(q)A_j^2`. Hence

\[
\boxed{
\limsup_{H\to\infty}
\frac{\log(1+U^F_{H,D})}{\log H}
=1.
}
\tag{39}
\]

Thus equality of the total and nonsquarefree polynomial exponents, the physical conclusion isolated in `FD-046` under the RH-scale frontier, is not enough to force a same-horizon occupation fraction.

## 5. A squarefree row still captures the whole new spike

Set

\[
H_j:=r_0K_j.
\tag{40}
\]

Then row `r_0` samples the center exactly:

\[
\left\lfloor\frac{H_j}{r_0}\right\rfloor=K_j.
\tag{41}
\]

For every integer `r>D`, `r\ne r_0`,

\[
\left|
\frac{r_0K_j}{r}-K_j
\right|
\ge
\frac{K_j}{r_0+1}.
\tag{42}
\]

Since `W_j=o(K_j)`, no other row samples the current tent for large `j`. Future tents are beyond the horizon by (14).

Let `Q_{j-1}` be the critical mass of the initial pulse and all previous tents. By (29),

\[
Q_{j-1}=O(j).
\tag{43}
\]

The same quotient-block estimate as in `FD-039`, using the lacunarity to ensure the previous supports lie below the square-root quotient range, gives

\[
E^F_{\rm old}(H_j)
\le
2H_jQ_{j-1}
=
O_{D,r_0}(K_jj).
\tag{44}
\]

The current squarefree row contributes

\[
w(r_0)A_j^2
=
(1+o(1))w(r_0)
K_j e^{\frac23\sqrt{L_j}}.
\tag{45}
\]

Because `r_0` is prime, this contribution is absent from `U^F`. Therefore

\[
U^F_{H_j,D}
\le
E^F_{\rm old}(H_j)
=
O(K_jj),
\tag{46}
\]

whereas

\[
E^F_{H_j,D}
\ge
w(r_0)A_j^2.
\tag{47}
\]

Consequently

\[
\boxed{
\frac{U^F_{H_j,D}}{E^F_{H_j,D}}
\ll
j\,e^{-\frac23\sqrt{\log K_j}}
\longrightarrow0,
}
\tag{48}
\]

proving (3). At the same horizons,

\[
E^F_{H_j,D}
=
H_j^{1+o(1)}
\quad\text{and}\quad
\frac{E^F_{H_j,D}}{H_j}\longrightarrow\infty,
\tag{49}
\]

so the escape no longer relies on the `H^(4/3)` spike scale of `FD-039`; it survives arbitrarily close to the critical linear energy exponent.

## 6. What this rules out, and what it does not

Equation (1) is a genuine new unconditional property of the physical quotient-shell source. It rules out the literal unit-slope triangular mechanism used in `FD-039`, and it is sourced by state-of-the-art all-interval Möbius cancellation rather than by the elementary coefficient bound.

Equations (2)--(49) show that this improvement is nevertheless insufficient **as an abstract regularity input**. The matched profile has endpoint variation far smaller than the transferred Möbius bound on every comparable interval, has `n^(1/2+o(1))` shell size, divergent critical energy, and total/nonsquarefree Jordan energy exponent `1`, yet still realizes vanishing same-horizon occupation on sparse selected horizons.

There is no conflict with `FD-041` or `FD-047`. The scalar energy of this profile is deliberately multiplicatively irregular, so the dominated-scaling theorem of `FD-041` does not apply. Its bad horizons are superlacunary and jump between distinct fixed-dilation chains, exactly the sparse cross-chain escape left open by the geometric-mean and lower-tail controls in `FD-047`. Nor is there a conflict with `FD-042`--`FD-045`: the tents are not a uniformly conditioned low-dimensional Mellin packet.

The half-power in (2) is also a boundary of this particular tent mechanism, not a theorem that a `n^(-1/2)` increment modulus would settle the physical clue. With slope `K^(-delta)`, constant critical mass requires width `K^(2(1+delta)/3)` and the selected spike dominates the accumulated `O(H)`-per-tent background exactly while `delta<1/2`. At the endpoint `delta=1/2`, the required width becomes linear and the spike loses the superlinear factor used in (48). No converse is claimed there.

## 7. Prior art and falsification boundary

Matomäki--Teräväinen's all-short-interval Möbius theorem is prior art and is the only new load-bearing external input. Their published theorem gives (9) for every fixed `theta>0.55`; no novelty is claimed for that estimate. The transfer (6)--(13) is an elementary consequence of the already canonical coefficient identity `zeta(s+1)/zeta(s)` and Dirichlet convolution.

A targeted search around Farey discrepancy, the coefficient `mu(rad(n)) phi(rad(n))/n`, the Dirichlet series `zeta(s+1)/zeta(s)`, and Möbius cancellation in short intervals did not locate a theorem matching the joint Jordan-row consequence or the near-half-power matched control above. The synthetic construction is therefore used only as an implication-separation device, not as a claim of a new general theorem about short-interval multiplicative functions.

The finding is falsified if the convolution identity (6), the transfer estimate (12)--(13), the critical-mass normalization (27)--(29), or the selected-horizon separation (42)--(48) fails. It must not be cited as a counterexample for the actual Mertens quotient-shell source, as evidence that the physical occupation ratio ever vanishes, or as a weakening of the accepted clue. Its exact consequence is narrower: **known all-short-interval cancellation, and even an abstract near-half-power smoothing law far stronger than it, cannot close the joint nonsquarefree occupation problem without using the arithmetic placement of the physical coefficients.**
