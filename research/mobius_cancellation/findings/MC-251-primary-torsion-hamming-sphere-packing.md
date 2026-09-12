# MC-251 — Primary blind torsion obeys a q-ary Hamming sphere-packing squeeze

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `FRONTIER-REFINEMENT`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the blind quotient and level-`a` primary code of `MC-238`–`MC-250`. For a prime `\ell`, an integer `a\ge1`, and

\[
d=\ell^a,
\]

`MC-250` constructs an `\mathbb F_\ell`-linear code

\[
C_{\ell,a}\subseteq \mathbb F_\ell^{S_d},
\qquad
S_d=\{r\in S:r\equiv1\pmod d\},
\]

whose parameters are

\[
[n_d,m_{\ell,a},\delta_{\ell,a}]_\ell,
\qquad
n_d=|S_d|,
\qquad
\delta_{\ell,a}\ge D_y.
\tag{1}
\]

Here `m_{\ell,a}` is the number of `\ell`-primary invariant factors of the blind quotient whose order is at least `\ell^a`, and `D_y` is any valid integer lower bound for the support of every nonprincipal blind character.

Put

\[
t_y:=\left\lfloor\frac{D_y-1}{2}\right\rfloor
\tag{2}
\]

and define the `q`-ary Hamming-ball volume

\[
V_q(n,t):=\sum_{j=0}^{t}\binom nj(q-1)^j.
\tag{3}
\]

Then the classical sphere-packing argument applied to `(1)` gives the exact primary-rank constraint

\[
\boxed{
\ell^{m_{\ell,a}}V_\ell(n_d,t_y)\le \ell^{n_d},
}
\tag{4}
\]

or equivalently

\[
\boxed{
n_d-m_{\ell,a}\ge \log_\ell V_\ell(n_d,t_y).
}
\tag{5}
\]

This is the `\ell`-ary, order-compatible-shell extension of the binary quadratic bound in `MC-243`. The new point is that `MC-250` identifies the correct code separately at **every primary torsion level** `\ell^a`; sphere packing can therefore be imposed after the progression restriction `r\equiv1\pmod{\ell^a}` rather than only on the full quadratic blind sector.

Combining `(5)` with the Singleton inequality already used in `MC-250` yields

\[
\boxed{
m_{\ell,a}\le
n_d-
\max\!\left\{
D_y-1,
\log_\ell V_\ell(n_d,t_y)
\right\}.
}
\tag{6}
\]

Thus the fixed-low-order regime left open by `MC-250` has a substantially stronger generic coding constraint than Singleton alone whenever the compatible shell is much wider than the support floor. Since

\[
V_\ell(n,t)\ge \binom nt(\ell-1)^t
\ge \left(\frac{(\ell-1)n}{t}\right)^t
\qquad(1\le t\le n),
\tag{7}
\]

`(5)` implies

\[
\boxed{
n_d-m_{\ell,a}
\ge
t_y\log_\ell\!\left(
\frac{(\ell-1)n_d}{t_y}
\right).
}
\tag{8}
\]

whenever `t_y\ge1`. In particular, when `n_d/t_y\to\infty`, the primary-rank deficit forced by minimum support is of order

\[
\Omega\!\left(
D_y\log_\ell\frac{n_d}{D_y}
\right),
\tag{9}
\]

not merely the `D_y-1` deficit supplied by Singleton.

The progression count from `MC-250` can be inserted without knowing the exact shell occupancy. Let

\[
B_{\ell,a}(y)
:=
\left\lfloor
\frac{2y}{\varphi(\ell^a)
\{\log(y/\ell^a)+0.8601\}}
\right\rfloor,
\tag{10}
\]

in the same range where the arbitrary-interval Brun–Titchmarsh estimate used there applies. Since `n_d\le B_{\ell,a}(y)`, append `B_{\ell,a}(y)-n_d` zero coordinates to `C_{\ell,a}`. This preserves its dimension and minimum distance, so `(4)` gives the explicit order-compatible bound

\[
\boxed{
m_{\ell,a}
\le
B_{\ell,a}(y)
-
\log_\ell
V_\ell\!\left(B_{\ell,a}(y),t_y\right).
}
\tag{11}
\]

Together with Singleton one may take the smaller of `(11)` and the `MC-250` bound

\[
m_{\ell,a}\le B_{\ell,a}(y)-D_y+1.
\tag{12}
\]

For fixed `\ell^a`, `(11)` is asymptotically the stronger generic code bound in the wide-shell regime. With the unconditional support floor of `MC-242`,

\[
D_y=
\left(\frac1{\log2}-o(1)\right)\log\log y,
\tag{13}
\]

and fixed `\ell^a`, the Brun–Titchmarsh length in `(10)` is `y^{1+o(1)}` up to logarithmic factors, so `(8)` gives a coding deficit on the scale

