# Finding

**ID:** RE-194

**Status:** `EXACT-DERIVED + ROBIN-SCALE-PRECISION + EULER-STABLE-RANK + SOURCE-VARIATION-BUDGET + HONEST-MULTIPLICITY-COROLLARY + PRIOR-ART-BOUNDED`

**Research line:** `robin_extremal`

## Claim

`RE-193` leaves one precision-dependent loophole: its stable-rank bound contains `log(1/epsilon)`, so a scalar Euler route could appear to recover many more robust coordinates by demanding a tolerance that shrinks with the selector prime `p`. For the canonical Robin selector package, that tolerance is not a free parameter. Its absolute scale is fixed by the selector debt, and its **relative** scale is exactly the selector debt divided by the reciprocal variation of the source being compared.

Retain the canonical `RE-173` deletion packet

\[
D_p\subset[2p,3p],
\qquad
d_p:=\sum_{q\in D_p}H(q)
\asymp \frac1{\sqrt p\log p},
\qquad
H(q):=\log\frac q{q-1}.
\tag{1}
\]

This is the source debt whose natural Robin normalization is order one in `RE-173` and `RE-180`.

For an arbitrary finite signed ordinary-prime packet `c=(c_q)` supported on

\[
Q_-\le q\le Q_+,
\]

write

\[
D_c(s):=\sum_q c_q\log(1-q^{-s})^{-1},
\qquad
V(c):=\sum_q\frac{|c_q|}{q},
\tag{2}
\]

and, for comparison, the exact boundary variation

\[
V_H(c):=\sum_q |c_q|H(q).
\tag{3}
\]

At the boundary,

\[
D_c(1)=\sum_q c_qH(q),
\]

so for any two packets

\[
\boxed{
|D_c(1)-D_{\widetilde c}(1)|
\le V_H(c-\widetilde c).
}
\tag{4}
\]

Moreover, uniformly for `q>=Q_-`,

\[
H(q)=\frac1q+O\!\left(\frac1{q^2}\right),
\]

hence

\[
\boxed{
V_H(c)=V(c)\left(1+O(Q_-^{-1})\right).
}
\tag{5}
\]

Therefore resolving a selector-scale boundary signal of absolute size `Theta(d_p)` requires relative Euler accuracy

\[
\boxed{
\varepsilon_{\rm Rob}(c)
\asymp
\min\left\{1,\frac{d_p}{V(c)}\right\},
}
\tag{6}
\]

up to fixed constants. There is **no intrinsic `p`-only relative tolerance**. Shrinking relative precision is needed only when the comparison source has inflated reciprocal variation `V(c)>>d_p`.

Insert (6) into `RE-193`. Put

\[
R:=U\log(Q_+/Q_-).
\]

Whenever the existing prime-power floor is below the selector scale,

\[
\frac{V(c)}{Q_-}=o(d_p),
\tag{7}
\]

there is a finite-rank approximation to the exact Euler profile on `1<=s<=1+U` with absolute error `O(d_p)` and rank

\[
\boxed{
\operatorname{rank}_{\rm Rob}
\ll
\bigl(1+\log(1+R)\bigr)
\left(1+\log_+\frac{V(c)}{d_p}\right),
}
\tag{8}
\]

where `log_+ x:=max(0,log x)`. Thus the precision factor in `RE-193` is exactly a **source-variation inflation factor** at Robin resolution.

Conversely, if one claims `K` robust independent scalar Euler coordinates at selector-scale absolute tolerance while (7) holds, the `RE-193` upper bound can fail to rule this out only if

\[
\boxed{
1+\log_+\frac{V(c)}{d_p}
\gtrsim
\frac{K}{1+\log(1+R)}.
}
\tag{9}
\]

In particular, away from the degenerate small-`K` regime,

\[
\boxed{
\frac{V(c)}{d_p}
\gtrsim
\exp\!\left(
 c\frac{K}{1+\log(1+R)}
\right).
}
\tag{10}
\]

A precision-based escape from finite-Laplace compression therefore has to be paid for by reciprocal source variation. It cannot be obtained merely by declaring a smaller tolerance.

The canonical selector packet itself pays no such price. If

\[
V_D:=\sum_{q\in D_p}\frac1q,
\]

