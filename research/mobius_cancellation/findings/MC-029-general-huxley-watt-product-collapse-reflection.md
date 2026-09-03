# MC-029 — Arbitrary Huxley–Watt cutoffs collapse to a Möbius step coefficient

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `DECISIVE-NEGATIVE`, `NO-NOVELTY-CLAIM`.

## Claim

The product-collapsed obstruction of `MC-028` is not special to equal cutoffs or degree two. For the full Huxley–Watt finite identity with arbitrary independent cutoffs, the **signed sum of all inclusion–exclusion correction degrees**, after every factor and auxiliary coordinate is grouped by the total product, is an exact scalar multiple of the Möbius function on every admissible coefficient.

Fix `d>=2` and positive integer cutoffs `N_1,...,N_d`. For a subset `S` of `{1,...,d}` with `|S|=s>=2`, define the total-product coefficient

\[
D_S(q)
:=
\sum_{\substack{n_i\le N_i\ (i\in S),\\
k_1,\ldots,k_{s-1}\ge1,\\
(\prod_{i\in S}n_i)(\prod_{j=1}^{s-1}k_j)=q}}
\prod_{i\in S}\mu(n_i),
\tag{1}
\]

and combine the correction degrees with the signs appearing in the Huxley–Watt identity:

\[
C_{\mathbf N}(q)
:=
\sum_{\substack{S\subseteq\{1,\ldots,d\}\\|S|\ge2}}
(-1)^{|S|}D_S(q).
\tag{2}
\]

Let

\[
r_{\mathbf N}(q):=\#\{i:q\le N_i\}.
\tag{3}
\]

Then for every integer

\[
1\le q<\prod_{i=1}^d(1+N_i),
\]

the exact coefficient identity is

\[
\boxed{
C_{\mathbf N}(q)=\bigl(r_{\mathbf N}(q)-1\bigr)\mu(q).
}
\tag{4}
\]

In particular, throughout the entire admissible upper block

\[
\max_iN_i<q<\prod_i(1+N_i),
\]

one has

\[
\boxed{C_{\mathbf N}(q)=-\mu(q).}
\tag{5}
\]

Thus **neither unequal cutoffs nor cross-degree inclusion–exclusion recombination creates a weaker signed carrier once the Huxley–Watt factor coordinates are collapsed to the total product**. The upper new block is exactly the target Möbius block with opposite sign, independently of the degree and independently of the anisotropy of the cutoffs.

This closes two product-collapsed escapes left open by `MC-028`. Unequal ranges may still matter before product grouping, and cross-degree cancellation may still matter before the individual multilinear coordinates are forgotten. What is ruled out is obtaining a new power gain by first performing the complete Huxley–Watt recombination and then estimating only its scalar coefficient as a function of `q`.

## 1. Coefficient extraction from the general Huxley–Watt identity

Huxley and Watt prove, for a totally multiplicative `g` and

\[
K<\prod_{i=1}^d(1+N_i),
\tag{6}
\]

a finite identity of the form

\[
M(g,K)
=
\sum_{i=1}^d M\bigl(g,\min\{N_i,K\}\bigr)
-
\sum_{\substack{S\subseteq\{1,\ldots,d\}\\|S|\ge2}}
(-1)^{|S|}T_S(g,K),
\tag{7}
\]

where `T_S` is the finite sum over the Möbius variables indexed by `S` together with `|S|-1` unrestricted auxiliary factors, subject to total product at most `K`.

Take the admissible specialization `g=1`. For `q>=2` satisfying (6), subtract (7) at `K=q-1` from (7) at `K=q`. The left-hand side contributes exactly `mu(q)`. The first term contributes `mu(q)` once for each cutoff with `N_i>=q`, hence

\[
r_{\mathbf N}(q)\mu(q).
\tag{8}
\]

For each subset `S`, the increment of `T_S(1,K)` is exactly the coefficient `D_S(q)` in (1). Therefore

\[
\mu(q)
=
r_{\mathbf N}(q)\mu(q)-C_{\mathbf N}(q),
\tag{9}
\]

which proves (4) for `q>=2`.

At `q=1`, every factor in (1) must equal one, so `D_S(1)=1`. Hence

\[
C_{\mathbf N}(1)
=
\sum_{s=2}^d(-1)^s\binom ds
=d-1
=\bigl(r_{\mathbf N}(1)-1\bigr)\mu(1),
\tag{10}
\]

and (4) holds on the whole admissible range.

The proof uses no analytic continuation, zeta-zero information, asymptotic estimate, probabilistic model, or conjectural cancellation. It is exact finite coefficient bookkeeping inside the source identity.

## 2. Unequal degree-two cutoffs only insert a zero band

Let `d=2` and order the cutoffs as `A<=B`. Equation (4) becomes

\[
\boxed{
C_{A,B}(q)=
\begin{cases}
\mu(q),&q\le A,\\
0,&A<q\le B,\\
-\mu(q),&B<q<(A+1)(B+1).
\end{cases}}
\tag{11}
\]

