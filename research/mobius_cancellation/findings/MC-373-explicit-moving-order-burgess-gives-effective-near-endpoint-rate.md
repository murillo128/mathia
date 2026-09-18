# MC-373 — Explicit moving-order Burgess gives an effective near-endpoint rate

**Status:** `LITERATURE+DERIVED` · `EXACT-DERIVED` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

The fixed-deficit prime Halász–Montgomery bounds in `MC-323` and `MC-329` can be made genuinely moving-order in the cubefree source regime. A non-optimized but explicit asymptotic choice is

\[
L=\log\log y,\qquad J=\log\log\log y,\qquad
r=\left\lfloor \frac{L}{32}\right\rfloor,
\qquad
\Delta(y)=K\frac{J}{L},
\tag{1}
\]

where `K>0` is a sufficiently large absolute constant and `y` is sufficiently large.

With this choice, the explicit cubefree Burgess theorem of Hasanalizade--Lin--Martin--Luna Martínez--Treviño can be propagated through the Selberg-sieve step in Schlage-Puchta's Proposition 9 without losing the shrinking deficit. In the common-modulus regime, for a family `Xi` of distinct nonprincipal characters whose relevant product moduli are cubefree and satisfy

\[
q\le y^{4-\Delta(y)},
\tag{2}
\]

the normalized prime-shell bias energy admits a bound of the same structural form as `MC-329`, but now with shrinking deficit:

\[
E_y(\Xi)
\ll \frac1{\Delta(y)}
   + |\Xi|\,\exp\!\left(-c\frac{(\log y)J}{L^2}\right)\log y
\tag{3}
\]

for some absolute `c>0` after enlarging `K`. The implied constants are absolute once the displayed choice of `K` is fixed; no optimization of `K` is claimed.

For a family of primitive cubefree characters of individual conductor at most `Q`, Schlage-Puchta's pairwise product step replaces the modulus by an lcm at most `Q^2`. Hence the same argument gives the varying-modulus analogue whenever

\[
Q\le y^{2-\Delta(y)}.
\tag{4}
\]

Consequently the qualitative source frontiers in `MC-323` and `MC-329` can be made effective at the scale

\[
\boxed{
2-O\!\left(\frac{\log\log\log y}{\log\log y}\right)
\quad\text{and}\quad
4-O\!\left(\frac{\log\log\log y}{\log\log y}\right).
}
\tag{5}
\]

This does **not** cross the quadratic or quartic exponents, does not improve the fixed-power horizon of `MC-329`, and gives no estimate for `M(x)`. Its content is that the previously qualitative `y^{2-o(1)}` / `y^{4-o(1)}` approach to those boundaries survives a fully explicit moving Burgess order at a concrete shrinking rate.

## 1. The explicit Burgess theorem permits `r` on the `log log y` scale

Hasanalizade, Lin, Martin, Luna Martínez and Treviño, *Explicit Burgess inequalities for cubefree moduli*, arXiv:2511.17778v1 (21 November 2025), Theorem 1.1, gives for a primitive character modulo cubefree `q` and integer `r>=2` an explicit Burgess estimate with the classical power

\[
N^{1-1/r}q^{(r+1)/(4r^2)}
\tag{6}
\]

and an additional factor

\[
(\log q)^{1/(2r)}
\Bigl((4r)^{\omega(q)}m_r(q)\Bigr)^{1/(2r)-1/(2r^2)}
\left(\frac q{\phi(q)}\right)^{1/r},
\tag{7}
\]

where

\[
m_r(q)=\min\left\{\tau_{2r}(q),\left(\frac{\tau(q)}2\right)^{2r-1},\frac q{2r}\right\}.
\tag{8}
\]

The theorem assumes

\[
q\ge \max\{10^{1145},\exp(\exp(a(r)))\},
\tag{9}
\]

with

\[
a(r)=2\log 2\bigl(3.0758r+1.38402\log(4r)-1.5379\bigr),
\tag{10}
\]

and its tabulated constant is bounded for `r>=10`.

For `r=floor(L/32)`, equation `(10)` gives `a(r)=O(L)` with coefficient strictly below one for all sufficiently large `y`. Thus

\[
\exp(\exp(a(r)))=\exp\bigl((\log y)^{c_0+o(1)}\bigr)=y^{o(1)}
\tag{11}
\]

for some `c_0<1`. The theorem's lower-modulus threshold therefore does not force `r` to remain fixed. Primitive conductors below that subpower threshold can instead be handled by Pólya--Vinogradov; after the prime-shell normalization their contribution is `y^{-1+o(1)}` and is negligible compared with `(3)`.

## 2. Cubefree modulus complexity costs only `exp(O(log y J/L^2))`

