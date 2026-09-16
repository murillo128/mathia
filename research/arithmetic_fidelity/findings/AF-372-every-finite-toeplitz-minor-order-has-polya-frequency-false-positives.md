# AF-372 — Every finite Toeplitz-minor order has Pólya-frequency false positives

**Status:** `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `TARGET-FIDELITY`, `TOTAL-POSITIVITY`, `LAGUERRE-POLYA`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-REDIRECT`, `NO-NOVELTY-CLAIM`

## Claim

The exact total-positivity lift in AF-371 cannot be replaced, on the unrestricted translation-kernel class, by checking all minors only up to any fixed finite order.

For every integer `r >= 2`, there exists a nonzero integrable function `Lambda_r >= 0` such that its Toeplitz kernel

\[
K_r(x,y)=\Lambda_r(x-y)
\tag{1}
\]

is totally nonnegative of order `r` but is not totally nonnegative of order `r+1`. Hence `Lambda_r` passes **every** translation-minor test of size at most `r` while failing to be a Pólya-frequency function.

An explicit witness comes from the classical Karlin kernel

\[
\Omega(x)=x e^{-x}\mathbf 1_{x>0}.
\tag{2}
\]

Set

\[
\alpha_r=r-\frac32,
\qquad
\Lambda_r(x)=\Omega(x)^{\alpha_r}.
\tag{3}
\]

Karlin's critical-exponent theorem gives `Lambda_r in TN_r` because

\[
\alpha_r>r-2.
\tag{4}
\]

Khare's converse gives `Lambda_r notin TN_{r+1}` because `alpha_r` is nonintegral and

\[
0<\alpha_r< (r+1)-2=r-1.
\tag{5}
\]

Therefore the hierarchy

\[
TN_2 \supsetneq TN_3 \supsetneq TN_4 \supsetneq \cdots \supsetneq TN_\infty
\tag{6}
\]

has an explicit strict witness at every finite stage within this one-parameter family.

In Arithmetic Fidelity language, the bounded-order certificate

\[
C_r(\Lambda)=\mathbf 1_{\{\Lambda\in TN_r\}}
\tag{7}
\]

is never target-faithful for

\[
D(\Lambda)=\mathbf 1_{\{\Lambda\in TN_\infty\}}.
\tag{8}
\]

This closes the finite-order version of the minimality question left open by AF-371: **no fixed maximum Toeplitz-minor order can certify the Pólya-frequency/Laguerre–Pólya target on the full admissible class.**

## Classical derivation

Karlin proved that for every integer `p >= 2`, the power `Omega^alpha` is `TN_p` whenever

\[
\alpha\in \mathbb Z_{\ge0}\cup[p-2,\infty).
\tag{9}
\]

Khare proved the converse in the remaining nonintegral critical range: for

\[
\alpha\in(0,p-2)\setminus\mathbb Z,
\tag{10}
\]

`Omega^alpha` is not `TN_p`.

Now fix `r >= 2` and choose `alpha_r` as in `(3)`. Equation `(4)` puts the witness on Karlin's allowed side for order `r`, while `(5)` puts the same witness inside Khare's forbidden interval for order `r+1`. Thus

\[
\Omega^{r-3/2}\in TN_r\setminus TN_{r+1}.
\tag{11}
\]

No limiting or numerical argument is involved. The witness is integrable because `alpha_r>0` and, on `(0,\infty)`,

\[
\Lambda_r(x)=x^{\alpha_r}e^{-\alpha_r x}.
\tag{12}
\]

Since a Pólya-frequency function is `TN_p` for every finite `p`, failure at order `r+1` proves that `Lambda_r` is not Pólya-frequency. By Schoenberg's transform theorem, the reciprocal bilateral-Laplace-transform denominator associated with a Pólya-frequency function lies in the Laguerre–Pólya class; therefore finite-order total positivity cannot by itself certify that real-zero target either.

The construction is stronger than exhibiting one low-order false positive. It gives a **moving matched control**: however high a fixed cutoff `r` is chosen, there is a kernel that agrees with the desired positivity signature on the entire order-`<=r` test family and fails immediately at the next order.

## Fidelity interpretation

AF-371 showed that all-order translation total positivity is an exact relational lift for the Laguerre–Pólya target, whereas an infinite Hankel-positivity hierarchy is not. The remaining question was whether a materially smaller portion of the translation-minor family might already be sufficient.

