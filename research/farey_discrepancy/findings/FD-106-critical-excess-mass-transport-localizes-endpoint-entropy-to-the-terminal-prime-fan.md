# FD-106 — critical excess-mass transport localizes endpoint entropy to the terminal prime fan

**Status:** `EXACT-DERIVED + CONTRACTION-SUMMABILITY + CRITICAL-EXCESS-MASS + SOURCE-TAGGED-PREDECESSOR + TERMINAL-HARMONIC-ENDPOINT + EPSILON-AMORTIZATION + SOURCE-NEUTRAL-POTENTIAL-COUPLING + FALSE-RH-COMPOSITION + NO-RH-CONTRADICTION`.

`FD-105` leaves one explicit quantitative gate: the predecessor theorem selects a branch using a global constant `b_sigma`, so it forgets how much physical horizon contraction that branch actually bought and whether the contraction was source-neutral. That loss is avoidable at the natural high-mass scale.

Write

\[
R_H:=\frac{U_H}{H}.
\tag{1}
\]

This is the exact excess above the linear nonsquarefree-mass floor, and the adaptive source cutoff of `FD-105` is `L_H=floor(R_H/log H)`. For every fixed `epsilon>0`, every sufficiently large high-mass state `R_H>=H^delta` has a genuine source-tagged predecessor `C<H` such that

\[
\boxed{
R_C\ge a_\epsilon
\left(\frac CH\right)^\epsilon R_H
}
\tag{2}
\]

for a constant `a_epsilon>0` independent of `H`. The destination mask can again be restricted to source arguments larger than `L_H/2`.

More sharply, **the epsilon loss is needed only in the repaired dyadic-terminal nonhead family**. If the selected predecessor comes from the odd repeated-square family, the already-eligible dyadic half-scale family, or the source-head retreat, then one can take `epsilon=0`:

\[
\boxed{R_C\ge a_0R_H.}
\tag{3}
\]

The terminal nonhead family has child scales `C_p/H=(1+o(1))/p`. Its critical contraction weights therefore have the harmonic-prime endpoint `sum_p C_p/H ~ sum_p 1/p`, so the raw packet-mass identity alone cannot give an `H`-uniform version of (3). But every arbitrarily small positive power is enough:

\[
\sum_p\left(\frac{C_p}{H}\right)^{1+\epsilon}=O_\epsilon(1),
\]

which gives (2).

Thus the branch-sensitive quantity requested after `FD-105` is explicit. Physical contraction is not an independent loss: at the critical mass ratio it costs only an arbitrarily small power, and away from the terminal prime fan it costs no power at all. Iterating (2) along any high-mass predecessor chain gives the telescoping law

\[
\boxed{
R_{H_m}
\ge
a_\epsilon^m
\left(\frac{H_m}{H_0}\right)^\epsilon
R_{H_0}.
}
\tag{4}
\]

This is exactly compatible with the carrier-free potential of `FD-102`. On a source-neutral nonhead segment, the same cumulative horizon contraction that appears with coefficient `epsilon` in (4) is the quantity that drains the source-neutral potential. Hence large odd-prime contractions cannot simultaneously be charged once as geometric descent and again as a full fixed normalized-mass loss.

The remaining endpoint is now narrower. To remove the `epsilon` from the terminal family one must use information absent from the aggregate packet theorem: the deterministic least-prime-factor partition of the complete odd-squarefree terminal prefix and the common quotient-shell source values. A matched abstract packet distribution shows that total raw mass plus the scale law `C_p~H/p` alone cannot do it.

## 1. A contraction-summability lemma

The mechanism is elementary and independent of the detailed arithmetic construction. Suppose one parent state at horizon `H` produces a finite family of genuine child states `C_i<H` with nonnegative child mask energies `N_i<=U_(C_i)` satisfying

\[
\sum_iN_i\ge cU_H
\tag{5}
\]

for some fixed `c>0`. Put

\[
\theta_i:=\frac{C_i}{H},
\qquad
R_i:=\frac{U_{C_i}}{C_i}.
\tag{6}
\]

Since `N_i<=C_iR_i`,

\[
cR_H
\le
\sum_i\theta_iR_i.
\tag{7}
\]

For any `epsilon>=0`, define

