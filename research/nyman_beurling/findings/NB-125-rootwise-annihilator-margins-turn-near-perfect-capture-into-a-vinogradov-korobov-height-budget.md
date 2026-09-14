# NB-125 — rootwise annihilator margins turn near-perfect capture into a Vinogradov–Korobov height budget

**Status:** `EXACT-DERIVED + ROOTWISE-ANNIHILATOR-MARGIN + AGGREGATE-HORIZONTAL-DEPTH + VINOGRADOV-KOROBOV-ZERO-FREE-INPUT + ADDITIVE-HEIGHT-ENTROPY + GROWING-PACKET-TRADEOFF + NB-124-STRENGTHENING + ROUTE-NARROWING`.

`NB-124` gives a stable target-angle gap for every fixed finite packet of actual right-half zeta zeros. Its source-only lower bound compresses the packet to the single number

\[
\beta_F=\max_{\rho\in F}\Re\rho,
\]

so in the growing-packet regime one extremely rightward zero is allowed to set the radial margin for every root. The exact annihilator contains more information than that minimum-gap reduction: its missing-root value is a **product over the individual zeros**. Keeping that product, and keeping the natural coefficient weight in the annihilator norm, gives a rootwise margin law.

Let `F` be a finite multiset of actual nontrivial zeta zeros

\[
\rho=\beta+i\gamma,
\qquad
\frac12<\beta<1,
\qquad
|\gamma|\ge3,
\]

with multiplicity retained, and put

\[
d=d(F).
\]

Fix an integer `q>=2`, set

\[
r=q^{-1},
\qquad
D_q:=\frac{\log q}{2\sqrt q},
\]

and use the annihilator from `NB-124`,

\[
A_{F,q}(z)
=
\prod_{\rho\in F}\left(z-q^{-\bar\rho}\right)
=
\sum_{j=0}^{d}a_jz^j.
\]

Then the normalized missing-root margin satisfies the **rootwise** bound

\[
\boxed{
\mathfrak s_{F,q}
\ge
(1-r)
\prod_{\rho\in F}
\left(
\frac{q^{-\beta}-r}{q^{-\beta}+\sqrt r}
\right)^2
\ge
(1-r)D_q^{2d}
\prod_{\rho\in F}(1-\beta)^2.
}
\tag{1}
\]

Consequently, whenever `R>=q^(d+1)` and the finite packet target angle from `NB-124` satisfies

\[
\chi_{F,R}\ge1-\varepsilon,
\qquad 0<\varepsilon<1,
\]

one necessarily has the aggregate horizontal-depth bill

\[
\boxed{
\sum_{\rho\in F}
\log\frac1{1-\beta}
\ge
\frac12
\log\frac{(1-r)(1-\varepsilon)}{L_R\varepsilon}
-d\log D_q^{-1},
\qquad
L_R=1-\frac1R.
}
\tag{2}
\]

Thus polynomially near-perfect capture cannot be purchased merely by letting the rightmost zero drift toward `Re s=1`; the **product** of all rootwise horizontal depths must become small enough.

Now insert the published explicit Vinogradov–Korobov zero-free region. Bellotti proves that for `|t|>=3`, zeta has no zero in

\[
\sigma
\ge
1-rac1{K_{\rm VK}
(\log|t|)^{2/3}(\log\log|t|)^{1/3}},
\qquad
K_{\rm VK}=53.989.
\]

Hence every zero in `F` obeys

\[
1-\beta
\ge
\frac1{K_{\rm VK}
(\log|\gamma|)^{2/3}(\log\log|\gamma|)^{1/3}}.
\tag{3}
\]

Combining `(2)` and `(3)` gives the main height-entropy inequality

\[
\boxed{
\frac12
\log\frac{(1-r)(1-\varepsilon)}{L_R\varepsilon}
\le
 d\log\frac{K_{\rm VK}}{D_q}
+
\frac23\sum_{\rho\in F}\log\log|\gamma|
+
\frac13\sum_{\rho\in F}\log\log\log|\gamma|.
}
\tag{4}
\]

For `epsilon=R^{-alpha}` with fixed `alpha>0` and fixed `q`, this becomes

