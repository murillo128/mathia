# FD-135 — local ancestry rigidity has an exact rough-core threshold

**Status:** `EXACT-DERIVED + PRIME-PREFIX-ANCESTRY + FIXED-RANK-ANCHOR + ROUGH-CORE-COMPONENTS + SHARP-FINITE-HORIZON-RECOVERY + LOCAL-LINFINITY-THRESHOLD + NEGATIVE/BOUNDARY`.

`FD-130`--`FD-134` progressively show that several averaged forms of approximate prime ancestry can vanish while a squarefree-unit source remains macroscopically non-Möbius. Those findings leave a genuinely local condition as one of the obvious repairs: instead of averaging defective prime edges, require every active ancestry edge to be small. In the squarefree-unit source class this turns out not to create a new soft regime. There is an exact finite-horizon threshold, determined solely by the first sufficiently high-rank rough core, at which local ancestry plus a finite Möbius anchor reconstructs the entire physical source.

Fix integers `H>=1`, `K>=0`, and a real prime cutoff `Y>=1`. Let `a_1,...,a_H` satisfy

\[
a_n=0\quad(n\le H\text{ nonsquarefree}),
\qquad
a_n\in\{-1,+1\}\quad(n\le H\text{ squarefree}),
\tag{1}
\]

with the fixed-rank Möbius anchor

\[
\boxed{
a_n=\mu(n)
\quad\text{for every squarefree }n\le H\text{ with }\omega(n)\le K.
}
\tag{2}
\]

For squarefree admissible prime edges define the local ancestry defect

\[
\mathfrak D_{\infty}(H,Y;a)
:=
\max_{\substack{p\le Y\text{ prime}\\n\le H/p\text{ squarefree}\\p\nmid n}}
|a_{pn}+a_n|,
\tag{3}
\]

with value `0` if the edge set is empty. Let

\[
p_1^+(Y)<p_2^+(Y)<\cdots
\tag{4}
\]

be the primes strictly larger than `Y`, and put

\[
\boxed{
Q_{K+1}(Y):=\prod_{j=1}^{K+1}p_j^+(Y).
}
\tag{5}
\]

Then the following boundary is exact:

\[
\boxed{
Q_{K+1}(Y)>H
\quad\Longleftrightarrow\quad
\text{the anchor (2) and exact ancestry through }Y
\text{ force }a_n=\mu(n)\text{ for every }n\le H.
}
\tag{6}
\]

Moreover, because the source values are unit signs, every summand in (3) is either `0` or `2`. Hence

\[
\boxed{
\mathfrak D_{\infty}(H,Y;a)<2
\quad\Longleftrightarrow\quad
\mathfrak D_{\infty}(H,Y;a)=0,
}
\tag{7}
\]

so the same sharp threshold applies to every genuinely local defect condition once it drops below `2`. In particular, a vanishing `L^\infty` ancestry defect is eventually **exact ancestry**, not an intermediate approximation, in this source class.

A convenient deterministic corollary is

\[
\boxed{
Y^{K+1}\ge H
\quad\Longrightarrow\quad
Q_{K+1}(Y)>H
\quad\Longrightarrow\quad
a\equiv\mu\text{ on }[1,H].
}
\tag{8}
\]

Thus a rank-`K` anchor combined with exact/local ancestry through only the polynomial cutoff `Y=H^{1/(K+1)}` already reconstructs the entire horizon. For example, if the source is anchored at rank `1`—so `1` and every prime already have their Möbius values—then ancestry through primes up to `sqrt(H)` leaves no synthetic freedom anywhere below `H`. A rank-`2` anchor lowers that deterministic breadth threshold to `H^{1/3}`.

The converse in (6) is constructive. If `Q_{K+1}(Y)<=H`, one can flip exactly the ancestry component whose `Y`-rough core is `Q_{K+1}(Y)`. The resulting source agrees with Möbius at every rank at most `K`, satisfies **every** ancestry identity for primes `p<=Y`, and nevertheless differs from Möbius below `H`. Hence the threshold is not merely a sufficient estimate obtained from `FD-029`; it exactly classifies when fixed-rank anchoring kills the residual rough-core gauge freedom.

## 1. Exact prime ancestry is constancy on rough-core components

For squarefree `n<=H`, split uniquely

\[
n=q_Y(n)r_Y(n),
\tag{9}
\]

