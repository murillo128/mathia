# PF-086 — the exact/reference direct-scattering kernel has sharp Hilbert–Schmidt threshold `Re s = 1/4`

**Status:** `POSITIVE-CANONICAL-OPERATOR` + `EXACT-SCHATTEN-THRESHOLD`, with an explicit scope restriction: the operator below is the canonically normalized **identity-double-coset/direct-scattering part** of the cusp scattering matrix, not yet the full physical scattering matrix of the infinite-cusp flute.

PF-084 found an abscissa `Re s = 1/4` for a canonical relative Ruelle sector built from all finite block separators. PF-085 then showed that the most direct conformal/Grunsky Fredholm completion is too regular: it is trace class and has no quarter-plane wall. This note finds a different operator-level occurrence of the same quarter threshold, now inside standard cusp-scattering geometry.

The key point is that, after width-one normalization, every ordered pair of cusps has a canonical **direct scattering geodesic** represented by the identity group element. Comparing the exact prime-circle endpoint geometry

\[
V(p)=\pi\cot\frac{\pi}{p}
\]

with the projective reference `V_0(p)=p` gives a relative matrix of those direct contributions. That matrix is Hilbert–Schmidt exactly for

\[
\boxed{\operatorname{Re}s>\frac14.}
\]

Hence a canonical Carleman–Fredholm determinant `det_2` exists in that half-plane. This does **not** yet identify its zeros with Laplace resonances; the remaining gate is to show that the non-direct double-coset part of the physical scattering difference has compatible operator-ideal control.

## 1. Width-one normalization for every prime cusp

Use the globally rescaled exact endpoints

\[
x_n^E=V(p_n)=\pi\cot(\pi/p_n),
\]

and the projective reference endpoints

\[
x_n^0=p_n.
\]

The common factor `pi` relative to the original `cot(pi/p)` coordinate is Möbius and changes no intrinsic hyperbolic data.

Write

\[
\Delta_n^\bullet=x_{n+1}^\bullet-x_n^\bullet,
\qquad
W_n^\bullet=2\left(\frac1{\Delta_{n-1}^\bullet}+\frac1{\Delta_n^\bullet}\right),
\qquad \bullet\in\{E,0\}.
\]

`W_n` is the exact parabolic width parameter already used in PF-019. The standard determinant-one scaling matrix at cusp `n` conjugates the primitive stabilizer to unit translation.

For any two distinct cusps `i,j`, not only adjacent ones, the identity element gives a distinguished double-coset representative. The lower-left entry in width-one coordinates has absolute value

\[
\boxed{
C_{ij}^\bullet
=\sqrt{W_i^\bullet W_j^\bullet}\,|x_j^\bullet-x_i^\bullet|.
}
\tag{1}
\]

This is the same elementary scaling-matrix calculation used in PF-019/PF-030, now with an arbitrary cusp pair.

For a finite-area surface with finitely many cusps, the standard scattering coefficient in `Re s>1` is a double-coset Dirichlet series with terms proportional to `|c|^{-2s}`. Thus

\[
(C_{ij}^\bullet)^{-2s}
\]

is precisely the Gamma-factor-stripped contribution of this canonical direct scattering geodesic.

Define the off-diagonal matrices

\[
B_\bullet(s)_{ij}
=
\begin{cases}
(C_{ij}^\bullet)^{-2s},&i\ne j,\\
0,&i=j,
\end{cases}
\]

and the relative direct-scattering kernel

\[
\boxed{D(s):=B_E(s)-B_0(s).}
\tag{2}
\]

No new spectral potential or prime generating weight has been introduced: (2) is the exact/reference difference of one geometrically distinguished term already present in every finite-cusp scattering entry.

## 2. Uniform exact/reference distortion is `O(p_i^-2+p_j^-2)`

Let

\[
D_V(x,y)=\frac{V(y)-V(x)}{y-x}.
\]

PF-083/PF-085 give

\[
\log D_V(x,y)=O(x^{-2})
\]

