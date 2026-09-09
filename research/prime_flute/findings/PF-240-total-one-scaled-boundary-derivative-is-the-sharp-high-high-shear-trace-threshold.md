# PF-240 — total one scaled boundary derivative is the sharp high-high shear trace threshold

**Status:** `EXACT-DERIVED + SHARP-CONDITIONAL-REDUCTION + TRACE-IDEAL-THRESHOLD + POSITIVE/ROUTE-NARROWING`.

PF-239 reduces the hypercycle-straightening shear problem to the high-high block

\[
H_Z=(I-\Pi_Z)\Delta_{21}(I-\Pi_Z),
\]

where `Delta_21` is the difference between the actual-seam-normalized sheared and diagonal crossing blocks and `Pi_Z=1_[0,Z](K_a)` is the PF-233 fixed-scaled-band projector. PF-239 proves that everything touching `Pi_Z` is already absolutely trace summable after the reciprocal-prime weight, but leaves open what quantitative boundary-to-boundary smoothing is actually sufficient for `H_Z`.

The required theorem is much weaker than preserving PF-238's full exponential `F(sm)=sm/sinh(sm)` envelope. Because the boundary is one-dimensional and PF-233 gives the exact scaled spectral law `k_m(K_a) asymp s(m+alpha)`, **any uniform high-high Sobolev gain of total order strictly larger than one closes the shear block in strong trace class at cost `O(beta/s)`**. The threshold is sharp for this abstract information: total order exactly one forces only weak trace class in the model case, and any smaller total order need not even be weak trace class.

Consequently the remaining PF shear PDE gate can be stated precisely. It is enough to prove, for some `r_1,r_2>0` with `r_1+r_2>1`, a canonical-tail estimate

\[
\boxed{
\left\|K_a^{r_2}H_ZK_a^{r_1}\right\|
\le C_{Z,r_1,r_2}\,\beta
}
\tag{1}
\]

uniformly in the shrinking corridor. No mode-by-mode exponential transfer law is required for the **shear correction**. Once (1) holds, the reciprocal-prime weighted high-high family is absolutely summable in trace norm, just like PF-239's low-touch part.

This does not prove (1) for the exact PF-232 hypercycle form. It converts the vague phrase "prove high-high smoothing" into a sharp scaled operator target and shows exactly how much smoothing the arithmetic budget buys.

## Claim

Let `K=K_a` be PF-233's positive transverse operator on one canonical diagonal corridor. On the canonical tail there are constants `c,C>0`, independent of the corridor index, such that its eigenvalues `k_m`, `m>=0`, satisfy

\[
 c\,s(m+\alpha)\le k_m\le C\,s(m+\alpha),
 \qquad
 \alpha=\frac{1+\sqrt5}{2}.
\tag{2}
\]

Fix `Z>0` and write

\[
P_Z=\mathbf 1_{(Z,\infty)}(K).
\tag{3}
\]

Let `T` be any boundary operator and put

\[
H_Z=P_ZTP_Z.
\tag{4}
\]

Suppose there are `r_1,r_2>0` with

\[
r_1+r_2>1
\tag{5}
\]

such that

\[
A_Z:=K^{r_2}H_ZK^{r_1}
\tag{6}
\]

extends boundedly and obeys

\[
\|A_Z\|\le M\beta.
\tag{7}
\]

Then `H_Z` is trace class and

\[
\boxed{
\|H_Z\|_1
\le
C_{r_1,r_2}\,M\,rac{\beta}{s}\,
Z^{1-r_1-r_2},
}
\tag{8}
\]

with the harmless convention that `Z` is kept in a fixed positive scaled range. In particular, for every fixed `Z>0`,

\[
\|H_Z\|_1=O\!\left(\frac{\beta}{s}\right).
\tag{9}
\]

For PF-239's actual shear correction, take

\[
T=\Delta_{21}=\bigl(D_1-D_0\bigr)_{21},
\qquad
D_j=(I+Q^{-1/2}\Lambda_jQ^{-1/2})^{-1},
\tag{10}
\]

with the same complete-lift seam form `Q` on both corridors. If (7) holds uniformly with `beta=beta_n`, then PF-221/PF-239's reciprocal-prime weight

\[
\delta_n=P_n^{-1}-P_{n+1}^{-1}
\tag{11}
\]

gives

\[
\boxed{
\sum_n\delta_n\|H_{n,Z}\|_1<\infty.
}
\tag{12}
\]

