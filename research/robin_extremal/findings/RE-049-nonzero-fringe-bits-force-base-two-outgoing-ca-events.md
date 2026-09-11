# RE-049 — nonzero fringe bits force base-two outgoing CA events

**Status:** `EXACT-DERIVED + QUANTITATIVE-RH-FAILURE + CURVATURE-CLEARANCE + BASE-2-EVENT-REDUCTION + LOGARITHMIC-HOST-SPARSITY + SUMMABLE-FRINGE-VARIATION + COUNTEREXAMPLE-NARROWING + PRIOR-ART-BOUNDED`. `RE-048` pins every nonzero first-layer fringe switch to the final `O(1/log p)` fraction of the genuine CA support chamber of the entered state, but leaves the outgoing physical event unclassified. Combining amplitude maximality with the strict concavity of the same adaptive barrier supplies a lower clearance from the outgoing event. Under the nonzero-fringe hypothesis, the two bounds collapse the outgoing CA transition to a single possibility: a deep exponent increment of the prime `2`.

Assume RH is false, fix

\[
J=[b_0,b_1]\Subset(1-\Theta,1/2),
\]

and work on one sufficiently late common positive CA counterexample block from `RE-040`. Let `beta` be an interior breakpoint at which the rightmost adaptive fan makes a unique adjacent first-layer switch

\[
C_-<C,
\qquad C=pC_-,
\tag{1}
\]

through the ordinary prime `p`. Put

\[
Y=\log C,
\qquad h=\log G(C)-\gamma>0,
\qquad a=1-e^{-h},
\tag{2}
\]

and let `Z=Z_C(beta)` be the upper adaptive tangent selector,

\[
g(Z)=g(Y)-\frac{\beta a}{Y},
\qquad g(x)=\frac1{x\log x}.
\tag{3}
\]

Let `D` be the immediate next CA state after `C`, write

\[
\Delta:=\log D-\log C=\log(D/C)>0,
\tag{4}
\]

and let `xi` be the outgoing CA event coordinate,

\[
\varepsilon_+(C)=g(\xi).
\tag{5}
\]

Let `p^+` be the next ordinary prime and retain the fringe bit

\[
\chi_p:=\mathbf 1_{\{p^+\le Z\}}.
\tag{6}
\]

If

\[
\boxed{\chi_p=1,}
\tag{7}
\]

then the entered state's amplitude maximality and barrier curvature imply

\[
\boxed{
\xi-Z\ge\left(\frac12-o_J(1)\right)\Delta.
}
\tag{8}
\]

On the other hand `RE-048` gives the source-specific upper clearance

\[
\boxed{0<\xi-Z<\frac12.}
\tag{9}
\]

Therefore

\[
\Delta<1+o_J(1).
\tag{10}
\]

The exact CA event representation makes `D/C` an integer product of the prime-layer atoms firing at `xi`. Since `1<log 3`, equation (10) eventually forces

\[
\boxed{\frac DC=2.}
\tag{11}
\]

Hence the outgoing event is neither a generic higher-layer event, nor the next ordinary first-layer event, nor a tied transition. It is one deep base-two layer:

\[
\boxed{\xi=\eta_{2,j}}
\tag{12}
\]

for some `j->infinity`.

The same argument gives a second quantization. `RE-048` also yields

\[
p^+\le Z<\xi\le\eta_{p^+,1}<p^++\frac12,
\tag{13}
\]

while (8) and (11) imply

\[
\xi-Z\ge\frac{\log2}{2}-o_J(1).
\tag{14}
\]

Thus, for every sufficiently late nonzero-fringe switch,

\[
\boxed{
\left\lfloor\eta_{2,j}\right\rfloor=p^+,
\qquad
\frac{\log2}{2}-o_J(1)
\le
\{\eta_{2,j}\}
<\frac12.
}
\tag{15}
\]

So the remaining binary mismatch can occur only when a deep event of the **fixed base-2 CA ladder** lands in a narrow interval above an ordinary prime, and that prime is exactly the successor of the prime generating the incoming switch.

These hosts are logarithmically sparse. If `N_1(X)` counts sufficiently late nonzero-fringe switches whose outgoing event satisfies `xi<=X`, then

