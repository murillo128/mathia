# MC-294 — Page-balanced cheap subspaces force a quotient-girth tax on near-negative modes

**Status:** `EXACT-DERIVED` · `FRONTIER-REFINEMENT` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the weighted Boolean-shell notation of `MC-291`–`MC-293`. Let

\[
H\cong \mathbf F_2^r,
\qquad
p(s)=\frac{n_s}{N},
\qquad
x_\lambda=\sum_{s\in H}p(s)(-1)^{\lambda(s)},
\qquad
d_\lambda=\frac{1+x_\lambda}{2}.
\tag{1}
\]

Thus `d_lambda` is the shell mass on which the character `lambda` fails to take its preferred value `-1`.

Use the source cost `Q(lambda)` and the Page scale from `MC-293`,

\[
D_y=\exp\!\left(\kappa\frac{\log y}{\log\log y}\right),
\tag{2}
\]

with `kappa>0` chosen sufficiently small. Then there is `epsilon_y=O((\log y)^{-2})` and at most one nonzero shell functional `lambda_*` such that

\[
Q(w)\le D_y,
\qquad w\ne0,\lambda_*
\quad\Longrightarrow\quad
|x_w|\le\epsilon_y.
\tag{3}
\]

Call a subspace

\[
W\le H^*,\qquad \dim W=d,
\tag{4}
\]

**uniformly Page-cheap** when every nonzero `w in W` has `Q(w)<=D_y`. A sufficient concrete construction is to take the span of lower-prime coordinate functionals from a set `U` whose total square-free source product is at most `D_y`; every element of that span then has a representative supported inside `U`.

Let

\[
\lambda_1,\ldots,\lambda_R\in H^*
\tag{5}
\]

be linearly independent and satisfy

\[
d_{\lambda_i}\le\tau
\qquad(1\le i\le R).
\tag{6}
\]

Let `pi:H^* -> H^*/W` be the quotient map. Fix an integer `t>=1` such that

\[
\boxed{2t\tau+\epsilon_y<1.}
\tag{7}
\]

Then:

1. among all nonempty subsets `I subset {1,...,R}` with `|I|<=t`, **at most one** can satisfy
   \[
   \sum_{i\in I}\pi(\lambda_i)=0;
   \tag{8}
   \]
2. after deleting at most one `lambda_i`, the remaining quotient vectors have no nonempty zero-sum subset of size at most `t`;
3. consequently, with
   \[
   m=\left\lfloor\frac t2\right\rfloor,
   \tag{9}
   \]
   the classical binary Hamming sphere-packing bound gives
   \[
   \boxed{
   2^{r-d}
   \ge
   \sum_{j=0}^{m}\binom{R-1}{j}.
   }
   \tag{10}
   \]

In particular, whenever `R-1>=m>=1`,

\[
\boxed{
r-d
\ge
m\log_2\!\left(\frac{R-1}{m}\right).
}
\tag{11}
\]

Thus `MC-293` has a collective strengthening. It was already known there that all but at most one **individual** near-negative direction must have source cost above `D_y`. The new statement says that many independent near-negative directions cannot merely reuse a small number of expensive quotient directions while differing by cheap corrections: modulo any uniformly Page-cheap subspace, their images must form, after one possible exceptional deletion, a parity-check configuration of minimum dependence length greater than `t`. A large near-negative family therefore spends genuine **high-source-complexity quotient dimension**, not only high source cost one mode at a time.

No estimate for `M(x)` follows. The surviving escape remains that the shell dual may have enough high-source-cost quotient dimension to pay `(10)`.

## 1. A short quotient relation would create a strongly biased cheap character

Let `I` be nonempty, write `k=|I|<=t`, and suppose `(8)` holds. Then

\[
\mu_I:=\sum_{i\in I}\lambda_i\in W.
\tag{12}
\]

Because the `lambda_i` are linearly independent and `I` is nonempty,

\[
\mu_I\ne0.
\tag{13}
\]

For shell point `s`, define

\[
Y_i(s):=-(-1)^{\lambda_i(s)}.
\tag{14}
\]

The variable `Y_i` equals `+1` on the preferred set `lambda_i(s)=1` and equals `-1` on the defect set `lambda_i(s)=0`, whose `p`-mass is `d_{lambda_i}`. Hence

\[
\Pr_p[Y_i=-1]=d_{\lambda_i}\le\tau.
\tag{15}
\]