\[
\boxed{
\frac\alpha2\log R
\le
 d\log\frac{K_{\rm VK}}{D_q}
+
\frac23\sum_{\rho\in F}\log\log|\gamma|
+
\frac13\sum_{\rho\in F}\log\log\log|\gamma|
+O_q(1).
}
\tag{5}
\]

Equation `(5)` converts the remaining horizontal escape in `NB-124` into an **additive rank–height budget**. If all ordinates satisfy `|gamma|<=H`, then either the recurrence is not visible because `d>log_q R-1`, or

\[
\boxed{
 d
\ge
\frac{
\frac12\log\frac{(1-r)(1-R^{-\alpha})}{L_RR^{-\alpha}}
}{
\log(K_{\rm VK}/D_q)
+\frac23\log\log H
+\frac13\log\log\log H
}.
}
\tag{6}
\]

In particular, for every fixed `C>0`,

\[
\boxed{
H\le R^C,
\quad
\chi_{F,R}\ge1-R^{-\alpha}
\quad\Longrightarrow\quad
 d(F)
\ge
\left(\frac{3\alpha}{4}+o(1)\right)
\frac{\log R}{\log\log R}.
}
\tag{7}
\]

At fixed rank the same inequality forces a much more extreme height escape. If `d(F)=d` is fixed along a family with polynomially near-perfect capture, then

\[
\boxed{
H
\ge
\exp\!\left(
R^{\frac{3\alpha}{4d}-o(1)}
\right).
}
\tag{8}
\]

So the two freedoms left by `NB-124` are not independent for actual zeta zeros. Growing rank can pay for near-perfect target capture, and large height can pay for horizontal approach toward `Re s=1`, but a low-rank packet cannot use ordinary polynomial-height zeros to make the annihilator margin disappear polynomially fast.

## 1. Keep the coefficient weight before estimating the annihilator

Write

\[
\lambda_\rho=q^{-\bar\rho},
\qquad
|\lambda_\rho|=q^{-\beta}.
\]

The margin of `NB-124` is

\[
\mathfrak s_{F,q}
=
\frac{(1-r)|A_{F,q}(r)|^2}
{\sum_{j=0}^{d}|a_j|^2r^j}.
\tag{9}
\]

Instead of discarding the weights `r^j`, consider

\[
A_{F,q}(\sqrt r\,z)
=
\sum_{j=0}^{d}a_jr^{j/2}z^j
=
\prod_{\rho\in F}(\sqrt r\,z-\lambda_\rho).
\]

The weighted coefficient norm therefore satisfies

\[
\begin{aligned}
\left(
\sum_{j=0}^{d}|a_j|^2r^j
\right)^{1/2}
&\le
\sum_{j=0}^{d}|a_j|r^{j/2}\\
&\le
\prod_{\rho\in F}
(\sqrt r+|\lambda_\rho|).
\end{aligned}
\tag{10}
\]

On the other hand,

\[
|A_{F,q}(r)|
=
\prod_{\rho\in F}|r-\lambda_\rho|
\ge
\prod_{\rho\in F}(|\lambda_\rho|-r),
\tag{11}
\]

because every right-half nontrivial zero has `beta<1`, hence `|lambda_rho|>r`. Equations `(9)`--`(11)` give the first inequality in `(1)`.

Since `beta>1/2`,

\[
|\lambda_\rho|=q^{-\beta}\le q^{-1/2}=\sqrt r,
\]

while

\[
q^{-\beta}-r
=r\left(q^{1-\beta}-1\right)
\ge
r(1-\beta)\log q.
\tag{12}
\]

Thus

\[
\frac{q^{-\beta}-r}{q^{-\beta}+\sqrt r}
\ge
\frac{\sqrt r\log q}{2}(1-\beta)
=D_q(1-\beta),
\tag{13}
\]

which proves all of `(1)`.

The improvement over the coarse `beta_F` bound is structural, not just a better constant. Replacing every factor by the smallest radial gap allows one extremely rightward zero to be charged `d` times. Equation `(1)` charges each root only for its own horizontal depth.

## 2. Near-perfect target angle forces aggregate horizontal depth

