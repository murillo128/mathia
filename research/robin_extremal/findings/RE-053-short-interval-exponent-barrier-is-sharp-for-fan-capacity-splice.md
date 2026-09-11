# RE-053 — short-interval exponent barrier is sharp for the fan-capacity splice

**Status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + GENERALIZED-FIRST-LAYER-CONTROL + SHARP-SHORT-INTERVAL-BARRIER + BOUNDED-FAN-REALIZABILITY + NEAR-CRITICAL-BOUNDARY + PRIOR-ART-BOUNDED`. `RE-051` combines the genuine CA support chamber with a prime-in-short-interval exponent `theta` and proves polynomial fan complexity only when the hypothetical zero frontier satisfies `Theta>theta`. `RE-052` removes the additive half-unit defect from that argument, but leaves open whether more careful use of the same prime-gap capacity could push into `Theta<=theta`.

It cannot. The exponent condition is **sharp for this entire support-capacity/short-interval splice**. Fix

\[
\frac12<\theta<1,
\qquad
J=[b_0,b_1]\Subset(0,1/2),
\qquad
b_0>1-\theta,
\tag{1}
\]

and `c_0>0`. There are asymptotic synthetic blocks with exactly one positive-width exposed threshold state on all of `J` which simultaneously satisfy:

- the exact adaptive-amplitude breakpoint laws of `RE-038`--`RE-041` and the quantitative left-endpoint normalization `A_{b_0}=c_0`;
- the uniform small-positive-height regime `h log Y -> 0`;
- an exact strictly concave support polygon and exact adaptive selector equation;
- **exact first-layer CA mass/slope formulas** at both support boundaries for two increasing real generalized-prime labels `q_-<q_+`, namely

\[
\Delta Y=\log q,
\qquad
\Delta F=\log(1+q^{-1}),
\qquad
s(q)=\frac{\log(1+q^{-1})}{\log q};
\tag{2}
\]

- and nevertheless the two bounding labels obey

\[
\boxed{
q_+-q_-
=
\bigl(c_0(b_1-b_0)+o(1)\bigr)
T^{1-b_0}\log T
=o(T^\theta).
}
\tag{3}
\]

Thus a one-cell fan is already compatible with a worst-case gap ceiling of exponent `theta` whenever `b_0>1-theta`. The failure of the `RE-051` partition argument at `b_1+theta-1>=0` is not a removable bookkeeping loss: below the frontier `Theta>theta`, the local CA-style geometry itself admits matched controls whose whole threshold interval fits between two first-layer events separated by less than `T^theta`.

The control can also be embedded into an increasing real prime-like sequence with counting function `Pi_Q(x)~x/log x` and all sufficiently large gaps `o(x^theta)`. Hence adding prime-number-theorem density to the same metric gap input does not repair the obstruction. What remains unmatched is the genuinely ordinary-prime common source: the labels are real rather than the actual primes, and the construction does not require the same labels to generate the standard/reciprocal prime races of `RE-040` across the whole system.

In particular, if RH is false with

\[
\frac12<\Theta\le\theta,
\tag{4}
\]

then every admissible compact interval `J subset (1-Theta,1/2)` has `b_0>1-Theta>=1-theta`, so the control applies. Therefore no argument whose arithmetic input has been compressed to **support geometry + first-layer event formulas + a prime-gap exponent `theta` + PNT-scale density** can extend `RE-051` into that chamber. With the currently anchored `theta=0.52`, the band `1/2<Theta<=0.52` genuinely requires a different source-sensitive input, not another rearrangement of the same capacity inequality.

## 1. An exact generalized-first-layer transition can be solved from one breakpoint

The key strengthening over `RE-041` is that the synthetic support atoms need not keep free masses and slopes. They can be forced to obey the exact first-layer CA formulas (2) for real labels.

Suppose a synthetic state has intrinsic coordinate `Y`, positive excess `R`, and

\[
F(Y,R):=\log\log Y+\log(1+R),
\tag{5}
\]

with

\[
R\log Y\longrightarrow0.
\tag{6}
\]

Fix a breakpoint exponent `beta` in a compact subset of `(0,1/2)`. For a proposed intrinsic jump `d>0`, put

\[
Y_d:=Y+d,
\qquad
R_d:=R\left(\frac{Y}{Y+d}\right)^\beta,
\tag{7}
\]

so the adaptive amplitudes of the two states tie exactly at `b=beta`:

\[
R_dY_d^\beta=RY^\beta.
\tag{8}
\]

Define

\[
D_{Y,R,\beta}(d)
:=
F(Y+d,R_d)-F(Y,R).
\tag{9}
\]

We choose `d` by the exact equation

\[
\boxed{
D_{Y,R,\beta}(d)
=
\log(1+e^{-d}).
}
\tag{10}
\]

For all sufficiently large `Y`, equation (10) has a unique solution and

\[
\boxed{d=\log Y+o(1).}
\tag{11}
\]

Indeed,

\[
\frac{d}{dd}D_{Y,R,\beta}(d)
=
\frac1{(Y+d)\log(Y+d)}
-
\frac{\beta}{Y+d}
\frac{R_d}{1+R_d}.
\tag{12}
\]

Condition (6) makes this derivative positive uniformly for `d=log Y+O(1)`, whereas the derivative of `log(1+e^{-d})` is negative. Thus the difference of the two sides of (10) is strictly increasing there. For any fixed `C>0`, uniformly in `beta`,

\[
D_{Y,R,\beta}(\log Y\pm C)
=\frac{1+o(1)}Y,
\tag{13}
\]

while

\[
\log(1+e^{-(\log Y-C)})
=\frac{e^C+o(1)}Y,
\qquad
\log(1+e^{-(\log Y+C)})
=\frac{e^{-C}+o(1)}Y.
\tag{14}
\]

Taking, say, `C=1` brackets one unique root. At that root (13) and (10) give `e^{-d}=(1+o(1))/Y`, which sharpens the bracket to (11).

Now set

\[
q:=e^d.
\tag{15}
\]

Then `d=log q`, and (10) becomes exactly

\[
F(Y_d,R_d)-F(Y,R)=\log(1+q^{-1}).
\tag{16}
\]

Consequently the secant slope of this transition is

\[
\boxed{
\frac{F(Y_d,R_d)-F(Y,R)}{Y_d-Y}
=
\frac{\log(1+q^{-1})}{\log q}.
}
\tag{17}
\]

These are precisely the first-layer CA jump-mass and supporting-slope formulas, except that `q` is allowed to be a positive real label rather than an ordinary prime. No approximation enters (16)--(17).

## 2. Two exact first-layer transitions support one state across the whole threshold interval

Start at

\[
Y_0=T,
\qquad
R_0=c_0T^{-b_0}.
\tag{18}
\]

Apply the transition construction of Section 1 first with `beta=b_0`, obtaining `(Y_1,R_1,q_-)`, and then from `(Y_1,R_1)` with `beta=b_1`, obtaining `(Y_2,R_2,q_+)`. By construction,

\[
R_1
=R_0\left(\frac{Y_0}{Y_1}\right)^{b_0}
=c_0Y_1^{-b_0},
\tag{19}
\]

and

\[
R_2
=R_1\left(\frac{Y_1}{Y_2}\right)^{b_1}.
\tag{20}
\]

For

\[
A_b(i):=Y_i^bR_i,
\tag{21}
\]

the adjacent score differences are exactly

\[
\log A_b(1)-\log A_b(0)
=(b-b_0)\log\frac{Y_1}{Y_0},
\tag{22}
\]

\[
\log A_b(2)-\log A_b(1)
=(b-b_1)\log\frac{Y_2}{Y_1}.
\tag{23}
\]

Hence state `1` is the unique maximizer for every `b in (b_0,b_1)`, with only endpoint guard ties. There is therefore **one positive-width threshold cell carrying all of `J`**. Moreover

\[
A_{b_0}(1)=c_0,
\qquad
A_b(1)=c_0Y_1^{b-b_0}
\quad(b\in J),
\tag{24}
\]

so the same quantitative inheritance used in `RE-038`--`RE-040` is preserved exactly.

Equations (11), (19), and (20) give

\[
Y_i=T+O(\log T),
\qquad
R_i=(c_0+o(1))T^{-b_0},
\tag{25}
\]

and therefore

\[
\boxed{
\log(1+R_i)\log Y_i\longrightarrow0.
}
\tag{26}
\]

Thus the construction lives in the same small-height regime as the physical adaptive fan.

Let

\[
F_i:=F(Y_i,R_i),
\qquad
s_1:=\frac{F_1-F_0}{Y_1-Y_0},
\qquad
s_2:=\frac{F_2-F_1}{Y_2-Y_1}.
\tag{27}
\]

By (17), these are not free synthetic slopes:

\[
\boxed{
s_1=\frac{\log(1+q_-^{-1})}{\log q_-},
\qquad
s_2=\frac{\log(1+q_+^{-1})}{\log q_+}.}
\tag{28}
\]

At each breakpoint the corresponding adaptive barrier

\[
H_\beta(x)
=
\log\log x+\log(1+c x^{-\beta})
\tag{29}
\]

has the two adjacent states as endpoints. On intervals of length `log T+o(1)`, its positive second-derivative correction is smaller than the negative curvature of `log log x` by the factor `O(R_i log T)=o(1)`. Hence the barriers are strictly concave, exactly as in `RE-041`. For the middle state, with

\[
a_1:=\frac{R_1}{1+R_1},
\qquad
t_1(b):=g(Y_1)-\frac{ba_1}{Y_1},
\qquad
g(x)=\frac1{x\log x},
\tag{30}
\]

we obtain

\[
\boxed{
s_1>t_1(b_0)>t_1(b_1)>s_2.}
\tag{31}
\]

Define the exact first-layer event coordinate of a real label `q>1` by

\[
g(\eta(q))
=
\frac{\log(1+q^{-1})}{\log q}.
\tag{32}
\]

The right side is strictly decreasing in `q`, so `eta(q)` is strictly increasing. From (28)--(31), for every `b in J^\circ`, the adaptive selector

\[
g(Z_1(b))=t_1(b)
\tag{33}
\]

satisfies

\[
\boxed{
\eta(q_-)<Z_1(b)<\eta(q_+).}
\tag{34}
\]

Thus the single threshold state is supported between **two exact generalized first-layer CA events**, not merely between free abstract atoms.

## 3. The bounding generalized-prime gap has the exact fan scale

The concavity estimate used above also quantifies the endpoint slack. Since

\[
\sup_{x\asymp T}|H_\beta''(x)|
=O\!\left(\frac1{T^2\log T}\right)
\tag{35}
\]

and both transition lengths are `log T+o(1)`, the secant-tangent errors satisfy

\[
s_1-t_1(b_0)=O(T^{-2}),
\qquad
t_1(b_1)-s_2=O(T^{-2}).
\tag{36}
\]

The middle difference is exact:

\[
t_1(b_0)-t_1(b_1)
=(b_1-b_0)\frac{a_1}{Y_1}.
\tag{37}
\]

Because (19) gives

\[
a_1=(c_0+o(1))T^{-b_0},
\tag{38}
\]

and `b_0<1`, the term in (37) dominates the two `O(T^-2)` errors. Therefore

\[
\boxed{
s_1-s_2
=
\bigl(b_1-b_0+o(1)\bigr)
\frac{a_1}{Y_1}.}
\tag{39}
\]

For

\[
m(q):=\frac{\log(1+q^{-1})}{\log q},
\tag{40}
\]

we have

\[
m'(q)
=-\frac{1+o(1)}{q^2\log q}.
\tag{41}
\]

Equation (11) gives `q_-/T->1` and `q_+/T->1`. Applying the mean-value theorem to `m(q_-)-m(q_+)=s_1-s_2` and using (38)--(41) yields

\[
\boxed{
q_+-q_-
=
\bigl(c_0(b_1-b_0)+o(1)\bigr)
T^{1-b_0}\log T.}
\tag{42}
\]

This proves the first equality in (3).

The associated first-layer event coordinate has the elementary expansion

\[
\eta(q)=q+\frac12+O\!\left(\frac1{\log q}\right),
\tag{43}
\]

so the genuine support-chamber width in selector space has the same leading order:

\[
\eta(q_+)-\eta(q_-)
=
\bigl(c_0(b_1-b_0)+o(1)\bigr)
T^{1-b_0}\log T.
\tag{44}
\]

If `b_0>1-theta`, then `1-b_0<theta`, and (42)--(44) are `o(T^theta)`. Hence a prime-in-short-interval theorem that supplies only a worst-case gap ceiling `O(T^theta)` has **strictly more physical room than this entire one-state threshold fan requires**.

This is the sharpness point. In `RE-051`, the useful inequality is `b_1<1-theta`, because then every physical support chamber is too short to carry a fixed threshold width and the fan must fragment. On the opposite side, already the stronger condition `b_0>1-theta` admits a one-cell matched control whose complete generalized-first-layer chamber lies below the allowed gap scale. For the false-RH application with `Theta<=theta`, every compact admissible `J` lies strictly on this realizable side.

## 4. PNT-scale density and a global `theta` gap ceiling can be matched as well

The control is not exploiting a globally sparse label set. One can embed infinitely many such blocks into an increasing real sequence `Q` with

\[
\boxed{
\Pi_Q(x):=\#\{q\in Q:q\le x\}
\sim\frac{x}{\log x}}
\tag{45}
\]

and

\[
\boxed{
q_{n+1}-q_n=o(q_n^\theta).}
\tag{46}
\]

A direct construction suffices. Start from the real mesh

\[
r_n:=n\log n,
\tag{47}
\]

for which the counting function is asymptotic to `x/log x` and consecutive gaps are `O(log x)`. Choose the block scales `T_k` so rapidly increasing that the intervals used below are disjoint and each earlier modification is negligible at the next scale.

At scale `T_k`, perform the one-cell construction above and obtain its two boundary labels `q_{k,-}<q_{k,+}`. Delete all baseline mesh points in `(q_{k,-},q_{k,+})` and insert the two boundary labels. By (42), the number of deleted points is

\[
O\!\left(
\frac{q_{k,+}-q_{k,-}}{\log T_k}+1
\right)
=
O(T_k^{1-b_0}),
\tag{48}
\]

which is

\[
o\!\left(\frac{T_k}{\log T_k}\right).
\tag{49}
\]

Taking, for example, `T_{k+1}>=T_k^2` makes the cumulative perturbation of the counting function negligible, proving (45). Outside the modified intervals the gaps remain `O(log x)`, while inside each modified interval the only enlarged gap is (42), which is `o(T_k^theta)`. This proves (46).

Associate to every real label `q in Q` its exact first-layer event coordinate by (32). Since `eta(q)` is increasing, deleting every label strictly between `q_{k,-}` and `q_{k,+}` also makes their two event coordinates consecutive in the generalized first-layer mesh. Thus the local support chamber (34) survives the embedding unchanged.

This global extension is only a **metric/density control**. It is not claimed to be the ordinary primes and is not claimed to generate a single global zeta function whose standard and reciprocal prime races reproduce `RE-040`. Its role is narrower: neither PNT-scale density nor a uniform short-interval exponent repairs the local capacity obstruction once the labels are allowed the generalized-prime freedom already exposed by the synthetic-support program.

## 5. Consequence for the false-RH chambers

Let `theta` denote any exponent for which one knows that every sufficiently large interval of length `x^theta` contains an ordinary prime. `RE-051` proves a genuine arithmetic consequence when

\[
\Theta>\theta,
\tag{50}
\]

because one can choose

\[
J\Subset(1-\Theta,1-\theta)
\tag{51}
\]

and force every threshold cell to vanish polynomially.

Suppose instead

\[
\frac12<\Theta\le\theta.
\tag{52}
\]

For every admissible compact fan interval

\[
J=[b_0,b_1]\Subset(1-\Theta,1/2),
\tag{53}
\]

we necessarily have

\[
b_0>1-\Theta\ge1-\theta.
\tag{54}
\]

The inequality is strict at the left endpoint, so `theta>1-b_0`; Sections 1--4 apply. Thus the entire admissible threshold interval can be carried by one state while the exact generalized first-layer boundary gap remains `o(T^theta)`.

Therefore the frontier in `RE-051` is structural for its present information set:

\[
\boxed{
\text{support capacity}
+
\text{first-layer metric law}
+
\text{gap exponent }\theta
\not\Longrightarrow
\text{fan growth when }\Theta\le\theta.
}
\tag{55}
\]

The same conclusion survives adding PNT-scale label density. In particular, using the currently anchored unconditional exponent `theta=0.52`, no refinement that only rearranges these ingredients can reach the near-critical band

\[
\frac12<\Theta\le0.52.
\tag{56}
\]

A route through that band must spend information absent from the control: actual-prime discreteness together with the full CA state accumulation, a finer distribution theorem than a worst-case `x^theta` gap ceiling, or the fact that the **same ordinary primes** simultaneously generate the support events and the standard/reciprocal race coordinates in `RE-040`.

## 6. Stress tests and exact evidence boundary

The real labels `q` in the control are not asserted to be integer primes. The result therefore does not construct a Robin counterexample, a colossally abundant integer, or a model of the Riemann zeta function. It also does not refute `RE-051` or `RE-052`: those are statements about the genuine prime source, and `RE-051` operates precisely on the opposite parameter side `b_1<1-theta`.

What is matched exactly is stronger than the free support geometry of `RE-041`. At the two active boundaries, the intrinsic state jump, abundance gain, support slope, and event coordinate all arise from one generalized first-layer label through

\[
\Delta Y=\log q,
\qquad
\Delta F=\log(1+q^{-1}),
\qquad
s=\frac{\Delta F}{\Delta Y},
\qquad
g(\eta(q))=s.
\tag{57}
\]

Thus replacing the free abstract atoms by first-layer-form atoms still does not make a `theta`-scale gap theorem obstruct a bounded fan on the realizable side `b_0>1-theta`.

The control does **not** reproduce the common-source prime races of `RE-040`, integer primality, higher-layer arithmetic, or a global Euler product. Those omissions define rather than weaken the conclusion: any proposed improvement of `RE-051` must identify which of those source-specific data it uses. It cannot be justified from threshold capacity, first-layer formulas, and the same short-interval exponent alone.

The logarithmic factor in (42) also makes the exact boundary visible. At `b_0=1-theta`, the one-cell generalized gap has scale `T^theta log T`, so the present control no longer fits an `O(T^theta)` gap ceiling. In the false-RH application this equality causes no ambiguity: admissible `J` has the strict inequality `b_0>1-Theta`, so when `Theta=theta` the control lies strictly below the boundary and still applies.

## 7. Prior-art boundary and research consequence

Alaoglu--Erdos supplies the classical CA first-layer mass/slope formulas; Musin bounds the convex-envelope novelty; Mantovanelli is the nearest current prime-layer event representation; and Runbo Li supplies the `0.52` short-interval input used by `RE-051`. All are already anchored in `SOURCES.md`. Generalized-prime and prime-like sequences are classical objects, and no novelty is claimed for the elementary real mesh (47) or for preserving PNT-scale counting after sparse sublinear deletions.

A targeted current search of Robin/CA counterexamples, consecutive CA transitions, short prime intervals, prime-gap restrictions, convex-envelope extremizers, and the 2026 prime-layer workload found no source identifying the `Theta>theta` frontier as a **sharp matched-control boundary for an adaptive Robin threshold fan**, nor a construction imposing the exact local first-layer formulas (57) while retaining a one-cell fan below the same gap exponent. No new external theorem is load-bearing, so `SOURCES.md` requires no addition.

The line-specific result is negative but decisive. `RE-052` shows that every genuine fan cell has a proportional ordinary-prime-gap cost; the present finding shows exactly how far that currency can be spent. A worst-case gap exponent can force fan complexity only when the zero frontier outruns that exponent. In the complementary chamber, even exact generalized first-layer quantization admits bounded complexity. The next useful theorem must therefore couple fan complexity to information that generalized first-layer labels cannot fake—most plausibly the ordinary-prime common-source race, higher-layer/integer compatibility, or a distributional statistic of the selected gaps stronger than their maximum allowed size.