Moreover,

\[
\prod_{i\in I}Y_i(s)
=(-1)^k(-1)^{\mu_I(s)}.
\tag{16}
\]

The product in `(16)` can differ from `+1` only if at least one defect event occurs. By the union bound,

\[
\Pr_p\!\left[\prod_{i\in I}Y_i=-1\right]
\le
\sum_{i\in I}d_{\lambda_i}.
\tag{17}
\]

Therefore

\[
(-1)^k x_{\mu_I}
=\mathbb E_p\prod_{i\in I}Y_i
\ge
1-2\sum_{i\in I}d_{\lambda_i}
\ge
1-2k\tau,
\tag{18}
\]

and in particular

\[
\boxed{|x_{\mu_I}|\ge1-2t\tau>\epsilon_y.}
\tag{19}
\]

But `mu_I` belongs to the uniformly cheap subspace `W`, so `(3)` says that the only possible nonzero cheap character with bias larger than `epsilon_y` is the single Page-exceptional shell functional `lambda_*`. Thus every short quotient relation must satisfy

\[
\boxed{\mu_I=\lambda_*.}
\tag{20}
\]

If the Page-exceptional functional does not belong to `W`, there are no such short quotient relations at all.

## 2. Global independence leaves at most one Page-exceptional relation

The subset-sum map

\[
I\longmapsto\sum_{i\in I}\lambda_i
\tag{21}
\]

is injective because the `lambda_i` are linearly independent over `F_2`. Hence two distinct subsets cannot both have sum `lambda_*`.

Together with `(20)`, this proves that there is at most one nonempty quotient dependency of cardinality at most `t`.

If no such dependency exists, keep all `R` quotient vectors. If one exists, choose any index contained in its unique support and delete that one `lambda_i`. No short quotient dependency can remain: a surviving dependency would either produce a nonexceptional element of `W`, contradicting `(19)` and `(3)`, or would be a second subset summing to `lambda_*`, contradicting injectivity of `(21)`.

Thus after deleting at most one element we obtain `n>=R-1` quotient vectors

\[
v_1,\ldots,v_n\in H^*/W
\tag{22}
\]

with no nonempty subset of at most `t` vectors summing to zero.

This is stronger than the individual conclusion of `MC-293`. Even if every original `lambda_i` has high source cost, the family cannot collapse modulo `W` to many short combinations of a few expensive directions.

## 3. The quotient vectors are a parity-check matrix with distance greater than `t`

Let

\[
c:=\dim\langle v_1,\ldots,v_n\rangle
\le r-d.
\tag{23}
\]

Place the `v_i` as columns of a `c x n` binary matrix `A`, after choosing a basis of their span. Consider the binary linear code

\[
C=\{a\in\mathbf F_2^n:Aa=0\}.
\tag{24}
\]

A nonzero codeword of weight `k` is exactly a `k`-element subset of columns summing to zero. Section 2 therefore gives

\[
d_{\min}(C)\ge t+1.
\tag{25}
\]

The code has dimension `n-c`. Hamming balls of radius `m=floor(t/2)` around distinct codewords are disjoint, so the standard sphere-packing count yields

\[
2^{n-c}\sum_{j=0}^{m}\binom nj
\le2^n.
\tag{26}
\]

Therefore

\[
2^c\ge\sum_{j=0}^{m}\binom nj
\ge\sum_{j=0}^{m}\binom{R-1}{j}.
\tag{27}
\]

Since `c<=r-d`, equation `(10)` follows. If `R-1>=m>=1`, the elementary bound

\[
\binom{R-1}{m}
\ge
\left(\frac{R-1}{m}\right)^m
\tag{28}
\]

gives `(11)`.

For the natural choice `t` of order `1/tau` allowed by `(7)`, `(11)` has the scale

\[
r-d
\gtrsim
\tau^{-1}\log\!\bigl(R\tau\bigr)
\tag{29}
\]

when `R tau` is sufficiently large. Constants are deliberately not optimized.

## 4. Concrete cheap subspaces exist inside the Page-universal coordinate window

The definition `(4)` is not merely formal. If `U` is a set of lower odd-prime coordinates and

\[
\prod_{p\in U}p\le D_y,
\tag{30}
\]

then every character in the coordinate span `W_U` has a representative supported on a subset of `U`, hence source cost at most the full product in `(30)`.

Moreover `MC-284` proves full Boolean-cube realization for coordinate bundles satisfying the smaller joint-conductor condition

