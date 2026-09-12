# MC-233 — The smooth inverse removes the first-shell CRT roughness mask at subpower cost

**Status:** `EXACT-DERIVED`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the stronger diagonalized first-shell route of `MC-232`. Fix

\[
0<c<\frac12,
\qquad
y=c\log X,
\qquad
P=\prod_{p\le y}p,
\qquad
T=X-P,
\]

and let

\[
\mathcal D_y=\{d:\ y<d\le2y,\ d\text{ prime}\}.
\]

For a nonempty shell-incidence set `S`, write

\[
Q_S:=\prod_{d\in S}d^2.
\]

The partial-intersection coordinate exposed by `MC-232` is

\[
B_S(X)
=
\sum_{\substack{n\le T\\ n\equiv-P\pmod{Q_S}\\(n,P)=1}}
\mu(n).
\tag{1}
\]

Thus the only support mask left after Boolean incidence inversion is logarithmic primorial roughness. That mask can also be removed exactly, at only subpower combinatorial cost.

Define

\[
g_y(n):=\mu(n)\mathbf 1_{(n,P)=1}
\]

and the all-powers smooth indicator

\[
s_y(d):=\mathbf 1_{P^+(d)\le y},
\qquad s_y(1)=1.
\]

`MC-181` established the exact classical convolution identity

\[
\boxed{g_y=\mu*s_y.}
\tag{2}
\]

Substituting `(2)` into `(1)` and interchanging the finite divisor sums gives

\[
B_S(X)
=
\sum_{\substack{d\le T\\P^+(d)\le y}}
\sum_{\substack{m\le T/d\\dm\equiv-P\pmod{Q_S}}}
\mu(m).
\tag{3}
\]

Every prime factor of a smooth `d` is at most `y`, while every prime factor of `Q_S` lies in `(y,2y]`. Hence `(d,Q_S)=1`. Therefore the congruence in `(3)` is equivalent to one reduced residue class

\[
m\equiv a_{S,d}:=-P d^{-1}\pmod{Q_S},
\qquad
(a_{S,d},Q_S)=1.
\tag{4}
\]

If

\[
M_\mu(Z;q,a)
:=
\sum_{\substack{m\le Z\\m\equiv a\pmod q}}\mu(m),
\tag{5}
\]

then the exact reduction is

\[
\boxed{
B_S(X)
=
\sum_{\substack{d\le T\\P^+(d)\le y}}
M_\mu\!\left(\frac Td;Q_S,a_{S,d}\right).
}
\tag{6}
\]

At the logarithmic cutoff, the number of smooth dilation parameters is subpower:

\[
\Psi(T,y)
:=
\#\{d\le T:P^+(d)\le y\}
=X^{o(1)}.
\tag{7}
\]

Equation `(7)` was already proved directly in `MC-181` by a crude Rankin bound; no Dickman asymptotic is needed.

Consequently, **roughness itself is not a fixed-power obstruction in the `MC-232` sufficient route**. It can be unfolded into only `X^{o(1)}` ordinary Möbius progression sums, all at the same modulus `Q_S`, with the smooth dilation recorded only in the length and in the reduced residue `a_{S,d}`.

There is a second useful consequence. For any threshold `D>=1`, the contribution of smooth dilations `d>=D` satisfies trivially

\[
\begin{aligned}
\sum_{\substack{D\le d\le T\\P^+(d)\le y}}
\left|
M_\mu\!\left(\frac Td;Q_S,a_{S,d}\right)
\right|
&\le
\Psi(T,y)
\left(\frac{T}{D Q_S}+1\right)\\
&=
X^{o(1)}
\left(\frac{X}{D Q_S}+1\right).
\end{aligned}
\tag{8}
\]

Thus, whenever `Q_S<=X^{1/2+o(1)}`, choosing

\[
D_S:=\max\!\left(1,\frac{X^{1/2}}{Q_S}\right)
\tag{9}
\]

makes the entire `d>=D_S` tail harmless at the target amplitude:

\[
\boxed{
\sum_{\substack{d\ge D_S\\P^+(d)\le y}}
\left|
M_\mu\!\left(\frac Td;Q_S,a_{S,d}\right)
\right|
\le X^{1/2+o(1)}.
}
\tag{10}
\]

Therefore only the smooth dilations below `D_S` require genuine Möbius cancellation.

For the incidence-depth scaling of `MC-232`,

