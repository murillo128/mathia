# MC-250 — Blind primary multiplicity obeys a Singleton shell-occupancy tradeoff

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `FRONTIER-REFINEMENT`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the shell-square blind quotient of `MC-238`–`MC-249`. Write

\[
G=(\mathbb Z/Q_S\mathbb Z)^\times,
\qquad
H=\langle p\bmod Q_S:p\le y\text{ prime}\rangle,
\qquad
\mathcal Q=G/H,
\]

and identify the blind-character group

\[
A:=H^\perp\cong \widehat{\mathcal Q}.
\]

Fix a prime `\ell` and an integer `a\ge1`, put

\[
d=\ell^a,
\]

and write the `\ell`-primary part of `A` as

\[
A_{(\ell)}\cong
\bigoplus_{j=1}^{r_\ell}\mathbb Z/\ell^{b_j}\mathbb Z.
\tag{1}
\]

Define the level-`a` primary multiplicity

\[
m_{\ell,a}:=\#\{j:b_j\ge a\}.
\tag{2}
\]

Because finite abelian groups and their character groups have the same invariant factors, `m_{\ell,a}` is also the number of cyclic `\ell`-primary invariant factors of `\mathcal Q` whose order is at least `\ell^a`.

Let `D_y` be any **integer** lower bound valid for the active shell support of every nonprincipal blind character at this scale. For example, `MC-242` gives unconditionally

\[
D_y=\left(\frac1{\log2}-o(1)\right)\log\log y,
\tag{3}
\]

and `MC-247` gives under its ERH hypothesis

\[
D_y=\left(\frac1{\sqrt2}-o(1)\right)
\frac{\sqrt y}{\log y}.
\tag{4}
\]

Then whenever `m_{\ell,a}>0`, the order-`\ell` shadow of the level-`a` blind torsion is an `\mathbb F_\ell`-linear code supported only on

\[
S_d:=\{r\in S:r\equiv1\pmod d\},
\qquad n_d:=|S_d|,
\tag{5}
\]

with dimension exactly `m_{\ell,a}` and minimum Hamming distance at least `D_y`. The classical Singleton bound therefore gives the exact shell inequality

\[
\boxed{
D_y+m_{\ell,a}-1\le n_d.
}
\tag{6}
\]

Combining `(6)` with the same arbitrary-interval Brun–Titchmarsh input used in `MC-249` yields

\[
\boxed{
D_y+m_{\ell,a}-1
\le
\#\{r\in S:r\equiv1\pmod{\ell^a}\}
<
\frac{2y}{\varphi(\ell^a)
\{\log(y/\ell^a)+0.8601\}}.
}
\tag{7}
\]

In particular, because `\varphi(\ell^a)\ge \ell^a/2`, if

\[
z:=\frac{y}{\ell^a},
\qquad
R_{\ell,a}:=D_y+m_{\ell,a}-1,
\]

then for all sufficiently large `y`,

\[
\boxed{
R_{\ell,a}
<
\frac{4z}{\log z+0.8601}.
}
\tag{8}
\]

Thus `MC-249` is the special case in which only `m_{\ell,a}\ge1` is used. The additional invariant-factor multiplicity cannot be simultaneously large with a large surviving torsion order.

When `R_{\ell,a}\to\infty`, inversion of `(8)` gives the asymptotic order–rank tradeoff

\[
\boxed{
\ell^a
\le
(4+o(1))
\frac{y}{R_{\ell,a}\log R_{\ell,a}}.
}
\tag{9}
\]

For a prime divisor `d=\ell\to\infty`, `\varphi(\ell)/\ell=1+o(1)` improves the leading factor `4` to `2`:

\[
\boxed{
\ell
\le
(2+o(1))
\frac{y}{R_{\ell,1}\log R_{\ell,1}}.
}
\tag{10}
\]

Equations `(6)`–`(10)` are a genuine refinement of the current frontier. Support, torsion order, and primary rank remain different currencies, but the shell arithmetic now couples them quantitatively: **a level-`\ell^a` quotient component of multiplicity `m` consumes at least `D_y+m-1` shell primes in the progression `1 mod \ell^a`.**