\[
\boxed{
B_{\ell,a}(y)-m_{\ell,a}
\ge
\left(
\frac{1}{2\log2\,\log\ell}-o(1)
\right)
\log y\,\log\log y.
}
\tag{14}
\]

For `\ell=2`, `(14)` recovers the binary rank-pressure scale already isolated in `MC-243`; it is not a new quadratic theorem. Its value here is the uniform transfer to every `\ell`-primary level after the exact shell restriction of `MC-250`.

Under the ERH support floor used in `MC-247`,

\[
D_y=
\left(\frac1{\sqrt2}-o(1)\right)
\frac{\sqrt y}{\log y},
\tag{15}
\]

the same fixed-`\ell^a` calculation upgrades the generic rank deficit from the Singleton scale `\asymp \sqrt y/\log y` to

\[
\boxed{
B_{\ell,a}(y)-m_{\ell,a}
\ge
\left(
\frac{1}{4\sqrt2\,\log\ell}-o(1)
\right)
\sqrt y.
}
\tag{16}
\]

The logarithmic gain comes from packing all `\ell^{m_{\ell,a}}` blind characters simultaneously rather than testing one minimum-weight character at a time.

Equations `(4)`–`(16)` materially sharpen the low-order multiplicity frontier, but they still do **not** force the blind quotient to vanish. For fixed `\ell`, the compatible shell has size on the order of `y/log y`, whereas even the ERH sphere-packing deficit in `(16)` is only `O(\sqrt y)`. A primary code of dimension `n_d-o(n_d)` remains compatible with these generic coding constraints. The missing theorem must therefore use arithmetic structure of the residue-symbol matrix beyond minimum distance, or bypass generation by controlling the signed rough Möbius coset of `MC-245`–`MC-246`.

No estimate for `M(X)`, no proof that the blind quotient is trivial, and no consequence for the zeta zero set is obtained.

## 1. Sphere packing applies at every primary torsion level

By `MC-250`, each nonzero vector of `C_{\ell,a}` is a nonprincipal blind character and hence has Hamming weight at least `D_y`. Therefore any two distinct codewords differ in at least `D_y` coordinates.

Balls of radius `t_y=floor((D_y-1)/2)` around distinct codewords are disjoint. A radius-`t_y` ball in `\mathbb F_\ell^{n_d}` has exactly

\[
V_\ell(n_d,t_y)
=
\sum_{j=0}^{t_y}\binom{n_d}{j}(\ell-1)^j
\]

vectors: choose the `j` changed coordinates and then one of `\ell-1` nonzero changes at each coordinate. Since the ambient space has `\ell^{n_d}` vectors and the code has `\ell^{m_{\ell,a}}` codewords, disjointness proves `(4)`.

No distributional assumption on shell primes or residue symbols enters this argument. The arithmetic input is exactly the identification of the level-`a` shadow as an `\ell`-ary code and the universal blind-support floor.

The classical source of the sphere-packing mechanism is R. W. Hamming, *Error Detecting and Error Correcting Codes*, Bell System Technical Journal **29** (1950), 147–160, DOI `10.1002/j.1538-7305.1950.tb00463.x`. `MC-243` already audited the binary specialization. The `q`-ary volume in `(3)` is the standard same counting argument over an alphabet of size `q`; no novelty is claimed for the coding bound.

## 2. Why this is stronger exactly where Singleton was weakest

`MC-250` obtains

\[
n_d-m_{\ell,a}\ge D_y-1.
\tag{17}
\]

Sphere packing instead gives `(5)`. Keeping only the outer shell of the Hamming ball yields `(7)` and hence `(8)`. If

\[
\frac{n_d}{D_y}\to\infty
\]

with fixed `\ell`, then `t_y=(1/2+o(1))D_y` and

\[
\log_\ell V_\ell(n_d,t_y)
\ge
\left(\frac{1}{2\log\ell}+o(1)\right)
D_y\log\frac{n_d}{D_y}.
\tag{18}
\]

So the Hamming deficit exceeds Singleton's `D_y-1` by a growing logarithmic factor whenever

\[
\log\frac{n_d}{D_y}>2\log\ell+o(1).
\tag{19}
\]

This is precisely the fixed-low-order regime identified as unresolved in `MC-250`: small `\ell^a` leaves a broad progression shell, and broad shells make the number of disjoint radius-`t_y` balls expensive.

Conversely, when `n_d` is close to `D_y`, the Hamming volume need not beat Singleton. Equation `(6)` therefore retains both bounds rather than pretending that sphere packing dominates uniformly.

## 3. Brun–Titchmarsh can be used by zero-extension

A subtle point is that replacing the actual code length `n_d` by an upper bound cannot be done blindly inside every coding inequality. Here it is valid for a simple structural reason.

If `N\ge n_d`, map

\[
C_{\ell,a}\longrightarrow\mathbb F_\ell^N
\]

by appending `N-n_d` zero coordinates. This is an injective linear map, preserves every Hamming distance exactly, and produces an `[N,m_{\ell,a},\delta_{\ell,a}]_\ell` code. Applying sphere packing in the larger ambient space gives

