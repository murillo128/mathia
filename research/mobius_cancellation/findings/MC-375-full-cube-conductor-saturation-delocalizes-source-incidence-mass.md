# MC-375 — Full-cube conductor saturation delocalizes source-incidence mass

**Status:** `LITERATURE+DERIVED` · `EXACT-DERIVED` · `FRONTIER-ADVANCE` · `DECISIVE-NEGATIVE` · `CONDUCTOR-SATURATION` · `SOURCE-DELOCALIZATION` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the exact reciprocal endpoint and common source-package setup of `MC-323`, `MC-327`, `MC-371`, and `MC-374`. Let

\[
L=\langle\lambda_1,\ldots,\lambda_R\rangle\cong\mathbf F_2^R,
\qquad R\to\infty,
\]

and choose fixed lower-prime product representatives `V_1,...,V_R` for the generators. Put

\[
U=\bigcup_{i=1}^R V_i,
\qquad
P=\prod_{p\in U}p.
\tag{1}
\]

For each source prime `p\in U`, define its nonzero incidence column

\[
c_p=(1_{p\in V_1},\ldots,1_{p\in V_R})\in\mathbf F_2^R\setminus\{0\}.
\tag{2}
\]

Group source primes by equal incidence column and write

\[
W_c:=\sum_{\substack{p\in U\\ c_p=c}}\log p,
\qquad
\pi_c:=\frac{W_c}{\log P},
\qquad
\sum_{c\ne0}\pi_c=1.
\tag{3}
\]

For every mode `I\in\mathbf F_2^R`, let

\[
V_I=\mathop{\triangle}_{i:I_i=1}V_i,
\qquad
m_I=\prod_{p\in V_I}p,
\tag{4}
\]

and let `\mathcal Q(\lambda_I)` denote the minimum primitive lower-prime source conductor of the same endpoint mode when `I\ne0`.

Assume the quartic-saturated common-source regime

\[
\boxed{\frac{\log P}{\log y}=4+o(1)}
\tag{5}
\]

and the mild growth condition `R=y^{o(1)}`. Then the fixed-gap frame theorem of `MC-374` applies for every fixed `\delta>0` and gives only `O_\delta(R)` nonzero modes with

\[
\mathcal Q(\lambda_I)\le y^{2-\delta}.
\tag{6}
\]

Because there are `2^R` modes, `(6)` combines with an exact full-cube averaging identity to force **quadratic conductor saturation on almost the entire Fourier cube**, not only on the middle Hamming layer treated in `MC-374`:

\[
\boxed{
\frac1{2^R}\#\left\{I:
\left|\frac{\log m_I}{\log y}-2\right|>\varepsilon
\right\}\longrightarrow0
}
\tag{7}
\]

for every fixed `\varepsilon>0`, and

\[
\boxed{
\frac1{2^R}\#\left\{I\ne0:
\left|\frac{\log\mathcal Q(\lambda_I)}{\log y}-2\right|>\varepsilon
\right\}\longrightarrow0.
}
\tag{8}
\]

The full-cube statement has a new source-side consequence. The package log-conductor has the exact Walsh expansion

\[
\log m_I
=
\frac12\log P
-
\frac12\sum_{c\ne0}W_c(-1)^{\langle I,c\rangle}.
\tag{9}
\]

Hence uniform averaging over `I\in\mathbf F_2^R` gives

\[
\boxed{
2^{-R}\sum_I\log m_I=\frac12\log P
}
\tag{10}
\]

and Walsh orthogonality gives the exact variance identity

\[
\boxed{
2^{-R}\sum_I
\left(\log m_I-\frac12\log P\right)^2
=
\frac14\sum_{c\ne0}W_c^2.
}
\tag{11}
\]

By `(5)` and `(7)`, the normalized variable `\log m_I/\log y` converges in probability to `2` and is uniformly bounded by `4+o(1)`. Therefore its variance tends to zero. Substituting into `(11)` yields

\[
\boxed{
\sum_{c\ne0}\pi_c^2\longrightarrow0.
}
\tag{12}
\]

In particular,

\[
\boxed{
\max_{c\ne0}\pi_c\longrightarrow0,
\qquad
\frac1{\sum_c\pi_c^2}\longrightarrow\infty.
}
\tag{13}
\]

