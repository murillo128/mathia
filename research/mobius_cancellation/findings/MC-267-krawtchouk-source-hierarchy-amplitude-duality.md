# MC-267 — The source-support hierarchy is exactly the Krawtchouk transform of the shell-amplitude histogram

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the shell notation of `MC-264`–`MC-266`. For each shell subset

\[
T\in\binom{\mathcal R_y}{t},
\]

write

\[
\sigma_p(T)=\prod_{r\in T}\left(\frac pr\right)\in\{-1,+1\},
\qquad
B_y(T)=\sum_{p\in\mathcal P_y}\sigma_p(T),
\]

and let

\[
b_y(T)=\#\{p\in\mathcal P_y:\sigma_p(T)=-1\}.
\]

Then exactly

\[
B_y(T)=k_y-2b_y(T).
\tag{1}
\]

Let the binary Krawtchouk polynomial in the combinatorial normalization be

\[
K_s(b;k)
=
\sum_{j=0}^s(-1)^j\binom bj\binom{k-b}{s-j},
\tag{2}
\]

so that

\[
(1-z)^b(1+z)^{k-b}
=
\sum_{s=0}^k K_s(b;k)z^s.
\tag{3}
\]

Recall the source-support aggregate from `MC-266`,

\[
H_{s,y}(t)
=
\sum_{\substack{q:\omega(q)=s\\p\mid q\Rightarrow p\in\mathcal P_y}}
K_t(d_y(q);N_y),
\tag{4}
\]

where

\[
d_y(q)=\#\left\{r\in\mathcal R_y:\left(\frac qr\right)=-1\right\}.
\]

The first exact identification is

\[
\boxed{
H_{s,y}(t)
=
\sum_{|T|=t}
K_s\!\left(b_y(T);k_y\right).
}
\tag{5}
\]

Thus the radial source hierarchy is not an independent family of shell observables. It is the Krawtchouk transform of the empirical Hamming-weight distribution of the original lower-prime sign vectors.

More explicitly, define the shell-amplitude histogram

\[
A_{y,t}(b)
=
\#\{T\in\tbinom{\mathcal R_y}{t}:b_y(T)=b\}.
\tag{6}
\]

Then

\[
\boxed{
H_{s,y}(t)
=
\sum_{b=0}^{k_y}A_{y,t}(b)K_s(b;k_y).
}
\tag{7}
\]

The full vectors `A_{y,t}` and `H_{\bullet,y}(t)` are exactly interconvertible. Binary Krawtchouk orthogonality gives

\[
\boxed{
A_{y,t}(b)
=
\frac{\binom{k_y}{b}}{2^{k_y}}
\sum_{s=0}^{k_y}
\frac{H_{s,y}(t)}{\binom{k_y}{s}}
K_s(b;k_y).
}
\tag{8}
\]

At the finite moment depth relevant to `MC-264`, the equivalence is even sharper. Let

\[
M_{j,y}(t)=\sum_{|T|=t}B_y(T)^j.
\tag{9}
\]

For fixed `k`, `K_s((k-B)/2;k)` is a polynomial in `B` of degree `s`, parity `s`, and leading coefficient `1/s!`. Hence the triangular maps

\[
\{H_{0,y},H_{2,y},\ldots,H_{2m,y}\}
\longleftrightarrow
\{M_{0,y},M_{2,y},\ldots,M_{2m,y}\}
\tag{10}
\]

are invertible. In particular, the even source-support hierarchy through level `2m` contains exactly the same scalar-distribution information as the first `m+1` even moments of the original shell amplitude `B_y(T)`.

The `MC-266` source-walk coefficients make this equivalence explicit at the top moment. If `C_{2m,k}(s)` denotes the number of length-`2m` words on `k` coordinates having any fixed parity-support set of size `s`, then for every integer `0\le b\le k`,

\[
\boxed{
(k-2b)^{2m}
=
\sum_{\substack{0\le s\le2m\\s\ \mathrm{even}}}
C_{2m,k}(s)K_s(b;k).
}
\tag{11}
\]

Consequently, summing `(11)` against `A_{y,t}(b)` gives exactly the radial decomposition of `MC-266`,

\[
\boxed{
S_{2m,y}(t)
=
\sum_{\substack{0\le s\le2m\\s\ \mathrm{even}}}
C_{2m,k_y}(s)H_{s,y}(t).
}
\tag{12}
\]

Equation `(12)` is therefore not merely analogous to a moment decomposition: it is the unique Krawtchouk-basis expansion of the original `2m`-th shell-amplitude moment.

This has a concrete negative consequence for the frontier left by `MC-266`. **Pure Krawtchouk/association-scheme recurrence among source-support layers cannot by itself provide the missing high-moment estimate.** Without an additional arithmetic theorem constraining the actual Legendre-sign image `T\mapsto(\sigma_p(T))_p`, such recurrence is only a change of basis among the same amplitude moments.

The surviving route through `H_{s,y}(t)` is still genuine, but only if one proves new arithmetic cancellation in those transforms that is not a consequence of universal Krawtchouk identities. The missing information must come from the distribution of the Legendre sign vectors themselves, not from the radialization algebra.

