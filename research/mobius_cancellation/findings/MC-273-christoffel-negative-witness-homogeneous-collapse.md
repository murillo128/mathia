# MC-273 — One negative witness collapses the Christoffel ball to a homogeneous shell

**Status:** `EXACT-DERIVED`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the flat Christoffel source formulation of `MC-268`–`MC-272`. Let

\[
\mathcal P_y=\{p\le y:p\text{ odd prime}\},
\qquad k=k_y=|\mathcal P_y|,
\]

and for a shell target

\[
T\in\binom{\mathcal R_y}{t}
\]

write

\[
\sigma_p(T)=\prod_{r\in T}\left(\frac pr\right)\in\{-1,+1\},
\qquad
b(T)=\#\{p\in\mathcal P_y:\sigma_p(T)=-1\}.
\tag{1}
\]

For `0\le s\le k`, let

\[
E_s(T)
:=
\sum_{\substack{S\subseteq\mathcal P_y\\|S|=s}}
\prod_{p\in S}\sigma_p(T)
=
K_s(b(T);k),
\tag{2}
\]

where `K_s` is the binary Krawtchouk polynomial in the normalization used in `MC-267`. The flat Christoffel numerator isolated in `MC-268` and `MC-269` is

\[
g_m(T)
:=
\sum_{s=0}^mE_s(T)
=
\sum_{\substack{S\subseteq\mathcal P_y\\|S|\le m}}
\prod_{p\in S}\sigma_p(T).
\tag{3}
\]

There is an exact collapse:

\[
\boxed{
\sum_{s=0}^mK_s(b;k)
=
K_m(b-1;k-1).
}
\tag{4}
\]

For every **nonblind** target `T`, so `b(T)>=1`, choose any lower prime `p_0` with `\sigma_{p_0}(T)=-1`. Then `(4)` has the direct character form

\[
\boxed{
g_m(T)
=
\sum_{\substack{S\subseteq\mathcal P_y\setminus\{p_0\}\\|S|=m}}
\prod_{p\in S}\sigma_p(T).
}
\tag{5}
\]

Thus, once a single negative source witness exists, the apparently mixed-degree Hamming-ball sum over all source supports `|S|<=m` is **exactly one homogeneous degree-`m` shell sum on the remaining `k-1` source coordinates**. The identity holds for every choice of negative witness `p_0`.

Consequently every nonblind row satisfies the sharp deterministic amplitude bound

\[
\boxed{
|g_m(T)|\le H_{k,m}:=\binom{k-1}{m},
}
\tag{6}
\]

with equality already when `b(T)=1` because all remaining signs are then `+1`.

A blind row instead has `b(T)=0` and amplitude

\[
Z_{k,m}:=\sum_{s=0}^m\binom ks.
\tag{7}
\]

The blind/nonblind endpoint gap is therefore explicit:

\[
\boxed{
Z_{k,m}-H_{k,m}
=2\sum_{s=0}^{m-1}\binom{k-1}{s}.
}
\tag{8}
\]

When `m=o(k)`,

\[
\frac{H_{k,m}}{Z_{k,m}}
=1-\frac{2m}{k}
+O\!\left(\frac{m^2}{k^2}\right),
\tag{9}
\]

and hence

\[
\boxed{
Z_{k,m}^2-H_{k,m}^2
=
\left(\frac{4m}{k}+O\!\left(\frac{m^2}{k^2}\right)\right)Z_{k,m}^2.
}
\tag{10}
\]

At the live Christoffel scale

\[
m=t+1,
\qquad
t\asymp\frac{1}{\log2}\log\log y,
\tag{11}
\]

`MC-268` and `MC-270` give

\[
\frac{C}{Z_{k,m}}
=(1+o(1))\frac{m}{k},
\qquad
C=\binom{N_y}{t}.
\tag{12}
\]

Combining `(10)` and `(12)` yields the calibrated endpoint separation

\[
\boxed{
Z_{k,m}^2-H_{k,m}^2
=(4+o(1))\,C Z_{k,m}.
}
\tag{13}
\]

So the squared-amplitude gap between one blind row and the largest possible nonblind row is itself only a constant multiple of the **entire diagonal/binomial energy scale** `C Z` targeted in `MC-268`–`MC-270`.