Thus a quartic-efficient endpoint cannot hide a macroscopic fraction of its source logarithmic mass in one incidence signature, or in any bounded collection of signatures. Its source mass must spread over an increasing number of distinct incidence columns.

This is independent of the half-loading statement of `MC-327`. That finding proves that quartic saturation forces almost all source log mass into columns with Hamming weight `R/2+o(R)`, but explicitly leaves open which of the exponentially many such columns occur. Combining `MC-327` with `(12)` now gives the joint rigidity:

\[
\boxed{
\text{source log mass is asymptotically central in Hamming weight
and delocalized across central incidence signatures.}
}
\tag{14}
\]

More explicitly, for every fixed `\epsilon>0`,

\[
\sum_{\substack{c:\,||c|/R-1/2|\ge\epsilon}}\pi_c\to0
\tag{15}
\]

by `MC-327`, while `(12)` implies that the collision mass of the remaining central signatures also tends to zero.

There is also a pair-difference consequence. If `I,J` are independent uniform modes, then `I+J` is uniform on `\mathbf F_2^R`. Hence `(7)`--`(8)` imply

\[
\frac{\log m_{I+J}}{\log y}\to2,
\qquad
\frac{\log\mathcal Q(\lambda_{I+J})}{\log y}\to2
\tag{16}
\]

in probability (the zero difference has probability `2^{-R}`). So a typical coherent pair difference also lives at the quadratic source boundary.

This closes another cheap-source escape but does **not** cross the quadratic analytic barrier. In particular, `(16)` cannot simply be inserted into Schlage-Puchta's Halász--Montgomery proof in place of its pairwise lcm conductor: that proof extends the shell characters through globally defined representatives, and a separately minimized primitive representative for `\lambda_I+\lambda_J` need not be the product of separately minimized representatives for `\lambda_I` and `\lambda_J`. A new coherent pair-sensitive prime-family estimate would still be required. No estimate for `M(x)` follows.

## 1. Every nonzero source column is balanced on the full mode cube

For `I\in\mathbf F_2^R`, a source prime `p` occurs in the symmetric-difference package `V_I` exactly when

\[
\langle I,c_p\rangle=1\pmod2.
\tag{17}
\]

Since `c_p\ne0`, the linear functional `I\mapsto\langle I,c_p\rangle` takes each value on exactly `2^{R-1}` modes. Therefore each source prime contributes its logarithmic weight to exactly half of the `m_I`. Summing first over modes and then over primes proves `(10)` directly.

Equivalently,

\[
1_{\langle I,c\rangle=1}
=\frac{1-(-1)^{\langle I,c\rangle}}2,
\]

and grouping equal columns gives `(9)`.

Under `(5)`, equation `(10)` becomes

\[
2^{-R}\sum_I\frac{\log m_I}{\log y}=2+o(1).
\tag{18}
\]

This exact mean is available on the full cube without the central-Hamming conditioning or the defect-balance calculation needed in `MC-372`--`MC-374`.

## 2. The prime-frame theorem removes the full-cube lower tail

Fix `\varepsilon>0` and choose a fixed `\delta\in(0,\varepsilon)`. Let

\[
\mathcal E_\delta
=
\{I\ne0:\mathcal Q(\lambda_I)\le y^{2-\delta}\}.
\tag{19}
\]

`MC-374` applies its coefficient-uniform Schlage-Puchta frame bound to **any** family of distinct endpoint modes. Under `R=y^{o(1)}`, its absorption condition

\[
R y^{-c_\delta}\log y=o(1)
\]

holds for every fixed `\delta`, so

\[
|\mathcal E_\delta|=O_\delta(R).
\tag{20}
\]

Since `R\to\infty`,

\[
\frac{|\mathcal E_\delta|}{2^R}\to0.
\tag{21}
\]

For every `I\ne0`, the minimum primitive conductor is bounded by the fixed package representative,

\[
\mathcal Q(\lambda_I)\le m_I.
\tag{22}
\]

Therefore

\[
\left\{I:\frac{\log m_I}{\log y}<2-\varepsilon\right\}
\subseteq
\mathcal E_\delta\cup\{0\}
\tag{23}
\]