\[
|S|
=\left(\alpha+o(1)\right)
\frac{\log X}{\log\log X},
\qquad
0\le\alpha<\frac14,
\]

we have

\[
Q_S=X^{2\alpha+o(1)}.
\tag{11}
\]

If a smooth dilation lies at scale

\[
d=X^{\beta+o(1)},
\qquad \beta\ge0,
\]

then the corresponding progression in `(6)` contains at most

\[
X^{1-2\alpha-\beta+o(1)}+1
\tag{12}
\]

terms. The `MC-232` amplitude target remains `X^{1/2+o(1)}`. Hence the fixed-power gain required of that component is exactly

\[
\boxed{
X^{\max(0,\,1/2-2\alpha-\beta)+o(1)}.
}
\tag{13}
\]

The hard region is therefore the two-parameter half-plane

\[
\boxed{2\alpha+\beta<\frac12.}
\tag{14}
\]

Above the boundary `2alpha+beta=1/2`, support alone suffices. Below it, the missing power decreases continuously as either shell incidence or smooth dilation increases.

A sufficient uniform theorem surface for the remaining diagonal route is consequently

\[
\boxed{
\left|
M_\mu\!\left(\frac Td;Q_S,a_{S,d}\right)
\right|
\le X^{1/2+o(1)}
}
\tag{15}
\]

for every hard pair `(S,d)` with `0<|S|<r_{1/4}(X)`, `P^+(d)<=y`, and `d<D_S`. Since both the number of admissible `S` and the number of smooth `d` are `X^{o(1)}`, `(15)` implies the `MC-232` uniform bound `|B_S(X)|<=X^{1/2+o(1)}`, and hence its stronger diagonal-energy target.

This is only a sufficient componentwise surface, not an equivalence: cancellation between the smooth-dilation components in `(6)` may make `B_S` substantially smaller than the triangle bound. In particular, no individual progression estimate in `(15)` is proved here.

## 1. The convolution identity removes roughness coefficientwise

The identity `(2)` is algebraic. At a prime `p<=y`, the local generating factors are

\[
(1-z)(1+z+z^2+\cdots)=1,
\]

so every positive power of `p` is removed. At a prime `p>y`, the smooth factor is `1`, leaving the Möbius local factor `1-z`. Multiplicativity therefore gives

\[
(\mu*s_y)(n)
=
\begin{cases}
\mu(n),&(n,P)=1,\\
0,&(n,P)>1,
\end{cases}
\]

which is exactly `g_y(n)`.

This is the same inverse already used in `MC-181`; the new step is to apply it to the source-selected CRT coordinate `(1)` and exploit the separation of prime supports between smooth `d` and shell modulus `Q_S`.

Because `(d,Q_S)=1`, multiplication by `d` permutes the reduced residue classes modulo `Q_S`. Thus the roughness mask does not create a new modulus or a non-reduced progression after inversion. It becomes a subpower family of ordinary reduced Möbius progression sums at the original shell modulus.

## 2. The smooth family is subpower at `y=c log X`

For completeness, `MC-181` proves `(7)` without a delicate smooth-number asymptotic. A Rankin bound with a slowly vanishing positive exponent gives

\[
\Psi(T,y)
\le
T^\sigma
\prod_{p\le y}(1-p^{-\sigma})^{-1},
\]

and at `y=c log X` both factors are `X^{o(1)}` for the choice used there. Thus even allowing arbitrary powers of all primes below `y` produces only a subpower number of dilation parameters up to height `X`.

Classical smooth-number theory is much stronger. Hildebrand and Tenenbaum, *Integers without large prime factors*, Journal de théorie des nombres de Bordeaux 5 (1993), 411--484, DOI `10.5802/jtnb.101`, surveys the distribution of `Psi(x,y)` in much greater precision. No novelty is claimed here for smooth-number counting, Rankin's method, or the convolution `(2)`.

A targeted prior-art check also found the extensive literature on smooth numbers in arithmetic progressions, including recent large-modulus work. That literature concerns the distribution of the **smooth integers themselves**. Equation `(6)` is different: the smooth numbers index a subpower family of dilation parameters, while the inner objects are Möbius sums in source-selected residue classes. No external theorem located in that check supplies the fixed-power estimates `(15)` for this moving family.

## 3. The remaining cancellation budget is genuinely two-dimensional

At incidence depth `alpha`, `MC-232` showed that the lifted rough sum has natural length