uniformly for `y>x>2`. Since

\[
\Delta_n^E=g_nD_V(p_n,p_{n+1}),
\]

the same estimate, applied to the two reciprocal gaps entering `W_n`, gives

\[
\boxed{
\log\frac{W_n^E}{W_n^0}=O(p_{n-1}^{-2}).
}
\tag{3}
\]

Using (1), for `i<j`,

\[
\log\frac{C_{ij}^E}{C_{ij}^0}
=
\frac12\log\frac{W_i^E}{W_i^0}
+
\frac12\log\frac{W_j^E}{W_j^0}
+
\log D_V(p_i,p_j).
\]

Therefore

\[
\boxed{
\left|\log\frac{C_{ij}^E}{C_{ij}^0}\right|
\le C\,(p_i^{-2}+p_j^{-2}).
}
\tag{4}
\]

The normalized denominators are uniformly bounded away from zero. Indeed, for `i<j`,

\[
W_i^0\ge\frac2{g_i},
\qquad
W_j^0\ge\frac2{g_{j-1}},
\]

while `p_j-p_i` is at least both endpoint gaps. Hence

\[
\boxed{C_{ij}^0\ge2.}
\tag{5}
\]

The same holds in the exact coordinate.

On a compact `s`-set in `Re s>0`, (4)-(5) imply

\[
\boxed{
|D(s)_{ij}|
\le C_K(p_i^{-2}+p_j^{-2})(C_{ij}^0)^{-2\operatorname{Re}s}.
}
\tag{6}
\]

For `i<j`, the first prime dominates, so the right side is `O(p_i^-2 C_ij^{-2 sigma})`.

## 3. The reference denominator reduces to a harmonic gap weight

Put

\[
H_n:=\frac1{W_n^0}
=\frac{g_{n-1}g_n}{2(g_{n-1}+g_n)}.
\]

Then

\[
\boxed{
(C_{ij}^0)^{-4\sigma}
=
H_i^{2\sigma}H_j^{2\sigma}|p_j-p_i|^{-4\sigma}.
}
\tag{7}
\]

For odd primes, `g_n>=2`, hence

\[
\boxed{H_n\ge\frac12.}
\tag{8}
\]

Also `H_n<=g_n/2` and `H_n<=g_{n-1}/2`.

The threshold now comes from the elementary dyadic fact

\[
\boxed{
\sum_n H_n^\alpha p_n^{-2\alpha}<\infty
\quad\Longleftrightarrow\quad
\alpha>\frac12.
}
\tag{9}
\]

For the upper direction with `1/2<alpha<1`, on `P<=p_n<2P`,

\[
\sum H_n\ll P
\]

because `H_n<=g_n/2` and the prime gaps telescope (Bertrand controls the final boundary gap). Concavity then gives

\[
\sum_{P\le p_n<2P}H_n^\alpha
\le N_P^{1-\alpha}\left(\sum H_n\right)^\alpha
\ll P.
\]

Therefore the dyadic contribution to (9) is

\[
O(P^{1-2\alpha}),
\]

which is summable exactly for `alpha>1/2`. Larger `alpha` are easier by monotonic domination from any fixed exponent in `(1/2,1)`.

For the lower direction, (8) reduces the series to the prime Dirichlet series `sum_p p^{-2 alpha}`, which diverges for `2 alpha<=1` (Euler at the boundary).

## 4. Sharp Hilbert–Schmidt threshold

Let `K` be a compact subset of `Re s>1/4`. Choose

\[
\frac14<\sigma_0<\min\left(\frac12,\inf_{s\in K}\operatorname{Re}s\right),
\qquad
\alpha=2\sigma_0\in(1/2,1).
\]

Because of (5), it is enough to prove square summability using `sigma_0`. From (6), for `i<j`,

\[
|D(s)_{ij}|^2
\ll_K
p_i^{-4}(C_{ij}^0)^{-4\sigma_0}.
\]