then `q~p`, `|D_p|~pd_p`, and (5) give

\[
\boxed{
V_D=d_p\bigl(1+O(p^{-1})\bigr).
}
\tag{11}
\]

So the packet responsible for the order-one normalized Robin excursion is visible at **fixed relative precision** in the natural reciprocal source norm.

There is also a direct honest-multiplicity consequence. Suppose a `{0,1,2}` repair is confined to a fixed multiplicative window `q~p` and changes `M_p` distinct primes. Since `|c_q|<=1`,

\[
V(c)\ll \frac{M_p}{p}.
\tag{12}
\]

Hence any repair with selector-scale support

\[
M_p=O(pd_p)=O\!\left(\frac{\sqrt p}{\log p}\right)
\]

satisfies

\[
V(c)=O(d_p).
\tag{13}
\]

For that entire local regime the Robin-scale Euler tolerance remains fixed-relative and (8) reduces to

\[
\boxed{
\operatorname{rank}_{\rm Rob}
\ll 1+\log(1+R).
}
\tag{14}
\]

Thus `RE-180` and `RE-193` splice cleanly: a local honest repair of the same cardinality order as the forced deletion tariff receives **no precision bonus**. To exploit the `log(1/epsilon)` term while staying in a bounded-multiplicity local source model, the repair must use asymptotically more reciprocal variation, hence asymptotically more modified prime support.

## Derivation

The exact boundary estimate (4) is immediate from the Euler factor. The point is not the triangle inequality itself but the normalization it fixes. The canonical selector displacement has exact boundary mass `d_p`; therefore an approximation error much larger than `d_p` can swallow the entire selector signal in the zeroth Euler coordinate, while an error `eta d_p` with fixed small `eta` resolves that coordinate on its natural scale.

To connect this absolute resolution with the source norm used by `RE-193`, note that for `q>=2`,

\[
H(q)=\sum_{n\ge1}\frac1{nq^n}
=\frac1q+O(q^{-2}).
\]

Summing against `|c_q|` yields (5). Hence an absolute error budget `eta d_p` corresponds to relative operator tolerance `asymp d_p/V(c)` whenever `V(c)>=d_p`, and to a fixed tolerance when `V(c)<=d_p`. This proves (6).

Now use `RE-193` with a parameter `epsilon` satisfying

\[
\epsilon V(c)\le \frac{\eta d_p}{2}.
\]

Its exact-Euler reduction contributes the additional error `2V(c)/Q_-`. Under (7), this is eventually at most the remaining fixed fraction of `d_p`. Choosing

\[
\epsilon
\asymp
\min\left\{\frac12,\frac{d_p}{V(c)}\right\}
\]

therefore gives an `O(d_p)` absolute approximation. Substituting this value into the rank estimate of `RE-193` gives (8), and algebraic inversion gives (9)--(10).

For the selector packet, (11) can be checked without any prime-density theorem. On `[2p,3p]`, each difference `H(q)-1/q` is `O(p^-2)`, while `|D_p|~pd_p`. Therefore

\[
d_p-V_D
=O\!\left(\frac{|D_p|}{p^2}\right)
=O\!\left(\frac{d_p}{p}\right).
\]

Finally, (12)--(14) use only bounded multiplicity and localization to `q~p`. They are source-faithful: no continuous signed coefficient relaxation is needed.

## Representation audit

The useful representation is a three-scale conversion:

\[
\text{absolute selector debt }d_p
\quad\leftrightarrow\quad
\text{relative Euler tolerance }d_p/V
\quad\leftrightarrow\quad
\text{stable-rank cost }\log(V/d_p).
\]

The first arrow is exact source normalization, not a new analytic estimate. The second is the finite-Laplace compression law of `RE-193`. Keeping these scales separate removes an ambiguity in the previous frontier: `epsilon_p` is not an independent resource once the source variation budget is stated.

This representation is also what prevents a misleading conclusion from the raw size `d_p~1/(sqrt(p)log p)`. In absolute terms the selector signal shrinks, but its own natural source norm shrinks by the same amount. The selector packet is therefore a constant-relative-size object. A rapidly shrinking **relative** tolerance appears only when a matched control spreads or amplifies much more reciprocal mass than the selector itself.