Let `w=omega(q)` and suppose `q<=y^4`. Since the distinct prime divisors are at least the first `w` primes, the elementary factorial bound already gives

\[
w=O\left(\frac{\log y}{L}\right).
\tag{12}
\]

For cubefree `q`, every prime exponent is at most two, so

\[
\tau_{2r}(q)\le (C r^2)^w
\tag{13}
\]

for an absolute constant `C`. Therefore the logarithm of the first arithmetic factor in `(7)` is

\[
O\left(\frac{w\log r}{r}\right)
=O\left(\frac{(\log y)J}{L^2}\right).
\tag{14}
\]

The remaining factors are smaller at this scale. Ordering the distinct prime divisors gives the crude but sufficient bound

\[
q/\phi(q)\ll w+1,
\tag{15}
\]

so `(q/phi(q))^{1/r}=\exp(O(1))`; likewise `(log q)^{1/(2r)}=\exp(O(1))`. Hence the complete explicit Burgess overhead in `(7)` is

\[
\boxed{
\exp\left(O\left(\frac{(\log y)J}{L^2}\right)\right).
}
\tag{16}
\]

For the actual endpoint source package, where the odd part is squarefree and only the factor `4` can contribute a squared prime, `(13)` is conservative.

## 3. Induction from primitive conductors does not destroy the scale

The explicit 2025 theorem is stated for primitive characters. If a character modulo `q` is induced from a primitive character `chi*` of conductor `q_0`, write

\[
s=\prod_{p\mid q,\,p\nmid q_0}p.
\tag{17}
\]

Then inclusion--exclusion reduces an interval sum for the induced character to primitive sums with a multiplicative loss bounded by

\[
J_r(s)=\prod_{p\mid s}\left(1+p^{-1+1/r}\right).
\tag{18}
\]

If `w=omega(s)`, ordering the primes gives

\[
\log J_r(s)
\le \sum_{j\le w}j^{-1+1/r}
=O(rw^{1/r})=O(L),
\tag{19}
\]

for `r asymp L`. Thus imprimitive reduction contributes only `exp(O(L))`, negligible relative to `(16)`. If the primitive conductor lies below the threshold `(9)`, Pólya--Vinogradov together with the same inclusion--exclusion is again `y^{-1+o(1)}` after normalization.

## 4. The Selberg-sieve convolution has only polynomial moving-order cost

Schlage-Puchta, *Primes in short arithmetic progressions*, Acta Arith. 106 (2003), 143--149; arXiv:1105.1623, Proposition 9, transfers an incomplete character-sum estimate to the prime-supported Selberg weight. In his notation the resulting Burgess term has the shape

\[
R^{2/r}N^{1-1/r}q^{(r+1)/(4r^2)},
\tag{20}
\]

with the dependence on fixed `r` hidden in the constant. To expose that dependence, write the Selberg cutoff as `B` to avoid collision with the Burgess order `r`. Expanding the sieve weight produces the lcm sum

\[
\Sigma_r(B)=\sum_{d_1,d_2\le B}[d_1,d_2]^{-(1-1/r)}.
\tag{21}
\]

Writing `d_1=gu`, `d_2=gv`, `(u,v)=1`, and summing first over `g` gives the elementary bound

\[
\Sigma_r(B)\ll r^3 B^{2/r}.
\tag{22}
\]

The exact polynomial exponent in `r` is immaterial here; the load-bearing point is that the hidden sieve constant grows only polynomially in `r`, while the only exponential moving-order cost is already accounted for in `(16)`.

Choose

\[
B=y^{\Delta/(64)}.
\tag{23}
\]

Then `B^2<y` for large `y`, the normalized Selberg diagonal is

\[
\frac{\log y}{\log B}=\frac{64}{\Delta}=O(L/J),
\tag{24}
\]

and the factor `B^{2/r}` contributes `Delta/(32r)` to the exponent of `y`.

## 5. The shrinking Burgess deficit dominates every explicit overhead

At a common modulus `q=y^{4-Delta}`, the raw Burgess power after prime-shell normalization is

\[
-\frac1r+\frac{(4-\Delta)(r+1)}{4r^2}.
\tag{25}
\]

Including `(23)`, the exact exponent becomes

\[
-\frac1r+\frac{(4-\Delta)(r+1)}{4r^2}+\frac{\Delta}{32r}
=
\frac{-7\Delta r-8\Delta+32}{32r^2}.
\tag{26}
\]

Thus for `r asymp L` and `Delta=KJ/L`, the structural saving is

\[
\exp\left(-c_1K\frac{(\log y)J}{L^2}ight)
\tag{27}
\]

up to the lower-order `O((log y)/L^2)` term. Combining `(27)` with the overhead `(16)`, the imprimitive cost `(19)`, and the polynomial sieve factor leaves