\[
S_\epsilon:=\sum_i\theta_i^{1+\epsilon}.
\tag{8}
\]

Then

\[
\sum_i\theta_iR_i
\le
\left(
\max_i\theta_i^{-\epsilon}R_i
\right)S_\epsilon.
\]

Therefore, whenever `S_epsilon` is bounded uniformly in the parent state, some child obeys

\[
\boxed{
R_i\ge \frac{c}{S_\epsilon}\theta_i^\epsilon R_H.
}
\tag{9}
\]

This is the branch-sensitive pigeonhole principle missing from the scalar `b_sigma` recurrence. It retains the actual contraction ratio rather than first normalizing every child at an unrelated fixed exponent and then taking the worst branch constant.

At `epsilon=0`, the criterion is especially transparent: **a raw child family transports a fixed fraction of critical excess mass whenever the sum of its horizon ratios is uniformly bounded**.

## 2. Three predecessor mechanisms are already critical-lossless

Apply the source-rich compression of `FD-105`. Its compressed packets carry `(1-o(1))U_H`, all retained quotient-shell arguments exceed `L_H`, and every exact repair keeps the destination source above `L_H/2`.

### Odd repeated-square family

If the odd first-stage labels carry the relevant fixed fraction, `FD-104` gives repaired masks with

\[
\sum_{p\ge3}N_{p,H}
\ge
\left(\frac1{2\zeta(2)}-o(1)\right)U_H
\tag{10}
\]

and

\[
\theta_{p,H}
:=\frac{C_p}{H}
=rac4{p^2}(1+o(1))
\tag{11}
\]

uniformly over the retained source-rich packet. Hence

\[
\sum_{p\ge3}\theta_{p,H}
\le
(4+o(1))\sum_{p\ge3}p^{-2}
=O(1).
\tag{12}
\]

Taking `epsilon=0` in (9) gives a selected odd predecessor with

\[
\boxed{R_{C_p}\gg R_H.}
\tag{13}
\]

Thus the potentially very large contraction `H/C_p~p^2/4` is not a critical-mass penalty. The square contraction makes the family summable strongly enough to pay its own prime-label entropy.

### Already-eligible dyadic family

If the dyadic mask is already nonsquarefree after first deflation, the selected state is

\[
A_2=\frac H2+O(1)
\]

and, in the branch split of `FD-104`, it carries a fixed raw fraction of `U_H`. Therefore

\[
\boxed{R_{A_2}\gg R_H.}
\tag{14}
\]

There is no growing family entropy here.

### Source-head retreat

If the terminal head atom dominates, `FD-104` gives

\[
U_C\ge\left(\frac1{32}-o(1)\right)U_H,
\qquad C<H.
\tag{15}
\]

Consequently

\[
\boxed{R_C\gg R_H.}
\tag{16}
\]

In fact the head mechanism is better than critical-lossless: its physical contraction is the same backward source retreat already exposed by `FD-095`, so no source-neutral interpretation is available for this branch.

Equations (13)--(16) show that neither odd repeated-square entropy, the dyadic half-step, nor the head retreat causes the critical endpoint loss hidden inside `b_sigma`.

## 3. The repaired terminal prime family has exactly one harmonic endpoint

The only remaining case is the dyadic-terminal nonhead family. In the source-rich version of the `FD-093` repair, its masks satisfy

\[
\sum_{p\ge3}N_{p,H}
\ge
\left(\frac18-o(1)\right)U_H
\tag{17}
\]

whenever this branch is selected. The source-rich cutoff forces `B/p>=L_H+O(1)`, so the floor in the repaired horizon is uniformly negligible and

\[
\boxed{
\theta_{p,H}
:=\frac{C_p}{H}
=rac1p(1+o(1))
}
\tag{18}
\]

throughout the packet.

At the critical exponent `epsilon=0`, the contraction sum is therefore of harmonic-prime type and is not uniformly bounded. For every fixed `epsilon>0`, however,

\[
\sum_{p\ge3}\theta_{p,H}^{1+\epsilon}
\le
(1+o(1))\sum_{p\ge3}p^{-1-\epsilon}
=O_\epsilon(1).
\tag{19}
\]

Applying (9) to (17)--(19) gives some terminal repaired predecessor with