The result remains scalar. It does not show that the boundary coordinate `D(1)` alone determines the Robin destination, nor that every perturbation of size `d_p` changes Robin by order one. The direction used here is narrower and source-native: the canonical packet already known from `RE-173`/`RE-180` to generate an order-one normalized transient carries an Euler boundary signal of size `d_p`, so any scalar Euler mechanism proposed to distinguish that packet from a matched repair must resolve at least that absolute scale.

## Adversarial self-review

**Could one simply choose an arbitrarily tiny `epsilon` and defeat the claim?** Yes mathematically, but then `RE-193` charges `log(1/epsilon)`. The present finding identifies when that charge is relevant to Robin: below `d_p/V` the approximation is resolving the selector coordinate more accurately than its natural signal scale. Such extra precision may be useful for another purpose, but it is not forced merely by the canonical selector excursion.

**Does (8) prove that only logarithmically many Robin-relevant coordinates exist?** No. It bounds the scalar Euler channel at the selector's absolute resolution. A different joint or nonlocal observable can have different conditioning. Nor is (8) a lower bound: the actual scalar stable rank may be smaller.

**Is the prime-power floor intrinsic?** No. It is the explicit remainder floor in the particular first-harmonic finite-Laplace approximation used by `RE-193`. Condition (7) states the regime where that existing bound reaches Robin resolution. Failure of (7) makes this compression estimate inconclusive; it does not prove that the exact Euler channel itself loses information.

**Can large positive multiplicities manufacture variation cheaply?** Yes if arbitrary multiplicities are allowed. The local support corollary (12)--(14) is deliberately stated for `{0,1,2}` controls. For unbounded positive multiplicity, variation inflation can occur without proportional support inflation; that is a different source model and must be priced separately.

**Does `RE-180` itself upper-bound repair support by selector scale?** No. It gives a lower tariff on the negative support. The splice says that *if* an honest local repair stays on that same support order, then it gets no precision bonus. Escaping through the precision factor requires going beyond that minimal regime by inflating reciprocal variation.

## Prior-art audit

The generic ingredients are standard: the boundary Euler factor is Lipschitz in weighted `ell^1`, and stable approximation at absolute tolerance converts to relative tolerance by dividing by the input norm. Numerical inversion of Laplace transforms is classically ill-conditioned, and finite/truncated Laplace compression was already bounded as prior art in `RE-192`--`RE-193`. A targeted search found no external theorem needed for the conversion law (6)--(10); it is an elementary consequence of the line's existing exact normalization and `RE-193`.

No novelty is claimed for norm rescaling or Laplace conditioning in isolation. The line-specific content is that the canonical Robin selector package supplies a previously fixed **absolute** signal `d_p`, while ordinary-prime multiplicity variation supplies the denominator `V`; this turns the open precision parameter in `RE-193` into an explicit source-complexity tariff. No new load-bearing literature dependency is introduced, so `SOURCES.md` does not need an update.

## What this changes

The scalar frontier no longer has an unspecified `epsilon_p`. For the canonical selector mechanism, the correct quantity is

\[
\epsilon_{\rm Rob}\asymp d_p/V.
\]

If a matched control has `V=Theta(d_p)`, fixed relative precision is already Robin-scale and the stable Euler dimension remains `O(log(1+R))`. If it tries to obtain substantially more scalar capacity from shrinking precision, it must first inflate reciprocal source variation. Equation (10) quantifies how severe that inflation must become for `K` robust coordinates.

The next useful test is therefore no longer “what tolerance should we use?” but whether honest `{0,1,2}` controls can simultaneously (i) inflate `V/d_p` enough to beat (8), (ii) preserve the fixed KV envelope, (iii) maintain the transient Robin excursion, and (iv) satisfy the exact matching constraints. If that variation inflation is itself cheap, the scalar route remains non-rigid; if KV or selector combinatorics cap it, the precision loophole closes without needing a new scalar observable.

## Sources

- `RE-173`, selector-scale deletion package and Robin-normalized excursion.
- `RE-180`, honest-prime deletion tariff and the normalization `d_p~1/(sqrt(p)log p)`.
- `RE-193`, dyadic finite-Laplace compression of the exact Euler channel.