\[
\boxed{
N_1(X)\le\log_2X+O(\log\log X)=O(\log X).
}
\tag{16}
\]

Their event coordinates are multiplicatively lacunary: for the distinct hosts `xi_n` in increasing order,

\[
\boxed{
\liminf_{n\to\infty}\frac{\xi_{n+1}}{\xi_n}\ge2.
}
\tag{17}
\]

Since `p~p^+~xi`, the generating primes of the nonzero-fringe switches have the same asymptotic lacunarity.

Finally, the `RE-045` first-prime-scale fringe increments are absolutely summable on this host set. If

\[
\Delta\mathcal R_p
:=
\mathcal R_\beta(Z_+)-\mathcal R_\beta(Z_-)
\tag{18}
\]

at a nonzero-fringe switch, then `RE-045` gives uniformly on `J`

\[
|\Delta\mathcal R_p|
\ll_J\frac{\log p}{\sqrt p}.
\tag{19}
\]

Consequently

\[
\boxed{
\sum_{\chi_p=1}|\Delta\mathcal R_p|<\infty,
}
\tag{20}
\]

and, more quantitatively,

\[
\boxed{
\sum_{\substack{\chi_p=1\\p\ge X}}
|\Delta\mathcal R_p|
\ll_J\frac{\log X}{\sqrt X}.
}
\tag{21}
\]

Thus the binary fringe quantum isolated in `RE-045` cannot build an unbounded late-scale correction by accumulation. Any closing aggregate obstruction must use additional interruption data or a global common-source relation, not merely sum the surviving first-prime-scale bits.

## 1. Maximality supplies the curvature-clearance inequality

At the breakpoint `beta`, put

\[
c:=A_\beta(C)=Y^\beta(e^h-1)>0
\tag{22}
\]

and use the adaptive barrier from `RE-034`, `RE-040`, and `RE-043`,

\[
\tau(x):=\log(1+cx^{-\beta}),
\qquad
H(x):=\log\log x+\tau(x).
\tag{23}
\]

At `C`,

\[
H(Y)=\log\log Y+h.
\tag{24}
\]

For a CA state `E`, write

\[
F(E):=\log\rho(E)-\gamma
=\log\log(\log E)+h(E).
\tag{25}
\]

The immediate successor `D` satisfies

\[
h(D)\le\tau(\log D).
\tag{26}
\]

If `D` remains in the same positive block this is exactly the maximality of `C` for `A_\beta`; if `D` is the first state outside the block then `h(D)<=0<\tau(\log D)`. Hence

\[
F(D)\le H(Y+\Delta),
\qquad
F(C)=H(Y).
\tag{27}
\]

The physical CA support identity is

\[
F(D)-F(C)=\varepsilon_+(C)\Delta=g(\xi)\Delta,
\tag{28}
\]

so

\[
g(\xi)
\le
\frac{H(Y+\Delta)-H(Y)}{\Delta}.
\tag{29}
\]

At the selected state the barrier tangent is

\[
H'(Y)
=g(Y)-\frac{\beta a}{Y}
=g(Z).
\tag{30}
\]

`RE-040` gives the uniform small-height curvature control on the neighboring CA interval,

\[
-H''(x)
=(1+o_J(1))|g'(Y)|,
\tag{31}
\]

because consecutive CA neighbors have `Delta=O(log Y)`, `g'` is asymptotically constant on that scale, and `tau''=o_J(|g'|)`.

The exact tangent-minus-secant identity gives

\[
H'(Y)-
\frac{H(Y+\Delta)-H(Y)}{\Delta}
=
\frac1\Delta
\int_0^\Delta
(\Delta-u)(-H''(Y+u))\,du,
\tag{32}
\]

hence

\[
g(Z)-g(\xi)
\ge
\left(\frac12+o_J(1)\right)|g'(Y)|\Delta.
\tag{33}
\]

Now use the nonzero-fringe hypothesis. `RE-048` gives `0<xi-Z<1/2` and `Z~Y~p`, so the mean-value theorem yields

\[
g(Z)-g(\xi)
=(1+o_J(1))|g'(Y)|(\xi-Z).
\tag{34}
\]