Indeed PF-239 already proves

\[
\delta_n\frac{\beta_n}{s_n}
\lesssim \frac1{P_nP_{n+1}},
\tag{13}
\]

and the latter series converges.

The total-order threshold in (5) is sharp if one assumes only (2) and (7). For the exact model spectrum

\[
k_m=s(m+\alpha)
\tag{14}
\]

and `R=r_1+r_2`, consider on the high subspace

\[
T_Z=\beta P_ZK^{-R}P_Z.
\tag{15}
\]

Then

\[
K^{r_2}T_ZK^{r_1}=\beta P_Z,
\tag{16}
\]

so the scaled smoothing bound is saturated. If `R=1`, the singular values are

\[
\mu_m(T_Z)=\frac{\beta}{s(m+\alpha)}
\tag{17}
\]

past the cutoff. Thus `T_Z` is weak trace class with scale `O(beta/s)` but is not trace class. If `R<1`, the model singular values decay like `m^{-R}` and need not belong to `S_{1,\infty}`. Therefore **strictly more than one total scaled boundary derivative is exactly the threshold at which this abstract route forces strong trace class**.

## 1. Schatten factorization turns scaled Sobolev gain into trace norm

Because `r_1+r_2>1`, one can choose conjugate exponents `p,q in (1,infty)` with

\[
\frac1p+\frac1q=1,
\qquad
pr_2>1,
\qquad
qr_1>1.
\tag{18}
\]

Since `P_Z` commutes with `K`,

\[
H_Z
=
(P_ZK^{-r_2})\,
A_Z\,
(K^{-r_1}P_Z).
\tag{19}
\]

Schatten Hölder therefore gives

\[
\|H_Z\|_1
\le
\|P_ZK^{-r_2}\|_p\,
\|A_Z\|\,
\|K^{-r_1}P_Z\|_q.
\tag{20}
\]

It remains only to count the PF-233 transverse spectrum.

For any `t>0` and exponent `ar>1`, (2) gives

\[
\|P_ZK^{-r}\|_a^a
=
\sum_{k_m>Z} k_m^{-ar}.
\tag{21}
\]

The upper half of (2) implies that `k_m>Z` forces

\[
m+\alpha>\frac{Z}{Cs},
\tag{22}
\]

while the lower half gives

\[
k_m^{-ar}\le (cs)^{-ar}(m+\alpha)^{-ar}.
\tag{23}
\]

An integral comparison of the tail of the convergent `ar`-series yields

\[
\|P_ZK^{-r}\|_a^a
\le
C_{a,r}\,s^{-1}Z^{1-ar},
\tag{24}
\]

and hence

\[
\boxed{
\|P_ZK^{-r}\|_a
\le
C_{a,r}\,s^{-1/a}Z^{1/a-r}.
}
\tag{25}
\]

Apply (25) with `(a,r)=(p,r_2)` and `(q,r_1)`. Because `1/p+1/q=1`, (20) becomes exactly (8).

The `s^{-1}` factor is not an artifact of a crude estimate: it is the one-dimensional density of transverse modes in a fixed scaled-frequency interval. PF-233 already identified the same `O(s^{-1})` population at the critical band.

## 2. Symmetric half-derivative formulation

A particularly simple sufficient target is obtained by taking

\[
r_1=r_2=r>\frac12.
\tag{26}
\]

Then it is enough to prove

\[
\boxed{
\|K^rH_ZK^r\|\le C_r\beta.
}
\tag{27}
\]

The conclusion is

\[
\|H_Z\|_1
\le
C_r\frac{\beta}{s}Z^{1-2r}.
\tag{28}
\]

Thus the exact sheared-corridor problem does **not** need to recover a full analytic/exponential Poisson envelope for the perturbation. Slightly more than one-half scaled derivative on each boundary leg already buys absolute trace summability after the PF reciprocal-prime weight.

The endpoint `r=1/2` is genuinely critical under abstract spectral information alone. The model (15) gives `mu_m~beta/(sm)`: weak `S_1`, not strong `S_1`. This is the same one-dimensional counting threshold that repeatedly appears in the PF endpoint program, but here it is attached to the **shear correction's scaled Sobolev regularity**, not to its low-mode rank.

## 3. What classical DtN smoothing does and does not supply

