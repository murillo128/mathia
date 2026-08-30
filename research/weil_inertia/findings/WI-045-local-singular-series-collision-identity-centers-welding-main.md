# WI-045 — exact local singular-series collision identity centers the Yang welding main

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + PRIOR-ART-REDIRECTION + NEEDS-AUDIT`. This finding does **not** certify the Yang--Yang one-sided fourth-moment theorem and does not change Mathia's current unconditional simple-critical proportion. It resolves the local-factor fork left open by WI-044 on the asymptotically dominant coprime `(b1,b2)` family: the deterministic `p`-adic modes that can make an isolated pair-centered covariance large are exactly absorbed by the source's cell singular-series main. More precisely, the `k`-averaged product of the two structured twin-prime local factors in the `S1` swap equals the second local moment `E2(b1,b2)` used in `S3`, prime by prime; the corresponding `S2` local mean is the same quantity. Thus parity is not a special escape hatch: it is the `p=2` instance of a general finite CRT collision identity.

What remains open is the genuinely analytic/global step. The actual Yang band has nonuniform overlap/kernel weights, moving windows, boundary terms, and a shift-only Cauchy consumer. The identity below removes a possible **local singular-series mismatch** from that step; it does not prove that the weighted residual is `o(1)` or that the printed appeal to MRT closes the welding layer. A valid completion must still carry the exact local centering through the weighted `S1-2S2+S3` expression before applying Abel summation, MRT, or any other cancellation theorem.

## 1. Source objects and the fork left by WI-044

The pinned public source remains

`JoshuaHKU/zeta-0.7947-reproduction@d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8`.

Its one-sided fourth-moment band uses

\[
A_{b_2,j}
 =\sum_m \Lambda(m)
   \Lambda\!\left(\frac{b_2m+j}{b_1}\right)
   1_{b_1\mid b_2m+j},
\qquad
MT_{b_2,j}
 =\mathfrak S_{b_1,b_2}(j)\frac{\mathrm{len}}{b_1b_2},
\tag{1}
\]

and the exact dispersion

\[
D=\sum_{b_2,j}(A_{b_2,j}-MT_{b_2,j})^2
  =S_1-2S_2+S_3.
\tag{2}
\]

The public `scripts/t2_swaps.py` expands `S1` by the equal-lock equation. With

\[
g=(b_1,b_2),\qquad r=b_1/g,\qquad q=b_2/g,
\tag{3}
\]

one has exactly

\[
m'=m-rk,\qquad n'=n-qk.
\tag{4}
\]

The same source defines

\[
E_2(b_1,b_2)
=\prod_p \mathbb E_{j\bmod p}\bigl[\kappa_p(j)^2\bigr]
\tag{5}
\]

as the local second moment entering the `S3` main. Its `pipeline/face_dispersion.py` independently builds the model four-point profile from the product of the two twin singular-series factors along the exact CRT progression, plus the exact diagonal pieces.

WI-043 isolated a covariance after centering the two shifted-pair processes separately. WI-044 then showed that such an isolated covariance can be macroscopically large while the **cell-centered** dispersion is exactly zero, and therefore asked whether the full singular-series main cancels the coherent local modes. The calculation below answers that local question affirmatively on the coprime family.

Primary source artifacts:

- `paper.tex`, subsection `Covered zone, middle band, bridge and aggregation` and the later local-closure proposition;
- `scripts/t2_swaps.py`, especially `kap_p`, `e2_const`, the exact `S1/S2/S3` swaps, and the fixed-window bridge;
- `pipeline/face_dispersion.py`, which uses the product twin-singular-series CRT model for the resolved four-point profile.

## 2. The universal twin local factor

For a prime `p`, write the ordinary Hardy--Littlewood two-point local factor as

\[
\tau_p(h)
:=\frac{1-\nu_p(\{0,h\})/p}{(1-1/p)^2}.
\tag{6}
\]

Hence

\[
\tau_p(h)=
\begin{cases}
\dfrac{p}{p-1},&p\mid h,\\[2mm]
\dfrac{p(p-2)}{(p-1)^2},&p\nmid h.
\end{cases}
\tag{7}
\]

This formula includes `p=2`: the two values are respectively `2` and `0`. Its mean over one residue period is exactly one,

\[
\frac1p\sum_{k\bmod p}\tau_p(k)=1.
\tag{8}
\]

For `p\nmid b_1b_2`, the Yang cell factor `\kappa_p(j)` implemented in `m1_suite.py` is exactly (7) with `h=j`.

## 3. Generic primes: the `S1` product has exactly the `S3` second moment

Assume first

\[
p\nmid b_1b_2.
\tag{9}
\]

Multiplication by either coefficient permutes the residue classes modulo `p`, and the divisibility events

\[
p\mid b_1k,\qquad p\mid b_2k
\tag{10}
\]

are therefore the same event `p|k`. Consequently

\[
\frac1p\sum_{k\bmod p}
\tau_p(b_1k)\tau_p(b_2k)
=
\frac1p\sum_{k\bmod p}\tau_p(k)^2.
\tag{11}
\]

Using (7),

\[
\begin{aligned}
\frac1p\sum_k\tau_p(k)^2
&=\frac1p\left(\frac{p}{p-1}\right)^2
 +\frac{p-1}{p}
  \left(\frac{p(p-2)}{(p-1)^2}\right)^2\\[1mm]
&=\frac{p(p^2-3p+3)}{(p-1)^3}
 =1+\frac1{(p-1)^3}.
\end{aligned}
\tag{12}
\]

But the right side is exactly the generic local factor of `E2` in `scripts/t2_swaps.py`:

\[
\mathbb E_{j\bmod p}\kappa_p(j)^2
=1+\frac1{(p-1)^3}.
\tag{13}
\]

Thus

\[
\boxed{
\mathbb E_{k\bmod p}
\bigl[\tau_p(b_1k)\tau_p(b_2k)\bigr]
=
\mathbb E_{j\bmod p}\bigl[\kappa_p(j)^2\bigr]
}
\qquad (p\nmid b_1b_2).
\tag{14}
\]

At `p=2`, when both coefficients are odd, (12)--(14) read simply

\[
\tfrac12(2^2+0^2)=2,
\tag{15}
\]

so the parity mode of WI-044 is already contained in the same identity.

## 4. Coefficient primes: the identity still holds

Now assume `(b1,b2)=1` and, without loss of generality,

\[
p\mid b_1,\qquad p\nmid b_2.
\tag{16}
\]

Since `p|b1 k` for every `k`,

\[
\tau_p(b_1k)=\frac{p}{p-1}.
\tag{17}
\]

Since `b2` is a unit modulo `p`, (8) gives

\[
\mathbb E_{k\bmod p}\tau_p(b_2k)=1.
\tag{18}
\]

Therefore

\[
\mathbb E_k\bigl[\tau_p(b_1k)\tau_p(b_2k)\bigr]
=\frac{p}{p-1}.
\tag{19}
\]

The Yang local table for exactly one coefficient divisible by `p` is

\[
\kappa_p(j)=
\begin{cases}
0,&p\mid j,\\[1mm]
\dfrac{p}{p-1},&p\nmid j,
\end{cases}
\tag{20}
\]

independently of the positive valuation of that coefficient. Hence

\[
\mathbb E_j\kappa_p(j)^2
=\frac{p-1}{p}\left(\frac{p}{p-1}\right)^2
=\frac{p}{p-1},
\tag{21}
\]

which is again exactly (19). The case `p|b2` is symmetric. For `p=2`, (19)--(21) all equal `2`.

Thus every prime satisfies the same matching identity whenever `(b1,b2)=1`.

## 5. Exact finite CRT collision identity

The preceding calculation can be packaged without any limiting interchange. Let `Q` be squarefree and define the finite local products

\[
\tau_Q(h)=\prod_{p\mid Q}\tau_p(h),
\qquad
\kappa_Q(j)=\prod_{p\mid Q}\kappa_p(j),
\tag{22}
\]

and

\[
E_{2,Q}(b_1,b_2)
:=\prod_{p\mid Q}
\left(\frac1p\sum_{j\bmod p}\kappa_p(j)^2\right).
\tag{23}
\]

If `(b1,b2)=1`, the Chinese remainder theorem and (14)/(19) give the **exact finite identity**

\[
\boxed{
\frac1Q\sum_{k\bmod Q}
\tau_Q(b_1k)\tau_Q(b_2k)
=E_{2,Q}(b_1,b_2).
}
\tag{24}
\]

No prime-distribution theorem enters (24). It is a finite collision count over residue classes. It says that the deterministic local main produced by the two structured twin shifts in the `S1` swap has exactly the same Euler data as the second cell main used by `S3`.

The infinite `E2` product in the source is the convergent Euler completion of the factors on the right: at generic primes the factor is `1+O(p^{-3})`, with only finitely many coefficient-prime replacements. Equation (24) is therefore the safe exact statement to carry through the proof audit; any passage from finite local products to the fully weighted band remains a separate analytic step rather than being hidden inside the Euler notation.

## 6. The `S2` main is the same local second moment

The middle term has the same local law for an elementary reason. At a generic prime, choose `m,n` uniformly among units modulo `p` and put

\[
j=b_1n-b_2m.
\tag{25}
\]

For fixed `j`, the number of unit pairs solving (25) is `p-1` when `j=0` and `p-2` when `j\ne0`. Therefore the induced distribution of the lock is

\[
\Pr(j=a)=\frac1p\,\kappa_p(a).
\tag{26}
\]

Because `\mathbb E_a\kappa_p(a)=1`, weighting the cell main once more gives

\[
\mathbb E_{m,n\in(\mathbb Z/p\mathbb Z)^\times}
\kappa_p(b_1n-b_2m)
=
\frac1p\sum_{a\bmod p}\kappa_p(a)^2.
\tag{27}
\]

At a coefficient prime, say `p|b1`, equation (25) forces `j\ne0`; then `\kappa_p(j)=p/(p-1)` identically on the unit pair, again equal to the right side of (21). The same statement holds at `p=2`.

Thus the three deterministic local objects have a common factor:

\[
\boxed{
S_1^{\rm local\ main}
\quad\leftrightarrow\quad
E_2(b_1,b_2)
\quad\leftrightarrow\quad
S_2^{\rm local\ main}
\quad\leftrightarrow\quad
S_3^{\rm local\ main}.
}
\tag{28}
\]

At the local-density level, the combination `S1-2S2+S3` therefore centers the coherent congruence modes exactly rather than leaving the isolated covariance of WI-043 as an unavoidable remainder.

## 7. Why restricting to coprime `(b1,b2)` is asymptotically legitimate here

The Yang bases are prime powers. If two bases have distinct underlying primes then they are coprime, and Sections 3--6 apply. WI-039 already computed the normalized two-base Mertens mass of same-prime pairs:

\[
\frac1{\ell^2}
\sum_p
\left(\sum_{a\ge1}\frac{\log p}{p^a}\right)^2
=
\frac1{\ell^2}
\sum_p\frac{(\log p)^2}{(p-1)^2}
=O(\ell^{-2}).
\tag{29}
\]

Hence the noncoprime prime-power family is `o(1)` in the continuum normalization already used by this audit. The present identity therefore resolves the local-factor question on asymptotically full normalized two-base mass.

This does **not** authorize silently dropping the noncoprime family inside an unnormalized finite ledger. Any end-to-end proof must charge it in the exact normalization being consumed. Equation (29) supplies the relevant asymptotic mechanism, not a finite-height numerical bound.

## 8. What this corrects and what it does not

WI-043 remains correct as an information-theoretic statement: marginal maximal discrepancy does not control an isolated locked covariance. WI-044 correctly warned that such a covariance can be an artifact of centering at the wrong level. The present calculation resolves the natural next test:

\[
\boxed{
\text{the Yang singular-series cell main absorbs the shared local }p\text{-adic modes.}
}
\tag{30}
\]

The alternating parity model in WI-044 is therefore not an accidental toy cancellation; it mirrors the exact `p=2` factor in (15)/(21). The same mechanism persists at every odd prime through (14) and (19).

However, (30) is **not** the missing welding theorem. The actual source contains:

- overlap weights depending on `k`, block geometry, and the strip;
- moving intervals in the welding coefficient;
- the Montgomery kernel and continuum selectors;
- diagonal/Poisson terms that must be booked separately;
- a shift-only Cauchy step whose normalization is load-bearing;
- major/minor-arc analytic errors.

The finite CRT average (24) does not commute those weights through the `k`-average for free. A nonuniform weight can correlate with residue classes. The source itself says this passage is handled by exact main-term factorization and Abel summation on major arcs; the corresponding theorem-level write-out is precisely what WI-037 and WI-042 found missing from the public package.

So the remaining obligation is narrower than WI-043 suggested but still nontrivial:

\[
\boxed{
\text{exact locally centered }(S_1-2S_2+S_3)
\to
\text{weighted shift residual}
\to
\text{established cancellation theorem}.
}
\tag{31}
\]

## 9. Prior-art and novelty audit

No novelty is claimed for Hardy--Littlewood local factors, the singular series, CRT, residue collision counts, or the fact that averaging a singular series can be evaluated prime by prime. These are classical mechanisms.

More importantly, the **source itself points toward this factorization**. Its `kap_p`/`e2_const` code defines exactly the two sides of (24); its later coincidence-counting closure states that the local proposition supplies the `j`-averaged factorization identities used by the higher-cycle ledgers; and `pipeline/face_dispersion.py` models the resolved four-point density by the product of two twin singular series on the exact CRT progression. The Mathia contribution here is therefore not a new singular-series theorem. It is the audit reconstruction that places these source pieces into one exact finite identity and uses that identity to decide the WI-044 fork.

A bounded prior-art check around Gallagher-type singular-series averages and constrained/smooth singular-series sums found the expected classical/modern literature on precisely this kind of local incidence averaging. Nothing in that literature is needed for the finite identity (24), and absence of this exact notation is not a priority claim.

## 10. Decisive audit and falsification tests

The finding should be rejected or narrowed if any of the following fails.

1. Recompute the generic-prime square mean (12) and verify it equals the generic `e2_const` factor `1+1/(p-1)^3`.
2. Check the coefficient-prime cases against the exact `kap_p` table, including arbitrary positive `v_p(b_i)` and `p=2`.
3. Verify (24) directly for several squarefree `Q` by CRT or exhaustive residue enumeration; no prime data are needed.
4. Verify the lock-bias identity (26) by counting unit pairs, including the one-coefficient-divisible cases.
5. Confirm from the exact `S1` swap that the two pair shifts are `rk` and `qk`; on the coprime family these are `b1 k` and `b2 k`.
6. Do not infer a weighted asymptotic from (24) without proving that the actual kernel/overlap weights preserve the local averaging or charging their residue bias explicitly.
7. Do not promote the Yang `0.6916` candidate unless the remaining weighted residual in (31), the continuum/tail bookkeeping, and every other live gate are all discharged in the consumed normalization.

## 11. Consequence for `weil_inertia`

The local-congruence branch of the welding audit is now substantially sharper. A new four-prime theorem is **not** justified merely to kill parity or another deterministic `p`-adic mode: the exact cell main already projects those modes into `E2` and cancels them in the centered dispersion. Conversely, WI-037/WI-042 are not repaired by this observation; their missing step is now identifiable as an analytic transport problem rather than a local-factor problem.

The shortest evidence-changing target is therefore to write the actual weighted, locally centered shift-first residual after (28), with the `k`-dependent overlap/kernel weights still present. If it reduces to a linear combination of marginal twin deviations with controlled coefficients, WI-041's maximal MRT machinery may become sufficient. If a genuinely joint residual survives **after** the exact local projection, then and only then does the stronger bilinear/four-point or higher-uniformity machinery become logically necessary.