Cancelling the common derivative scale between (33) and (34) proves (8). The conditionality matters: the present finding needs the `chi_p=1` half-unit window to identify the derivative scales without introducing a separate large-gap estimate.

The load-bearing point is that (29) uses **amplitude maximality**, not merely chamber membership. Abstract support geometry alone can place a selector arbitrarily near a support edge; an exposed Robin-amplitude state must also dominate its immediate physical successor, paying the tangent-secant curvature cost in (32).

## 2. The half-unit window forces the integer quotient to be two

Under `chi_p=1`, `RE-048` gives

\[
p^+\le Z<\xi\le\eta_{p^+,1}<p^++\frac12,
\tag{35}
\]

so (9) holds. Combining (8) with (9),

\[
\Delta
\le
(2+o_J(1))(\xi-Z)
<1+o_J(1).
\tag{36}
\]

The event representation of `RE-001` gives

\[
\Delta
=\sum_{(q,k)\text{ firing at }\xi}\log q
=\log Q,
\qquad
Q:=D/C\in\mathbf Z_{\ge2}.
\tag{37}
\]

Since `1<log3`, equation (36) eventually implies `Delta<log3`, so `Q=2`. Any tied event would have product quotient strictly larger than `2`, and any single base `q>=3` would contribute at least `log3`. Therefore the outgoing event is uniquely one exponent increment of the prime `2`, proving (11)--(12) without assuming the open Alaoglu--Erdos conjecture that all consecutive CA quotients are prime.

With `Delta=log2`, (8) gives

\[
\xi-Z\ge\frac{\log2}{2}-o_J(1).
\tag{38}
\]

Together with (35), this places `xi` in

\[
p^++\frac{\log2}{2}-o_J(1)
\le\xi<p^++\frac12,
\tag{39}
\]

which proves the floor-prime and fractional-part restriction (15). The limiting width of this admissible fractional window is

\[
\frac{1-\log2}{2}\approx0.1534.
\tag{40}
\]

No equidistribution statement for `\{eta_(2,j)\}` is assumed or claimed.

## 3. The fixed base-two ladder gives logarithmic host count

For the base-two layer `j`, use the exact notation from `RE-020`,

\[
S_{2,j}=2+2^2+\cdots+2^j=2^{j+1}-2.
\tag{41}
\]

The exact event equation gives

\[
\boxed{
S_{2,j}
\le
\frac{\eta_{2,j}\log\eta_{2,j}}{\log2}
\le
S_{2,j}+1.
}
\tag{42}
\]

If `eta_(2,j)<=X`, then

\[
2^{j+1}-2
\le
\frac{X\log X}{\log2},
\tag{43}
\]

so

\[
j\le\log_2X+O(\log\log X).
\tag{44}
\]

Each physical CA state has one immediate outgoing event and the rightmost fan enters a state at most once. Distinct nonzero-fringe switches therefore inject into distinct base-two layers, proving (16).

Equation (42) also gives

\[
\eta_{2,j}\log\eta_{2,j}
=(\log2)2^{j+1}(1+o(1)),
\tag{45}
\]

and hence

\[
\frac{\eta_{2,j+1}}{\eta_{2,j}}\longrightarrow2.
\tag{46}
\]

Any increasing subsequence of distinct base-two layers is at least as lacunary asymptotically, proving (17). Since the incoming first-layer switch geometry gives `p~Z~xi`, the same multiplicative separation holds for the corresponding generating primes.

This is much sharper than generic zero density of higher CA layers. The union of all higher-layer bases still has roughly square-root-scale complexity at event height `X`; nonzero fringe hosts have collapsed to one fixed-base ladder with only logarithmically many candidates below `X`.

## 4. Lacunarity makes the local fringe contribution absolutely summable

At a nonzero-fringe switch, `RE-045` gives

\[
\Delta\mathcal R_p
=
\frac{\log p}{\beta\sqrt p}
+o_J\!\left(\frac{\log p}{\sqrt p}\right).
\tag{47}
\]

Because `beta\in J` is bounded away from zero, for all sufficiently late hosts

\[
|\Delta\mathcal R_p|
\ll_J\frac{\log p}{\sqrt p}.
\tag{48}
\]

