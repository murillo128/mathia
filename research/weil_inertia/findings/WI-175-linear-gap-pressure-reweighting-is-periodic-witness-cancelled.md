# WI-175 — linear gap-pressure reweighting is cancelled by the period-33 witness

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + ROUTE-SPECIFIC-BARRIER + NO-NOVELTY-CLAIM`. WI-026 left changing the local pressure coefficients as a possible escape because its displayed calculation used the uniform three-gap-span pressure at `p=1/2500`. That escape is now closed for the entire class of nonnegative **linear gap pressures** whenever the proof keeps the same single Montgomery--Taylor Gram defect and the same scalar shifted-block bookkeeping. The period-33 witness averages every relative gap position to the same mean, so the complete pressure vector collapses to its total coefficient and cancels from the witness comparison exactly.

No unconditional simple-critical-zero proportion changes in this finding. The conclusion is a barrier on a proof architecture, not a statement about zeta-zero configurations.

## 1. Statement

Let `m>=2` and let an ordered `m`-point block have consecutive gaps

\[
g_1,\ldots,g_{m-1}\ge0.
\]

Keep the Montgomery--Taylor single-profile Gram defect `D(G)=tr Psi(G)` used in WI-011--WI-026. Replace the special WI-026 span pressure by an arbitrary fixed nonnegative linear pressure

\[
P_\alpha(g):=\sum_{j=1}^{m-1}\alpha_j g_j,
\qquad
\alpha_j\ge0,
\qquad
A:=\sum_{j=1}^{m-1}\alpha_j.
\tag{1}
\]

Suppose a universal local theorem gives

\[
\boxed{D(G)+P_\alpha(g)\ge C}
\tag{2}
\]

for every ordered Montgomery--Taylor translation Gram block, and suppose the global shifted-block assembly uses exactly the scalar accounting

\[
\boxed{
R(C,A)
=\frac{mH_{\rm MT}-A}{m-C}.
}
\tag{3}
\]

Equation (3) is the natural position-weighted version of WI-026's assembly: only the total local gap coefficient `A` survives the complete shift average. The claim here is explicitly conditional on this bookkeeping identity; a genuinely different global assembly is outside the theorem.

Then every nontrivial instance of (2)--(3) satisfies

\[
\boxed{R(C,A)<\frac{673604}{10^6}=0.673604.}
\tag{4}
\]

Thus **retuning or redistributing a nonnegative linear gap pressure cannot evade the WI-026 period-33 ceiling if the source observable and scalar shifted-block assembly are otherwise unchanged.**

## 2. Exact period-33 input

Use the same interval-certified periodic Montgomery--Taylor configuration from WI-019/WI-026. Its retained density is

\[
r=\frac{67361}{100000},
\tag{5}
\]

and its full directed pair energy per atom obeys

\[
d<d_*:=
\frac{1637}{10^6}
+
\frac{45379580714321}{74507812500000000000}.
\tag{6}
\]

WI-026 also records

\[
H_{\rm MT}<H_*:=\frac{672500704}{10^9}
\tag{7}
\]

and the exact positive witness margin

\[
\delta:=r(1-d_*)-H_*
=
\frac{46091743024440123119}
{7450781250000000000000000}
>\frac6{10^6}.
\tag{8}
\]

Nothing numerical beyond these already-certified inputs is required below.

## 3. Phase averaging forgets the pressure shape exactly

Cut the infinite period-33 configuration into an `m`-point block at each of its `33` starting phases. Write `D_a` and `P_{\alpha,a}` for the resulting defect and pressure.

WI-026's nonnegative-energy argument is unchanged and gives

\[
\frac1{33}\sum_{a=1}^{33}D_a<md_*.
\tag{9}
\]

For the pressure, fix a relative gap position `j`. As the starting phase `a` runs through all `33` values, that relative gap runs once through every gap of the periodic configuration. Since one period has length `33/r`, its mean gap is exactly `1/r`. Therefore

\[
\frac1{33}\sum_{a=1}^{33}g_{a+j-1}=\frac1r
\tag{10}
\]

for every `j`, with indices understood periodically. By linearity,

\[
\boxed{
\frac1{33}\sum_{a=1}^{33}P_{\alpha,a}
=\frac1r\sum_{j=1}^{m-1}\alpha_j
=\frac Ar.
}
\tag{11}
\]

Consequently at least one phase cut has

\[
D_a+P_{\alpha,a}<md_*+\frac Ar.
\tag{12}
\]

Any universal constant in (2) must hold on this cut, hence

\[
\boxed{C<md_*+\frac Ar.}
\tag{13}
\]

The individual coefficients `alpha_j` have disappeared completely. The witness sees only their total mass `A`.

## 4. The global pressure tax cancels the local pressure credit

If `mH_MT-A<=0`, (3) cannot yield a positive lower proportion, so it is irrelevant to an improvement. In the nontrivial branch put

\[
a:=\frac Am,
\qquad
0\le a<H_{\rm MT}<H_*.
\tag{14}
\]

Equation (8) implies

\[
H_*<r(1-d_*),
\]

so

\[
1-d_*-\frac ar>0.
\tag{15}
\]

In particular, the upper bound in (13) is strictly below `m`. Since (3) is increasing in `C` when its numerator and denominator are positive, (7) and (13) give

\[
R(C,A)
<
U(a):=
\frac{H_*-a}{1-d_*-a/r}.
\tag{16}
\]

Now subtract from the witness density. The entire pressure contribution cancels algebraically:

\[
\begin{aligned}
r-U(a)
&=
\frac{r(1-d_*-a/r)-(H_*-a)}
{1-d_*-a/r}\\
&=
\boxed{
\frac{r(1-d_*)-H_*}{1-d_*-a/r}
}
=
\frac{\delta}{1-d_*-a/r}.
\end{aligned}
\tag{17}
\]

The denominator in (17) is positive and strictly below `1`. Therefore

\[
r-U(a)>\delta>\frac6{10^6}.
\tag{18}
\]

With `r=0.673610`, equations (16)--(18) imply

\[
R(C,A)<0.673610-0.000006=\boxed{0.673604},
\]

which proves (4). The bound is uniform in `m`, in every coefficient vector `alpha`, and in the strength or proof method of the universal local constant `C`.

## 5. What this closes, and what it does not

WI-026 proved the same ceiling for its particular summed three-gap-span pressure and explicitly left **changing local pressure coefficients** outside scope. WI-174 then showed that squeezing the fixed `p=2500` four-point constant has very little theorem-level headroom. The calculation above closes the intervening idea of keeping the same scalar architecture but merely redistributing or retuning a fixed nonnegative linear gap tax: phase averaging turns every such pressure into `A/r`, while the global numerator spends exactly the same `A`.

This does **not** close pressure as a concept. The proof can be escaped by changing a load-bearing interface: a source-dependent or nonlinear pressure whose periodic mean is not determined solely by the same scalar tax; a global Fenchel/Bellman or geometry-aware assembly not reducible to (3); a different window/profile or multiple independent profiles; a source observable that excludes the period-33 configuration; the uncollapsed exceptional indefinite block; or genuinely new arithmetic information. In particular, the public `trmdy/zeta-simple-zeros-673137` construction changes the window/profile as well as the position-weighted local inequality, so it is not an instance of this barrier.

## 6. Prior-art and novelty audit

The phase-average/coboundary philosophy is classical, and no priority is claimed for periodic-orbit cancellation. The closest source-specific prior art already recorded in `SOURCES.md` is `teal-sea/zeta-lab/hunts/family_wall`, where a pressure-cancelling witness bounds the different parametric `n_point_bound` family; WI-013 independently audited a conservative exact version of that obstruction. WI-014 likewise uses vanishing periodic mean to obstruct a Bellman retuning.

A targeted audit of the current local corpus and the recent public pressure-family/position-weighted work found the ingredients separately but not an established statement of (11)--(18) for **arbitrary nonnegative position weights in the WI-026 single-profile `D+P` shifted-block scalar assembly**. This absence is not a novelty or priority claim. The durable contribution here is the exact closure of the coefficient-reweighting escape explicitly left open by WI-026.

## 7. Consequence for the live source-constrained program

The accepted `CLUE-kernel-constrained-positive-cover-escape` should no longer treat pressure-vector tuning by itself as a materially different architecture. Within a single MT Gram and scalar shift-averaged deduction, every fixed nonnegative linear pressure is compressed to one number `A` and is exactly neutralized by the period-33 density comparison.

A material continuation must therefore make the periodic witness pay for information that is **not** represented by the same scalar `A`: changed source profile, genuinely joint source-placement information, a nonlinear/source-conditioned budget, an independent observable, or coupling to the exceptional block. This sharpens the clue without resolving its broader source-specific question.