The qualitative PDE mechanism is classical. For a fixed smooth compact manifold with several boundary components, the interaction between distinct components of the Dirichlet-to-Neumann map is smoothing: equivalently, after replacing the interior by disjoint capped collars with the same boundary germs, the DtN maps differ by an operator with smooth kernel. Girouard and Polterovich describe this surface argument in their Steklov survey, *J. Spectr. Theory* 7 (2017), 321--359, DOI `10.4171/JST/164`, in the proof discussion surrounding their sharp two-dimensional Steklov asymptotics. Hislop and Lutzer prove the analogous approximately-diagonal/smoothing decomposition for multiply connected smooth elliptic domains in *Inverse Problems* 17 (2001), 1717--1741, DOI `10.1088/0266-5611/17/6/313`.

Those fixed-geometry results do **not** by themselves prove (7). The PF corridors collapse with `s_n->0`, the relevant frequency is the scaled variable `s_nm`, and the desired estimate must retain the small perturbation factor `beta_n=O(P_n^{-1})` after the actual seam normalization. A family can be infinitely smoothing for every fixed `s>0` while its Sobolev constants diverge too rapidly as `s->0` to give any useful PF Schatten budget.

The literature audit therefore changes the target rather than closes it: fixed-domain off-diagonal smoothing is established prior art; the missing theorem is a **scaled-uniform perturbative smoothing estimate** for the explicit PF-232 hypercycle form and PF-238 complete-lift normalization.

A structure-directed search for DtN off-diagonal smoothing, multiply connected boundary asymptotics, and Schatten boundary estimates did not locate a result whose stated hypotheses directly provide the collapsing-corridor estimate (7) with the PF `beta_n` factor. No novelty is claimed for pseudodifferential smoothing, Schatten Hölder, or the one-dimensional Sobolev/Schatten threshold. The project-specific mathematical delta is the exact conversion of PF-233's scaled spectral law and PF-239's reciprocal-prime arithmetic budget into the sharp total-order threshold (5).

## 4. Falsification and boundary checks

1. **Conditional PDE input.** Equation (7) is not proved here for the sheared corridor. PF-240 is an exact operator-ideal reduction, not the missing elliptic regularity theorem.
2. **Uniformity is essential.** Ordinary `C^infty` smoothing for each fixed corridor is insufficient unless the scaled Sobolev norm is uniform at the `O(beta_n)` level.
3. **The same high projector is used on both legs.** `P_Z` is PF-233's spectral projector for `K_a`, exactly as in PF-239. No replacement by a physical Fourier cutoff is made.
4. **Actual seam normalization stays inside `T`.** The criterion is applied directly to PF-239's normalized difference `Delta_21`; it does not assume a nonexistent two-sided comparison between PF-237's actual and matched seam forms.
5. **Strong trace requires strict total order greater than one.** At total order one the abstract model gives only weak trace class. Any claim that the endpoint alone is enough for the later nested PF-222 sum needs an additional reassembly theorem and is not made here.
6. **No exponential envelope is inferred.** Strong trace class from (7) does not imply PF-238's `F(sm)` singular-value profile, pointwise mode preservation, or analytic smoothing.
7. **Finite heads are irrelevant.** As in PF-239, all estimates are canonical-tail statements; finitely many initial corridors contribute only finite trace-class corrections.
8. Physical `P/H` recoupling, one-cusp pant completion, neighboring-cell coupling, the exact nested PF-222 global identity, wave operators, determinants/resonances, prime/clone separation, zeta zeros, and RH remain outside the result.

## Consequences for the research line

PF-239 showed that only the high-high shear block remains. PF-240 now identifies the exact amount of high-high regularity that is sufficient: **more than one total scaled tangential derivative across the two boundary legs**. This is substantially weaker than reproducing the entire diagonal corridor's exponential transfer envelope.

The next local theorem should therefore attack the explicit PF-232 form at this precise scale. A positive proof may use parameter-uniform elliptic regularity, a separated-boundary Poisson estimate, a commutator/pseudodifferential argument in the PF-233 `K_a` scale, or another exact mechanism, but it must deliver the `O(beta_n)` uniform bound in (7). A decisive negative result should exhibit a canonical high-high family for which this scaled Sobolev norm grows faster than `beta_n` or fails at every total order above one.

If (7) is established, the entire shear correction becomes an absolutely trace-summable error under the reciprocal-prime commutator weight. The local frontier then moves cleanly to the physical `P/H` recoupling and finite-pant completion before the genuinely nested PF-222 global weak-trace reassembly.