\[
\exp\left(-c\frac{(\log y)J}{L^2}\right)
\tag{28}
\]

once `K` is chosen larger than the absolute constant in `(16)`. Bombieri's Hilbert-space step is then exactly the one already used in `MC-323` and `MC-329`, giving `(3)`.

For varying primitive cubefree moduli `q_chi<=Q`, Schlage-Puchta Theorem 3 replaces the common modulus by the pairwise lcm and notes that the lcm remains cubefree. Since `[q_chi,q_chi']<=Q^2`, condition `(4)` places every product modulus at most `y^{4-2Delta}`, which is inside the common-modulus range above. This proves the varying-modulus statement.

## 6. Consequences for the existing endpoint frontiers

For a fixed lower bound on individual normalized endpoint bias, `(3)` implies that at most

\[
O(1/\Delta)=O(L/J)
\tag{29}
\]

members of a varying-modulus family can remain below conductor `y^{2-Delta}`, once the exponentially small second term is absorbed. Hence the `MC-323` statement that all but boundedly many biased modes cross every fixed subquadratic range becomes the effective statement that all but `O(L/J)` cross

\[
y^{2-KJ/L}.
\tag{30}
\]

For the common endpoint source family of `MC-329`, the exact lower energy is exponentially large in the rank (`~2^R/R` in the balanced model). Comparing it with `(3)` yields the corresponding source-package exclusion below

\[
y^{4-KJ/L}
\tag{31}
\]

whenever the same rank-side conditions used in `MC-329` make the exponentially small error term negligible and `2^R\Delta/R` tends to infinity.

Equations `(30)`--`(31)` are deliberately rate statements, not new exponent barriers. They quantify how close the existing method can get to its already-proved quadratic/quartic horizon.

## 7. Prior art and novelty boundary

The two external analytic inputs are classical/primary-source mechanisms rather than Mathia inventions:

- Jan-Christoph Schlage-Puchta, *Primes in short arithmetic progressions*, Acta Arith. 106 (2003), 143--149, arXiv:1105.1623. Proposition 9 gives the Selberg-sieve transfer and Theorem 3 the prime-supported Halász--Montgomery family estimate, including the `Q^2` replacement for varying cubefree moduli.
- Elchin Hasanalizade, Hua Lin, Greg Martin, Andradis Luna Martínez and Enrique Treviño, *Explicit Burgess inequalities for cubefree moduli*, arXiv:2511.17778v1 (21 November 2025). Theorem 1.1 gives the explicit cubefree Burgess inequality and explicit admissibility threshold used above. This is an arXiv v1 manuscript and is not treated as peer-reviewed evidence.

A targeted search for the combination of these two results found no source explicitly carrying the 2025 constants through Schlage-Puchta's prime family theorem. **No novelty claim is made**: the durable result here is a derived specialization showing that the previously qualitative Mathia endpoint approach can be made effective at one explicit asymptotic rate.

## 8. Boundaries and falsification tests

- **Primitive-input boundary.** The explicit Burgess theorem is primitive; `(17)`--`(19)` are required before it can be used for induced endpoint characters.
- **Cubefree boundary.** Arbitrary moving Burgess order depends on cubefree product moduli. The actual lower-prime source radicals satisfy this apart from the harmless fixed `2`-adic square in `4P`; the statement does not extend to unrestricted highly powerful moduli.
- **No endpoint crossing.** Equation `(26)` still has the quartic Burgess horizon. Letting `r` grow only makes a shrinking deficit effective; it cannot produce a fixed gain beyond exponent `4`, and the varying-modulus squaring keeps the corresponding exponent at `2`.
- **The rate is not optimized.** The constants `32`, `64`, and `K` were chosen for a clean domination argument. Better bookkeeping can improve the coefficient and may improve the slowly varying function, but such optimization is not part of this finding.
- **Large-`q` manuscript threshold matters.** The explicit theorem's enormous threshold is handled asymptotically by `(11)`, not numerically. This is an asymptotic research result, not a practical finite-height estimate.
- **No Möbius conclusion.** The result quantifies a source-conductor frontier inside the endpoint realization program. It supplies no unconditional improvement for `M(x)` and no zero-free region for zeta.

## Consequence

The proposed moving-order clue is resolved positively in a non-optimized form: the explicit 2025 cubefree Burgess theorem is strong enough to pass through the prime Selberg/Halász--Montgomery mechanism with `r` growing like `log log y`. The first explicit rate that survives all audited costs is

\[
\Delta(y)=O\left(\frac{\log\log\log y}{\log\log y}\right).
\]

The dominant near-endpoint tariff is the modulus-complexity factor in the explicit Burgess theorem, not the tabulated `C(r)` and not an exponential blow-up hidden in Schlage-Puchta's Selberg convolution. The quadratic and quartic horizons themselves remain intact.