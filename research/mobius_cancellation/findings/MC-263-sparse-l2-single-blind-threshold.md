# MC-263 — Sparse-family L2 balance cannot by itself certify blind-kernel triviality

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the quadratic shell notation of `MC-238`, `MC-243`, `MC-253`, and `MC-262`. Let

\[
\mathcal P_y=\{p\le y:p\text{ odd prime}\},
\qquad
\mathcal R_y=\{r:y<r\le2y,\ r\text{ prime}\},
\]

write

\[
k_y=|\mathcal P_y|,
\qquad
N_y=|\mathcal R_y|,
\]

and for a `t`-element subset `T\subset\mathcal R_y` put

\[
B_y(T)=
\sum_{p\in\mathcal P_y}
\prod_{r\in T}\left(\frac pr\right).
\tag{1}
\]

A quadratic blind relation supported on `T` is exactly the condition

\[
\prod_{r\in T}\left(\frac pr\right)=1
\qquad(p\in\mathcal P_y),
\tag{2}
\]

hence every blind `T` satisfies

\[
B_y(T)=k_y.
\tag{3}
\]

Define the weight-`t` blind enumerator and the corresponding shell second moment by

\[
A_y(t)
:=
\#\{T\subset\mathcal R_y:|T|=t,\ T\text{ is blind}\},
\tag{4}
\]

\[
S_y(t)
:=
\sum_{\substack{T\subset\mathcal R_y\\|T|=t}}
|B_y(T)|^2,
\qquad
C_y(t):=\binom{N_y}{t}.
\tag{5}
\]

Then positivity and `(3)` give the exact counting inequality

\[
\boxed{
A_y(t)\,k_y^2\le S_y(t).
}
\tag{6}
\]

Consequently a second-moment **upper bound alone** can certify the absence of every weight-`t` blind relation only when the proved numerical upper bound is strictly below the contribution of one blind vector:

\[
\boxed{
S_y(t)<k_y^2.
}
\tag{7}
\]

Equivalently, in the normalized average used in `MC-253` and `MC-262`, the required threshold is

\[
\boxed{
\frac1{C_y(t)}
\sum_{|T|=t}
\left|\frac{B_y(T)}{k_y}\right|^2
<
\frac1{C_y(t)}.
}
\tag{8}
\]

This exposes a stronger information barrier than the explicit-constant obstruction of `MC-262`. At the first support scale where a blind relation can survive, `MC-242` gives

\[
t\ge
\left(\frac1{\log2}-o(1)\right)\log\log y.
\tag{9}
\]

For any

\[
t=(\alpha+o(1))\log\log y,
\qquad \alpha>0,
\tag{10}
\]

the prime number theorem gives `N_y\sim y/\log y` and therefore

\[
\log C_y(t)
=t\log\frac{N_y}{t}+O(t)
=(\alpha+o(1))\log y\,\log\log y.
\tag{11}
\]

Thus the normalized L2 threshold capable of excluding even **one** blind relation is

\[
\boxed{
C_y(t)^{-1}
=
\exp\!\left(- (\alpha+o(1))\log y\,\log\log y\right)
=
y^{-\alpha\log\log y+o(\log\log y)}.
}
\tag{12}
\]

At the support floor `(9)`, take `\alpha=1/\log2` up to the existing `o(1)` term. The required average is then far smaller than any fixed power `y^{-A}`.

This has an immediate consequence for the sparse-product-family escape suggested after `MC-262`. Suppose a future direct large-sieve theorem over the exact shell-product family proves only the natural family-size/diagonal-scale estimate

\[
S_y(t)
\le
L_y\,C_y(t)\,k_y,
\tag{13}
\]

where `L_y\ge1` is polylogarithmic, subpower, or even bounded. Such an estimate may be extremely strong as an **average balance theorem**, but `(6)` gives only

\[
A_y(t)
\le
L_y\frac{C_y(t)}{k_y}.
\tag{14}
\]

To force `A_y(t)=0` from `(13)` would require

\[
L_y C_y(t)<k_y.
\tag{15}
\]

In the live range `(9)`, however,

\[
C_y(t)/k_y
=
\exp\!\left((1/\log2+o(1))\log y\,\log\log y\right),
\tag{16}
\]

up to the negligible single factor `k_y=y^{1+o(1)}` in logarithmic scale, so `(15)` fails overwhelmingly. Indeed it already fails for the natural diagonal-scale estimate at every fixed `t>=2` once `y` is large.

Therefore:

\[
\boxed{
\text{a shell-specific quadratic large sieve whose leading cost merely tracks the number of shell products}
\not\Rightarrow
\text{quadratic blind-kernel triviality.}
}
\tag{17}
\]

Reducing the ambient all-squarefree-moduli cost from `MC-262` to the sparse-family cardinality would remove a real analytic inefficiency, but it would still leave an **exceptional-set barrier**: generation asks whether there are zero exact blind subsets, while a second moment at natural scale is designed to show that almost all subsets are balanced. One exceptional codeword may be invisible to that conclusion.

