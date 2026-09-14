# RE-111 — near-minimal Robin recovery forces first-layer PNT saturation packets

**Status:** `EXACT-DERIVED + INTER-BLOCK-RECOVERY + POSITIVE-WORKLOAD-PACKET + FIRST-LAYER-EXTRACTION + CHEBYSHEV-SATURATION + FALSE-RH-CONSEQUENCE + MATCHED-CONTROL + PRIOR-ART-AUDITED`.

`RE-110` shows that recovery from a positive adaptive Robin witness cannot be fast unless the full CA event workload develops a large positive forward defect. In particular, a recovery at the natural `RE-109` scale forces at least one crossed event to reach the full one-sided PNT envelope. That leaves a serious loophole: perhaps the recovery can be paid by one isolated extreme event, with the rest of the source behaving normally.

It cannot. The recovery budget is an **area** budget, while the PNT controls the height of the workload. Combining those two facts forces a packet of positive workload of macroscopic event mass. In the quantitative false-RH regime, the total higher-layer mass is asymptotically too small to carry that packet, so almost all of the marked event mass must lie on ordinary first-layer prime events. This converts the full-event statement of `RE-110` into a multiplicity statement for the ordinary Chebyshev error.

Let `C<D` be CA states, put

\[
Y:=\log C,\qquad V:=\log D,\qquad L:=V-Y,
\]

and assume

\[
h(C)>0,\qquad h(D)\le0,\qquad L\le Y.
\tag{1}
\]

Suppose that `C=C_b` is one of the quantitative adaptive witnesses of `RE-034`, for a fixed

\[
1-\Theta<b<\frac12.
\tag{2}
\]

Write

\[
\mathcal E(Y)
:=
\exp\!\left[-a(\log Y)^{3/5}(\log\log Y)^{-1/5}\right]
\tag{3}
\]

for the PNT envelope already used in `RE-109`--`RE-110`. Then there is a set `P(C,D)` of distinct primes whose **first-layer CA events are crossed between `C` and `D`** such that

\[
\boxed{
\sum_{p\in P(C,D)}\log p
\gg
\frac{h(C)Y\log Y}{\mathcal E(Y)},
}
\tag{4}
\]

and every `p in P(C,D)` satisfies

\[
\boxed{
p-\vartheta(p)
\gg
\frac{h(C)Y^2\log Y}{L}.
}
\tag{5}
\]

Since all these primes satisfy `p\asymp Y`, (4) gives

\[
\boxed{
\#P(C,D)
\gg
\frac{h(C)Y}{\mathcal E(Y)}.
}
\tag{6}
\]

For the false-RH quantitative witnesses, `h(C)\gg_JY^{-b}`, so

\[
\boxed{
\#P(C,D)
\gg_J
\frac{Y^{1-b}}{\mathcal E(Y)}.
}
\tag{7}
\]

The near-minimal recovery branch is stronger still. If

\[
L
\ll
\frac{h(C)Y\log Y}{\mathcal E(Y)},
\tag{8}
\]

then `RE-109` supplies the matching lower bound for `L`, and (5) becomes

\[
\boxed{
p-\vartheta(p)\asymp Y\mathcal E(Y)
\qquad (p\in P(C,D)).
}
\tag{9}
\]

Thus recovery near the minimum allowed by the unconditional PNT does not merely require one envelope-saturating event. It requires at least

\[
\gg_J Y^{1-b}/\mathcal E(Y)
\]

distinct ordinary primes with the **same favorable sign** and with Chebyshev deficit of full PNT-envelope order. Their first-layer atomic mass occupies a fixed positive proportion of the near-minimal recovery corridor.

## 1. Recovery area plus the PNT height bound forces a positive-mass workload packet

Use the physical/event partition from `RE-110`. A crossed event group at coordinate `eta_e`, of logarithmic mass `m_e`, occupies

\[
I_e=(u_e,u_e+m_e],
\qquad
u_e:=\Phi(\eta_e^-).
\tag{10}
\]

The intervals `I_e` partition `(Y,V]`. On each interval set

\[
Q(s):=\eta_e,
\qquad
f(s):=(Q(s)-s)_+.
\tag{11}
\]

Then the positive workload area of `RE-110` is exactly

\[
\mathcal W_+(C,D)=\int_Y^V f(s)\,ds.
\tag{12}
\]

Put

\[
A:=h(C)Y^2\log Y.
\tag{13}
\]

`RE-110` gives

\[
\mathcal W_+(C,D)\ge(1-o(1))A.
\tag{14}
\]

Because `L\le Y`, every physical coordinate `s` lies in `[Y,2Y]`. If `f(s)>0`, then `Q(s)>s`; the PNT estimate

\[
\Phi(x)=x+O(x\mathcal E(x))
\]