AF-372 settles one natural reduction sharply. Let `T_r` retain the truth values of **all** Toeplitz-minor inequalities of orders at most `r`. Then the pair consisting of any Pólya-frequency kernel and the explicit `Lambda_r` above lies in the same positive verdict fiber of `T_r`, while their all-order target discriminator differs. Equivalently,

\[
D\not\!\!\factor T_r
\qquad\text{for every finite }r.
\tag{13}
\]

Consequently, testing more locations at a fixed determinant order does not repair the loss: `Lambda_r` satisfies the required sign at every allowed choice of locations. Any finite collection of Toeplitz-minor nonnegativity tests also fails generically as a certificate, because its largest minor size is bounded by some `r` and `Lambda_r` passes every test up to that order.

This identifies the retained resource more precisely than "more positivity." The exact classical certificate needs **unbounded relational arity**: determinant constraints of arbitrarily large order. The obstruction is therefore an arity ceiling, not a shortage of sampled locations within a fixed order.

## Riemann specialization

AF-371 records the Schoenberg/Gröchenig equivalence between the Riemann hypothesis and Pólya-frequency total positivity for the reciprocal transform associated with the Riemann `Xi` function. AF-372 implies that replacing that all-order condition by

\[
\text{all translation minors of size at most }r\text{ are nonnegative}
\tag{14}
\]

cannot be an exact **general** Laguerre–Pólya certificate for any fixed `r`.

This is not a counterexample to an `Xi`-specific theorem. The witnesses `Lambda_r` are generic translation kernels, not kernels proved to arise from `Xi` or from rational-prime arithmetic. Additional source-specific identities could, in principle, make a low-order condition sufficient on a much smaller arithmetic subclass. Any such claim must therefore identify and use that extra structure explicitly; finite-order total positivity alone does not supply the missing fidelity.

Nor does the result make finite-order tests useless. They remain necessary conditions and may provide falsifiers, quantitative diagnostics, or finite approximations. What fails is their promotion to a source-independent exact certificate of the all-order target.

## Prior-art and novelty audit

- Samuel Karlin, **“Total Positivity, Absorption Probabilities and Applications,”** *Transactions of the American Mathematical Society* **111**(1) (1964), 33–107, DOI `10.1090/S0002-9947-1964-0168010-2`. Role: proves the finite-order critical-exponent inclusion for powers of `Omega(x)=x e^{-x} 1_{x>0}`.
- I. J. Schoenberg, **“On Pólya Frequency Functions. I. The Totally Positive Functions and Their Laplace Transforms,”** *Journal d'Analyse Mathématique* **1** (1951), 331–374, DOI `10.1007/BF02790092`. Role: classical Pólya-frequency / reciprocal Laguerre–Pólya transform characterization and the all-order target used here.
- Apoorva Khare, **“Multiply Positive Functions, Critical Exponent Phenomena, and the Jain–Karlin–Schoenberg Kernel,”** arXiv:`2008.05121` (2020; revised 2021). Role: proves the converse critical-exponent obstruction `Omega^alpha notin TN_p` for nonintegral `alpha in (0,p-2)`, making the strict finite-order witnesses exact.
- Alexander Belton, Dominique Guillot, Apoorva Khare and Mihai Putinar, **“Preservers of Totally Positive Kernels and Pólya Frequency Functions,”** *Mathematics Research Reports* **3** (2022), 35–56, DOI `10.5802/mrr.12`. Role: modern survey confirming the Karlin kernel, finite-order `TN_p` language, and the separation between integer all-order powers and noninteger finite-order powers.

No novelty is claimed for Karlin's kernel, its critical exponent, Khare's converse, the strictness of the classical finite-order hierarchy, or Schoenberg's transform theory. The Arithmetic Fidelity contribution is the target-fidelity reading after AF-371: the critical-exponent family is an explicit matched-control theorem showing that **every bounded relational arity leaves false-positive fibers** for the exact Pólya-frequency/Laguerre–Pólya certificate.

## Decisive audit rule

When total positivity is proposed as the structure that survives a compression, distinguish all-order positivity from any fixed-order truncation. Passing every determinant inequality up to an arbitrarily large but fixed size does not certify the all-order target on the unrestricted class.

A proposed smaller certificate must therefore do something genuinely different from imposing a fixed arity ceiling. Viable residual questions include special structured infinite subfamilies of minors, an order cutoff that grows under a controlled limit, or extra source-specific relations that collapse the generic Karlin–Khare false-positive family. AF-372 does not rule out those possibilities.