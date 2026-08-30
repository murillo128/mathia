# WI-036 — multiscale span packing recovers the full four-point constant at `m=515`

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED`. This is a strict unconditional refinement of WI-024 within Mathia's established four-point evidence chain. It uses only the same `sorry`-free Lean four-point certificate, the same Montgomery--Taylor Gram kernel, the exact trace--energy envelope, and the same shifted-block assembly. No new prime-side moment, no Fourier support beyond one, and no new computer-assisted gap certificate are introduced. The new observation is that the short-span occupancy argument should be charged at several nested distance scales rather than collapsing all forced close pairs to one threshold. That recovers the **full** local four-point constant at block length `m=515`, where the one-scale argument of WI-024 lost `3/10^6`.

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

consecutive simple critical zeros, write

\[
E=\operatorname{tr}(G-I)^2,
\qquad
D=\operatorname{tr}\Psi(G),
\]

and let `P` be the nonnegative three-gap span pressure obtained by summing the Lean-proved four-point certificate over the `m-3=512` internal windows. As in WI-011/WI-023/WI-024,

\[
E+P\ge A,
\qquad
A:=\varepsilon(m-3)
=\frac{3696}{3125}
=1.18272,
\tag{1}
\]

and, if `Y=y_{515}-y_1` is the normalized block span,

\[
P\ge pY.
\tag{2}
\]

The new local conclusion is

\[
\boxed{D+P\ge A.}
\tag{3}
\]

Consequently the shifted-block assembly gives

\[
\boxed{
\liminf_{T\to\infty}
\frac{N_0^s(T,2T)}{N(T,2T)}
\ge
\frac{515H_{\rm MT}-1536/2500}{515-3696/3125}
=
\frac{1609375H_{\rm MT}-1920}{1605679}.
}
\tag{4}
\]

A high-precision non-load-bearing evaluation is

\[
\boxed{0.6728529301211843197511878001\ldots}.
\]

WI-024 gave

\[
0.6728529261926306156447555546\ldots,
\]

so (4) is a strict improvement by

\[
3.9285537041064322\times10^{-9}
\]

in proportion. The numerical gain is tiny; the structural gain is that a purely combinatorial multiscale packing argument removes the last `3/10^6` local loss at `m=515` without strengthening the four-point certificate itself.

## 2. Nested occupancy lemma

Let

\[
Y_0:=460.
\tag{5}
\]

Assume first that `Y<Y_0`. For any integer `B<=515`, cover

\[
[y_1,y_1+Y_0)
\]

by `B` half-open intervals of equal length

\[
a_B=\frac{Y_0}{B}.
\]

If their occupancies are `n_1,...,n_B`, then

\[
\sum_{j=1}^B\binom{n_j}{2}
\ge
\sum_{j:n_j>0}(n_j-1)
\ge
515-B.
\tag{6}
\]

Hence at least `515-B` unordered pairs have separation strictly below `a_B`.

Use the nested choices

\[
B\in\{510,500,490,480,470,460\}.
\tag{7}
\]

The corresponding thresholds and cumulative forced-pair counts are

\[
\begin{array}{c|c|c|c}
B&a_B&L_B:=515-B&\text{new pairs charged at this scale}\\ \hline
510&46/51&5&5\\
500&23/25&15&10\\
490&46/49&25&10\\
480&23/24&35&10\\
470&46/47&45&10\\
460&1&55&10
\end{array}
\tag{8}
\]

To justify the incremental charging rigorously, sort all unordered pair distances as

\[
d_1\le d_2\le\cdots.
\]

Equation (6) says `d_{L_B}<a_B`. Therefore the pairs with indices

\[
L_{B^-}<r\le L_B
\]

may all be charged at the current threshold `a_B`. No pair is double-counted. This is the exact gain over WI-024, which used only one occupancy scale and charged every forced pair at one common worst-case distance.

## 3. Exact rational lower bounds for the Montgomery--Taylor kernel

WI-022 proves that the Montgomery--Taylor kernel is positive and strictly decreasing on `[0,1]`. For `0<a<=1`, WI-024 records the exact representation

\[
k_{\rm MT}(a)
=
\frac{\cos z+B_0a\sin z}{2\pi^2a^2-1},
\qquad
z=\pi(1-a),
\qquad
B_0=\sqrt2\,\pi\cot(1/\sqrt2).
\tag{9}
\]

The same elementary rational enclosures used in WI-024 suffice here:

\[
\frac{333}{106}<\pi<\frac{355}{113},
\qquad
\sqrt2>\frac{140}{99},
\qquad
\cot(1/\sqrt2)>\frac{117}{100}.
\tag{10}
\]

For each `a<1`, put

\[
z_-=(1-a)\frac{333}{106},
\qquad
z_+=(1-a)\frac{355}{113}.
\]

Since all six thresholds lie in `[46/51,1]`, one has `0<=z<pi/2`. Thus

\[
\cos z>1-\frac{z_+^2}{2},
\qquad
\sin z>z_--\frac{z_-^3}{6},
\tag{11}
\]

and therefore

\[
k_{\rm MT}(a)>
K_-(a):=
\frac{
1-z_+^2/2+
(140/99)(333/106)(117/100)\,a\,(z_--z_-^3/6)
}{
2(355/113)^2a^2-1
}.
\tag{12}
\]

Every quantity on the right is rational. Direct exact subtraction gives the deliberately coarse bounds

\[
\begin{aligned}
k_{\rm MT}(46/51)&>\frac3{20},\\
k_{\rm MT}(23/25)&>\frac{27}{200},\\
k_{\rm MT}(46/49)&>\frac{23}{200},\\
k_{\rm MT}(23/24)&>\frac{19}{200},\\
k_{\rm MT}(46/47)&>\frac{37}{500}.
\end{aligned}
\tag{13}
\]

For auditability, the exact positive margins `K_-(a)-q` in the order displayed are

\[
\frac{7656663509069597497}{1003605668583187717520},
\quad
\frac{642243747081293737}{272003042970951875000},
\quad
\frac{10468974718490769687}{5986064468088912561200},
\]

\[
\frac{469958758452013821}{559842707625279795200},
\quad
\frac{133446699388556873877}{193698369559684633402000}.
\tag{14}
\]

At `a=1`, (9) has `z=0`, so

\[
k_{\rm MT}(1)
=\frac1{2\pi^2-1}
>
\frac1{2(355/113)^2-1}
>\frac{53}{1000},
\tag{15}
\]

with exact final margin

\[
\frac{87107}{239281000}>0.
\tag{16}
\]

No floating-point enclosure is used in (13)--(16).

## 4. Short spans force enough energy to recover the full local constant

Because `k_MT` is positive and decreasing on `[0,1]`, the nested pair counts (8) and rational kernel bounds (13)--(15) imply

\[
\begin{aligned}
E
&=2\sum_{i<j}k_{\rm MT}(y_i-y_j)^2\\
&>
2\left[
5\left(\frac3{20}\right)^2
+10\left(\frac{27}{200}\right)^2
+10\left(\frac{23}{200}\right)^2
+10\left(\frac{19}{200}\right)^2
+10\left(\frac{37}{500}\right)^2
+10\left(\frac{53}{1000}\right)^2
\right]\\
&=
\boxed{\frac{6001}{5000}}.
\end{aligned}
\tag{17}
\]

The trace--energy envelope from WI-011/WI-020 is

\[
D\ge\Phi_{515}(E),
\]

where

\[
\Phi_{515}(E)=
\begin{cases}
E,&E\le515/514,\\[1mm]
2\sqrt{\frac{514}{515}E}-1+\frac{E}{515},&E\ge515/514.
\end{cases}
\tag{18}
\]

Set

\[
E_*:=\frac{6001}{5000}>\frac{515}{514}.
\]

Since `Phi_515` is increasing, it suffices to show `Phi_515(E_*)>A`. This is one exact rational square comparison:

\[
\boxed{
\frac{514}{515}E_*
-
\frac14\left(A+1-\frac{E_*}{515}\right)^2
=
\frac{247850262991}{26522500000000}>0.
}
\tag{19}
\]

The quantity being squared is positive, so (19) is equivalent to

\[
\Phi_{515}(E_*)>A.
\]

Hence every block with `Y<460` satisfies

\[
\boxed{D>A,}
\tag{20}
\]

and therefore `D+P>A` since `P>=0`.

The substantial margin in (19) is intentional: the six kernel bounds were rounded down aggressively so that the proof remains elementary and rational rather than depending on a delicate numerical optimum.

## 5. Long spans recover the constant from pressure exactly

Now assume

\[
Y\ge460.
\]

Then from (2),

\[
P\ge P_0:=\frac{460}{2500}=\frac{23}{125}.
\tag{21}
\]

Equation (1) gives `E>=A-P`. If `P>=A`, then trivially `D+P>=A`. Otherwise `P in [P_0,A]` and

\[
D+P\ge\Phi_{515}(A-P)+P.
\tag{22}
\]

The function on the right is nondecreasing in `P`, because `Phi_515` is nondecreasing and 1-Lipschitz. At the endpoint `P=P_0`,

\[
A-P_0
=\frac{3121}{3125},
\tag{23}
\]

and this lies strictly below the kink:

\[
\frac{515}{514}-\frac{3121}{3125}
=\frac{5181}{1606250}>0.
\tag{24}
\]

Therefore `Phi_515(A-P_0)=A-P_0`, and (22) gives

\[
D+P\ge(A-P_0)+P_0=A.
\tag{25}
\]

Together with the short-span branch, this proves the local full-recovery statement (3).

## 6. Global assembly and strict improvement over WI-024

The shifted-block ledger is unchanged from WI-011/WI-023/WI-024. With `m=515`, every full block contributes its local `D+P` lower bound divided by 515, and the pressure tax is

\[
\frac{512}{515}\frac3{2500}N+o(N).
\]

Thus (3) gives

\[
\mathcal D(M^\circ)
\ge
\frac{A}{515}S
-
\frac{512}{515}\frac3{2500}N
-o(N).
\tag{26}
\]

Substituting into the stability bridge and solving for `S/N` yields (4).

The strict comparison with WI-024 is immediate at the exact level. WI-024 used the same `m=515` and the same pressure tax but only

\[
C_{024}=\frac{1182717}{1000000}=1.182717,
\]

whereas here

\[
A=\frac{3696}{3125}=1.182720>C_{024}.
\tag{27}
\]

The numerator of the global ratio is unchanged and positive, while the denominator `515-C` decreases strictly. Therefore (4) is strictly larger than the WI-024 bound independently of the displayed decimal evaluations.

As in WI-024, the finite-`T` passage is harmless. The short-span branch uses finitely many thresholds in the fixed compact interval `[0,1]`, where the limiting Montgomery--Taylor Gram asymptotic is uniform for fixed `m=515`; the exact margins in (14), (16), and (19) survive `o(1)` perturbations. The long-span branch is carried by the exact pressure ledger.

## 7. What this changes and what it does not

The improvement is entirely inside the support-one, simple-critical Gram contribution. It shows that **one-scale occupancy was not the optimal way to convert a span constraint into pair energy**. Nested occupancy constraints contain extra information even before one introduces a new local certificate, Bellman coboundary, or optimized analytic window.

It does not challenge the broader conclusions of WI-019/WI-025/WI-026. In particular:

- the new number is still far below WI-019's certified `0.67361` obstruction for the deliberately collapsed single-profile Montgomery--Taylor interface;
- it does not distinguish multiple critical-line zeros from screened off-line pairs, so WI-005--WI-007 remain untouched;
- it does not repair WI-003's separate Yang--Yang higher-moment truncation gap or import any of the recent computer-assisted `0.673...` candidates as established evidence.

The reusable lesson is narrower: whenever an argument knows only a total span `Y`, replacing the full family of occupancy inequalities

\[
N_{\rm pairs}(<Y_0/B)\ge m-B
\]

by a single chosen `B` can leave exact pair-energy slack. A multi-threshold charge is a cheap deterministic strengthening.

## 8. Prior-art and novelty audit

The load-bearing external ingredients are already anchored in `SOURCES.md`:

- Alpöge--Furman for the unconditional Montgomery/Weil-form bridge and Montgomery--Taylor kernel;
- `teal-sea/zeta-lab` for the `sorry`-free four-point certificate with `epsilon=231/100000` and pressure `p=1/2500`;
- `tawanerguo-cn/zeta-simple-zeros` and `trmdy/zeta-simple-zeros-673137` for the trace--energy envelope and shifted block-frame assembly;
- WI-022--WI-024 for kernel monotonicity, the span-pressure ledger, and the one-scale `m=515` specialization.

A targeted current search for the exact decimal in (4), an `m=515` full-recovery refinement, or a multiscale/nested span-packing version of the four-point assembly did not locate a matching public statement. Existing public stronger `0.673...` candidates use different finite certificates, Bellman/subaction machinery, or optimized windows. Absence of a search hit is **not** a priority claim. The Mathia contribution asserted here is only the exact deduction (6)--(27) from already attributed ingredients.

## 9. Decisive audit tests

Reject or narrow this finding if any of the following fails.

1. Recompute the nested occupancy implication (6)--(8), preferably by sorting pair distances and verifying that each incremental batch can be charged without double-counting.
2. Recompute every rational kernel enclosure in (12)--(16) using only the inequalities in (10)--(11); no floating-point kernel values are load-bearing.
3. Verify the exact energy identity in (17) gives `6001/5000`.
4. Verify the square comparison (19) exactly and check that its right-hand square root comparison is in the positive branch.
5. Verify the pressure endpoint algebra (21)--(25), especially `A-P_0=3121/3125<515/514`.
6. Reuse the shifted-block assembly with the same multiplicity and pressure tax as WI-024; changing the number of local four-point windows or the factor `3/2500` would invalidate (4).
7. Keep the conclusion at the current evidence tier: it is an exact refinement of the established four-point chain, not an independent proof of any stronger recent computer-assisted headline.

## 10. Consequence for `weil_inertia`

Mathia's exact four-point baseline can be raised from WI-024's

\[
0.6728529261926306156\ldots
\]

to

\[
\boxed{0.6728529301211843198\ldots}.
\]

More importantly, the local `m=515` block now reaches the full four-point energy `A`; the residual slack in this particular block length is no longer caused by the span-packing conversion. Any further gain with the same four-point certificate must come from a different block length, a stronger use of the entire ordered-gap geometry than total-span occupancy, or a stronger local/global certificate.