from `RE-109` forces `Q(s)\asymp Y` and hence uniformly

\[
0\le f(s)\ll Y\mathcal E(Y).
\tag{15}
\]

Let

\[
T:=\frac{A}{4L}
\tag{16}
\]

and define the high-forward-workload set

\[
S:=\{s\in(Y,V]:f(s)\ge T\}.
\tag{17}
\]

Writing `M:=\sup f`, equation (14) is at least `3A/4` for all sufficiently large witnesses, while

\[
\int_Y^V f(s)\,ds
\le
TL+M|S|
=
\frac A4+M|S|.
\tag{18}
\]

Therefore

\[
\boxed{
|S|
\gg
\frac{A}{Y\mathcal E(Y)}
=
\frac{h(C)Y\log Y}{\mathcal E(Y)}.
}
\tag{19}
\]

This is the first strengthening of `RE-110`: the positive recovery workload cannot live only at a single extremal event. A set of physical event mass of order at least (19) must see forward defect at least

\[
T
\asymp
\frac{h(C)Y^2\log Y}{L}.
\tag{20}
\]

The statement is a deterministic layer-cake consequence of the one-sided recovery area and the PNT supremum envelope. No distributional theorem for primes is used here.

## 2. Higher layers have too little mass to carry the marked event groups

Let `G_S` be the set of crossed event groups whose physical intervals `I_e` meet `S`. Since the intervals are disjoint and their union covers `S`, the total logarithmic mass of groups in `G_S` is at least `|S|`.

The packet is initially a packet of **full CA event groups**, so it could in principle be supported mostly on higher layers. The quantitative false-RH range excludes that possibility by a power margin. As in `RE-109`, the total logarithmic mass of all higher-layer events up to scale `x` satisfies

\[
\Phi_{\ge2}(x)
\ll
\sqrt{x}(\log x)^{3/2}.
\tag{21}
\]

All event coordinates in `G_S` are `\asymp Y` by the same PNT localization used in (15), so the entire higher-layer atomic mass available to those groups is at most

\[
O\!\left(\sqrt Y(\log Y)^{3/2}\right).
\tag{22}
\]

For an adaptive false-RH witness, `h(C)\gg_JY^{-b}` with fixed `b<1/2`. Hence the packet scale in (19) is

\[
\frac{h(C)Y\log Y}{\mathcal E(Y)}
\gg_J
\frac{Y^{1-b}\log Y}{\mathcal E(Y)},
\tag{23}
\]

and

\[
\frac{\sqrt Y(\log Y)^{3/2}}
{Y^{1-b}\log Y/\mathcal E(Y)}
\ll_J
Y^{b-1/2}(\log Y)^{1/2}\mathcal E(Y)
=o(1).
\tag{24}
\]

Consequently, after removing **all** higher-layer atoms from the marked groups, their remaining first-layer atomic mass is still

\[
\boxed{
\gg
\frac{h(C)Y\log Y}{\mathcal E(Y)}.
}
\tag{25}
\]

Ties cause no allocation ambiguity here: the argument counts the complete mass of every group meeting `S` and then subtracts the total higher-layer mass globally. It does not assign points of `S` to individual tied atoms.

Each surviving first-layer atom is indexed by one distinct ordinary prime `p`, has mass `\log p`, and has event coordinate `\eta_1(p)`. Since `\eta_1(p)-p=O(1)` by `RE-042`/`RE-069` and `\eta_1(p)\asymp Y`, we have `p\asymp Y` and `\log p\asymp\log Y`. Dividing (25) by the maximal atomic mass proves (4) and (6).

## 3. Every marked first-layer group transfers to an ordinary Chebyshev deficit

Let a marked group in `G_S` contain a first-layer atom indexed by `p`, and write `\eta=\eta_1(p)`. Since its interval meets `S`, there exists `s\in I_e\cap S`, and therefore

\[
\eta-s\ge T.
\tag{26}
\]

The group begins at `u_e=\Phi(\eta^-)\le s`, so

\[
\eta-\Phi(\eta^-)
\ge T.
\tag{27}
\]

The decomposition used in `RE-109` gives, uniformly on this scale,

\[
\Phi(x^-)
=
\vartheta(x^-)
+O\!\left(\sqrt Y(\log Y)^{3/2}\right).
\tag{28}
\]

The threshold (20) is much larger than this error throughout the quantitative false-RH branch. Indeed `L\le Y` and `h(C)\gg_JY^{-b}` imply

\[
T
\gg_J
Y^{1-b}\log Y,
\tag{29}
\]

whereas the error in (28) is only `Y^{1/2}(\log Y)^{3/2}`; their ratio tends to infinity because `b<1/2`. Thus (27)--(29) give

\[
\eta-\vartheta(\eta^-)
\gg
T.
\tag{30}
\]