where every prime factor of `q_Y(n)` is at most `Y` and every prime factor of `r_Y(n)` is strictly larger than `Y`. Thus `r_Y(n)` is the `Y`-rough core of `n`.

Introduce the Möbius gauge

\[
g(n):=\mu(n)a_n
\qquad(n\text{ squarefree}).
\tag{10}
\]

For an admissible edge `n -> pn`, with `p<=Y`, squarefreeness gives `mu(pn)=-mu(n)`, and therefore

\[
g(pn)-g(n)
=
-\mu(n)(a_{pn}+a_n).
\tag{11}
\]

Consequently exact ancestry

\[
a_{pn}=-a_n
\tag{12}
\]

is equivalent to

\[
g(pn)=g(n).
\tag{13}
\]

Multiplication or division by active primes `p<=Y` never changes the rough core. Conversely, every squarefree integer with rough core `r` is reached from `r` by multiplying by the active prime divisors of its smooth part. Hence the connected components of the exact ancestry graph are **exactly** the rough-core classes, and

\[
\boxed{
g(n)=c_{r_Y(n)}}
\tag{14}
\]

for arbitrary component signs `c_r in {+1,-1}` indexed by squarefree `Y`-rough cores `r<=H`.

This is the gauge form of the rough-core parametrization in `FD-029`. It is useful here because the fixed-rank anchor has an immediate graph interpretation.

## 2. The rank anchor pins exactly the low-rank rough cores

If a rough core `r` satisfies

\[
\omega(r)\le K,
\tag{15}
\]

then `r` itself lies in the anchored set (2). Thus

\[
g(r)=\mu(r)a_r=1,
\tag{16}
\]

and (14) forces

\[
c_r=1
\tag{17}
\]

throughout that entire component.

Conversely, if `omega(r)>=K+1`, every member `qr` of the same component has

\[
\omega(qr)\ge\omega(r)\ge K+1,
\tag{18}
\]

so the rank-`K` anchor never touches the component. Its sign `c_r` remains completely free. We therefore obtain the exact finite-scale solution space

\[
\boxed{
 a_n
 =
 \mu(n)c_{r_Y(n)},
 \qquad
 c_r=1\ \text{if }\omega(r)\le K,
 \qquad
 c_r\in\{\pm1\}\ \text{if }\omega(r)\ge K+1.
}
\tag{19}
\]

There is no hidden coupling between two different rough cores. In particular, the number of remaining binary degrees of freedom is exactly

\[
\#\{r\le H:r\text{ squarefree and }Y\text{-rough},\ \omega(r)\ge K+1\}.
\tag{20}
\]

Thus the full horizon is reconstructed precisely when the set in (20) is empty.

## 3. The first free component gives the sharp threshold

Among squarefree `Y`-rough integers with at least `K+1` prime factors, the smallest possible one is the product of the first `K+1` primes strictly larger than `Y`:

\[
Q_{K+1}(Y)
=
p_1^+(Y)\cdots p_{K+1}^+(Y).
\tag{21}
\]

Indeed, if

\[
r=q_1\cdots q_m,
\qquad
m\ge K+1,
\qquad
Y<q_1<\cdots<q_m,
\tag{22}
\]

then termwise `q_j>=p_j^+(Y)` for `1<=j<=K+1`, and therefore

\[
r\ge Q_{K+1}(Y).
\tag{23}
\]

If `Q_{K+1}(Y)>H`, no free component in (20) exists, so (19) gives `a_n=mu(n)` for every squarefree `n<=H`; nonsquarefree coefficients already agree by (1). This proves the forward implication in (6).

If instead

\[
Q_{K+1}(Y)\le H,
\tag{24}
\]

put `r_*=Q_{K+1}(Y)`. Set `c_(r_*)=-1` and `c_r=1` for every other rough core. Equation (19) then defines a legal source satisfying every exact ancestry equation through `Y` and every anchor equation through rank `K`, while

\[
a_{r_*}=-\mu(r_*)\ne\mu(r_*).
\tag{25}
\]

This proves the converse and supplies the matched control at the exact boundary. The control does not exploit horizon-dependent weakening of the ancestry law: its local defect is identically zero.

## 4. Why the crude polynomial threshold is enough, but not the exact boundary

Every prime factor of a nontrivial `Y`-rough core is strictly larger than `Y`. Hence

\[
Q_{K+1}(Y)>Y^{K+1}.
\tag{26}
\]