No blind relation is excluded here, no estimate of the `MC-264` candidate moment is proved, and no bound for `M(X)` follows.

## 1. Exact duality by swapping the two fixed-weight sums

For a square-free lower-prime source

\[
q=\prod_{p\in S}p,
\qquad |S|=s,
\]

we have, for every shell subset `T`,

\[
\prod_{r\in T}\left(\frac qr\right)
=
\prod_{p\in S}\sigma_p(T).
\tag{13}
\]

The fixed-weight identity used already in `MC-264` says

\[
K_t(d_y(q);N_y)
=
\sum_{|T|=t}
\prod_{r\in T}\left(\frac qr\right).
\tag{14}
\]

Summing `(14)` over all source supports `S\subset\mathcal P_y` of size `s` and interchanging the finite sums gives

\[
H_{s,y}(t)
=
\sum_{|T|=t}
\sum_{|S|=s}
\prod_{p\in S}\sigma_p(T).
\tag{15}
\]

For a `\{\pm1\}` vector with exactly `b` negative coordinates, its degree-`s` elementary symmetric sum is exactly `K_s(b;k)`, by `(3)`. This proves `(5)` and `(7)`.

The standard dual orthogonality identity

\[
\sum_{s=0}^{k}
\frac{K_s(b;k)K_s(c;k)}{\binom ks}
=
\frac{2^k}{\binom kb}\,\mathbf 1_{b=c}
\tag{16}
\]

then gives `(8)`. So the complete source-support profile and the complete shell-amplitude histogram are simply two bases for the same finite data.

A blind shell subset has `B_y(T)=k_y`, hence `b_y(T)=0`. In the full transform its count is therefore reconstructible exactly from `(8)` as

\[
A_{y,t}(0)
=
2^{-k_y}\sum_{s=0}^{k_y}H_{s,y}(t),
\tag{17}
\]

because `K_s(0;k_y)=\binom{k_y}{s}`. This identity is exact but not useful by itself at the live scale: controlling the entire support spectrum up to `s=k_y` is far stronger than the logarithmic-support information currently available.

## 2. Finite-depth source layers are just ordinary amplitude moments in another basis

Put `B=k-2b`. Differentiating `(3)` or using its standard three-term recurrence gives

\[
\boxed{
B K_s(b;k)
=(s+1)K_{s+1}(b;k)
+(k-s+1)K_{s-1}(b;k).
}
\tag{18}
\]

Starting from `K_0=1` and `K_1=B`, `(18)` shows inductively that

\[
K_s\!\left(\frac{k-B}{2};k\right)
=
\frac{B^s}{s!}
+P_{s-2}(B),
\tag{19}
\]

where `P_{s-2}` has degree at most `s-2` and the same parity as `s`. Therefore the even polynomials

\[
K_0, K_2,\ldots,K_{2m}
\]

form a triangular basis of the even polynomials in `B` through degree `2m`. Summing against the empirical distribution of shell subsets proves `(10)`.

The first nontrivial example is already revealing:

\[
K_2\!\left(\frac{k-B}{2};k\right)
=
\frac{B^2-k}{2},
\tag{20}
\]

so

\[
H_{2,y}(t)
=
\frac12\left(
M_{2,y}(t)-k_y\binom{N_y}{t}
\right).
\tag{21}
\]

Higher even source layers similarly repackage the higher even moments together with lower-moment correction terms.

This does **not** make estimates for individual `H_s` useless. An arithmetic theorem may be much easier to state or prove in the source-support basis than directly as a moment bound. But the representation itself supplies no extra scalar-distribution information: any gain must enter through a theorem that uses the special Legendre arithmetic of the actual sign vectors.

## 3. The tensor-walk coefficients are exactly the change-of-basis coefficients

For a fixed sign vector `x=(x_1,\ldots,x_k)\in\{\pm1\}^k`, expand

\[
(x_1+\cdots+x_k)^{2m}
\]

as a sum over ordered words `(i_1,\ldots,i_{2m})`. Reduce each word modulo two in every coordinate. If its parity support is `S`, the word contributes

\[
\prod_{i\in S}x_i.
\]

For every fixed support `S` of size `s`, the number of words yielding that parity vector is precisely the radial cube-walk coefficient `C_{2m,k}(s)` of `MC-266`. Grouping first by support size gives

\[
(x_1+\cdots+x_k)^{2m}
=
\sum_{s\ \mathrm{even}}
C_{2m,k}(s)
\sum_{|S|=s}\prod_{i\in S}x_i.
\tag{22}
\]

If `x` has `b` negative coordinates, the inner sum is `K_s(b;k)` and the left side is `(k-2b)^{2m}`. This proves `(11)` without any analytic estimate or probabilistic assumption.

Thus the hypercube walk in `MC-266` does not create an independent averaging mechanism. Its radial transition counts are exactly the connection coefficients expressing a power of the first Krawtchouk coordinate in the Krawtchouk basis.

## 4. Why the naive recurrence escape does not add information

One surviving possibility stated after `MC-266` was to exploit a relation among neighboring source-support layers before taking absolute values. Equation `(18)` identifies the limitation of the purely algebraic version of that idea. Summing it over the shell family gives

