# FD-070 — Lipschitz spikes expand into persistent cubic four-adic packets but normalization is onset-optimal

**Status:** `EXACT-DERIVED + SOURCE-SPECIFIC + ARBITRARY-HORIZON-PACKET + ONE-LIPSCHITZ + FOUR-ADIC-NONSQUAREFREE + CUBIC-SPIKE-ENERGY + ZERO-FRONTIER-CALIBRATED + GROWING-SCHUR-HEAD + NORMALIZATION-OBSTRUCTION`.

`FD-069` removes host selection from pointwise spike capture: once a physical source spike at `X` passes its reciprocal-mesh threshold, every sufficiently later horizon contains a nonsquarefree row that still sees that spike. The same geometry has a stronger packet form. The exact one-Lipschitz law does not preserve merely one nearby source value; a spike of height `A_X` automatically creates a backward source interval of length comparable with `A_X` on which the source retains comparable size. At an arbitrary later horizon `T`, reciprocal-floor geometry expands that interval into a row packet of cardinality comparable with `T A_X/X^2`, and one quarter of those rows are deterministically divisible by four.

Consequently, if

\[
A_X:=|\mathcal H(X)|\to\infty,
\qquad A_X=o(X),
\qquad \frac{T A_X}{X^2}\to\infty,
\tag{1}
\]

and the Schur head satisfies `D<T/X`, then

\[
\boxed{
U_{T,D}
\ge
\left(\frac{1}{32\zeta(2)}-o(1)\right)
\frac{T A_X^3}{X^2}.
}
\tag{2}
\]

Thus the single-row `A_X^2` witness of `FD-069` becomes a **persistent cubic spike packet** after the capture scale: its absolute nonsquarefree energy grows linearly with every later horizon. This quantifier strengthening still does not repair the RH-facing normalization. On a zero-frontier spike `A_X=X^(Theta+o(1))`, the generic same-horizon denominator grows faster than the forced packet once `Theta>1/2`; among all later polynomial horizons the strongest scalar lower bound is therefore obtained at the **earliest** packet onset, not farther in the future. Optimizing the Schur head does not change that conclusion. With a fixed head the limiting packet exponent is

\[
\boxed{
\gamma_{\rm cubic}(\Theta)
=
\frac{2\Theta(1-\Theta)}{2-\Theta},
}
\tag{3}
\]

while the deterministic terminal mechanism has exponent `2Theta-1`. Their difference is

\[
\boxed{
\gamma_{\rm cubic}-(2\Theta-1)
=
\frac{2-3\Theta}{2-\Theta}.
}
\tag{4}
\]

Hence arbitrary-horizon persistence reproduces, rather than breaks, the `Theta=2/3` direct-packet boundary isolated in `FD-066`. The remaining missing input is genuinely denominator-coupled: one must beat the generic zero-frontier bound for `E_(T,D)` on horizons carrying the persistent packet, not merely obtain more rows or wait longer.

## 1. A coherent source interval produces a packet at every horizon

Retain

\[
w(r):=\frac{J_2(r)}{r^2},
\qquad
U_{T,D}:=
\sum_{\substack{D<r\le T\\ \mu(r)=0}}
 w(r)\mathcal H\!\left(\left\lfloor\frac Tr\right\rfloor\right)^2.
\tag{5}
\]

First state the geometric packet lemma independently of how source coherence is obtained. Let `1<=L<X` be an integer and suppose

\[
\boxed{
\min_{0\le h\le L}
|\mathcal H(X-h)|\ge B.
}
\tag{6}
\]

For an arbitrary integer horizon `T`, consider the row interval

\[
I_{T,X,L}
:=
\left[
\left\lceil\frac TX\right\rceil,
\left\lfloor\frac{T}{X-L}\right\rfloor
\right]\cap\mathbb Z.
\tag{7}
\]

Every `r` in this interval satisfies

\[
X-L
\le
\left\lfloor\frac Tr\right\rfloor
\le X.
\tag{8}
\]

