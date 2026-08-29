# PC-041 — Weil–Petersson divisor refinement is exact-order orthogonal and transport-flat

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` for obtaining a new RH-sensitive coupling or holonomy from the Weil–Petersson **metric-level** interaction of full-root divisor covers. The cover homothety of the Weil–Petersson metric is classical; the exact-order organization below is elementary cyclic representation theory specialized to the prime-circle tower. No novelty claim is made for either ingredient.

PC-040 showed that at a prime level the Weil–Petersson cotangent metric is diagonal in the cyclic-character basis and that its diagonal weights are samples of one universal holonomy profile on the thrice-punctured sphere. That left an obvious possible escape: perhaps the **relations between levels** carry the missing arithmetic information even though each level separately is a universal sample.

For the canonical divisor-cover maps of the original roots-of-unity geometry, that bilinear route is flat. After the natural degree normalization, pullback is an exact isometric inclusion of character modes, exact-order birth sectors are mutually orthogonal in every common refinement, and transport along different divisor chains agrees identically.

## 1. The full-root cotangent space has exact-order birth sectors at every level

For every `n >= 2`, let

\[
Y_n=\widehat{\mathbb C}\setminus\bigl(\{0,\infty\}\cup\mu_n\bigr).
\]

As in PC-040, define for `1 <= j <= n-1`

\[
\boxed{
q_{n,j}(z)=\frac{z^{j-2}}{z^n-1}\,dz^2.
}
\]

The same pole check used there does not require `n` to be prime, so the `n-1` differentials form a basis of

\[
Q(Y_n),\qquad \dim_{\mathbb C}Q(Y_n)=n-1.
\]

For the deck generator

\[
T_n(z)=\zeta_n z,
\]

we have

\[
\boxed{T_n^*q_{n,j}=\zeta_n^j q_{n,j}.}
\]

The character carried by `q_{n,j}` has exact order

\[
\boxed{
d(j)=\frac{n}{\gcd(j,n)}.
}
\]

For each divisor `d | n`, `d>1`, define the exact-order cotangent birth sector

\[
\boxed{
\mathcal Q_d^{\rm birth}(Y_n)
:=
\operatorname{span}\left\{
q_{n,(n/d)a}:(a,d)=1
\right\}.
}
\]

Its dimension is `phi(d)`. Since the Weil–Petersson pairing is invariant under the deck rotation, distinct characters are orthogonal. Therefore

\[
\boxed{
Q(Y_n)
=
\bigoplus_{\substack{d\mid n\\d>1}}^{\perp_{WP}}
\mathcal Q_d^{\rm birth}(Y_n).
}
\]

The dimension identity is exactly

\[
\sum_{\substack{d\mid n\\d>1}}\varphi(d)=n-1.
\]

Thus the finite-dimensional Weil–Petersson cotangent geometry has the same exact-order divisor decomposition as the automorphic `L^2` tower in PC-022 and the primitive-root decomposition of the vertices themselves.

## 2. Divisor pullback preserves the exact-order label exactly

Let `d | n` and write

\[
n=md.
\]

The canonical divisor-cover map is

\[
\pi_{n,d}:Y_n\to Y_d,
\qquad
\pi_{n,d}(z)=z^m.
\]

For `1 <= a <= d-1`, direct substitution gives

\[
\begin{aligned}
\pi_{n,d}^*q_{d,a}
&=
\frac{(z^m)^{a-2}}{z^{md}-1}
\left(mz^{m-1}dz\right)^2\\
&=
\boxed{
m^2 q_{n,ma}.}
\end{aligned}
\]

The character index `a mod d` therefore maps to `ma mod n`, and

\[
\frac{n}{\gcd(ma,n)}
=
\frac{md}{m\gcd(a,d)}
=
\frac{d}{\gcd(a,d)}.
\]

So pullback preserves the exact order of every character. In particular,

\[
\boxed{
\pi_{n,d}^*\mathcal Q_e^{\rm birth}(Y_d)
\subset
\mathcal Q_e^{\rm birth}(Y_n)
\qquad(e\mid d).
}
\]

No exact-order sector is mixed with another by canonical refinement.

## 3. Weil–Petersson pullback is a pure degree homothety

Because `pi_{n,d}` is an unbranched hyperbolic covering, the complete hyperbolic metric on `Y_n` is the pullback of that on `Y_d`. For quadratic differentials `q,r in Q(Y_d)`, the Petersson integral therefore gives directly

\[
\boxed{
\langle \pi_{n,d}^*q,\pi_{n,d}^*r\rangle_{WP,*;Y_n}
=
m\,\langle q,r\rangle_{WP,*;Y_d}.
}
\]

This is the cotangent form of the standard covering-construction identity

\[
f^*g_{WP}=\deg(f)\,g_{WP},
\]

proved for totally marked covering constructions, for example, in Serván's Corollary 6.5.

Let

\[
h_{n,j}=\|q_{n,j}\|_{WP,*}^2.
\]

Combining the exact pullback formula with the degree homothety gives

\[
m^4h_{n,ma}=m h_{d,a},
\]

hence

\[
\boxed{
h_{n,ma}=m^{-3}h_{d,a}.}
\]

This is exactly consistent with the universal profile of PC-040. In fact its pushdown proof also works for composite `n`, giving

\[
\boxed{
h_{n,j}=n^{-3}I(j/n),}
\]

and when `j=ma`,

\[
n^{-3}I(a/d)=m^{-3}d^{-3}I(a/d).
\]

Thus divisor refinement creates no additional weight beyond the forced degree factor.

## 4. Degree-normalized pullback has identity transport in the normalized character basis

Define the degree-normalized pullback

\[
\boxed{
J_{n,d}:=m^{-1/2}\pi_{n,d}^*.
}
\]

By the previous section, `J_{n,d}` is an isometric embedding for the Weil–Petersson pairing.

Now normalize each character mode by

\[
\widehat q_{d,a}
:=
\frac{q_{d,a}}{\sqrt{h_{d,a}}}.
\]

Using

\[
\pi_{n,d}^*q_{d,a}=m^2q_{n,ma},
\qquad
h_{n,ma}=m^{-3}h_{d,a},
\]

we get the exact identity

\[
\boxed{
J_{n,d}\widehat q_{d,a}
=
\widehat q_{n,ma}.
}
\]

There is no phase, no nontrivial transfer coefficient and no matrix mixing.

If

\[
d\mid e\mid n,
\]

then the covering maps compose exactly, and the square-root degree normalizations multiply. Therefore

\[
\boxed{
J_{n,e}J_{e,d}=J_{n,d}.
}
\]

So transport around any commutative divisor-refinement diagram is the identity on every normalized exact-order mode. The canonical Weil–Petersson refinement connection is flat in the strongest discrete sense relevant here: different refinement paths do not even differ by a scalar phase.

## 5. Distinct birth levels are orthogonal in every common refinement

Let `d` and `e` divide a common level `N`. Pull their exact-order sectors into `Y_N` using the normalized maps above. Because exact character order is preserved, their images land in

\[
\mathcal Q_d^{\rm birth}(Y_N)
\quad\text{and}\quad
\mathcal Q_e^{\rm birth}(Y_N).
\]

For `d != e` these sectors are orthogonal. Hence for

\[
u\in\mathcal Q_d^{\rm birth}(Y_d),
\qquad
v\in\mathcal Q_e^{\rm birth}(Y_e),
\qquad d\ne e,
\]

we have

\[
\boxed{
\left\langle
J_{N,d}u,
J_{N,e}v
\right\rangle_{WP,*;Y_N}=0.
}
\]

For two distinct primes `p` and `q`, this becomes especially transparent in `Y_{pq}`:

\[
J_{pq,p}\widehat q_{p,a}
=
\widehat q_{pq,qa},
\qquad
J_{pq,q}\widehat q_{q,b}
=
\widehat q_{pq,pb}.
\]

An equality `qa=pb` with `1<=a<p`, `1<=b<q` would force `p|a` and `q|b`, impossible. Thus the prime birth sectors have zero Weil–Petersson cross pairing in their canonical common refinement.

More generally, the only overlap between pullbacks from two levels is the collection of exact-order sectors already inherited from their common divisors. There is no new bilinear interaction generated merely by placing them in a finer full-root cover.

## 6. Decisive obstruction to the metric-level cross-scale escape from PC-040

PC-040 left open the possibility that the universal holonomy coordinate

\[
\alpha=\frac{k}{n}
\]

could become arithmetically meaningful when coupled to an independent scale/refinement variable. The canonical Weil–Petersson metric on the full-root divisor tower does **not** supply such a coupling.

At the metric level, refinement is exactly

\[
\boxed{
\text{exact-order label preserved}
\;+
\text{universal degree homothety}
\;+
\text{orthogonal birth sectors}
\;+
\text{path-independent normalized pullback}.
}
\]

Consequently, any proposed RH mechanism that uses only

- Weil–Petersson pairings of deformation directions pulled through the divisor-cover tower;
- parallel transport defined by the canonical normalized pullbacks;
- Gram matrices of exact-order birth sectors in a common full-root refinement; or
- a Berry/holonomy phase arising solely from the order of divisor refinement,

collapses before any zeta-specific analytic structure appears.

The result is the Weil–Petersson counterpart of the refinement flatness found for the inverse-square Kron operator in PC-039, but the mechanism is different: here flatness comes from functorial hyperbolic pullback plus cyclic-character orthogonality rather than Schur-complement associativity.

## 7. Boundary: nonlinear curvature and actual composite birth surfaces remain outside the no-go

This finding is deliberately **not** a statement that Weil–Petersson geometry is globally trivial across the prime-circle program.

First, the Weil–Petersson curvature tensor is nonlinear in the harmonic Beltrami fields and contains the Green/resolvent operator from the Tromba–Wolpert curvature formula. Orthogonal character directions can have nonzero mixed curvature even when their metric pairing vanishes. The present argument rules out bilinear metric/refinement mixing, not such higher nonlinear interactions.

Second, for composite `n`, the actual primitive-shell birth surface of PC-017 is not `Y_n`. The full-root divisor tower is canonical and is the correct common refinement for comparing roots-of-unity levels, but it omits the nonlinear uniformization defect created by deleting only primitive punctures at a composite level.

Thus the live boundary is now sharper:

\[
\boxed{
\text{a surviving WP route must use curvature/higher nonlinear response,}
\text{ or the composite birth-surface uniformization defect,}
}
\]

not the metric-level transport of the full-root cover tower.

## 8. Prior art and novelty audit

The ingredients are classical or immediate from classical structure:

- Lochak explicitly diagonalizes the cyclic action on the quadratic-differential cotangent space at the roots-of-unity point and notes Weil–Petersson invariance under the finite automorphism; this is the direct prior-art anchor already used in PC-040.
- Carlos A. Serván proves for totally marked covering constructions that pullback scales the Weil–Petersson metric by the covering degree, `f^*g_WP = deg(h) g_WP` (Corollary 6.5 of *Local rigidity of covering constructions and Weil–Petersson subvarieties of the moduli space of curves*, IMRN 2026; arXiv:2509.25523).
- grouping cyclic characters by exact order is elementary representation theory, as already used in the automorphic setting in PC-022.

Directed searches did not locate this exact prime-circle packaging of the finite-dimensional cotangent tower, but that is not evidence of historical novelty. The durable contribution is the research consequence: the most canonical cross-level Weil–Petersson **metric** construction has no order-sensitive transport or cross-birth coupling to exploit for RH.

## 9. Audit and falsification tests

The exact claims can be checked independently without numerical approximation:

1. verify that `q_{n,j}`, `1<=j<n`, form the standard basis of `Q(Y_n)` and have deck character `zeta_n^j`;
2. group indices by `n/gcd(j,n)` and recover the orthogonal exact-order decomposition with dimensions `phi(d)`;
3. for `n=md`, substitute `z^m` directly to verify `pi_{n,d}^*q_{d,a}=m^2q_{n,ma}`;
4. evaluate the Petersson integral under the `m`-sheeted unbranched cover to recover the factor `m`;
5. combine the previous two identities to check `h_{n,ma}=m^{-3}h_{d,a}`;
6. normalize by `m^{-1/2}` and verify exact path composition `J_{n,e}J_{e,d}=J_{n,d}`;
7. embed two distinct exact-order sectors into a common multiple and verify their deck characters differ, forcing zero Weil–Petersson pairing.

A failure of the degree homothety, the exact pullback exponent, or the character-order preservation would invalidate the no-go. No claim is made about the Weil–Petersson curvature tensor, nonlinear uniformization on composite birth surfaces, or any zeta-zero correspondence.
