# AF-434 — The full-column saddle does not transport the source-shell index

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `NEGATIVE/OBSTRUCTION` · `SOURCE-PROVENANCE` · `SHELL-DECOMPOSITION` · `SADDLE-INDEX` · `NO-NOVELTY-CLAIM`

## Claim

Continue AF-416--AF-433 with

\[
h(x)=-\log\!\left(\frac{1-e^{-x}}x\right),
\qquad R=2\pi,
\qquad a=\left(\frac cR\right)^2.
\]

The source singularity ladder admits an exact shell-resolved coefficient decomposition. Using the classical product for `sinh`,

\[
\frac{1-e^{-x}}x
=e^{-x/2}\frac{\sinh(x/2)}{x/2},
\qquad
\frac{\sinh(x/2)}{x/2}
=\prod_{j\ge1}\left(1+\frac{x^2}{R^2j^2}\right),
\tag{1}
\]

so for `|x|<R`,

\[
\boxed{
h(x)
=\frac x2-
\sum_{j\ge1}\log\!\left(1+\frac{x^2}{R^2j^2}\right)
=\frac x2+
\sum_{k\ge1}\frac{(-1)^k\zeta(2k)}{kR^{2k}}x^{2k}.
}
\tag{2}
\]

Thus the even coefficient has the exact source-shell resolution

\[
c_{2k}
=\sum_{j\ge1}c_{2k}^{[j]},
\qquad
c_{2k}^{[j]}
=\frac{(-1)^k}{kR^{2k}}j^{-2k}.
\tag{3}
\]

The shell index `j` in `(3)` is not the packet index `r` of the AF-421 full-column saddle. In the current determinant compression, the shell label is summed inside `c_{2k}` before the Cauchy--Binet partition decomposition is organized by shifts of the coefficient-order indices. For fixed packet depth `r`, AF-421 isolates the exact zeta factor

\[
Z_{n,r}
:=
\frac{\prod_{u=1}^{r}\zeta(2(n+u))}
     {\prod_{u=1}^{r}\zeta(2u)}.
\tag{4}
\]

The non-nearest source shells are exponentially suppressed at the large coefficient orders in the numerator. Indeed

\[
0<\zeta(2k)-1
=\sum_{j\ge2}j^{-2k}
\le
4^{-k}\left(1+\frac{2}{2k-1}\right),
\tag{5}
\]

so for every fixed `r`,

\[
\prod_{u=1}^{r}\zeta(2(n+u))
=1+O_r(4^{-n}),
\tag{6}
\]

and hence

\[
Z_{n,r}
=\frac{1+O_r(4^{-n})}
       {\prod_{u=1}^{r}\zeta(2u)},
\qquad
Z_{n,r}^{1/n}\longrightarrow1.
\tag{7}
\]

Therefore the exponential full-column saddle law of AF-421,

\[
C_{n,r}^{1/n}\longrightarrow
L_r(b)=\frac{b^r}{(r!)^2},
\tag{8}
\]

contains no surviving source-shell index. Its adjacent-packet transition is

\[
\frac{L_{r+1}(b)}{L_r(b)}
=\frac{b}{(r+1)^2},
\tag{9}
\]

so the square transition `b=m^2` comes from the packet factorial geometry together with the scalar effective coordinate `b`; it is not obtained by transporting the `m`-th source shell through the determinant.

The distinction remains at the first exact adjacent-packet prefactor. AF-421 gives

\[
F_{n,m}
=
\left(\frac{a}{n^2}\right)^n
\left(\frac{n+m}{m}\right)^{s_n-1}
\frac{\zeta(2(n+m))}{\zeta(2m)}
\left(\frac{2(n+m)-1}{2m-1}\right)^2.
\tag{10}
\]

Here

\[
\frac{\zeta(2(n+m))}{\zeta(2m)}
=\frac{1+O(4^{-n})}{\zeta(2m)}.
\tag{11}
\]

The denominator `\zeta(2m)=\sum_{j\ge1}j^{-2m}` is an aggregate over **all** source shells. Its `m` is a coefficient-order/packet parameter, not the source-shell label `j=m`. In particular, the source-shell contribution `j=m` is only the single summand `m^{-2m}` inside this aggregate and is not selected by `(10)`.

Consequently, within the AF-416--AF-433 determinant/compression mechanism, the exact coordinate coincidence

\[
c=r_m=mR
\quad\Longleftrightarrow\quad
a=m^2
\tag{12}
\]

from AF-433 does **not** constitute shell-index transport. It is exhausted, at the full-column saddle level, by source normalization `a=(c/R)^2` followed by the independently derived packet law `(9)`. Any genuine source-shell-to-packet transfer would require a different or enriched construction that retains the shell label before the coefficient aggregation `(3)`.

## 1. Exact shell decomposition and nearest-shell dominance

Equation `(1)` follows from the classical sine product after the substitution `z=ix/2`. Taking logarithms inside the disk `|x|<R` and expanding `-\log(1+u)` gives

\[
-\log\!\left(1+\frac{x^2}{R^2j^2}\right)
=
\sum_{k\ge1}
\frac{(-1)^k}{k}
\frac{x^{2k}}{R^{2k}j^{2k}}.
\tag{13}
\]

Absolute convergence on compact subsets of `|x|<R` permits interchange of the `j`- and `k`-sums, proving `(2)--(3)`.

For `(5)`, monotonicity of `t^{-2k}` gives