\[
(s+1)H_{s+1,y}(t)
+(k_y-s+1)H_{s-1,y}(t)
=
\sum_{|T|=t}
B_y(T)K_s(b_y(T);k_y).
\tag{23}
\]

The right side is not an independent controlled quantity; it is a `B_y`-weighted Krawtchouk moment of the same amplitude histogram. Iterating `(18)` produces `B_y^j`-weighted transforms, and by the same triangular basis relation these remain linear combinations of the same finite family of amplitude moments.

Therefore the classical three-term recurrence, orthogonality, hypercube adjacency algebra, or radial random-walk identities **cannot alone** close the candidate estimate of `MC-264`. They can reorganize where cancellation would have to occur, but they do not force that cancellation for the arithmetic shell family.

A neighboring-layer argument remains viable only if it inserts genuinely additional arithmetic information—for example a signed relation between different Legendre source supports, a distribution theorem for the map `T\mapsto b_y(T)` or for finer non-radial data, or an analytic estimate that couples support layers with cancellation not implied by `(3)`, `(16)`, or `(18)`.

This is narrower than the obstruction in `MC-265`. `MC-265` showed that first-order balance of individual product characters is quantitatively too weak after absolute values. The present result shows that **the obvious radial recurrence machinery itself is information-neutral**: before arithmetic input is added, the entire low-support hierarchy is only the low-order moment sequence of the original shell amplitude in an orthogonal-polynomial basis.

## 5. Prior art and novelty boundary

No novelty is claimed for Krawtchouk polynomials, their generating function, orthogonality, the Hamming association scheme, Walsh-Fourier characters on the Boolean cube, hypercube random-walk spectral decompositions, or the relation between Krawtchouk transforms and weight distributions.

NIST DLMF §18.23.3 records the standard Krawtchouk generating function; at `p=1/2` it is `(1-z)^b(1+z)^(k-b)` up to the conventional binomial normalization. Alex Samorodnitsky, *Weight distribution of random linear codes and Krawtchouk polynomials*, Random Structures & Algorithms 64 (2024), DOI `10.1002/rsa.21214`, explicitly describes a Krawtchouk polynomial as the sum of all Walsh-Fourier characters of fixed weight and uses the Krawtchouk/Boolean-cube connection to study moments of weight distributions. Persi Diaconis, Ronald Graham and John Morrison, *Asymptotic analysis of a random walk on a hypercube with many dimensions*, Random Structures & Algorithms 1 (1990), DOI `10.1002/rsa.3240010105`, is a classical hypercube-random-walk/Fourier reference. The broader coding-theory literature, including Pless power-moment identities and MacWilliams transforms, likewise treats moment/weight-distribution conversion through the Hamming scheme as standard structure.

A targeted literature check through 13 September 2026 therefore supports treating `(5)`–`(23)` as classical finite harmonic-analysis machinery specialized and recombined for the current shell object, not as a new special-function theorem. The durable Mathia contribution here is the **frontier audit**: the source-support route isolated in `MC-266` is exactly dual to the original shell-amplitude distribution, so an algebraic Krawtchouk recurrence is not the missing theorem. Any successful use of that route must import new arithmetic cancellation at the level of the actual Legendre shell image.

## 6. Boundaries and decisive consequence

- **No analytic gain is proved.** The identities reorganize the candidate moment; they do not bound it.
- **No source-layer estimate is ruled out.** A theorem giving strong signed control of `H_{s,y}(t)` from arithmetic structure could still prove the `MC-264` estimate.
- **Only the algebraic recurrence shortcut is closed.** The no-go concerns arguments whose only new input after `MC-266` is universal Krawtchouk orthogonality/recurrence or hypercube radialization.
- **The full transform is stronger than the live truncation.** Equation `(8)` reconstructs the exact amplitude histogram only from all `k_y+1` layers. At `m\asymp t\asymp\log\log y`, the available hierarchy reaches only logarithmic support and therefore does not reconstruct the blind atom directly.
- **Finite depth is moment-equivalent.** Up to support `2m`, the even hierarchy is exactly an invertible reparameterization of the even amplitude moments through order `2m`; it does not contain an additional hidden scalar statistic.
- **Arithmetic/non-radial structure can still matter.** The map from shell subsets to sign vectors is highly constrained by Legendre symbols. Any theorem using those constraints lies outside this representation-level no-go.

## Consequence for the research line

The high-moment threshold of `MC-264` remains the strongest live quantitative exit, and `MC-265` still rules out first-order shell balance as a sufficient proof input. `MC-266` correctly reduces the tensor-pair expansion to a finite source-support hierarchy, but that hierarchy now has an exact interpretation: it is the Krawtchouk moment transform of the original shell-amplitude histogram.

The next useful theorem cannot be obtained merely by pushing Krawtchouk recurrences harder. It must prove a **genuinely arithmetic signed estimate** for one or more source layers, a coupled estimate whose cancellation uses Legendre structure rather than association-scheme identities, or a direct restriction on the shell-amplitude distribution strong enough to control its `2(t+1)`-st moment near the diagonal scale required by `MC-264`.