\[
\boxed{
R_{C_p}
\ge
c_\epsilon
\left(\frac{C_p}{H}\right)^\epsilon
R_H,
}
\tag{20}
\]

where `c_epsilon>0` is fixed. Combining this with the three critical-lossless alternatives proves the unified one-step theorem (2), after reducing the constant if necessary.

This recovers the `sigma>1/2` endpoint of `FD-104` in a more informative currency. There the terminal family was summed using `p^(-2sigma)`. Here one writes

\[
1+\epsilon
\]

instead of `2sigma` and leaves the residual power as the actual contraction factor `(C/H)^epsilon`. The divergence at `sigma=1/2` is therefore not a generic failure of critical predecessor transport. It is one specific harmonic endpoint attached to the scale law `C_p~H/p`.

### Matched endpoint relaxation

The positive `epsilon` cannot be removed from **only** the two aggregate facts (17) and (18). To see this, truncate to primes `3<=p<=P`, let

\[
S_P:=\sum_{3\le p\le P}\frac1p,
\]

and consider the abstract nonnegative packet allocation

\[
N_p:=\frac{cU_H}{S_Pp},
\qquad
C_p:=\frac Hp.
\tag{21}
\]

Then `sum_pN_p=cU_H`, exactly as required by a raw family lower bound, but every child has

\[
\frac{N_p/C_p}{U_H/H}
=
\frac c{S_P}.
\tag{22}
\]

The classical divergence `S_P->infinity` follows directly from Euler's finite product argument: the product over `(1-1/p)^(-1)` dominates arbitrarily long harmonic partial sums, while its logarithm differs from `sum_(p<=P)1/p` by a bounded convergent `sum_pO(p^-2)` term. Thus the right-hand side of (22) tends to zero.

This is deliberately a **relaxed matched control**, not a claim that the physical terminal packets can realize arbitrary masses `N_p`. It proves only the correct information boundary: no uniform critical constant follows from total packet mass and the horizon law `H/p` alone. Any endpoint improvement must exploit the arithmetic structure discarded by that relaxation.

The physical terminal family has exactly such unused structure: `FD-093` partitions the complete odd-squarefree prefix by the **least prime factor** of each row, and every packet amplitude is generated by the same quotient-shell source. Whether that coherence forbids the harmonic matched allocation is now the precise endpoint question.

## 4. The epsilon law couples to the exact `FD-102` contraction currency

The carrier-free potential of `FD-102` is

\[
\mathfrak A(H,x)
=
\log_2\frac{H-1}{8x-1}
\tag{23}
\]

for a nonhead source tag `x`. For any nonhead transition from `(H,x)` to `(C,y)`, before using the coarse fact `C<=ceil(H/2)`, there is the exact algebraic identity

\[
\boxed{
\mathfrak A(C,y)
=
\mathfrak A(H,x)
-
\log_2\frac{H-1}{C-1}
+
\log_2\frac{8x-1}{8y-1}.
}
\tag{24}
\]

`FD-102` used only that the middle term is at least one. Equation (24) retains the full branchwise contraction. If the retag does not descend in source, `y>=x`, then

\[
\mathfrak A(C,y)
\le
\mathfrak A(H,x)
-
\log_2\frac{H-1}{C-1}.
\tag{25}
\]

Thus the same logarithmic contraction has two simultaneous roles:

- it spends source-neutral potential with coefficient `1` in (25);
- it costs critical excess mass with only coefficient `epsilon` in (2).

This is the desired amortization between the two currencies. A large-prime child is no longer represented as an arbitrary fixed `b_sigma` loss plus a separate geometric contraction. The contraction itself pays the prime-label entropy, except for the arbitrarily small terminal endpoint power.

Iterating (2) while the states remain in the high-mass regime gives exactly

\[
\boxed{
R_{H_m}
\ge
a_\epsilon^m
\left(\frac{H_m}{H_0}\right)^\epsilon
R_{H_0}.
}
\tag{26}
\]

If a consecutive nonhead segment remains source-neutral in the strong sense `x_m>=x_0`, then `H_m-1>=8x_m-1>=8x_0-1`. Hence (26), with harmless fixed factors from replacing `H` by `H-1`, yields