Indeed, the lower endpoint in (7) gives `T/r<=X`, while the upper endpoint gives `T/r>=X-L`. Thus every row in `I_(T,X,L)` samples the coherent source interval (6).

The real width of the reciprocal image is

\[
W_{T,X,L}
:=
\frac{T}{X-L}-\frac TX
=
\frac{TL}{X(X-L)}.
\tag{9}
\]

After the two endpoint roundings, the integer interval contains at least `W_(T,X,L)-1` rows. Any interval of `N` consecutive integers contains at least `N/4-1` multiples of four, so

\[
\boxed{
\#\{r\in I_{T,X,L}:4\mid r\}
\ge
\left(\frac{W_{T,X,L}}4-2\right)_+.
}
\tag{10}
\]

If `D<T/X`, every row in (7) lies above the head. Every row counted in (10) is nonsquarefree, and

\[
w(r)=\prod_{p\mid r}(1-p^{-2})\ge\frac1{\zeta(2)}.
\tag{11}
\]

Therefore (6), (10), and (11) give the exact arbitrary-horizon packet bound

\[
\boxed{
U_{T,D}
\ge
\frac{B^2}{\zeta(2)}
\left(
\frac{TL}{4X(X-L)}-2
\right)_+.
}
\tag{12}
\]

No divisibility condition on `T`, selected host, residue class, short-interval theorem, or asymptotic density estimate enters (12). It is just reciprocal-floor geometry plus the deterministic net of four-divisible rows.

## 2. Every physical spike supplies its own coherence length

The physical shell source has the exact coefficient law used in `FD-036`, `FD-048`, and `FD-069`, hence

\[
|\mathcal H(n)-\mathcal H(m)|\le |n-m|
\qquad(n,m\in\mathbb N).
\tag{13}
\]

Let

\[
A_X:=|\mathcal H(X)|
\tag{14}
\]

and suppose `A_X>=4`. Put

\[
L_X:=\left\lfloor\frac{A_X}{2}\right\rfloor.
\tag{15}
\]

Whenever `L_X<X`, equation (13) implies, for `0<=h<=L_X`,

\[
|\mathcal H(X-h)|
\ge A_X-h
\ge \frac{A_X}{2}.
\tag{16}
\]

Thus (12) applies with `B=A_X/2` and `L=L_X`. If additionally `A_X=o(X)` and

\[
\frac{TA_X}{X^2}\to\infty,
\tag{17}
\]

then

\[
W_{T,X,L_X}
=
\left(\frac12+o(1)\right)
\frac{TA_X}{X^2}
\to\infty.
\tag{18}
\]

The additive constants in (12) are negligible, and one obtains

\[
\boxed{
U_{T,D}
\ge
\left(\frac1{32\zeta(2)}-o(1)\right)
\frac{TA_X^3}{X^2},
}
\tag{19}
\]

uniformly along any such pair sequence `(X,T)` for which `D<T/X`. This proves (2).

The factor `A_X^3` has a simple origin. One power of `A_X` is the source width forced by one-Lipschitz rigidity; two powers are the squared source height carried by each row. The reciprocal Jacobian contributes `T/X^2`. `FD-069` corresponds to the onset where `TA_X/X^2` is only order one, so only a bounded number of rows can be forced. Once that dimensionless parameter diverges, the same spike necessarily occupies a growing four-adic packet at **every** horizon, not merely on a chosen ray.

This also gives a clean matched control. For an arbitrary shell profile without the physical Lipschitz law, a spike may collapse immediately and (19) is false even though the reciprocal row geometry is unchanged. Conversely, for any one-Lipschitz profile, (12)--(19) are source-independent: no Möbius cancellation beyond the exact increment bound is being smuggled into the packet.

## 3. Zero-frontier calibration and the all-horizon packet exponent

Assume `1/2<Theta<1` and take a zero-frontier spike sequence from `FD-046`,

\[
A_X=X^{\Theta+o(1)}.
\tag{20}
\]

Let