This still does not prove `\mathcal Q=1`. For fixed small `\ell^a`, the progression shell can contain far more than `D_y` primes, so a large low-order primary rank remains compatible with the present support information. The surviving generation problem is therefore reduced more sharply: it is not enough to squeeze the quotient exponent; one must control the low-order primary multiplicities beyond the generic coding bounds, or bypass generation by controlling the signed rough Möbius coset of `MC-246`.

No bound for `M(X)`, no proof of `H=G`, and no consequence for the zeta zero set is obtained.

## 1. The level-`a` torsion shadow is an exact `\mathbb F_\ell` code

Consider

\[
A[\ell^a]
:=
\{\eta\in A:\eta^{\ell^a}=1\}
\]

and the power map

\[
P_a:A[\ell^a]\longrightarrow A[\ell],
\qquad
P_a(\eta)=\eta^{\ell^{a-1}}.
\tag{11}
\]

Let

\[
C_{\ell,a}:=\operatorname{im}P_a.
\tag{12}
\]

Every element of `C_{\ell,a}` has exponent dividing `\ell`, so after choosing a primitive `\ell`th root of unity it is naturally an `\mathbb F_\ell`-vector space.

The decomposition `(1)` computes its dimension exactly. On a cyclic factor `\mathbb Z/\ell^{b_j}\mathbb Z`, the subgroup killed by `\ell^a` has order `\ell^{\min(a,b_j)}`. Multiplication by `\ell^{a-1}` has a one-dimensional order-`\ell` image exactly when `b_j\ge a`, and has zero image when `b_j<a`. Hence

\[
\boxed{
\dim_{\mathbb F_\ell}C_{\ell,a}=m_{\ell,a}.
}
\tag{13}
\]

By `MC-239` and `MC-249`, every blind character factors through the squarefree shell product

\[
\prod_{r\in S}(\mathbb Z/r\mathbb Z)^\times.
\tag{14}
\]

The local character group at a shell prime `r` is cyclic of order `r-1`. If a local coordinate of `P_a(\eta)` is nonprincipal, the corresponding local coordinate of `\eta` must have exact `\ell^a`-order before applying `P_a`; therefore

\[
\ell^a\mid r-1.
\tag{15}
\]

Consequently every codeword in `C_{\ell,a}` vanishes outside `S_d` from `(5)`.

At each `r\in S_d`, the local order-`\ell` character subgroup is one-dimensional over `\mathbb F_\ell`. Choosing one local generator identifies

\[
C_{\ell,a}\hookrightarrow \mathbb F_\ell^{S_d}.
\tag{16}
\]

The choice changes coordinates by nonzero scalars only and therefore does not change Hamming support. Every nonzero vector in `(16)` is a nonprincipal blind character, so by definition of `D_y` its weight is at least `D_y`. Thus `C_{\ell,a}` is an

\[
[n_d,m_{\ell,a},\delta_{\ell,a}]_\ell
\]

linear code with

\[
\delta_{\ell,a}\ge D_y.
\tag{17}
\]

No independence model for residue symbols or shell primes is used in this construction.

## 2. Singleton converts support into primary-rank pressure

For any `q`-ary linear `[n,k,\delta]_q` code, the Singleton bound states

\[
k\le n-\delta+1.
\tag{18}
\]

Applying `(18)` to `(17)` gives

\[
m_{\ell,a}
\le
n_d-\delta_{\ell,a}+1
\le
n_d-D_y+1,
\]

which is exactly `(6)`.

The mechanism can also be read without coding terminology. Puncturing any `\delta_{\ell,a}-1` coordinates of a code with minimum distance `\delta_{\ell,a}` remains injective, because two codewords that become equal would differ in at most `\delta_{\ell,a}-1` coordinates. An injective image in `\mathbb F_\ell^{n_d-\delta_{\ell,a}+1}` can have dimension at most that ambient dimension. The coding statement therefore records an elementary but exact information constraint on the blind-character family.

The source is Richard C. Singleton, *Maximum distance q-nary codes*, IEEE Transactions on Information Theory **10** (1964), 116–118, DOI `10.1109/TIT.1964.1053661`. Singleton proves that a `q`-ary code with `q^k` codewords and length `n=k+r` has minimum distance at most `r+1`; `(18)` is the linear-code form.