\[
\boxed{
R_{H_m}
\gg
 a_\epsilon^m
\left(\frac{8x_0-1}{H_0-1}\right)^\epsilon
R_{H_0}.
}
\tag{27}
\]

The entire multiplicative horizon contraction of a source-neutral segment is therefore charged only once, through an arbitrarily small power of the finite source-neutral budget. The remaining exponential-in-depth tax is the fixed packet-selection constant `a_epsilon^m`.

## 5. False-RH entries keep the optimal initial excess exponent

At the strict-record fixed-occupation entries of `FD-096`,

\[
U_{H_0}=H_0^{2\Theta-o(1)},
\]

so the critical excess starts at

\[
\boxed{
R_{H_0}=H_0^{2\Theta-1-o(1)}.
}
\tag{28}
\]

This is the maximal power margin above the exact linear floor isolated in `FD-104`. Equation (26) transports that margin without introducing an auxiliary normalization exponent `sigma`:

\[
\boxed{
R_{H_j}
\ge
 a_\epsilon^j
 H_0^{2\Theta-1-o(1)}
 \left(\frac{H_j}{H_0}\right)^\epsilon.
}
\tag{29}
\]

In particular, even if one uses only the trivial `H_j>=1`, every fixed

\[
0<\epsilon<2\Theta-1
\]

leaves a positive initial power after the total-contraction charge. Choosing a sufficiently small fixed multiple of `log H_0` for the depth absorbs the remaining factor `a_epsilon^j`, so (29) by itself again supplies a logarithmic high-mass chain. Feeding the `FD-105` adaptive source cap

\[
L_{H_j}
\asymp
\frac{R_{H_j}}{\log H_j}
\]

back into the construction keeps the selected source tags and child horizons polynomially large exactly as before.

The gain over `FD-105` is not merely another positive depth constant. The new formula records **where the loss occurred**. At critical excess scale, all variable odd-square contractions are already entropy-self-financing; the only scale-dependent loss is the arbitrarily small power attached to the terminal `H/p` family. This is the information needed to combine mass transport with `FD-102` rather than comparing two unrelated worst-case constants.

There is still no RH contradiction. The fixed factor `a_epsilon<1` can be paid at every selection, and the relaxed terminal harmonic control shows why the endpoint `epsilon=0` does not follow from aggregate mass alone. A source-neutral chain can therefore remain compatible with all present inequalities while spending its finite geometric potential and its repeated packet-selection tax together.

## 6. Stress tests, prior art, and the new frontier

The record-seeded odd-square cascades of `FD-099` remain admissible. Their repeated `p=3` source-neutral repairs have a fixed contraction `4/9`; equation (13) correctly says that this contraction does not force critical excess-mass decay. That is expected: the source amplitude is being transported essentially unchanged while the physical horizon shrinks.

The opposite stress test is the synthetic terminal allocation (21). It saturates exactly the harmonic failure at `epsilon=0` and therefore prevents us from claiming that the terminal branch is already critical-lossless. Since it ignores the least-prime-factor prefix geometry and quotient-shell coherence, it also identifies rather than obscures the next possible source of improvement.

A targeted literature audit covered the classical Franel--Landau/Farey--Mertens discrepancy bridge, GCD/Jordan-matrix factorizations, recent local-discrepancy formulas, and work on Farey fractions with squarefree or `k`-free denominators and their correlations. Those results study global or restricted-denominator discrepancy/correlation families; no located source gives this source-specific contraction-summability law for repeated-prime predecessor packets, nor the localization of the critical endpoint to the repaired dyadic-terminal least-prime-factor fan. The proof above uses only the exact internal packet identities already established in `FD-091`, `FD-093`, `FD-104`, and `FD-105`, plus the elementary finite Euler-product argument included above. No new external theorem is load-bearing, so `SOURCES.md` requires no change.

The live theorem is consequently narrower than the frontier stated in `FD-105`. **Horizon contraction itself is no longer the unidentified loss.** The remaining choices are:

1. exploit the deterministic least-prime-factor/source coherence of the terminal prefix to beat the harmonic matched relaxation and obtain `epsilon=0` there as well; or
2. combine the epsilon-amortized law (27) with repeated source descent/head events strongly enough that the fixed packet-selection tax cannot be sustained for the full false-RH chain.

A mere improvement of the old scalar `b_sigma` still misses this distinction.