\[
4\prod_{p\in U}p
\le
\exp\!\bigl(b\sqrt{\log y}\bigr).
\tag{31}
\]

Full cube realization makes those coordinate functionals linearly independent on the shell, so in that range

\[
\dim W_U=|U|.
\tag{32}
\]

Since the conductor in `(31)` is eventually far below `D_y`, these Page-universal coordinate bundles provide explicit nontrivial choices of `W` to which `(10)` applies. Thus the quotient tax separates two resources cleanly: a certified cheap coordinate subspace, and the additional high-source-complexity dimension required to host a large independent near-negative family.

## 5. Prior art and novelty boundary

The analytic input `(3)` is exactly the classical Landau–Page/prime-number-theorem mechanism already audited and specialized in `MC-293`; no new exceptional-zero theorem is asserted here. The full-cube corollary `(31)` is `MC-284`.

The passage from short column dependencies to minimum distance and then to `(26)` is the classical binary Hamming sphere-packing mechanism already source-audited in `MC-251` against R. W. Hamming, *Error Detecting and Error Correcting Codes*, Bell System Technical Journal **29** (1950), 147–160, DOI `10.1002/j.1538-7305.1950.tb00463.x`.

A targeted literature search on 14 September 2026 also checked the neighboring large-spectrum language. Chang-type large-spectrum theorems and later work such as Kaave Hosseini and Shachar Lovett, *On the structure of the spectrum of small sets*, Journal of Combinatorial Theory, Series A **144** (2016), 176–198, DOI `10.1016/j.jcta.2016.11.009`, constrain dissociated subsets or additive structure of large Fourier spectra. They are conceptually adjacent, but the present statement uses the much stronger one-sided fact that every selected mode is almost constantly `-1`, together with an arithmetic subspace on which Page theory leaves at most one large Fourier coefficient. The resulting relative quotient-girth statement is derived directly above; no novelty claim is made for it as an abstract additive-combinatorial theorem.

The durable Mathia delta is the **source-complexity interpretation**: the Page-cheap sector cannot absorb short relations among many independent near-negative shell modes, so generic coding bounds charge those modes to quotient dimension beyond that sector.

## Boundaries and falsification tests

- **Uniform cheapness is essential.** It is not enough that a basis of `W` consists of individually cheap characters; products of their representatives may exceed `D_y`. The theorem assumes `Q(w)<=D_y` for every nonzero `w in W`. Condition `(30)` is a sufficient construction.
- **Independence is load-bearing.** Without independence of the `lambda_i`, a subset may sum to zero in `H^*`; even-cardinality exact relations are compatible with all characters taking their preferred sign and are not excluded by `(18)`.
- **The defect threshold is quantitative.** The quotient-girth conclusion requires `(7)`. Once `2t tau` reaches one, the union estimate no longer forces a large Fourier coefficient and the argument stops.
- **One Page exception costs one deletion.** The theorem does not pretend to balance the exceptional functional. It uses uniqueness only. If a short relation lands on that mode, deleting one member of its unique support removes the sole permitted short quotient dependency.
- **The Hamming step is generic.** Equation `(10)` may be far from optimal for the arithmetic quotient. It is a necessary dimension tax, not a proof that the high-cost quotient is too small to exist.
- **Source cost and quotient dimension remain distinct currencies.** A single enormous coordinate can make an individual character expensive without creating many quotient dimensions. The point of `(10)` is precisely that a large family of independent near-negative modes cannot all hide behind that one expensive direction through cheap corrections.
- **No RH-scale import.** The only analytic balance used is the near-`1` Dirichlet-character Page estimate from `MC-293`. No zero-free information for `1/zeta(s)` in the critical strip and no RH-equivalent Mertens bound enters.

## Consequence for the research line

The fourth escape recorded after `MC-293` — that the required near-negative directions may all live beyond the low-source-cost range — is now narrower. High individual source cost is not enough. After quotienting by any certified Page-cheap subspace, all but at most one selected near-negative direction must occupy a binary configuration whose short-dependency radius is at least `t`; sphere packing forces the high-cost quotient to have the redundancy in `(10)`.

The next arithmetic target is therefore more specific: either bound the dimension of the high-source-cost quotient available to the shell, or prove additional arithmetic restrictions on the quotient code beyond the generic Hamming bound. Merely extending another individual conductor estimate will not address this collective escape.