This does not exclude a blind relation and does not prove the desired flat-energy estimate. It does sharpen the current frontier in two ways. First, cross-degree structure in the Christoffel numerator is algebraically redundant on every row for which nonblindness is already witnessed: after deleting one negative coordinate, the same row value is a pure degree-`m` character sum. Second, the endpoint separation that must distinguish blindness is naturally of diagonal-energy size, so an eventual phase-sensitive theorem cannot afford to lose an additional polynomial factor merely to distinguish the endpoint from the nearest nonblind configurations.

## 1. The cumulative Krawtchouk identity is a one-line generating-function collapse

The standard binary Krawtchouk generating function is

\[
\sum_{s=0}^kK_s(b;k)z^s
=(1-z)^b(1+z)^{k-b}.
\tag{14}
\]

Taking the coefficient of `z^m` after division by `1-z` gives

\[
\sum_{s=0}^mK_s(b;k)
=[z^m](1-z)^{b-1}(1+z)^{k-b}.
\tag{15}
\]

The right side is precisely the binary Krawtchouk generating function with parameters `(b-1,k-1)`, proving `(4)`:

\[
[z^m](1-z)^{b-1}(1+z)^{(k-1)-(b-1)}
=K_m(b-1;k-1).
\tag{16}
\]

Identity `(4)` is polynomially meaningful also at `b=0`, where the generating function contains `(1-z)^{-1}`. The arithmetic deletion interpretation below is needed only for `b>=1`.

No novelty is claimed for `(14)` or for coefficient extraction from it. The NIST Digital Library of Mathematical Functions, §18.23, records the standard Krawtchouk generating-function family; see https://dlmf.nist.gov/18.23. The present result uses that classical identity only to simplify the exact Mathia source vector.

## 2. A negative coordinate cancels the cumulative-degree denominator

The character version is more informative for the current arithmetic problem. From `(1)`–`(2)`,

\[
\prod_{p\in\mathcal P_y}(1+\sigma_p(T)z)
=
\sum_{s=0}^kE_s(T)z^s.
\tag{17}
\]

Therefore

\[
g_m(T)
=[z^m]
\frac{\prod_p(1+\sigma_p(T)z)}{1-z}.
\tag{18}
\]

If `T` is nonblind, choose `p_0` with `\sigma_{p_0}(T)=-1`. Its factor in `(17)` is exactly `1-z`, so it cancels the denominator in `(18)`:

\[
\frac{\prod_p(1+\sigma_p(T)z)}{1-z}
=
\prod_{p\ne p_0}(1+\sigma_p(T)z).
\tag{19}
\]

Extracting degree `m` proves `(5)`. This also makes the sharp bound `(6)` immediate: the right side of `(5)` is a sum of exactly `\binom{k-1}{m}` signs.

The identity is independent of which negative coordinate is removed. If `p_0` and `p_1` are both negative, the two degree-`m` shell sums obtained by deleting them are equal because both are the same coefficient `(18)`. This equality is algebraic, not a new arithmetic correlation theorem.

The equality case `b(T)=1` is useful for calibration. Deleting the unique negative coordinate leaves `k-1` positive coordinates, so every term in `(5)` equals `+1` and

\[
g_m(T)=\binom{k-1}{m}.
\tag{20}
\]

Hence `(6)` cannot be strengthened uniformly over all abstract nonblind sign vectors without using arithmetic information that rules out or suppresses these near-endpoint configurations.

## 3. The endpoint gap is exactly at the diagonal-energy scale

Pascal's identity gives

\[
Z_{k,m}
=
\sum_{s=0}^m
\left(\binom{k-1}{s}+\binom{k-1}{s-1}\right)
=
\binom{k-1}{m}
+2\sum_{s=0}^{m-1}\binom{k-1}{s},
\tag{21}
\]

which proves `(8)`.

For `m=o(k)`, the top term dominates the lower partial sum:

\[
\sum_{s=0}^{m-1}\binom{k-1}{s}
=
\binom{k-1}{m-1}
\left(1+O\!\left(\frac{m}{k}\right)\right).
\tag{22}
\]

Since

\[
\frac{\binom{k-1}{m-1}}{\binom{k-1}{m}}
=
\frac{m}{k-m},
\tag{23}
\]

we obtain

\[
\frac{Z_{k,m}-H_{k,m}}{H_{k,m}}
=
\frac{2m}{k}
+O\!\left(\frac{m^2}{k^2}\right),
\tag{24}
\]

which implies `(9)` and `(10)`.