## 3. Brun–Titchmarsh turns the rank pressure into an order–rank tradeoff

Equation `(6)` is shell-specific because the code is not allowed to use arbitrary coordinates: all of its active coordinates lie among primes

\[
r\equiv1\pmod{\ell^a}.
\]

As in `MC-249`, the selected shell count is safely bounded by all primes in that progression:

\[
n_d
\le
\pi(2y;\ell^a,1)-\pi(y;\ell^a,1).
\tag{19}
\]

If `m_{\ell,a}>0`, then `n_d\ge D_y`; in all current support regimes `D_y\to\infty`. Hence eventually `\ell^a<y`, since an interval `(y,2y]` contains at most one integer congruent to `1 mod d` when `d\ge y`. Tomohiro Yamada's explicit arbitrary-interval Brun–Titchmarsh estimate used in `MC-249` therefore applies:

\[
\pi(2y;d,1)-\pi(y;d,1)
<
\frac{2y}{\varphi(d)\{\log(y/d)+0.8601\}}.
\tag{20}
\]

Combining `(6)`, `(19)`, and `(20)` proves `(7)`. For `d=\ell^a`, the elementary bound

\[
\varphi(d)=d(1-1/\ell)\ge d/2
\]

gives `(8)`.

To invert `(8)`, suppose `R:=R_{\ell,a}\to\infty`. Then `z\to\infty`, and the increasing function

\[
z\mapsto \frac{z}{\log z+0.8601}
\]

has asymptotic inverse

\[
u\mapsto (1+o(1))u\log u.
\]

Thus `(8)` forces

\[
z\ge\left(\frac14-o(1)\right)R\log R,
\]

which is equivalent to `(9)`. For `d=\ell\to\infty`, `(20)` has coefficient `2+o(1)` after division by `\varphi(\ell)`, giving `(10)`.

Two checks recover the preceding frontier exactly:

- If `m_{\ell,a}=1`, then `R_{\ell,a}=D_y`, and `(9)` reproduces the prime-power order scale of `MC-249`.
- Under ERH, inserting `(4)` with `m_{\ell,a}=1` gives `(8\sqrt2+o(1))\sqrt y`, while `(10)` gives `(4\sqrt2+o(1))\sqrt y` for prime divisors, exactly the constants isolated in `MC-249`.

The new information appears when the primary multiplicity itself grows. If

\[
m_{\ell,a}\gg D_y,
\]

then `(9)` becomes

\[
\ell^a
\le
(4+o(1))
\frac{y}{m_{\ell,a}\log m_{\ell,a}},
\tag{21}
\]

so high-order torsion and high primary rank cannot coexist at the same shell scale.

## 4. Exact occupancy slack is the cleanest rank observable

The strongest form of the result is actually `(6)`, before replacing the selected shell by a Brun–Titchmarsh upper bound. It can be rewritten as

\[
\boxed{
m_{\ell,a}
\le
\#\{r\in S:r\equiv1\pmod{\ell^a}\}
-D_y+1.
}
\tag{22}
\]

Thus if the progression occupancy exceeds the universal blind-support floor by only `\Delta_y`,

\[
\#\{r\in S:r\equiv1\pmod{\ell^a}\}
\le D_y+\Delta_y,
\]

then necessarily

\[
\boxed{m_{\ell,a}\le\Delta_y+1.}
\tag{23}
\]

This is the missing bridge between the two currencies separated in `MC-249`: support and exponent do not determine quotient rank separately, but **support plus exact shell occupancy bounds the multiplicity at each torsion level**.

It also identifies what stronger shell arithmetic would have to supply. One does not need a direct full-rank theorem immediately. Any theorem proving near-minimal occupancy of the order-compatible sub-shell, or otherwise lowering the effective code length at fixed `\ell^a`, would directly squeeze the corresponding primary rank through `(22)`.

## 5. Why this still does not close the low-order quotient

The tradeoff is strongest for large `\ell^a`, because the progression `1 mod \ell^a` is thin. It is deliberately weak for fixed small `\ell`, where the shell has many admissible coordinates.