This proves (8) immediately. The exponent `1/(K+1)` is therefore a deterministic recovery scale requiring no information about prime gaps or rough-number density.

The exact criterion is nevertheless (6), not simply `Y^{K+1}>H`. Prime discreteness can make `Q_{K+1}(Y)` noticeably larger than `Y^{K+1}` at finite scale, and recovery may occur before the crude power inequality predicts it. Conversely, whenever `Q_{K+1}(Y)<=H`, the explicit component flip above shows that no argument using only the rank anchor and exact ancestry through `Y` can distinguish the synthetic source from Möbius on the entire horizon.

This sharpens the interaction-order statement of `FD-029`. There, `Y>=H^beta` bounds the rank of every surviving rough core. Here the additional rank-`K` Möbius anchor converts that bounded interaction order into a complete **uniqueness criterion** and identifies the exact first horizon at which all residual signs disappear.

## 5. Local ancestry is qualitatively different from the averaged regimes

For the unit-sign class (1), every admissible edge has

\[
a_{pn}+a_n\in\{-2,0,2\},
\tag{27}
\]

which proves (7). Thus any hypothesis of the form

\[
\mathfrak D_{\infty}(H,Y;a)\longrightarrow0
\tag{28}
\]

contains no asymptotically small nonzero defects: once the quantity is below `2`, all active prime edges satisfy exact ancestry.

This is precisely where the route separates from `FD-130`--`FD-134`. Their witnesses keep individual bad edges of full magnitude `2` but make those edges sparse inside increasingly large averages. A supremum norm cannot dilute such an interface. However, after it removes the averaging loophole, it immediately falls back onto the exact rough-core component geometry above.

Consequently, if a proposed source-sensitive coercivity argument uses a fixed rank-`K` anchor and an `L^infinity` ancestry condition over primes through a cutoff with

\[
Q_{K+1}(Y(H))>H,
\tag{29}
\]

then in the squarefree-unit class it has already reconstructed the physical Möbius vector coefficient by coefficient. Any subsequent critical Mertens/Farey estimate is no longer being proved on a genuinely larger synthetic source class.

Below the threshold, the situation is the opposite: even **zero** local ancestry defect leaves at least one exact binary gauge mode whenever `Q_{K+1}(Y)<=H`. Thus there is no softer local-defect theorem to discover inside this model without adding another ingredient. The next non-circular possibilities must either retain a norm between global averaging and a hard supremum, allow non-unit amplitudes with a genuinely quantitative stability question, make the rank/prime geometry scale jointly in a way that does not exhaust the rough cores, or bypass coefficient reconstruction and prove a destination-side Fourier-skeleton inequality directly.

## 6. Adversarial checks and prior-art boundary

The threshold uses primes **strictly larger** than `Y`; this matters at equality. If `Y^(K+1)>=H`, every rank-`K+1` rough core is strictly larger than `Y^(K+1)` and therefore larger than `H`, so (8) has no endpoint exception. The construction in the converse uses a rough core of rank exactly `K+1`, and every point in its ancestry component has rank at least `K+1`; hence the component flip cannot violate the rank-`K` anchor. Nonsquarefree integers play no role because all active edges are restricted to squarefree parents with `p` not dividing the parent.

The `L^infinity` conclusion is deliberately limited to the squarefree **unit-sign** source class. For sources with continuous amplitudes, an edge defect can take intermediate values and a genuinely quantitative path-stability problem remains; (7) must not be imported into that larger class. Likewise, the present finding says nothing by itself about Fourier-skeleton saturation of the matched control. Its role is an information boundary: it determines exactly when the local ancestry/anchor data cease to define a relaxation larger than Möbius.

The arithmetic ingredients are elementary. Splitting an integer into its `Y`-smooth and `Y`-rough parts is standard sieve language, and `FD-029` already records the exact rough-core parametrization relevant to this line. A targeted prior-art audit also finds the surrounding literature on rough numbers and on squarefree-supported multiplicative functions resembling Möbius, including Marco Aymone, *A note on multiplicative functions resembling the Möbius function*, J. Number Theory **212** (2020), 113--121. Those works do not supply a load-bearing step here. The new line-specific content is the exact splice of the `FD-029` component decomposition with the fixed-rank anchors introduced in `FD-130`, yielding the sharp finite-horizon uniqueness criterion (6) and closing the hard-local ancestry branch for unit-sign controls. No external theorem is required, so `SOURCES.md` does not change.