Split into near and far pairs.

### Near pairs: `p_j<2p_i`

Using only `(C_ij^0)^(-4 sigma_0)<=const`, there are at most `O(p_i)` possible indices `j`, so

\[
\sum_i\sum_{p_i<p_j<2p_i}|D(s)_{ij}|^2
\ll
\sum_i p_i^{-3}
<\infty.
\]

### Far pairs: `p_j>=2p_i`

Now `p_j-p_i>=p_j/2`, so (7) gives

\[
\sum_{i}\sum_{p_j\ge2p_i}|D(s)_{ij}|^2
\ll
\sum_i p_i^{-4}H_i^\alpha
\sum_j H_j^\alpha p_j^{-2\alpha}.
\]

The second factor is finite by (9), and the first is finite trivially from `H_i<=p_i` and `alpha<1`.

Hence

\[
\boxed{
D(s)\in\mathcal S_2(\ell^2(\text{cusps}))
\qquad(\operatorname{Re}s>1/4).
}
\tag{10}
\]

The convergence is locally uniform in Hilbert–Schmidt norm, so `s -> D(s)` is holomorphic as an `S_2`-valued function on that half-plane.

The boundary is sharp. Fix one cusp `i` and let `j->infinity`. Since `V'(x)>1`, every exact gap is larger than its reference gap, hence

\[
W_i^E<W_i^0.
\]

Meanwhile

\[
D_V(p_i,p_j)\to1,
\qquad
W_j^E/W_j^0\to1.
\]

Therefore

\[
\frac{C_{ij}^E}{C_{ij}^0}
\longrightarrow
\sqrt{W_i^E/W_i^0}<1.
\]

For every fixed `s` with `Re s>0`, the relative multiplicative factor in `D(s)_{ij}` tends to a nonzero constant. Using (8),

\[
|D(s)_{ij}|^2
\gg_{i,s} p_j^{-4\operatorname{Re}s}
\]

for all sufficiently large `j`. Consequently

\[
\boxed{
D(s)\notin\mathcal S_2
\qquad(0<\operatorname{Re}s\le1/4).
}
\tag{11}
\]

At the exact boundary the obstruction is Euler's `sum_p 1/p`.

Combining (10)-(11),

\[
\boxed{
D(s)\text{ is Hilbert--Schmidt exactly for }\operatorname{Re}s>\frac14.
}
\]

## 5. A natural Carleman–Fredholm determinant now exists

For a Hilbert–Schmidt operator the standard second regularized determinant is defined by

\[
\det_2(I+D)
=\det\bigl((I+D)e^{-D}\bigr).
\]

Therefore (10) gives the canonical holomorphic object

\[
\boxed{
\mathfrak D_{\rm dir}(s)
:=\det_2(I+D(s)),
\qquad
\operatorname{Re}s>\frac14.
}
\tag{12}
\]

This is qualitatively different from the artificial diagonal `det_2` warning in PF-022: the matrix entries of `D(s)` are forced by width-normalized cusp scattering geometry and are actual direct double-coset contributions.

The determinant (12) should nevertheless **not** yet be called the scattering determinant of the prime-flute. Its zeros only say that `-1` enters the spectrum of this relative direct-channel operator. No theorem presently identifies those zeros with Laplace eigenvalues or resonances of the infinite surface.

## 6. Why the quarter threshold is not a restatement of PF-084

For a long scattering connection, the direct denominator has the geometric scale

\[
C_{ij}^{-2s}
\sim
\left(\frac{\sqrt{H_iH_j}}{|p_j-p_i|}\right)^{2s}.
\]

The **Hilbert–Schmidt norm squares this physical scattering amplitude**, giving

\[
|D(s)_{ij}|^2
\sim
(\text{projective defect})^2
\left(\frac{\sqrt{H_iH_j}}{|p_j-p_i|}\right)^{4\operatorname{Re}s}.
\]

That square is exactly why the summability wall is at `Re s=1/4`.