This weakness is not merely a loose use of Singleton. If an `\mathbb F_\ell` code has ambient length `n` and minimum distance `D=o(n)`, the classical linear Gilbert–Varshamov mechanism permits codes of dimension

\[
n-O\!\left(
D\frac{\log(n/D)}{\log\ell}
\right).
\tag{24}
\]

Equivalently, minimum-support information with vanishing relative distance is compatible in the abstract coding category with nearly full dimension. The binary instance of this information barrier was already isolated for the quadratic blind code in `MC-243`; `(24)` shows that moving to odd primary layers does not remove the generic obstruction.

The Gilbert and Varshamov mechanisms are classical: E. N. Gilbert, *A Comparison of Signalling Alphabets*, Bell System Technical Journal **31** (1952), 504–522; R. R. Varshamov, *Estimate of the number of signals in error correcting codes*, Doklady Akademii Nauk SSSR **117** (1957), 739–741. No claim is made that an abstract near-full-rate code from those constructions occurs as a shell blind-character family. It is a matched information control only.

Therefore the post-`MC-249` problem genuinely has two layers:

1. large torsion order is increasingly incompatible with large primary multiplicity by `(9)`;
2. fixed low-order primary rank can still be large unless one uses simultaneous arithmetic structure beyond minimum support and coarse progression occupancy.

The first is new frontier information. The second prevents it from being mistaken for a generation theorem.

## 6. Prior-art and novelty audit

The external ingredients are established mathematics: finite-abelian primary decomposition and Pontryagin duality for finite groups; the Singleton bound; the Gilbert–Varshamov coding comparison; and the Brun–Titchmarsh estimate already audited in `MC-249`.

A targeted literature search was run for combinations of least primes outside multiplicative subgroups, Dirichlet-character support, subgroup generation by small primes, and `q`-ary coding bounds. It returned the standard coding-theory parameter bounds and the generic subgroup/nonresidue literature already represented in `MC-248`–`MC-249`, but no source was used to assert this exact shell-quotient invariant-factor tradeoff. **No novelty is claimed** for any coding or analytic-number-theory ingredient, and absence from the targeted search is not treated as evidence of novelty.

The durable Mathia delta is the exact composition of existing shell structure with those classical bounds: the level-`a` image `(12)` identifies the relevant quotient invariant-factor multiplicity as a linear-code dimension; its support is forced into one thin progression by shell arithmetic; Singleton then couples rank to occupancy; Brun–Titchmarsh turns that coupling into `(9)`.

This directly answers the next question left by `MC-249` at the level that current support information permits: **torsion rank is not independent of torsion order, but the coupling becomes too weak at fixed low order to force quotient triviality.**

## 7. Boundaries and falsification tests

- `m_{\ell,a}` counts cyclic `\ell`-primary factors of order at least `\ell^a`; it is not the full `\ell`-adic valuation of `|\mathcal Q|` and is not the same as the exponent.
- The code `C_{\ell,a}` is the image of the level-`a` torsion under the power map `(11)`, not the entire order-`\ell` blind sector unless `a=1`.
- The support restriction to `r\equiv1 mod \ell^a` uses the preimage order before applying `(11)`; replacing it by the weaker condition `r\equiv1 mod\ell` would lose the order–rank coupling.
- Singleton gives an upper bound on `m_{\ell,a}` from the actual selected-shell occupancy. It does not assert that the bound is sharp for the arithmetic code.
- Brun–Titchmarsh counts all primes in the progression and can be much weaker than the actual selected-shell occupancy; `(22)`, not `(9)`, is the exact shell statement.
- The current unconditional and ERH support floors are inherited unchanged from `MC-242` and `MC-247`; this finding does not strengthen them.
- The Gilbert–Varshamov comparison is a falsification control for information sufficiency, not an arithmetic construction of blind characters.
- Large-order torsion is squeezed more strongly when its multiplicity grows, but fixed small-order high-rank torsion remains a live possibility.
- No contour shift, reciprocal-`L` continuation, zero-free region, or assumption equivalent to the desired Mertens bound is introduced.