\[
T=X^{\tau+o(1)},
\qquad
D=T^{\delta+o(1)},
\qquad
0\le\delta<1.
\tag{21}
\]

A polynomially growing packet requires

\[
\boxed{\tau>2-\Theta,}
\tag{22}
\]

because its cardinality is `T A_X/X^2=X^(tau+Theta-2+o(1))`. The packet survives the moving head at the power level when

\[
D<\frac TX,
\qquad\text{that is}\qquad
\boxed{\tau>\frac1{1-\delta}.}
\tag{23}
\]

Endpoint equality in either condition depends on constants and subpower factors, so only strict power inequalities are asserted here.

Equations (19)--(21) give

\[
\boxed{
U_{T,D}
\ge
X^{\tau+3\Theta-2+o(1)}.
}
\tag{24}
\]

For every fixed `sigma>Theta`, the zero-frontier envelope from `FD-046` gives

\[
E_{T,D}
\ll_\sigma
T^{2\sigma}\sum_{r>D}r^{-2\sigma}
\ll_\sigma
T^{2\sigma}D^{1-2\sigma}.
\tag{25}
\]

Writing

\[
a_\delta(\Theta)
:=\delta+2\Theta(1-\delta),
\tag{26}
\]

and letting `sigma` approach `Theta` from the right yields the packet-derived occupation lower bound, at the power scale,

\[
\boxed{
\nu_{T,D}:=\frac{U_{T,D}}{E_{T,D}}
\ge
X^{-\beta_{\rm occ}(\Theta,\tau,\delta)+o(1)},
}
\tag{27}
\]

where

\[
\boxed{
\beta_{\rm occ}
=
2-3\Theta
+\tau(2\Theta-1)(1-\delta).
}
\tag{28}
\]

More precisely, as usual for a frontier exponent, an arbitrary fixed positive epsilon may be inserted on the decay side of (27). Formula (28) is the power exponent relevant for comparison and optimization.

For the scalar Schur relaxation, `FD-065` gives

\[
\Delta_{T,D}=C_T-C_D=T^{-\delta+o(1)},
\qquad
\mathfrak D_{T,D}
=\Delta_{T,D}\varepsilon_{T,D},
\qquad
\varepsilon_{T,D}\ge\nu_{T,D}.
\tag{29}
\]

Hence the corresponding scalar decay exponent in `X` is

\[
\boxed{
\beta_{\rm sc}
=
2-3\Theta
+\tau\bigl((2\Theta-1)(1-\delta)+\delta\bigr).
}
\tag{30}
\]

The coefficient of `tau` is strictly positive. Therefore waiting to a later horizon can only weaken the power lower bound supplied by this persistent packet. Absolute nonsquarefree energy grows linearly with `T`, but the generic same-horizon denominator and, for a moving head, the Schur leverage grow or decay faster in the normalization that matters.

## 4. The earliest packet is optimal, and moving the head cannot improve the scalar exponent

For fixed `delta`, equations (22)--(23) show that the earliest admissible power horizon is

\[
\tau_0(\delta)
=
\max\left\{2-\Theta,\frac1{1-\delta}\right\}.
\tag{31}
\]

The two constraints meet at exactly the exponent already isolated in `FD-069`,

\[
\boxed{
\alpha_\Theta
:=\frac{1-\Theta}{2-\Theta}.
}
\tag{32}
\]

For raw occupation, increasing `delta` up to this crossover improves the denominator side. Substituting `tau=2-Theta` into (28) shows that `beta_occ` decreases from

\[
2\Theta(1-\Theta)
\tag{33}
\]

at `delta=0` to

\[
1-\Theta
\tag{34}
\]

at `delta=alpha_Theta`. For every `delta>=alpha_Theta`, the head-survival branch `tau=1/(1-delta)` gives the same `X`-exponent

\[
\boxed{\beta_{\rm occ}=1-\Theta.}
\tag{35}
\]

Thus a head moved almost up to the reciprocal witness can improve the **packet-derived raw occupation** bound, exactly as `FD-065` predicts.