A useful next theorem must therefore do more than improve the average L2 normalization. It must supply at least one of:

- a maximum/large-deviation estimate strong enough to cross `(8)`;
- a direct upper bound for the weight enumerator `A_y(t)` that becomes `<1` in the live support range;
- an arithmetic theorem showing that one blind relation forces a sufficiently large family of additional blind relations at controlled weights, so that `(6)` amplifies one exception into detectable L2 mass;
- a direct rank/generation theorem; or
- signed cancellation of the surviving source projector/blind pretender, bypassing generation entirely.

No claim is made that a specialized sparse-family theorem of one of these stronger types is impossible. The obstruction concerns **second-moment balance at family-size scale**, not all possible uses of the shell-product family.

No new bound for `M(X)`, no improvement of the support floor `(9)`, and no proof or disproof of `H=G` is obtained.

## 1. Blind relations are atoms of the second moment

For each `T`, every summand in `(1)` is `+1` or `-1`. Hence

\[
|B_y(T)|\le k_y.
\tag{18}
\]

If `T` is blind, every sign is `+1`, so `(3)` is exact. Splitting the nonnegative sum `(5)` into blind and nonblind subsets immediately gives `(6)`.

Since `A_y(t)` is an integer, an upper estimate `S_y(t)\le U_y(t)` proves `A_y(t)=0` whenever `U_y(t)<k_y^2`. Conversely, if an upper-bound argument only reaches `U_y(t)\ge k_y^2`, that numerical estimate by itself cannot rule out the contribution of one blind subset. This is the precise sense in which `(7)` is the exclusion threshold for an upper-bound-only L2 route.

Dividing `(6)` by `C_y(t)k_y^2` gives

\[
\frac{A_y(t)}{C_y(t)}
\le
\frac1{C_y(t)}
\sum_{|T|=t}
\left|\frac{B_y(T)}{k_y}\right|^2.
\tag{19}
\]

Equation `(19)` is excellent for proving that blind subsets have density tending to zero. But generation requires `A_y(t)=0`, not merely `A_y(t)=o(C_y(t))`. The gap between those statements is exactly the factor `C_y(t)` in `(8)`.

## 2. The live support scale makes the exclusion threshold super-polynomially small

The prime number theorem gives

\[
N_y
=\pi(2y)-\pi(y)
\sim\frac y{\log y}.
\tag{20}
\]

When `t=(\alpha+o(1))\log\log y`, we have `t=o(N_y)`, so Stirling's formula yields

\[
\log\binom{N_y}{t}
=t\log\frac{N_y}{t}+O(t).
\tag{21}
\]

Now

\[
\log\frac{N_y}{t}
=
\log y-\log\log y-\log t+O(1)
=
(1+o(1))\log y.
\tag{22}
\]

Combining `(21)` and `(22)` proves `(11)` and `(12)`.

This scale comparison is independent of Liu's explicit `\varepsilon`-dependence. Even in the hypothetical situation where the normalized mean-square decay

\[
\frac1{C_y(t)}
\sum_{|T|=t}
\left|\frac{B_y(T)}{k_y}\right|^2
\le y^{-1+o(1)}
\tag{23}
\]

from the small-order regime of `MC-262` extended unchanged all the way to `t\asymp\log\log y`, `(23)` would still be vastly larger than the exclusion threshold `(12)`. It would prove spectacular typical balance while remaining compatible with isolated exact blind relations.

Thus the fourth-iterated-log ceiling in `MC-262` is not the only obstruction to the proposed L2 route. Improving its parameter uniformity without simultaneously changing the **tail strength / exceptional-set conclusion** does not reach generation.

## 3. A sparse-family large sieve needs more than the correct family cardinality

A natural direct large-sieve target for a family `\mathcal F` of `C` characters acting on `k` coefficients has the schematic diagonal scale

\[
\sum_{\chi\in\mathcal F}
\left|\sum_{j=1}^{k}a_j\chi(j)\right|^2
\lesssim
L\,C\sum_{j=1}^{k}|a_j|^2,
\tag{24}
\]

when the family-size term dominates the coefficient-length term. For the present coefficients `a_p=1` and shell-product family, `(24)` becomes exactly the schematic estimate `(13)`.

Equation `(13)` is **not asserted to be a universal lower bound or an unavoidable theorem shape**. Off-diagonal terms can cancel, and a shell-specific theorem could in principle be much stronger. The point is conditional and diagnostic: if the hoped-for improvement over `MC-262` changes only the ambient counting cost from all squarefree moduli to `C_y(t)` while retaining a natural L2 family-average scale, it still cannot satisfy `(7)` in the live range.

Indeed, substituting `(13)` into `(6)` gives `(14)` exactly. Since `k_y\sim y/\log y`, while for `t>=2`

\[
C_y(t)\ge\binom{N_y}{2}\asymp k_y^2,
\tag{25}
\]

up to asymptotically constant `N_y/k_y`, the right side of `(14)` is already much larger than `1` for any `L_y\ge1`. At `t\asymp\log\log y` the mismatch becomes the super-polynomial factor `(16)`.