for large `y`. The lower tail of the package exponent consequently has zero density.

To control the upper tail, put

\[
X_I:=\frac{\log m_I}{\log y}.
\]

Equation `(18)` says `E X_I=2+o(1)`, while outside `o(2^R)` exceptions `(23)` gives `X_I\ge2-\delta`. If `u_R(\varepsilon)` is the fraction with `X_I\ge2+\varepsilon`, nonnegativity on the exceptional set gives

\[
2+o(1)
\ge
(1-o(1)-u_R)(2-\delta)
+u_R(2+\varepsilon).
\tag{24}
\]

Hence

\[
\limsup u_R(\varepsilon)
\le\frac{\delta}{\varepsilon+\delta}.
\tag{25}
\]

The fixed `\delta` was arbitrary, so letting it tend to zero proves `(7)`.

For the minimum conductor, its lower tail is again contained in `\mathcal E_\delta`, while its upper tail is contained in the package upper tail by `(22)`. This proves `(8)`.

The argument is deliberately fixed-gap. The moving-order manuscript input from `MC-373` can quantify how close the exceptional family approaches exponent two, but no moving parameter is needed for the qualitative concentration and delocalization conclusions here.

## 3. Full-cube conductor concentration is exactly column-class delocalization

Starting from `(9)`, uniform Walsh orthogonality gives

\[
2^{-R}\sum_I
(-1)^{\langle I,c\rangle}
(-1)^{\langle I,d\rangle}
=1_{c=d}.
\tag{26}
\]

All nonzero Walsh characters also have mean zero. Squaring `(9)`, averaging, and using `(26)` proves `(11)`.

By `(5)`, every `X_I` lies in `[0,4+o(1)]`. Equation `(7)` therefore upgrades convergence in probability to convergence in `L^2`:

\[
2^{-R}\sum_I(X_I-2)^2\to0.
\tag{27}
\]

The difference between the exact mean `(\log P)/(2\log y)` and `2` is `o(1)`, so `(27)` is equivalent to

\[
\operatorname{Var}(X_I)\to0.
\tag{28}
\]

Dividing `(11)` by `(\log y)^2` and using `\log P=(4+o(1))\log y` gives `(12)`.

The first conclusion in `(13)` follows from

\[
\max_c\pi_c^2\le\sum_c\pi_c^2.
\]

The second follows by Cauchy--Schwarz: if `N_R` incidence classes carry positive log mass, then

\[
1=\left(\sum_c\pi_c\right)^2
\le N_R\sum_c\pi_c^2.
\tag{29}
\]

Thus `N_R\to\infty`; more invariantly, the inverse collision mass `1/\sum\pi_c^2` diverges.

This is stronger than merely requiring many source primes. Arbitrarily many primes can share one identical incidence column and behave as one Walsh direction. Equation `(12)` instead controls the **aggregate logarithmic mass of each distinct incidence signature**.

## 4. Relation to the half-loading theorem and pairwise analytic frontier

`MC-327` defines the source-imbalance energy

\[
\mathcal B_R
=
\sum_c\pi_c\left(\frac{2|c|-R}{R}\right)^2
\tag{30}
\]

and proves `\mathcal B_R\to0` under the same quartic saturation assumption. Hence for every fixed `\epsilon>0`, the total `\pi`-mass outside the central Hamming band tends to zero, giving `(15)`.

Equation `(12)` supplies an orthogonal kind of rigidity. A measure may have `\mathcal B_R=0` while being concentrated entirely on one exactly half-loaded column. The new collision conclusion forbids precisely that possibility. Conversely, collision delocalization alone would allow mass on many very sparse or very dense columns. The two results together say that an economical arithmetic source package must use **many distinct, near-half-loaded incidence signatures**.

For pair differences, addition on `\mathbf F_2^R` preserves uniform measure. Therefore if `I,J` are independent uniform modes, `I+J` is uniform and `(16)` follows immediately from `(7)`--`(8)`.

This sharpens the interpretation of the quadratic boundary exposed by `MC-323` and `MC-374`: it is not confined to specially selected generators or the middle layer. Under quartic saturation it is the typical scale of the whole endpoint Fourier group and of a typical pair difference.