`NB-124` proves, whenever `R>=q^(d+1)`,

\[
\chi_{F,R}
\le
\left(1+\frac{\mathfrak s_{F,q}}{L_R}\right)^{-1}.
\tag{14}
\]

If `chi_(F,R)>=1-epsilon`, then `(14)` implies

\[
\mathfrak s_{F,q}
\le
\frac{L_R\varepsilon}{1-\varepsilon}.
\tag{15}
\]

Combining `(15)` with the second bound in `(1)` yields

\[
\prod_{\rho\in F}(1-\beta)
\le
D_q^{-d}
\left(
\frac{L_R\varepsilon}
{(1-r)(1-\varepsilon)}
\right)^{1/2}.
\tag{16}
\]

Taking logarithms gives `(2)`. In the polynomial accuracy regime `epsilon=R^{-alpha}`,

\[
\sum_{\rho\in F}\log\frac1{1-\beta}
\ge
\frac\alpha2\log R
-d\log D_q^{-1}
+O_q(1).
\tag{17}
\]

This is the source-faithful strengthening missing from the maximum-root reduction. It does not say that every zero must approach the 1-line. It says that the packet must collectively provide enough logarithmic horizontal depth. One exceptionally shallow root can still pay a large part of the bill, but it pays only once.

## 3. Vinogradov–Korobov converts horizontal depth into height entropy

Bellotti's explicit theorem gives `(3)`. Therefore

\[
\log\frac1{1-\beta}
\le
\log K_{\rm VK}
+\frac23\log\log|\gamma|
+\frac13\log\log\log|\gamma|.
\tag{18}
\]

All logarithms are well-defined for `|gamma|>=3`; the last term may be negative at the bottom of the range and causes no problem. Summing `(18)` over the multiset `F` and comparing with `(2)` proves `(4)`.

The representation is worth keeping explicit. Define the packet height entropy

\[
\mathcal H_{\rm VK}(F)
:=
\frac23\sum_{\rho\in F}\log\log|\gamma|
+
\frac13\sum_{\rho\in F}\log\log\log|\gamma|.
\tag{19}
\]

Then `(4)` says

\[
\mathcal H_{\rm VK}(F)
+d\log\frac{K_{\rm VK}}{D_q}
\ge
\frac12
\log\frac{(1-r)(1-\varepsilon)}{L_R\varepsilon}.
\tag{20}
\]

Rank and height enter additively in this coordinate. This is exactly the tradeoff hidden by a bound written only in terms of `beta_F`.

## 4. Polynomial-height and fixed-rank consequences

Suppose first that every zero in `F` has `|gamma|<=H`. The right side of `(18)` is increasing with `|gamma|` for `|gamma|>=3`, so `(4)` gives `(6)` whenever `R>=q^(d+1)`.

If `H<=R^C` for fixed `C`, then

\[
\frac23\log\log H
+\frac13\log\log\log H
=
\frac23\log\log R
+o(\log\log R)
\]

as an upper envelope. Hence `(6)` yields

\[
d
\ge
\left(\frac{3\alpha}{4}+o(1)\right)
\frac{\log R}{\log\log R}.
\]

If instead `R<q^(d+1)`, then

\[
d>\log_qR-1,
\]

which is stronger. This proves `(7)` without an unmentioned recurrence-visibility hypothesis.

Now fix `d`. For large `R` the condition `R>=q^(d+1)` is automatic. Let `H` be the largest ordinate magnitude in the packet. Equation `(5)` gives

\[
\frac{2d}{3}\log\log H
+
\frac d3\log\log\log H
\ge
\frac\alpha2\log R-O_{q,d}(1).
\tag{21}
\]

Therefore

\[
\log\log H
\ge
\frac{3\alpha}{4d}\log R
-O_{q,d}(\log\log R),
\tag{22}
\]

which is equivalent to `(8)`.

The scale in `(8)` is deliberately stated only to first exponent order. No claim is made that the Bellotti constant, the coefficient-norm estimate, or the `o(1)` term is optimized.

## 5. Relation to the high-zero compression law