\[
\sum_{j=2}^{\infty}j^{-2k}
\le 2^{-2k}+\int_2^\infty t^{-2k}\,dt
=4^{-k}\left(1+\frac{2}{2k-1}\right).
\tag{14}
\]

Thus large-order source coefficients are exponentially dominated by the nearest shell `j=1`. This is stronger provenance information than merely knowing the convergence radius: the entire farther-shell aggregate is `O(4^{-k})` relative to the nearest-shell contribution.

This dominance does **not** by itself select the reciprocal-order probe `c=R`. It says what controls large coefficient order, not which admissible diagonal `x_n(c)=c/n` the source must choose.

## 2. Where the shell label is lost in the current compression

AF-416 writes each derivative-Hankel determinant as a Cauchy--Binet sum over exponent sets. The coefficient attached to an even exponent `2k` is already the scalar `c_{2k}` from `(3)`. Expanding the zeta factor would recover a sum over source-shell assignments, but the determinant construction retains only their aggregate coefficient unless an additional shell mark is carried explicitly.

By contrast, the AF-421 packet index `r` counts full-height columns in the partition decomposition `\lambda=(r^n)+\mu`. It records how far coefficient-order indices are shifted. It is therefore a combinatorial coordinate in the Cauchy--Binet/Schur organization, not a surviving label from the product factors in `(1)`.

Equation `(7)` makes this separation quantitative in the finite critical windows used to derive `(8)`: the shell-sensitive zeta factor has zero contribution to the `n`-th-root rate. The transition set of the exponential saddle is therefore fixed before any distinction among farther source shells can affect the rate.

## 3. The low-order zeta prefactor does not restore index provenance

It would be too strong to say that all source-shell information disappears from the exact determinant. The fixed denominator in `(7)` and the factor `\zeta(2m)^{-1}` in `(11)` retain aggregate information about the complete shell ladder. Exponentially small numerator corrections also retain farther-shell data.

What fails is the more specific transfer proposed by AF-433's open Gate 1: nothing in the current formula identifies the target packet label `m` with the source shell label `j=m`. The same symbol `m` can be used on both sides only after the external comparison `(12)` is made. Inside the determinant derivation, shell and packet indices enter at different mathematical layers.

This also explains why the coincidence is robust as an identity yet weak as provenance. The source supplies the unit `R`; the packet saddle supplies the integer-square thresholds; normalizing the probe by `R` maps the source radii `mR` to the same scalar squares. No shell-resolved observable is transported through the compression.

## Prior-art and novelty audit

No novelty is claimed for the Weierstrass product for sine/hyperbolic sine, the identity `\zeta(2k)=\sum_{j\ge1}j^{-2k}`, or the general principle that dominant singularities control large Taylor coefficients.

NIST DLMF §4.22 records the classical sine product, from which `(1)` follows by `z=ix/2`. Flajolet and Odlyzko's singularity-analysis framework is standard prior art for translating dominant-singularity structure into coefficient asymptotics. The elementary estimate `(5)` is derived directly and gives the needed quantitative specialization here.

The Mathia-specific result is the provenance audit obtained by combining that shell resolution with the exact AF-421 packet formula: the source shell index is aggregated before the partition packet index is formed, and the zeta/shell factor is subexponential in every fixed full-column saddle. This closes the current shell/packet-transfer branch negatively without claiming a general impossibility for other representations.

Sources:

- NIST Digital Library of Mathematical Functions, §4.22, infinite product for `\sin z`: https://dlmf.nist.gov/4.22
- Philippe Flajolet and Andrew Odlyzko, **“Singularity Analysis of Generating Functions,”** *SIAM Journal on Discrete Mathematics* 3(2), 216--240 (1990), DOI `10.1137/0403019`.

## Boundaries and falsification checks

- The conclusion concerns the AF-416--AF-433 coefficient/determinant route and the fixed-`r` finite critical-window saddle of AF-421. It is not a theorem about every possible compression of `h`.
- Equation `(7)` is for fixed packet depth `r`. No claim is made here for packet indices growing with `n`.
- Aggregate shell information survives in low-order constants such as `\zeta(2m)` and in exponentially small corrections. The result does not erase those terms or assert that they can never matter at a finer scale.
- The result does not rule out a new lift that carries the product-factor/shell label `j` explicitly through the determinant. Such a lift would be a genuinely different provenance-preserving construction and would need its own naturalness and fidelity audit.
- Nearest-shell dominance in `(5)` does not prove that `c=R` is the unique admissible reciprocal-order probe. AF-433's source-selection Gate 0 remains open.
- AF-426's no-cancellation theorem on exact square fibers remains unchanged.
- No rational-prime discriminator, zeta-zero recovery theorem, or implication for RH is established.

## Consequence for the research line

AF-433 left two possible ways to make the source shell ladder substantive: a source-side rule could select an admissible shell, or the same shell index could be transported into the target packet hierarchy. The present result closes the second possibility **for the current determinant mechanism**. The square packet law is formed after shell-resolved coefficient information has been aggregated, and the source-sensitive zeta factors do not contribute to its exponential saddle rate.

The live question is therefore narrower: can the source analytic structure force `c=R` or another probe rule independently of target behavior? Large-order coefficient asymptotics give a principled reason that the nearest shell is distinguished, but turning that distinction into a unique admissible reciprocal-order probe still requires an additional theorem. Further packet-cancellation or exceptional-set analysis should not be pursued for a freely chosen `c` until that source-selection gate is settled.