For `A=B=N`, this is exactly the square-annulus reflection found in `MC-028`. Unequal ranges do not weaken the upper coefficient; they merely create a middle interval where one cutoff still contributes the first-order Möbius term and the correction coefficient vanishes.

This matters for the active Huxley–Watt route because anisotropic cutoffs were a natural remaining candidate after the equal-range audit. Equation (11) shows that **anisotropy alone does not help after total-product collapse**. Any advantage of choosing `A` and `B` differently must be an estimate that still sees which factor lies in which cutoff range.

## 3. Higher degree and full cross-degree recombination have the same upper reflection

Sort the cutoffs as

\[
N_{(1)}\le\cdots\le N_{(d)}.
\]

Between successive cutoff levels the count `r_N(q)` is constant. If exactly `r` cutoffs still exceed `q`, equation (4) gives

\[
C_{\mathbf N}(q)=(r-1)\mu(q).
\tag{12}
\]

For equal cutoffs `N_i=N`, this reduces to only two levels:

\[
C_{N,\ldots,N}(q)
=
\begin{cases}
(d-1)\mu(q),&q\le N,\\
-\mu(q),&N<q<(N+1)^d.
\end{cases}
\tag{13}
\]

The degree disappears completely from the coefficient on the upper new block. All pair, triple, and higher inclusion–exclusion pieces may look individually complicated, but their source-prescribed signed recombination reconstructs `-mu(q)` after product grouping.

This strengthens the boundary in `MC-026`. There, collapsing one fixed unrestricted degree to the convolution power `mu_d` was shown to retain the same zeta zero boundary. Here, keeping the **finite cutoffs and all Huxley–Watt degrees**, but collapsing the full signed finite identity to `q`, is even more rigid: the upper coefficient is the original Möbius function itself rather than merely a convolution power.

## 4. What the result does and does not kill

The result kills the following generic strategy:

1. retain arbitrary Huxley–Watt cutoffs and/or several inclusion–exclusion degrees;
2. combine them with the exact source signs;
3. group all terms by their total product `q`;
4. seek an independently cheaper norm or summatory bound for the resulting coefficient on the new range.

Equation (5) shows that the resulting new-range coefficient is already `-mu(q)`. Any bound at a new power exponent is therefore the desired Möbius cancellation bound with a sign change.

The result does **not** kill genuinely pre-collapse information. In particular, it leaves open:

- anisotropic estimates that retain the individual factor coordinates and their separate cutoff faces;
- cancellation between inclusion–exclusion degrees proved before grouping by total product;
- multilinear estimates sensitive to which coordinate carries a large or small factor;
- unsplit analytic relations in which the terms cancel before separate absolute values are taken;
- scale couplings whose decisive observable cannot be expressed as a scalar function of `q` alone.

The distinction is now exact: unequal cutoffs and cross-degree coupling are only viable if their gain is extracted **before** the quotient that forgets factor provenance.

## 5. Prior art and novelty boundary

The source identity is classical prior art from M. N. Huxley and N. Watt, *Mertens Sums requiring Fewer Values of the Möbius function*, Chebyshevskii Sbornik 19(3) (2018), 20–34, DOI `10.22405/2226-8383-2018-19-3-20-34`, arXiv `1807.05890`. Their Theorem 1 gives the arbitrary independent-cutoff identity under condition (6). They explicitly observe that differencing their finite identity at consecutive terminal cutoffs gives a formula for `mu(K)` independent of `g`, and they place the equal-range special cases in the Meissel/Linnik/Vaughan/Heath-Brown lineage.

Accordingly, no novelty is claimed for recovering Möbius by differencing, for the general finite identity, or for the coefficient formula as an isolated arithmetic identity. The durable Mathia contribution is the **mechanism audit** obtained by applying that classical coefficient extraction to the exact residual questions left by `MC-025`–`MC-028`: after full source-prescribed recombination, arbitrary cutoff anisotropy and cross-degree structure are erased by total-product collapse and the upper coefficient is exactly `-mu`.

A targeted prior-art check around the Huxley–Watt source and its cited decomposition lineage found the original coefficient-recovery observation itself, so the result is intentionally classified as `CLASSICAL-IDENTITY` and `NO-NOVELTY-CLAIM` rather than as new number theory.

## 6. Consequence for the active frontier

`MC-025` ruled out higher degree as a generic product-norm power amplifier. `MC-026` ruled out unrestricted convolution powers as a cheaper product-collapsed signed observable. `MC-028` then showed exact Möbius reflection for the simplest equal-cutoff quadratic boundary. Equation (4) closes the remaining **product-collapsed** versions of unequal ranges and cross-degree recombination in one statement.

The Huxley–Watt route is therefore pushed one layer earlier. A future candidate must point to a specific factor-coordinate or pre-recombination statistic and prove why its cancellation is both source-natural and genuinely weaker than the target `M(x)` estimate. If its decisive estimate can be rewritten after exact recombination as a bound for `C_N(q)` or its upper-block partial sums, equation (5) shows that the Möbius target has merely been renamed.