At `m=t+1`, the Christoffel count ratio `(12)` identifies `m/k` with the one-row diagonal-energy ratio `C/Z` to first order. Substitution gives `(13)`.

This calibration complements `MC-270`. There the obstruction was that coefficient-uniform operator control has an unavoidable row-norm floor exactly at the blind-atom threshold. Here the pointwise row geometry says that even the deterministic separation between the blind endpoint and the sharp nonblind amplitude ceiling is only `O(CZ)` in squared energy. The same scale is therefore intrinsic both to the operator-norm obstruction and to endpoint discrimination.

## 4. What the collapse does and does not remove

The identity does **not** say that the mixed-degree Christoffel detector was a mistake. `MC-268` remains the endpoint-optimal positive detector under the binomial comparator, and the cumulative source vector is fixed before one knows whether a target row is blind.

What `(5)` says is narrower: conditional on the existence of one negative lower-prime response, the row evaluation of that cumulative source vector already equals a homogeneous shell evaluation. Therefore a proof strategy that hopes to gain solely from mysterious cancellation between different source degrees must explain why that representation is useful **before** nonblindness is known; the evaluated quantity itself contains no irreducible cross-degree contribution on a nonblind row.

The deletion is adaptive. The witness `p_0` depends on `T`, and for the blind row no such coordinate exists. One cannot therefore replace the global flat-energy problem by one fixed homogeneous large-sieve problem without additional work. In particular, choosing `p_0(T)` row by row and then applying a coefficient-uniform estimate would reintroduce exactly the type of relaxation that `MC-270` showed to be too coarse unless the adaptive partition is exploited arithmetically.

A surviving route may instead use the identity as a row classification: partition nonblind targets by a canonical first negative witness, estimate the corresponding homogeneous degree-`m` sums with the witness condition retained, and compare the aggregate with the blind endpoint. Whether the exact Legendre shell supplies a theorem strong enough for that partition remains open.

## 5. Prior-art and novelty boundary

Binary Krawtchouk polynomials, their generating functions, Hamming-scheme interpretations, and the representation of fixed-weight Walsh sums by Krawtchouk polynomials are classical. A targeted literature check through 13 September 2026 found the standard generating-function and Boolean-cube framework, including DLMF §18.23 and modern coding-theory uses of Krawtchouk weight transforms, but no basis for claiming novelty for `(4)` as a standalone polynomial identity.

The durable Mathia contribution claimed here is only the exact **specialization and frontier consequence** for the already-forced Christoffel source of `MC-268`–`MC-272`: a nonblind row collapses from the Hamming ball `|S|<=m` to one homogeneous shell after deleting a negative witness, and at the live support-matched scale the resulting sharp blind/nonblind squared-amplitude separation is `(4+o(1))CZ`.

No claim is made that this specialization is absent from the broader coding-theory or association-scheme literature.

## Boundaries

- **No blind-row exclusion.** The identity begins with a negative witness for the homogeneous interpretation and therefore cannot assume the conclusion it is meant eventually to help prove.
- **No flat-energy estimate.** The bound `|g_m(T)|<=H_{k,m}` applies only to known nonblind rows; it does not control how many blind rows exist.
- **No uniform large-sieve escape.** Replacing the adaptive row problem by arbitrary coefficients would inherit the `MC-270` operator-norm floor.
- **No new Krawtchouk theorem.** Equations `(4)` and `(14)`–`(16)` are classical generating-function algebra.
- **No probabilistic independence.** All identities are exact for the deterministic Legendre sign vectors; no random-sign model is assumed.
- **No Möbius or RH consequence.** Nothing here improves `M(X)`, the blind-support floor, or any zero-free region.

## Consequence for the research line

The phase-sensitive frontier after `MC-272` can now be narrowed further. The flat Christoffel source has an exact endpoint defect: blindness is precisely the failure of the denominator cancellation in `(18)`. Every nonblind row admits a homogeneous-shell representation `(5)`, while the blind row retains the larger cumulative amplitude `Z`.

The next useful theorem should therefore exploit the **arithmetic cost of having no negative witness** or the adaptive witness partition itself, rather than seek additional leverage from the mixed-degree source representation alone. Quantitatively, it must resolve an endpoint energy gap of only diagonal size `(13)` while retaining enough signed phase to avoid the absolute-value barriers of `MC-265`, `MC-271`, and `MC-272`.