Accordingly the phrase "product-family quadratic large sieve" is too weak as a frontier specification. The required object is closer to an **inverse/exceptional-set large sieve, weight-enumerator bound, or rank theorem**: it must distinguish `A_y(t)=0` from `A_y(t)=1`, not merely distinguish a positive-density exceptional family from a zero-density one.

## 4. Coding theory shows why linearity does not automatically amplify one exception enough

By `MC-238`, the full set of quadratic blind relations is the binary linear code

\[
K_y=\ker_{\mathbb F_2}A.
\tag{26}
\]

The numbers `A_y(t)` are precisely the nonzero weight distribution of this code. This is the classical weight-enumerator viewpoint: the Hamming weight enumerator records how many codewords occur at each support size. MacWilliams' identity relates the weight enumerator of a linear code to that of its dual, but it does not determine the needed shell weight distribution from low-order parity balance alone.

Most importantly, linearity by itself does not force many weight-`t` exceptions from one. As already noted in `MC-243`, a one-dimensional binary kernel

\[
K=\{0,v\}
\tag{27}
\]

has exactly one nonzero codeword, whatever the Hamming weight of `v` is. Thus an exact blind relation can contribute only the single atom `k_y^2` to one shell second moment. Any amplification theorem strong enough to make `(13)` decisive must use additional arithmetic structure of the Legendre shell matrix, not merely the fact that its kernel is linear.

This also sharpens the relation with `MC-244`. That finding showed that reducing a positive blind **dimension** does not buy a source-side exponent after the whole blind family is Fourier-inverted: mode count and source density cancel. The present finding is the complementary dual-space statement: reducing the **density of blind supports of a given weight** to almost zero does not eliminate the obstruction either. Generation is a zero-versus-nonzero question.

## 5. Prior-art and novelty audit

The analytic background is the quadratic large-sieve literature already audited in `MC-253` and `MC-262`: D. R. Heath-Brown, *A mean value estimate for real character sums*, Acta Arithmetica 72 (1995), 235–275, DOI `10.4064/aa-72-3-235-275`; and Zihao Liu, *Explicit quadratic large sieve inequality*, Acta Arithmetica 223 (2026), 227–252, DOI `10.4064/aa250722-27-1`, arXiv `2505.09637`.

The coding-theory language is classical. Jessie MacWilliams, *A Theorem on the Distribution of Weights in a Systematic Code*, Bell System Technical Journal 42 (1963), 79–94, DOI `10.1002/j.1538-7305.1963.tb04003.x`, establishes the classical weight-enumerator/dual-code relation. No novelty is claimed for weight enumerators, MacWilliams identities, Markov's inequality, second-moment counting, or the general fact that an average estimate need not exclude one exceptional object.

A targeted prior-art search through 13 September 2026 found no theorem that turns the currently available shell-product L2 information into zero weight enumerator at `t\asymp\log\log y`, and no shell-specific inverse large-sieve theorem was identified that supplies the missing amplification. This is not a bibliographic completeness claim.

The durable Mathia delta is the exact quantitative audit of the **proposed sparse-family L2 exit** at the current shell scale: one blind relation contributes `k_y^2`, the family contains `C_y(t)` candidates, and therefore the normalized mean square must cross `1/C_y(t)` to exclude a single exception unless additional arithmetic structure amplifies blindness. At the live support floor this threshold is `y^{-Theta(log log y)}`, so merely obtaining the natural sparse-family mean-square scale cannot close generation.

## 6. Boundaries and updated frontier

- `(6)` is one-way. Large `S_y(t)` does not imply a blind relation; nonblind subsets may also have large bias.
- `(7)` is the threshold for **certification from a scalar upper bound on this second moment alone**. It is not a claim that every proof of `A_y(t)=0` must pass through `S_y(t)<k_y^2`.
- `(13)` is a hypothetical theorem class used to audit the proposed route. It is not asserted as a known sharp bound for the sparse shell family and not as a deterministic lower floor.
- The existing Liu/Heath-Brown bounds remain valuable for typical parity pseudorandomness. This finding changes only their relevance to the zero-exception generation gate.
- A theorem proving that every nonzero shell kernel has many codewords in one controlled weight range could restore an L2 route by replacing the single-atom threshold in `(6)` with a larger compulsory mass. No such theorem is supplied here.
- A maximum bound `max_{|T|=t}|B_y(T)|<k_y` would exclude weight-`t` blindness immediately; obtaining such a uniform theorem is qualitatively stronger than mean-square balance.
- Direct proof of `H=G`, direct control of the single blind pretender/source projector, or another source-coupled signed theorem remain live alternatives.

The current generation frontier should therefore distinguish **family localization** from **exception elimination**. `MC-262` showed that the ambient all-moduli large sieve wastes too much uniformity before reaching the live support order. The present result shows that even after removing that waste, a natural L2 theorem would still stop at typicality unless it also upgrades the exceptional-set information.