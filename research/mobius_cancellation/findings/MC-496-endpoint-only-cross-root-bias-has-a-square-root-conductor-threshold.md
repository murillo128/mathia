# MC-496 — Endpoint-only cross-root bias has a square-root conductor threshold

**Status:** `LITERATURE+DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-WEIL+COMPLETION` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-495` reduces the incomplete repeated-residue cross-root problem to a weighted conductor-profile correlation. This finding isolates one of the possible sources of that profile: **endpoint truncation alone**.

Fix an odd prime conductor `p`, a nonprincipal Dirichlet character `chi (mod p)`, `h not congruent 0 (mod p)`, and a nonzero residue `a mod p`. For the two repeated-residue roots define

\[
K_a^+(m)=\chi(am+h)\overline{\chi(am)},
\qquad
K_a^-(m)=\chi(am)\overline{\chi(am-h)},
\]

and their cross-root phase

\[
R_a(m):=K_a^+(m)\overline{K_a^-(m)}.
\tag{1}
\]

With the usual extension `chi(0)=0`, this is a `p`-periodic bounded sequence. After the change of variable `t=am h^{-1}` on the nonzero conductor residues,

\[
R_a(m)=\chi(1-t^{-2}).
\tag{2}
\]

Let

\[
\mu_R:=\frac1p\sum_{t\bmod p}R_a(t).
\tag{3}
\]

The complete sum is the Jacobi sum already identified in `MC-492`, so

\[
|\mu_R|\ll p^{-1/2},
\tag{4}
\]

with the stronger `O(p^{-1})` scale in the quadratic case.

More importantly, classical complete mixed rational-character bounds plus Fourier completion give, uniformly for every finite integer interval `J`,

\[
\boxed{
\left|\sum_{m\in J}\bigl(R_a(m)-\mu_R\bigr)\right|
\ll \sqrt p\,\log p.
}
\tag{5}
\]

Now consider an **endpoint-only** repeated-residue block: retain arbitrary nonnegative row coefficients but remove the lower-prime pair-sieve masks and every other internal arithmetic weight. Thus

\[
A(m)=\sum_{q\in Q_+}\alpha_q\,\mathbf 1_{J_q^+}(m),
\qquad
B(m)=\sum_{r\in Q_-}\beta_r\,\mathbf 1_{J_r^-}(m),
\tag{6}
\]

where `alpha_q,beta_r>=0` and every `J_q^+,J_r^-` is an integer interval coming only from the source endpoints after the rowwise changes of variables `n=qm` and `n+h=rm`.

Put

\[
M_\times:=\sum_m A(m)B(m)
=\sum_{q,r}\alpha_q\beta_r\,|J_q^+\cap J_r^-|,
\tag{7}
\]

and

\[
P_\times:=
\sum_{\substack{q,r\\J_q^+\cap J_r^-\ne\varnothing}}
\alpha_q\beta_r.
\tag{8}
\]

When `P_x>0`, define the weighted average cross-overlap length

\[
L_\times:=\frac{M_\times}{P_\times}.
\tag{9}
\]

Then the exact cross-root term

\[
C_{A,B}:=\sum_m A(m)B(m)R_a(m)
\tag{10}
\]

satisfies

\[
\boxed{
\left|C_{A,B}-\mu_R M_\times\right|
\ll \sqrt p\,\log p\;P_\times,
}
\tag{11}
\]

and therefore

\[
\boxed{
\frac{|C_{A,B}|}{M_\times}
\ll
p^{-1/2}
+\frac{\sqrt p\,\log p}{L_\times}.
}
\tag{12}
\]

Thus whenever

\[
L_\times\gg \sqrt p\,\log p\;\omega(p),
\qquad \omega(p)\to\infty,
\tag{13}
\]

endpoint truncation alone produces only `o(1)` cross-root phase bias relative to the available overlap mass. In particular it cannot create the fixed order-one negative conductor bias required to cancel a fixed proportion of the same-root energy.

The statement can be upgraded to an explicit energy comparison. Let

\[
S_+:=\sum_m A(m)^2,
\qquad
S_-:=\sum_m B(m)^2,
\tag{14}
\]

and define `P_+`, `P_-` by summing `alpha_q alpha_{q'}` or `beta_r beta_{r'}` only over nonempty same-root interval intersections. Set

\[
L_+=S_+/P_+,
\qquad
L_-=S_-/P_-.
\tag{15}
\]

The character row `K_a^+` vanishes on at most two residue classes modulo `p`, and the same is true for `K_a^-`. Hence the actual diagonal energies

\[
E_+:=\sum_m |K_a^+(m)|^2A(m)^2,
\qquad
E_-:=\sum_m |K_a^-(m)|^2B(m)^2
\tag{16}
\]

obey

\[
E_+\ge\left(1-\frac2p-\frac2{L_+}\right)S_+,
\qquad
E_-\ge\left(1-\frac2p-\frac2{L_-}\right)S_-.
\tag{17}
\]

Since `M_x <= sqrt(S_+S_-) <= (S_++S_-)/2`, if

\[
\varepsilon:=
\max\left\{
\frac2p+\frac2{L_+},
\frac2p+\frac2{L_-}
\right\}<1,
\tag{18}
\]

then

\[
\boxed{
\frac{2|C_{A,B}|}{E_++E_-}
\ll
\frac{
 p^{-1/2}+\sqrt p\log p/L_\times
}{1-\varepsilon}.
}
\tag{19}
\]

Consequently, if `L_+,L_- -> infinity` and `L_x/(sqrt(p) log p) -> infinity`, cross-root interference caused by endpoints alone is `o(1)` of the diagonal energy. Long endpoint intervals therefore **cannot be the missing resource left open by `MC-495`**.

No estimate for `M(x)`, zero-free region, or RH follows.

## 1. Centered interval sums have square-root conductor resolution

Equation `(2)` shows that `R_a` is a multiplicative character evaluated on a fixed-degree rational function. That rational function is not an `ord(chi)`-th power in `F_p(t)`: its zeros at `t=+/-1` have multiplicity one. Therefore the standard Weil/Stepanov bound applies to the complete sum with any nontrivial additive twist. In the notation of `MC-S55`, for every `k not congruent 0 (mod p)`,

\[
\left|
\sum_{t\bmod p}R_a(t)e_p(kt)
\right|\ll\sqrt p.
\tag{20}
\]

For `k=0`, `MC-492` gives the exact Jacobi-sum evaluation and the same `O(sqrt(p))` bound. After centering by `mu_R`, the zero Fourier coefficient vanishes while all nonzero coefficients remain `O(sqrt(p))`.

For an interval of length below `p`, discrete Fourier inversion and the geometric-series estimate

\[
\left|\sum_{m\in J}e_p(km)\right|
\ll \min\left(|J|,\frac{p}{\min(k,p-k)}\right)
\tag{21}
\]

give `(5)` after summing the harmonic `k^{-1}` tail. For a longer interval, remove complete `p`-blocks first; their centered contribution is exactly zero, leaving one residual interval of length below `p`.

This is ordinary Pólya-Vinogradov-style completion for a bounded-complexity rational character phase. The `sqrt(p) log p` threshold is therefore a classical completion scale, not a new character-sum theorem.

## 2. Endpoint aggregation reduces to interval intersections

Expanding `(6)` gives

\[
A(m)B(m)
=\sum_{q,r}\alpha_q\beta_r
\mathbf 1_{J_q^+\cap J_r^-}(m).
\tag{22}
\]

Every nonempty intersection of two integer intervals is again an integer interval. Applying `(5)` separately to each intersection and summing with the nonnegative coefficient `alpha_q beta_r` gives

\[
|C_{A,B}-\mu_RM_\times|
\ll \sqrt p\log p
\sum_{q,r:J_q^+\cap J_r^-\ne\varnothing}\alpha_q\beta_r,
\tag{23}
\]

which is exactly `(11)`. Division by `M_x=L_xP_x` gives `(12)`.

The role of `L_x` is structural: adding many endpoint rows does not by itself worsen the bound. The only tariff is the number of nonempty pair intersections, and their total mass converts that count into the reciprocal of the **average intersection length**. A dense repeated-residue family can therefore evade this endpoint-only obstruction only by concentrating its relevant cross-root mass into conductor-scale-short intersections.

## 3. The diagonal remains large on long same-root overlaps

For `K_a^+`, the two zero classes are `am congruent 0,-h (mod p)`; for `K_a^-` they are `am congruent 0,h (mod p)`. An interval `I` of length `L` contains at most

\[
\frac{2L}{p}+2
\tag{24}
\]

points in either pair of residue classes. Expanding `A^2` into same-root interval intersections and subtracting only those zero locations gives the first inequality in `(17)`; the minus-root argument is identical.

Cauchy-Schwarz gives

\[
M_\times\le\sqrt{S_+S_-}\le\frac{S_++S_-}{2}.
\tag{25}
\]

Combining `(12)`, `(17)`, and `(25)` proves `(19)`. Thus the centered interval estimate does not merely say that the phase average is small: in the long-overlap regime it says that endpoint-only cross interference is too small **relative to the actual two-root diagonal energy** to drive a fixed fractional cancellation.

## 4. Relevance to the current first-exit frontier

`MC-492` rules out same-root cancellation for the native common-sign Buchstab coefficient, even on incomplete intervals. `MC-493` and `MC-494` show that complete cross-root interference needs large multiplicity and tensorizes before it can exploit source structure. `MC-495` then identifies the only remaining incomplete repeated-residue scalar resource as the centered conductor-profile weight

\[
w(t)-\overline w
\]

correlated with the fixed rational phase `chi(1-t^{-2})`.

The present result prices the simplest possible origin of that centered profile. If `w` is generated only by positive superposition of source endpoints, then long overlaps cannot carry order-one phase bias: completion already forces `(12)` and `(19)`. Therefore a successful continuation of the normalized first-exit route must obtain its conductor selectivity from at least one of the following:

- the **lower-prime pair-sieve masks or other internal source arithmetic** retained inside `w`;
- a genuinely `q`-dependent signed or complex coefficient introduced before the nonnegative repeated-residue aggregation;
- a short-overlap regime at or below the `sqrt(p) log p` completion scale, together with a reconstruction showing that enough source mass remains there;
- a different non-rowwise arithmetic transformation not covered by the `MC-484`--`MC-495` architecture.

Endpoint placement by itself is no longer a generic explanation for the incomplete-weight loophole.

## 5. Prior art and novelty boundary

The analytic ingredient is classical. `MC-S55` records Cochrane--Pinner's Weil/Stepanov bounds for complete mixed additive/multiplicative character sums of rational functions. Standard finite Fourier completion then gives the `sqrt(p) log p` incomplete-interval scale. The untwisted complete mean is the Jacobi-sum quantity already audited in `MC-492`.

No novelty is claimed for those character-sum estimates, Fourier completion, interval-intersection algebra, or the elementary zero-class count. The durable Mathia delta is the **frontier specialization**: after the exact `MC-495` amplitude collapse, source endpoints alone can be separated from the harder sieve/source arithmetic and shown quantitatively incapable of producing order-one cross-root cancellation whenever the weighted overlap lengths are above the square-root conductor resolution.

## Boundaries and falsification tests

- **Endpoint-only model.** The result deliberately removes lower-prime pair-sieve masks and any internal arithmetic coefficient. Restoring those weights can make the conductor profile highly non-interval-like and is not controlled by `(11)`.
- **Nonnegative row amplitudes.** The expansion uses `alpha_q,beta_r>=0`, exactly the common-sign repeated-residue setting inherited from the native first-exit coefficient. A derived signed or complex row coefficient is outside the theorem.
- **Average overlap, not minimum overlap.** The decisive quantity is `L_x=M_x/P_x`; some individual intersections may be short. The obstruction survives as long as the weighted average cross-overlap is long.
- **Diagonal comparison needs long same-root overlaps.** The stronger energy ratio `(19)` additionally requires `L_+` and `L_-` large enough that the two character-zero classes occupy a negligible fraction of the unphased same-root energy.
- **Square-root completion threshold is not claimed sharp.** Stronger incomplete rational-character bounds in special regimes could only strengthen the obstruction. The present theorem uses the robust classical `sqrt(p) log p` scale.
- **Short overlaps remain live.** When `L_x` is `O(sqrt(p) log p)`, `(12)` does not preclude order-one phase bias. A viable short-row mechanism must still show that its total source mass and reconstruction costs are favorable.
- **No Möbius summatory conclusion.** This is a source-frame obstruction inside one normalized Buchstab/character architecture, not a bound for `M(x)`.

## Consequence for the accepted clue

The unresolved `MC-495` weight question can now be narrowed: **endpoints alone are insufficient in the long-overlap regime**. Any future derivation of the exact conductor-profile weight should separate endpoint geometry from lower-prime sieve/source structure and identify which latter factor creates phase selectivity. If the exact first-exit source has weighted overlaps much larger than `sqrt(p) log p`, then the next load-bearing test is no longer endpoint completion but whether the hard pair-sieve mask has a nontrivial signed correlation with `chi(1-t^{-2})` after residue projection. If the overlaps are shorter, the reconstruction/source-mass cost of that short regime must be charged explicitly.