From (17), after discarding finitely many terms the host primes grow by a fixed ratio `r>1`; for example one may take any `r<2`. The function `(log x)/sqrt x` is eventually decreasing, and therefore the resulting geometric majorant gives

\[
\sum_{\chi_p=1}\frac{\log p}{\sqrt p}<\infty.
\tag{49}
\]

If the first host above `X` is `P>=X`, the same geometric estimate gives

\[
\sum_{\substack{\chi_p=1\\p\ge X}}
\frac{\log p}{\sqrt p}
\ll\frac{\log P}{\sqrt P}
\ll\frac{\log X}{\sqrt X},
\tag{50}
\]

where the final comparison uses the eventual decrease of `(log x)/sqrt x`. Equations (48)--(50) prove (20)--(21), including the `o_J` remainder because it is eventually dominated by the same summable majorant.

This closes one tempting continuation of `RE-045`: even if infinitely many nonzero bits exist, their individual-prime residual quanta cannot accumulate an unbounded tail. A viable aggregate contradiction must extract a different quantity from the exceptional interruption geometry or couple those sparse events to the full translated prime race.

## 5. Stress tests and boundary of the result

The finding does **not** prove that any nonzero fringe bit exists. If all sufficiently late adjacent first-layer switches have `chi_p=0`, the theorem is vacuous. Nor does the `O(log X)` host count contradict false RH: the current fan theory has no theorem requiring positive-density or even infinite fringe-bit occurrence.

The floor-prime condition (15) is a necessary host condition, not an assertion about the distribution of the fractional parts of `eta_(2,j)`. Proving that only finitely many such layers have prime floor, or that the extra predecessor-gap constraint inherited from `RE-045` is impossible infinitely often, would require new arithmetic input.

The summability statement concerns the **binary first-prime-scale component isolated in `RE-045`**. It does not say that every contribution created by a skipped state, a base-two layer transition, or the global nonlinear race is summable. Those quantities may live on different scales and have not been reduced to (47).

The argument does not assume every consecutive CA quotient is prime. It allows an arbitrary tied/multi-atom outgoing event until (36)--(37) force its total integer quotient to equal `2`. This is why the conclusion is stronger than merely invoking the prime/semiprime neighboring-CA theorem.

Finally, host sparsity is measured in physical event scale, not directly in threshold `b`. The fan can assign highly nonuniform threshold widths to the surviving hosts, so no threshold-capacity contradiction follows from (16) alone.

## 6. Prior-art boundary

Alaoglu--Erdos supplies the classical CA prime-exponent threshold structure and neighboring-transition quantization already anchored in `SOURCES.md`. Mantovanelli's August 2026 preprint gives the closest current prime-layer event-coordinate framework, and Zimov studies neighboring CA transition restrictions. The exact fixed-base event bracket (42) is already recorded in `RE-020`.

A targeted current search found the classical prime/semiprime consecutive-quotient discussion, the recent exact prime-layer workload, and recent Robin-counterexample transition work, but no result coupling an adaptive Robin-amplitude fringe switch to a tangent-secant curvature clearance that forces the outgoing quotient to equal `2`, nor the resulting floor-prime restriction or summable binary-fringe host set.

No new external theorem is load-bearing. The result combines `RE-040`'s strict adaptive-barrier concavity and local maximality, `RE-048`'s sub-half-unit support-edge window, `RE-001`'s exact event quantization, and `RE-020`'s fixed-base event bracket. `SOURCES.md` therefore requires no new dependency.

## Consequence

The exceptional currency isolated by `RE-046`--`RE-048` is no longer an amorphous mixture of skipped states, higher layers, and tied events. **Every nonzero fringe bit forces the entered CA state to exit through the deep base-two ladder, within less than half a physical unit of the next ordinary prime.** Such hosts are only logarithmically numerous, asymptotically doubling in event scale, and the associated `RE-045` binary residual quanta have finite total variation.

The next live target is correspondingly narrower. A closing argument can focus on the one-dimensional sequence `eta_(2,j)` and ask whether its prime/fractional hosts can carry any additional non-summable common-source statistic required by the false-RH fan. Merely accumulating the already-isolated binary fringe increments is now ruled out as a source of a divergent obstruction.