\[
m_{\ell,a}\le N-\log_\ell V_\ell(N,t_y).
\tag{20}
\]

Taking `N=B_{\ell,a}(y)` from `(10)` proves `(11)`. Thus the analytic shell-count input and the coding bound compose without any monotonicity assumption or hidden model for how the selected primes occupy the progression.

For fixed `d=\ell^a`, `(10)` has

\[
\log B_{\ell,a}(y)=\log y+O(\log\log y).
\tag{21}
\]

Under `(13)`, `t_y=(1/(2\log2)-o(1))\log\log y`, and `(7)`, `(20)`, `(21)` give `(14)` after division by `\log\ell`.

Under `(15)`,

\[
t_y=
\left(\frac1{2\sqrt2}-o(1)\right)
\frac{\sqrt y}{\log y},
\]

while `\log(B_{\ell,a}(y)/t_y)=(1/2+o(1))\log y`. Substitution into `(8)` gives `(16)`.

## 4. What the new bound does and does not buy

The result separates three regimes more cleanly than the Singleton-only frontier.

For large `\ell^a`, progression occupancy itself is thin and the `MC-249`/`MC-250` torsion-order squeeze remains the main constraint. For fixed small `\ell^a`, the shell is broad, but sphere packing converts the universal support floor into a much larger **family-size** penalty. The intermediate regime is governed by the exact Hamming-ball expression `(4)` rather than by a single asymptotic formula.

The gain is still generic coding theory. It does not use reciprocity among different shell primes, correlations among residue-symbol columns, Kummer/Chebotarev structure, or any Möbius sign amplitude. Therefore it cannot by itself prove that low-order primary rank is small relative to `n_d`.

This also clarifies the correct next target. A theorem that merely improves the least support of one blind character may feed `(4)`, but unless it pushes `D_y` to a positive fraction of `n_d` it still leaves an exponentially large family possible. Closing the quotient requires a statement about **simultaneous arithmetic dependence** of the codewords/columns, a substantially stronger distance profile, generalized weights tied to the arithmetic matrix, or direct signed cancellation in the exact rough Möbius coset.

## 5. Prior art and novelty audit

The Hamming sphere-packing bound is classical. The primary citation above is Hamming's 1950 paper; a fresh bibliographic check confirms the Bell System Technical Journal volume, pages, publication date, and DOI. The `q`-ary Hamming-ball formula is the standard alphabet-`q` extension of the same disjoint-ball count and is also derived explicitly here.

`MC-243` already applies the binary Hamming bound to the full quadratic blind kernel. Accordingly, **the coding-theory mechanism itself and its quadratic use are not new**. The durable delta of `MC-251` is narrower: `MC-250` supplies a separate `\ell`-ary code at every primary level with coordinates restricted to `r=1 mod \ell^a`; applying sphere packing there gives `(4)`–`(11)` and the fixed-low-order deficits `(14)` and `(16)`.

A targeted search found no basis for claiming a new coding bound, and none is claimed. The result should be read as an exact specialization/composition of established coding theory with the arithmetic code constructed in `MC-250`.

## Decisive audit

- Every nonzero `C_{\ell,a}` codeword is a nonprincipal blind character, so the distance input `\delta_{\ell,a}\ge D_y` is inherited exactly from `MC-250`.
- The ball radius uses `D_y`, not the unknown true distance, so `(4)` remains valid if the actual distance is larger.
- The factor `(\ell-1)^j` in `(3)` is essential for nonbinary codes.
- Passing from `n_d` to `B_{\ell,a}(y)` is justified by zero-extension, which preserves dimension and distance exactly.
- The unconditional and ERH asymptotics are consequences of the already-recorded support floors only; no new hypothesis on residue-symbol independence is introduced.
- For `\ell=2,a=1`, the mechanism reduces to the binary sphere-packing result of `MC-243`; this is an explicit consistency check, not a novelty claim.
- The bound remains `o(n_d)` in the fixed-order shell regimes of interest and therefore does not imply generation.

## Boundaries and updated frontier

- `MC-250`'s Singleton penalty `D_y-1` is not the strongest generic coding consequence at fixed low torsion order; the correct family-size penalty is at least the q-ary Hamming-ball logarithm in `(5)`.
- Unconditionally this raises the fixed-order generic deficit from `Theta(log log y)` to `Omega(log y log log y)` at the Brun–Titchmarsh shell scale.
- Under the ERH support floor it raises the corresponding generic deficit from `Theta(sqrt(y)/log y)` to `Omega(sqrt(y))`.
- These gains are still sublinear relative to a compatible shell of size `Theta(y/log y)`, so they do not close the low-order quotient.
- The remaining useful directions are arithmetic rank/dependence theorems, stronger distance-profile/generalized-weight information that is not generic-code data, or direct control of the signed rough Möbius coset/complete-annihilator aggregate.