For a first-layer event, `RE-069` gives

\[
p<\eta_1(p)<p+\frac12
\tag{31}
\]

for all sufficiently large `p`. Hence there is no ordinary prime between `p` and `\eta_1(p)`, so

\[
\vartheta(\eta_1(p)^-)=\vartheta(p),
\tag{32}
\]

and

\[
p-\vartheta(p)
=
\eta_1(p)-\vartheta(\eta_1(p)^-)+O(1).
\tag{33}
\]

Combining (20), (30), and (33) proves (5). This is the second strengthening of `RE-110`: the forced packet is carried by ordinary first-layer primes and is visible directly in the standard Chebyshev race.

## 4. Near-minimal recovery forces a packet at the full one-sided PNT envelope

Assume now (8). `RE-109` already gives

\[
L
\gg
\frac{h(C)Y\log Y}{\mathcal E(Y)},
\tag{34}
\]

so `L` is comparable with that natural scale. Substituting (8) into (5) yields

\[
p-\vartheta(p)
\gg
Y\mathcal E(Y).
\tag{35}
\]

The ordinary PNT remainder gives the reverse bound

\[
|p-\vartheta(p)|
\ll
Y\mathcal E(Y)
\tag{36}
\]

uniformly for `p\asymp Y`. This proves (9).

Moreover (4) and the near-minimal upper bound (8) show that the marked first-layer mass is `\gg L`. Since it is also at most the total crossed physical mass `L`, a fixed positive proportion of the whole recovery is carried by first-layer atoms in marked groups whose ordinary Chebyshev error has the favorable sign and saturates the unconditional PNT envelope up to constants.

Thus the minimal-scale escape remaining after `RE-109`--`RE-110` has become substantially more rigid:

\[
\boxed{
\text{near-minimal Robin recovery}
\Longrightarrow
\text{a positive-mass packet of one-sided first-layer PNT saturation.}
}
\tag{37}
\]

An isolated extreme prime or one exceptional higher-layer event cannot pay the recovery bill.

## 5. Matched control and sharpness of the packet scale

The packet exponents cannot be improved from the information used above alone. Consider a relaxed monotone event staircase on a local interval of physical length

\[
L_0
\asymp
\frac{hY\log Y}{\mathcal E(Y)}.
\tag{38}
\]

Split the interval into atoms of mass `\asymp\log Y`, and place their event coordinates so that each forward defect is

\[
M\asymp Y\mathcal E(Y).
\tag{39}
\]

Then the positive workload area is

\[
L_0M
\asymp
hY^2\log Y,
\tag{40}
\]

exactly the recovery budget of `RE-110`, while the number of atoms is

\[
\asymp
\frac{L_0}{\log Y}
\asymp
\frac{hY}{\mathcal E(Y)}.
\tag{41}
\]

This realizes the orders in (4)--(6) and, in the near-minimal branch, the saturation order in (9). The control is deliberately not asserted to arise from the ordinary primes. It shows that **area lower bound + PNT height envelope + logarithmic atomic masses** already determine the packet scale, so a further gain must exploit arithmetic structure of the actual prime source.

The higher-layer elimination is also quantitatively essential. Without the false-RH amplitude floor with `b<1/2`, the packet mass in (19) need not dominate the available higher-layer mass, and no first-layer extraction follows from this argument alone.

## 6. Prior-art boundary and research consequence

Large-value and concentration questions for the PNT error are classical, and recent work such as Bryce Kerr's study of large values of the PNT error investigates how large-error sets can concentrate under RH. Recent work of Bhattacharya--Martin--Simpson likewise studies correlations between weighted prime-counting errors. This finding does not claim a new unconditional density theorem for ordinary PNT errors. Its direction is the reverse and is conditional on the Mathia false-RH adaptive setup: **if a CA-selected Robin recovery is near-minimal, then the recovery itself forces a large same-sign packet of ordinary Chebyshev saturation points at first-layer event primes**. The existing literature audit did not identify this CA-selected implication.

No new external theorem is load-bearing. The PNT envelope, first-layer timing law, higher-layer mass estimate, adaptive amplitude floor, and recovery quadrature are all already anchored in `SOURCES.md` through earlier findings.

The next source-specific target is therefore sharper than the `RE-110` maximum-defect condition. It is enough to rule out, among the first-layer primes selected by a CA recovery, packets of

\[
\gg_J Y^{1-b}/\mathcal E(Y)
\]

distinct primes simultaneously satisfying

\[
p-\vartheta(p)\asymp Y\mathcal E(Y)
\]

with the recovery-favorable sign. Any theorem making such packets `o(hY/\mathcal E(Y))`, or forcing significant cancellation through the reciprocal-Mertens coordinate on the same packet, would push recovery strictly beyond the `RE-109` scale without requiring a stronger global PNT remainder.