The scalar quantity behaves in the opposite way. On the source-capture branch `delta<=alpha_Theta`, substituting `tau=2-Theta` in (30) gives

\[
\beta_{\rm sc}
=
2\Theta(1-\Theta)
+2(2-\Theta)(1-\Theta)\delta,
\tag{36}
\]

which is strictly increasing in `delta`. On the head-survival branch the extra leverage loss is larger still. Therefore the global optimum of this all-horizon cubic-packet mechanism is

\[
\boxed{
\delta=0,
\qquad
\tau\downarrow2-\Theta,
\qquad
\beta_{\rm sc,opt}=2\Theta(1-\Theta).
}
\tag{37}
\]

Since `T=X^(2-Theta+o(1))` at the limiting onset, the physical-horizon exponent is exactly (3):

\[
\boxed{
\gamma_{\rm cubic}(\Theta)
=
\frac{2\Theta(1-\Theta)}{2-\Theta}.
}
\tag{38}
\]

This is the `ell=Theta` specialization of the general coherence law in `FD-066`, now obtained from the automatic one-Lipschitz interval and with the stronger arbitrary-horizon quantifier. The stronger quantifier creates no new power gain because every additional row bought by increasing `T` is paid for by a still larger same-horizon normalization.

## 5. The two-thirds boundary survives persistent packet growth

The deterministic terminal-row mechanism of `FD-032`--`FD-065`, with fixed head, has scalar exponent

\[
\gamma_{\rm term}=2\Theta-1.
\tag{39}
\]

Subtracting from (38) gives

\[
\boxed{
\gamma_{\rm cubic}-\gamma_{\rm term}
=
\frac{2-3\Theta}{2-\Theta}.
}
\tag{40}
\]

Therefore the persistent cubic packet is a stronger scalar obstruction than the terminal mechanism precisely for

\[
\boxed{\Theta>\frac23,}
\tag{41}
\]

ties it at the power level when `Theta=2/3`, and is weaker when `1/2<Theta<2/3`.

This is an important falsification of a tempting inference from `FD-069`. The fact that one spike is visible on **all** sufficiently later horizons, and eventually on an unbounded number of nonsquarefree rows at each such horizon, does not accumulate into a better pointwise scalar exponent. The missing quantity is not packet cardinality. Below two thirds, the generic denominator can still grow quickly enough that the persistent packet is diluted faster than it expands.

Equivalently, the route left open by `FD-069` cannot be completed by waiting farther past the capture cone, replacing the single four-adic witness by its full one-Lipschitz packet, or moving the Schur head toward that packet. Any power improvement below the current boundary must instead supply a **same-horizon denominator saving correlated with the spike**, or source coherence longer than the automatic `A_X` scale, exactly as the general threshold in `FD-066` predicts.

## 6. Prior-art boundary and next use

A targeted search across classical Farey discrepancy, recent local-discrepancy work, Farey sequences with restricted squarefree or `k`-free denominators, Möbius/Farey transforms, and Jordan-totient formulations did not locate a theorem matching (12) or the cubic arbitrary-horizon consequence (19). No novelty is claimed for the elementary ingredients separately: the one-Lipschitz implication, reciprocal differentiation, density of multiples of four, or the standard zero-frontier envelope. The Mathia-specific content is their composition inside the exact Schur/Jordan energy and the resulting onset-optimal normalization law.

No external theorem beyond already anchored line dependencies is load-bearing, so `SOURCES.md` is unchanged.

The durable frontier is now narrower. `FD-069` shows that a spike cannot disappear absolutely after its capture cone; the present result shows that it in fact expands into a growing nonsquarefree packet at every later horizon. Yet even this strongest automatic local packet remains normalization-limited. A genuinely new step must therefore relate the current denominator `E_(T,D)` to the **same captured source episode** more sharply than the global bound (25), or prove source coherence on a scale `L_X` exceeding the automatic spike height by the amount quantified in `FD-066`. Merely increasing horizon persistence or four-adic packet multiplicity is exhausted by (30)--(40).