It still does not provide a new Halász--Montgomery inequality at that boundary. Schlage-Puchta's classical varying-modulus proof controls off-diagonal character products after choosing global Dirichlet-character representatives and pays for their pairwise lcm. The endpoint minimum-conductor map `\mathcal Q` is defined by minimizing each shell-equivalent mode separately. The identity

\[
\mathcal Q(\lambda_I+\lambda_J)
\ll
[\mathcal Q(\lambda_I),\mathcal Q(\lambda_J)]
\]

in a form strong enough to replace the analytic lcm bill is neither proved nor automatic. The common package does have exact coherent multiplication through `m_{I+J}`, but exploiting its typical quadratic cost requires retaining this pair-dependent structure instead of taking the worst conductor before the frame estimate.

## 5. Prior art and novelty boundary

The analytic input is not new. The low-conductor family bound is exactly the frame consequence of Jan-Christoph Schlage-Puchta, *Primes in short arithmetic progressions*, Acta Arithmetica **106** (2003), 143--149, arXiv `1105.1623`, already audited in `MC-323` and `MC-374`. No strengthening of the prime Halász--Montgomery or Burgess estimates is claimed.

The full-cube moment calculation is classical coding/Fourier structure. F. J. MacWilliams, *A theorem on the distribution of weights in a systematic code*, Bell System Technical Journal **42** (1963), 79--94, DOI `10.1002/j.1538-7305.1963.tb04003.x`, introduced the linear-code weight-distribution identities; standard Pless power moments express the first and second codeword-weight moments through dual low-weight structure. For a binary generator matrix, repeated equal columns are exactly the elementary source of the second-moment excess. The weighted formula `(11)` is the direct real-weight/Walsh analogue for the present source columns and is derived here from `(26)` rather than claimed as a new coding theorem.

A fresh mechanism-level search on 18 September 2026 found the standard MacWilliams/Pless moment theory and modern work on weight distributions and repeated-coordinate constructions, but no source was needed for the line-specific composition `(5)`--`(12)`: the new durable content is that the previously proved **prime-character conductor floor plus quartic source saturation** forces the weighted source-incidence collision mass to vanish. No general coding-theory novelty is claimed.

## Boundaries and falsification tests

- **Quartic saturation is load-bearing.** The conclusion `(12)` is an equality-regime result. If `\log P/\log y` stays above `4` by a fixed amount, the exact full-cube mean is above exponent two and the argument no longer forces small conductor variance.
- **The common source package is load-bearing.** Equations `(9)`--`(11)` require one fixed incidence column for every source prime across all generators. A mode-by-mode unrelated choice of minimizing representatives has no such Walsh expansion.
- **The result is logarithmically weighted.** It controls `W_c=\sum\log p` per incidence class, not the raw number of primes in that class. Many extremely small primes may remain combinatorially numerous while carrying negligible source log mass.
- **`R=y^{o(1)}` is used only to make the fixed-gap frame bound uniform.** A weaker explicit condition `R y^{-c_\delta}\log y=o(1)` for every fixed gap needed in the proof would suffice.
- **No classification of central signatures is obtained.** Equations `(12)` and `(15)` force mass to spread among many near-central columns but do not say which arithmetic incidence vectors occur or whether they satisfy further residue constraints.
- **Typical quadratic pair-difference cost is not yet an analytic cancellation theorem.** Turning `(16)` into a stronger prime-family bound requires a coherent pair-sensitive estimate that does not pay the worst pairwise lcm before using the group structure.
- **No Möbius or RH consequence is asserted.** The reciprocal endpoint remains a conditional candidate structure; this finding only removes concentration of source provenance as an escape from the quartic/quadratic conductor frontier.

The decisive internal checks are exact. Equation `(10)` fails if a nonzero source incidence column is not seen by exactly half of the full mode cube; equation `(11)` fails if distinct Walsh columns are not orthogonal; `(7)` fails if the `MC-374` low-conductor family bound cannot be applied to arbitrary endpoint modes; and `(12)` fails if package-conductor concentration does not follow from the exact mean and quartic bound. Each dependency has therefore been kept explicit rather than hidden in a probabilistic analogy.