`NB-116` and `NB-125` control different currencies. `NB-116` uses Selberg density to show that a packet supported **above** height `G` has continuum Burnol target mass `O(1/G)` and that any fixed finite-section target access must flow through cell-compression modes with retention `O(1/G+1/R)`. The new result instead says that a packet with a very large **finite target angle** cannot make the source-faithful annihilator margin tiny unless it accumulates enough rank-weighted height entropy.

There is no contradiction yet. A packet may include moderate-height zeros together with a few extremely high zeros, and `(4)` does not turn maximum height into minimum height. Nor does it provide a lower bound on the cell-compression eigenvalues singled out by `NB-116`. The useful reduction is narrower: **horizontal approach to the 1-line is no longer a free escape variable**. For actual zeta zeros it must be paid for by height, root by root.

The next source-facing target should therefore connect one of the two remaining currencies:

- convert the additive height entropy `(19)` into a lower bound for the target-bearing compression retention from `NB-116`; or
- prove that an endpoint-relevant packet cannot distribute the required entropy across arbitrarily high ordinates without exceeding its continuum norm/target-mass budget.

A theorem of either type would finally couple the recurrence separator `NB-123`--`NB-125` to the inverse-section obstruction `NB-115`--`NB-116` instead of improving either side in isolation.

## 6. Adversarial checks and method boundary

Several possible overclaims were tested explicitly.

First, multiplicity causes no exception. Repeated zeros are repeated roots of `A_(F,q)`, so every copy appears once in `(10)`, `(11)`, `(16)` and the height entropy. The rank `d(F)` is still total confluent multiplicity.

Second, phases can only help the lower bound used here. Equation `(11)` throws away all angular separation and keeps only the radial distance from the missing root. A phase arrangement with `gamma log q` near a multiple of `2pi` can approach the reverse-triangle lower bound, so no uniform phase improvement is available without a genuine ordinate-spacing input.

Third, the weighted coefficient estimate is essential. The denominator in `(9)` is not replaced by an unweighted coefficient norm: `(10)` first rescales the polynomial by `sqrt(r)` and then applies the elementary coefficient `l1` bound. This preserves the exact norm appearing in `NB-124`.

Fourth, `(7)` is not circular. The Vinogradov–Korobov region is an unconditional theorem about actual zeta zeros. It is used only to convert the independently derived horizontal-depth requirement `(2)` into a height bill; no RH-strength zero location is assumed.

Finally, the result concerns near-perfect packet target angle, not arbitrary fixed positive capture. If `epsilon` is a fixed constant, the right side of `(2)` has no growing `log R` term and the theorem gives no asymptotic rank-height obstruction. The fixed-fraction finite-access problem isolated in `NB-115`--`NB-116` remains open.

## 7. Prior-art and novelty boundary

The Vinogradov–Korobov zero-free region is classical. The quantitative input used here is Chiara Bellotti, *Explicit bounds for the Riemann zeta function and a new zero-free region*, J. Math. Anal. Appl. 536 (2024), 128249, DOI `10.1016/j.jmaa.2024.128249`, Theorem 1.2, which gives the constant `53.989` for every `|t|>=3`. No novelty is claimed for that theorem.

Jongho Yang, *Geometric sequences and zero-free region of the zeta function*, C. R. Math. 356 (2018), 133--137, DOI `10.1016/j.crma.2017.11.021`, is a nearby Nyman--Beurling prior-art boundary: it uses approximation along geometric structures to derive zero-free information. The direction here is different. The zero-free region is input, while the derived object is the finite **actual-zero packet** target angle from `NB-124`, with a rootwise annihilator product and an additive height budget.

A targeted search for Nyman--Beurling results combining a finite zero-packet annihilator, polynomial target-angle accuracy, and a Vinogradov--Korobov rootwise height product did not identify an equivalent statement. The line-local contribution is `(1)`--`(8)`: preserving the individual roots in the annihilator margin and converting their aggregate horizontal-depth bill into an explicit rank--height entropy constraint.

This remains a route-narrowing theorem, not an RH implication. The live escape is now quantitative: growing packets may still accumulate the required entropy through enough rank, sufficiently large ordinates, or both. What has disappeared is the looser interpretation that horizontal drift toward `Re s=1` can be treated independently of the actual zeta height law.