PF-084 instead obtained `1/4` from an ordinary relative Euler sum over long primitive block geodesics. The two mechanisms are therefore different:

```text
PF-084:
    long primitive block proliferation
      -> ordinary relative Ruelle logarithm
      -> Re s = 1/4

PF-086:
    exact/reference direct cusp scattering
      -> Hilbert-Schmidt operator ideal
      -> Re s = 1/4.
```

PF-085 also remains untouched: its Grunsky/Schiffer kernel decays one full conformal order faster and is trace class without such a wall.

The coincidence of the two quarter thresholds is therefore a new structural clue, not an algebraic rewriting of the same series.

## 7. Relation to distinguished cuffs

At cusp `n`,

\[
H_n
=\frac{g_{n-1}g_n}{2(g_{n-1}+g_n)}.
\]

Using

\[
\ell_k
=2\log\frac{4p_k}{g_{k-1}}+o(1),
\]

the endpoint factors entering a long direct channel can be written asymptotically as harmonic combinations of

\[
p_n e^{-\ell_n/2}
\]

and the neighboring cuff scale. Thus the direct scattering amplitude uses **both local cuff strengths and the nonlocal separation of the cusps**. It is not cuff-by-cuff factorization of the type ruled out by PF-002/PF-022.

This is the same general pattern that has survived throughout the program: absolute single-cuff data universalize, while relational coupling across separated pieces retains the prime-gap geometry.

## 8. Interior/exterior duality

The definition uses only width-one cusp normalization and the lower-left modulus of a distinguished double-coset representative. Under the ambient inversion exchanging the two orthogonal-circle copies, the Fuchsian configuration is conjugated and the normalized sojourn denominator is unchanged. The exterior construction therefore gives the unitarily relabelled same `D(s)`, not an independent determinant. The exact interior/exterior duality is preserved rather than discarded.

## 9. Novelty / prior-art audit

Known ingredients:

1. for a finite-area hyperbolic surface with finitely many cusps, each scattering-matrix entry has the standard double-coset/Kloosterman Dirichlet expansion in `c^{-2s}`;
2. width-one cusp scaling matrices and sojourn denominators are classical;
3. Hilbert–Schmidt/Schatten ideals and `det_2` are standard functional analysis;
4. scattering and generalized scattering theory for finite numbers of hyperbolic cusps is extensive.

The literature located in the audit remains in finite-cusp or geometrically finite settings. Standard finite-area scattering uses a finite `k x k` matrix; generalized inverse-scattering results for hyperbolic surfaces likewise assume finitely many cusps/ends. Searches for countably-cusped hyperbolic scattering matrices, Schatten thresholds for infinitely many cusp channels, and a relative `det_2` built from the identity-double-coset sector did not locate this construction.

Thus no novelty is claimed for scattering Dirichlet series or `det_2` themselves. The candidate-new statement is the composition

\[
\boxed{
\text{prime-circle exact/reference defect}
\to
\text{countable direct cusp-scattering kernel}
\to
\mathcal S_2\text{ iff }\operatorname{Re}s>1/4.
}
\]

## 10. Critical gate

The next step must test the **full** scattering difference, not decorate (12) with arithmetic interpretation.

For finite cusp truncations write schematically

\[
\Phi_E(s)-\Phi_0(s)
=A(s)D(s)+R(s),
\]

where `D(s)` is the direct identity-double-coset sector above and `R(s)` contains all non-direct double cosets.

A genuinely spectral relative determinant would require a uniform infinite-cusp construction in which `R(s)` is also Hilbert–Schmidt (or better) in a nonempty domain and in which the finite truncations converge. If that fails, PF-086 remains a canonical scattering-geometric operator but not a determinant of the Laplacian.

Conversely, if the same `S_2` control survives for the full physical difference, then `det_2` would provide the first natural global relative scattering determinant found for the prime-flute and the quarter-plane wall would be operator-theoretic rather than merely Euler-product combinatorics.