\[
L_S=X^{1-2\alpha+o(1)}
\]

and needs only amplitude `X^{1/2+o(1)}`. The inverse `(6)` decomposes that object by small-prime dilation. A component at smooth scale `beta` has natural progression occupancy

\[
L_{S,d}=X^{1-2\alpha-\beta+o(1)}.
\]

Thus there are now two independent ways to make a component easy by support alone:

- increase shell incidence, which enlarges `Q_S` by `X^{2alpha+o(1)}`;
- increase the smooth divisor, which shortens the remaining Möbius sum by `X^{beta+o(1)}`.

Only their combination `2alpha+beta` enters the trivial power budget. This yields the boundary `(14)`.

The bottom-left corner remains the genuine obstruction. At `alpha=beta=0`, and in particular at the `d=1` component, `(6)` contains the unsmoothed reduced progression

\[
M_\mu(T;Q_S,-P\bmod Q_S),
\]

and the sufficient target still asks for square-root-in-`X` amplitude. The smooth inverse therefore removes a representation mask but does not manufacture cancellation. It exposes where the fixed-power difficulty lives.

## 4. Relation to the current first-shell frontier

`MC-230` replaced the original shell by a stronger exact-cell diagonal energy. `MC-232` then showed that Boolean incidence inversion removes the exact shell-exclusion masks at only `X^{o(1)}` condition cost, leaving the clean CRT family `(1)` but retaining `(n,P)=1`.

The present result removes that final roughness mask in the same exponent-budget sense. The stronger route may now be formulated entirely in terms of ordinary Möbius sums in reduced arithmetic progressions. What remains source-specific is not a support exclusion but the correlated parameter family

\[
(Q_S,a_{S,d})
=\left(
\prod_{r\in S}r^2,
-Pd^{-1}\bmod Q_S
\right),
\]

with `S` drawn from one shell and `d` restricted to the logarithmically smooth semigroup.

This distinction matters for theorem search. Generic progression estimates that ignore the source-selected relation between `Q_S`, `P`, and the residue family may still lose the required power, as earlier first-shell findings already show. But future attempts no longer need to treat `(n,P)=1` as a separate combinatorial obstruction: any fixed-power advantage must come from cancellation in the ordinary progression family or from cancellation between its smooth-dilation components.

## 5. Boundaries and falsification tests

- Equation `(6)` is exact, but the passage from `(6)` to the componentwise sufficient surface `(15)` uses the triangle inequality. It can discard useful cancellation between different smooth dilations. The result is therefore a representation reduction for the stronger route, not an equivalence between every individual progression and `B_S`.
- The subpower count `(7)` depends on the logarithmic cutoff `y=c log X`. For a polynomially large smoothness cutoff the dilation family need not be `X^{o(1)}`, and the exponent-preserving conclusion can fail.
- The residue `a_{S,d}` is reduced only because the smooth primes and shell primes are disjoint. If the shell overlaps the smooth cutoff, `(4)` is no longer automatic.
- The support tail `(10)` controls the sum of absolute values, so it is robust but intentionally wasteful. It proves that the region `2alpha+beta>=1/2` is harmless; it does not assert that the complementary region is necessary for the true `B_S`.
- The `d=1` component prevents the inverse from turning the hard low-incidence problem into a purely short-support problem. Any claimed solution based only on the sparsity of smooth dilations must still explain that component or exploit cancellation across `d`.
- No bound `(15)`, no estimate `|B_S|<=X^{1/2+o(1)}`, no improvement of the first-shell energy, no Mertens power bound, and no consequence for the zeta zero set is proved here.

## Consequence for the live frontier

The `MC-232` diagonalized first-shell target can be stripped of both exact-incidence exclusions and primorial roughness without paying a fixed power of `X`. After these two representation reductions, the unresolved arithmetic core is a subpower, source-coupled family of **ordinary reduced-residue Möbius progression sums**. Its support-only phase diagram is the plane `2alpha+beta=1/2`: only pairs below that plane need genuine cancellation, with the hardest corner at simultaneously low shell incidence and low smooth dilation.

This does not make the target easier by itself. It makes the remaining proof obligation sharper: future bilinear, dispersion, character, or other analytic input should be judged directly by whether it crosses the fixed-power deficit `1/2-2alpha-beta` on this source-selected progression family, rather than by whether it manipulates the now-removable support masks.