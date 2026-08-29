# WI-024 — a balanced span threshold at `m=515` improves the exact four-point bound

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED`. This is an unconditional refinement of WI-023 using only the same `sorry`-free Lean four-point certificate, the same Montgomery--Taylor Gram kernel, the exact trace--energy envelope from WI-011/WI-020, and the same shifted-block assembly. No new prime-side moment, no support beyond one, and no new computer-assisted gap certificate are introduced. The new point is that full recovery `D+P >= A_m` is not required for the best block length: balancing a short-span packing lower bound against the long-span pressure transfer at `m=515` gives a slightly larger global proportion than the full-recovery choice `m=513` from WI-023.

## 1. Statement

Retain the four-point constants

\[
\varepsilon=\frac{231}{100000},
\qquad
p=\frac1{2500},
\]

and the Montgomery--Taylor stability bridge

\[
S\ge H_{\rm MT}N+\mathcal D(M^\circ)-o(N),
\qquad
H_{\rm MT}=\frac32-\frac1{\sqrt2}\cot\frac1{\sqrt2}.
\]

For a block of

\[
m=515
\]

consecutive simple critical zeros, put

\[
E=\operatorname{tr}(G-I)^2,
\qquad
D=\operatorname{tr}\Psi(G),
\]

and let `P` be the nonnegative three-gap span pressure obtained by summing the Lean-proved four-point certificate over the `m-3=512` internal windows. As in WI-011/WI-023,

\[
E+P\ge A,
\qquad
A:=\varepsilon(m-3)=\frac{3696}{3125}=1.18272.
\tag{1}
\]

Define the exact rational constant

\[
\boxed{C:=\frac{1182717}{1000000}=1.182717.}
\tag{2}
\]

Then every limiting 515-point Montgomery--Taylor block satisfies

\[
\boxed{D+P>C.}
\tag{3}
\]

Consequently the same shifted-block assembly as WI-011 gives

\[
\boxed{
\liminf_{T\to\infty}\frac{N_0^s(T,2T)}{N(T,2T)}
\ge
\frac{515H_{\rm MT}-1536/2500}{515-C}
=
\frac{515000000H_{\rm MT}-614400}{513817283}.
}
\tag{4}
\]

A high-precision non-load-bearing evaluation is

\[
\boxed{0.6728529261926306156447555\ldots}.
\]

WI-023 gives

\[
0.6728529220565555601699279\ldots,
\]

so (4) is a strict unconditional improvement by about

\[
4.1361\times10^{-9}
\]

in proportion. The numerical gain is tiny; the structural point is that the optimum of this elementary span-packing refinement occurs after the point where the stronger local statement `D+P >= A_m` has already failed.

## 2. Exact pressure ledger and the chosen threshold

Write the normalized block span as

\[
Y=y_{515}-y_1.
\]

Exactly as in WI-021/WI-023, every gap occurs at least once in the sum of the 512 three-gap pressures, hence

\[
\boxed{P\ge pY.}
\tag{5}
\]

Choose

\[
a:=\frac{9227}{10000},
\qquad
B:=482,
\qquad
Y_0:=Ba=\frac{2223707}{5000}=444.7414,
\tag{6}
\]

and therefore

\[
P_0:=pY_0
=\frac{2223707}{12500000}.
\tag{7}
\]

The proof of (3) is a dichotomy at `Y_0`.

## 3. Long spans: pressure alone almost recovers the full local constant

Assume first

\[
Y\ge Y_0.
\]

Then `P >= P_0`. WI-020 gives

\[
D\ge\Phi_m(E),
\]

where

\[
\Phi_m(E)=
\begin{cases}
E,&0\le E\le m/(m-1),\\[1mm]
2\sqrt{\frac{m-1}{m}E}-1+\frac Em,&E\ge m/(m-1).
\end{cases}
\tag{8}
\]

and (1) gives `E+P >= A`.

For `0 <= P <= A`, the function

\[
f(P):=\Phi_m(A-P)+P
\tag{9}
\]

is nondecreasing, because `Phi_m` is 1-Lipschitz and nondecreasing. If `P>A`, then trivially `D+P>=P>A>C`. Hence it suffices to evaluate (9) at `P=P_0`.

Put

\[
E_0:=A-P_0
=\frac{12560293}{12500000}.
\tag{10}
\]

This lies strictly above the kink:

\[
E_0-\frac{515}{514}
=\frac{9245301}{3212500000}>0.
\tag{11}
\]

Thus the high branch of (8) applies. To prove

\[
\Phi_{515}(E_0)+P_0>C,
\tag{12}
\]

it is enough to square one positive rational comparison. Indeed

\[
R:=\frac{514}{515}E_0
=\frac{3227995301}{3218750000},
\]

while

\[
T:=C+1-\frac{E_0}{515}-P_0
=\frac{25786942579}{12875000000}.
\]

The exact difference is

\[
\boxed{
R-\left(\frac T2\right)^2
=\frac{624433356828759}{663062500000000000000}>0.
}
\tag{13}
\]

Hence `2 sqrt(R) > T`, which is exactly (12). Therefore every long-span block satisfies (3).

## 4. Short spans: 33 close pairs force enough Montgomery--Taylor energy

Now suppose

\[
Y<Y_0.
\]

Since `Y_0=482a`, the containing interval can be covered by `482` consecutive half-open subintervals of length `a`. Place the `515` ordered points into these bins. If their occupancies are `n_j`, then

\[
\sum_j\binom{n_j}{2}
\ge
\sum_{j:n_j>0}(n_j-1)
\ge
515-482
=33.
\tag{14}
\]

Thus at least `33` unordered pairs have separation strictly below `a`.

WI-022 proves that the Montgomery--Taylor kernel is positive and strictly decreasing on `[0,1]`. We now need the explicit rational lower bound

\[
\boxed{k_{\rm MT}(a)>\frac{403}{3000}.}
\tag{15}
\]

For auditability, this follows from the same elementary bounds already used in WI-023. Write

\[
z:=\pi(1-a)=\frac{773\pi}{10000}
\]

and

\[
B_0:=\sqrt2\,\pi\cot(1/\sqrt2).
\]

The exact kernel formula from WI-022 becomes

\[
k_{\rm MT}(a)
=
\frac{\cos z+B_0a\sin z}{2\pi^2a^2-1}.
\tag{16}
\]

Use

\[
\frac{333}{106}<\pi<\frac{355}{113},
\qquad
\sqrt2>\frac{140}{99},
\qquad
\cot(1/\sqrt2)>\frac{117}{100},
\tag{17}
\]

where the last inequality is the exact Taylor comparison recorded in WI-023. Put

\[
z_-:=\frac{773}{10000}\frac{333}{106},
\qquad
z_+:=\frac{773}{10000}\frac{355}{113}.
\]

Since `0<z<pi/2`, the alternating Taylor bounds and monotonicity give

\[
\cos z>1-\frac{z_+^2}{2},
\qquad
\sin z>z_- -\frac{z_-^3}{6}.
\tag{18}
\]

Also

\[
B_0>
\frac{140}{99}\frac{333}{106}\frac{117}{100},
\qquad
2\pi^2a^2-1
<2\left(\frac{355}{113}\right)^2a^2-1.
\tag{19}
\]

Substitution of (18)--(19) into (16) yields a fully rational lower enclosure `K_-`, and direct subtraction gives

\[
\boxed{
K_- -\frac{403}{3000}
=
\frac{2734466481690185147122807819}
{84081782117062340397600000000000}>0.
}
\tag{20}
\]

This proves (15) without floating point.

Therefore the 33 close pairs force

\[
E
=2\sum_{i<j}k_{\rm MT}(y_i-y_j)^2
>
66\left(\frac{403}{3000}\right)^2
=
\frac{1786499}{1500000}.
\tag{21}
\]

Set

\[
E_1:=\frac{1786499}{1500000}.
\]

Since `Phi_515` is increasing, it remains only to check

\[
\Phi_{515}(E_1)>C.
\tag{22}
\]

Again this reduces to one rational square. The exact comparison is

\[
\boxed{
\frac{514}{515}E_1
-
\frac14\left(C+1-\frac{E_1}{515}\right)^2
=
\frac{1393051160795711}{9548100000000000000}>0.
}
\tag{23}
\]

Hence (22) holds. Since `P>=0`, every short-span block also satisfies `D+P>C`, completing the proof of (3).

## 5. Global shifted-block assembly

The shifted-block counting from WI-011/WI-023 is unchanged. With `m=515`, every full block contributes its local defect/pressure lower bound divided by `515`, while the pressure tax is

\[
\frac{512}{515}\frac3{2500}N+o(N).
\]

Thus (3) gives

\[
\mathcal D(M^\circ)
\ge
\frac{C}{515}S
-
\frac{512}{515}\frac3{2500}N
-o(N).
\tag{24}
\]

Substituting (24) into the stability bridge and solving for `S/N` gives (4).

As in WI-021/WI-023, the finite-`T` passage is harmless. The short-span branch lives in the fixed compact interval `Y<Y_0`, where the Montgomery--Taylor Gram asymptotic is uniform for fixed `m=515`; the exact margins in (20) and (23) survive as `o(1)` perturbations. The long-span branch is controlled by the pressure ledger itself.

## 6. Exact comparison with WI-023

Let `R_515` denote the right side of (4), and let

\[
R_{513}
=
\frac{513H_{\rm MT}-153/250}{513-11781/10000}
\]

be the WI-023 bound. Cross multiplication reduces `R_515>R_513` to

\[
\frac{12321}{1000000}H_{\rm MT}
-
\frac{1799541}{250000000}>0.
\tag{25}
\]

A very coarse exact lower bound on `H_MT` suffices. Put `x=1/sqrt(2)`. Alternating Taylor bounds give

\[
\sin x>x-\frac{x^3}{6}=\frac{11}{12}x,
\]

and

\[
\cos x<1-\frac{x^2}{2}+\frac{x^4}{24}
=\frac{73}{96}.
\]

Therefore

\[
\tan x>
\frac{11/12}{73/96}x
=\frac{88}{73}x
>\frac65x,
\]

so

\[
x\cot x<\frac56,
\qquad
\boxed{H_{\rm MT}>\frac23.}
\tag{26}
\]

Using (26), the left side of (25) is strictly larger than

\[
\frac{12321}{1000000}\frac23
-
\frac{1799541}{250000000}
=
\boxed{\frac{253959}{250000000}>0.}
\tag{27}
\]

Thus the improvement over WI-023 is exact and does not depend on the displayed decimal evaluations.

## 7. What changed relative to WI-023

WI-023 chose `m=513` because a single packing threshold was strong enough to prove the full local recovery

\[
D+P\ge A_m.
\]

At `m=515`, that stronger statement is no longer obtained by the same one-scale occupancy argument. However, the global proportion depends on the ratio between the block length and the **actual certified local constant**, not on full recovery as a binary property.

The present choice balances two strict lower bounds:

\[
\boxed{
\text{short span}
\Longrightarrow
\text{33 close pairs}
\Longrightarrow
D>C,
}
\]

and

\[
\boxed{
\text{long span}
\Longrightarrow
P\ge P_0
\Longrightarrow
D+P>C.
}
\]

The resulting `C=A-3/10^6` is slightly smaller than the full four-point energy `A`, but the extra two rows of block capacity more than compensate in the final assembly. This identifies a small but genuine optimization degree of freedom that the full-recovery criterion of WI-023 leaves unused.

## 8. Prior-art and novelty audit

The load-bearing external ingredients are all already recorded in `SOURCES.md`:

- Alpöge--Furman for the unconditional Montgomery/Weil-form bridge and Montgomery--Taylor kernel;
- `teal-sea/zeta-lab` for the `sorry`-free four-point certificate with `epsilon=231/100000` and pressure `p=1/2500`;
- `tawanerguo-cn/zeta-simple-zeros` and `trmdy/zeta-simple-zeros-673137` for the trace--energy envelope and shifted block-frame assembly;
- WI-021--WI-023 for the exact pressure ledger, kernel monotonicity, and span-packing specialization.

A targeted current search for the exact decimal in (4), the rational local constant `1182717/1000000`, an `m=515` four-point block refinement, or the specific threshold `(B,a)=(482,9227/10000)` found no matching public statement. Absence of a search hit is not a priority claim.

Michael Devine's public `0.673399` preprint is numerically much stronger, but it uses several independent bandlimited profiles plus interval-certified transition inequalities and remains `NEEDS-AUDIT` in this line. It is therefore neither imported as established evidence nor contradicted by the present single-profile exact deduction.

## 9. Boundaries and falsification tests

- The gain is intentionally very small. It does not challenge WI-019's interval-certified `0.67361` obstruction for the collapsed single-profile Montgomery--Taylor interface.
- The result concerns only the simple-critical Gram contribution. It does not distinguish multiple critical-line zeros from screened off-line pairs and does not weaken WI-005--WI-007.
- No optimality is claimed for `m=515`, for the threshold `Y_0`, or for one-scale interval occupancy. A multiscale pair-count lower bound may improve the local constant or permit larger `m`.
- The decisive audit is finite and exact: verify the occupancy count (14), the rational kernel enclosure (20), the two square comparisons (13) and (23), and the final comparison (25)--(27).
- A clean formalization target is the local statement (3); the existing block-frame bridge can then substitute `C` at `m=515` directly.

## 10. Consequence for `weil_inertia`

WI-023 showed that realizability can recover the entire abstract trace--energy loss at one explicit block length. WI-024 shows that **full local recovery is not the correct optimization objective**: a slightly weaker local constant at a slightly longer block can give a stronger global theorem.

The next exact support-one optimization target is therefore the two-parameter lower-envelope problem

\[
C_m=
\sup_{Y_0,\,\mathcal P}
\min\{\,C_{\rm short}(m,Y_0,\mathcal P),\ C_{\rm long}(m,Y_0)\,\},
\]

where `mathcal P` denotes a rigorous one- or multiscale deterministic pair-packing bound for spans below `Y_0`. The final objective is not to maximize `C_m` in isolation but

\[
\frac{mH_{\rm MT}-3p(m-3)}{m-C_m}.
\]

This reframing remains entirely within Fourier support one and uses no new arithmetic input. It also supplies a concrete falsification target: if sharper deterministic packing cannot improve the quotient above (4), then this local-realizability subroute has reached its own finite-dimensional wall.