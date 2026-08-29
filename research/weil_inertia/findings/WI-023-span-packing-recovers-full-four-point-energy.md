# WI-023 — span packing recovers the full four-point energy at `m=513`

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED`. This is an unconditional refinement of WI-021 using only the same `sorry`-free Lean four-point certificate, the same Montgomery--Taylor Gram kernel, and the exact trace--energy envelope already audited in WI-011/WI-020. No new prime-side moment, no support beyond one, and no new computer-assisted gap certificate are introduced. The new point is that at block length `m=513`, elementary span packing rules out the entire scalar-envelope loss: every admissible block satisfies `D+P >= A`, not merely `D+P >= Phi_m(A)`.

## 1. Statement and improved proportion

Retain the four-point constants from WI-009--WI-021,

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

For a block of `m=513` consecutive simple critical zeros, let

\[
E=\operatorname{tr}(G-I)^2,
\qquad
D=\operatorname{tr}\Psi(G),
\]

and let `P` be the nonnegative span pressure obtained by summing the Lean-proved four-point certificate over the `m-3=510` internal four-point windows. As in WI-011,

\[
E+P\ge A,
\qquad
A:=\varepsilon(m-3)=\frac{11781}{10000}.
\tag{1}
\]

The stronger block inequality is

\[
\boxed{
D+P\ge A=\frac{11781}{10000}.
}
\tag{2}
\]

Thus the trace--energy conversion loses nothing at this block size. Substituting (2) into the same shifted-block assembly as WI-011 gives

\[
\boxed{
\liminf_{T\to\infty}\frac{N_0^s(T,2T)}{N(T,2T)}
\ge
\frac{513H_{\rm MT}-153/250}{513-11781/10000}
=
\frac{5130000H_{\rm MT}-6120}{5118219}.
}
\tag{3}
\]

A high-precision, non-load-bearing evaluation is

\[
\boxed{0.6728529220565555601699279\ldots}.
\]

This is larger than WI-021's `0.672852564258567...` by about `3.58e-7` in proportion. The numerical gain is small; the structural gain is that the abstract high-branch envelope loss is completely eliminated for an explicit larger block using only realizability of the ordered Montgomery--Taylor translates.

## 2. The kink/pressure dichotomy

The exact WI-020 envelope has kink

\[
E_c=\frac{m}{m-1}.
\]

For `E <= E_c`, no shifted eigenvalue can enter the affine branch of `Psi`, so in fact

\[
D=E.
\tag{4}
\]

Consequently (1) already implies `D+P >= A` in the low-energy regime.

It remains to treat `E>E_c`. For `m=513`,

\[
E_c=\frac{513}{512},
\qquad
A-E_c
=\frac{56367}{320000}.
\tag{5}
\]

Write the normalized block span as

\[
Y=y_{513}-y_1.
\]

The exact pressure ledger from WI-021 gives

\[
P\ge pY.
\tag{6}
\]

Define the critical span

\[
Y_*:=\frac{A-E_c}{p}
=\frac{56367}{128}
=440.3671875.
\tag{7}
\]

If `Y >= Y_*`, then `P >= A-E_c`. Since WI-020 gives `D >= Phi_m(E) >= Phi_m(E_c)=E_c` for `E>E_c`,

\[
D+P\ge E_c+(A-E_c)=A.
\tag{8}
\]

Therefore any failure of (2) would have to occur in a block satisfying simultaneously

\[
E>E_c,
\qquad
Y<Y_*.
\tag{9}
\]

The rest of the proof shows that such a short block has much too much pair energy for (9) to be dangerous.

## 3. A 513-point short block forces at least 28 close pairs

The exact rational comparison

\[
\frac{56367}{128}
<
485\frac{10}{11}
\tag{10}
\]

has cross-multiplication margin

\[
4850\cdot128-56367\cdot11=763>0.
\]

Hence every interval of span `Y<Y_*` can be covered by `485` consecutive half-open subintervals of length `10/11`.

Place the `513` ordered points into those `485` bins. If the occupancies are `n_j`, then

\[
\sum_j\binom{n_j}{2}
\ge
\sum_{j:n_j>0}(n_j-1)
\ge
513-485
=28.
\tag{11}
\]

Thus at least `28` unordered pairs have separation at most `10/11`. This is a deterministic packing statement; no zero-spacing statistic is being assumed.

## 4. Exact lower bound for the Montgomery--Taylor kernel at `10/11`

WI-022 records the normalized Montgomery--Taylor kernel

\[
k_{\rm MT}(x)
=
\frac{
2\cos(\pi x)-2\pi\sqrt2\,x\cot(1/\sqrt2)\sin(\pi x)
}{
2-4\pi^2x^2
},
\tag{12}
\]

and proves that it is strictly decreasing and positive on `[0,1]`. We need only the coarse rational bound

\[
\boxed{k_{\rm MT}(10/11)>\frac{149}{1000}.}
\tag{13}
\]

For auditability, (13) can be discharged without floating point. Put `z=pi/11`. Since

\[
\cos(10\pi/11)=-\cos z,
\qquad
\sin(10\pi/11)=\sin z,
\]

multiplying numerator and denominator of (12) by `-1` gives a positive numerator at `x=10/11`. Use the classical rational bounds

\[
\frac{333}{106}<\pi<\frac{355}{113},
\qquad
\sqrt2>\frac{140}{99}.
\tag{14}
\]

For `u=1/\sqrt2`, alternating Taylor bounds give

\[
\cos u>
1-\frac14+\frac1{96}-\frac1{5760},
\]

and

\[
\sin u<u\left(1-\frac1{12}+\frac1{480}\right).
\]

Therefore

\[
\cot(1/\sqrt2)
>
\frac{140}{99}
\frac{1-1/4+1/96-1/5760}{1-1/12+1/480}
>
\frac{117}{100},
\tag{15}
\]

where the last rational difference is exactly `313/1871100 > 0`.

Likewise

\[
\cos z>1-\frac{z^2}{2},
\qquad
\sin z>z-\frac{z^3}{6}.
\tag{16}
\]

Using the lower rational bounds from (14)--(15) in the positive numerator and the upper bound `pi<355/113` in the positive denominator yields the explicit rational enclosure

\[
k_{\rm MT}(10/11)
>
\frac{427155993355837}{2855972587771622}
>
\frac{149}{1000},
\tag{17}
\]

with final margin

\[
\frac{808038888932661}{1427986293885811000}>0.
\]

Only (13) is used below; the larger fractions record a reproducible exact audit path.

## 5. Short span pushes the defect above the full certificate constant

Let

\[
w(x)=k_{\rm MT}(x)^2.
\]

By monotonicity on `[0,1]`, each of the at least `28` close pairs from (11) contributes more than `(149/1000)^2`. Hence

\[
E
=2\sum_{i<j}w(y_j-y_i)
>
56\left(\frac{149}{1000}\right)^2
=
\frac{155407}{125000}
=1.243256.
\tag{18}
\]

This is far above the kink. To compare with `A` using only exact rational arithmetic, note

\[
\frac{512}{513}\frac{155407}{125000}
=
\frac{9946048}{8015625}
>
\left(\frac{109}{100}\right)^2,
\tag{19}
\]

where the difference is

\[
\frac{6762943}{128250000}>0.
\]

On the high branch,

\[
\Phi_{513}(E)
=2\sqrt{\frac{512}{513}E}-1+\frac{E}{513}.
\]

Equations (18)--(19) imply

\[
D\ge\Phi_{513}(E)
>
2\frac{109}{100}-1
=
\frac{59}{50}
=1.18
>
\frac{11781}{10000}=A.
\tag{20}
\]

Thus every short-span block already has `D>A`, even before adding its nonnegative pressure. Together with (4) and (8), this proves (2) in all cases.

## 6. Global assembly

The shifted-block counting from WI-011 is unchanged. For block length `m`, a full block contributes its local lower bound divided by `m` after averaging the `m` block shifts, while the pressure tax is

\[
\frac{m-3}{m}\frac3{2500}N+o(N).
\]

Using the stronger local constant `C=A` at `m=513` therefore gives

\[
\mathcal D(M^\circ)
\ge
\frac{A}{513}S
-
\frac{510}{513}\frac3{2500}N
-o(N).
\tag{21}
\]

Substitution into the stability bridge and solution for `S/N` gives

\[
\frac SN
\ge
\frac{513H_{\rm MT}-510(3/2500)}{513-A}
-o(1),
\]

which is exactly (3), because `510(3/2500)=153/250`.

The finite-`T` compactness issue is no worse than in WI-011/WI-021. In the long-span case the pressure ledger alone closes the estimate. In the short-span case `Y<Y_*` gives a fixed compact span, on which the Montgomery--Taylor Gram asymptotic is uniform for fixed `m=513`; the strict margins above survive as `o(1)` perturbations per block.

## 7. What was recovered

WI-020 proves that `Phi_m(E)` is the exact scalar envelope over arbitrary unit-diagonal PSD Gram matrices. WI-022 then shows that the abstract high-branch equality matrix is not realizable by a 438-point Montgomery--Taylor translation Gram, while WI-021 extracts a tiny explicit amount of that nonrealizability through the span pressure.

The present argument goes one step further. At `m=513`, the same pressure variable and a crude one-dimensional packing estimate are already enough to prove

\[
\boxed{
E+P\ge A
\quad\Longrightarrow\quad
D+P\ge A
}
\]

inside the actual ordered Montgomery--Taylor Gram class. In other words, the full difference `A-Phi_m(A)` that an abstract Gram could lose at the spectral clipping step is unavailable to the concrete translation geometry.

This does not improve the abstract envelope and does not use a new local certificate. It recovers information that was discarded when the pair `(G,P)` was compressed to the two unrelated scalars `(E,P)`.

## 8. Prior-art and novelty audit

All load-bearing external inputs were already recorded in `SOURCES.md`: Alpöge--Furman's Montgomery/Weil-form bridge, the `teal-sea/zeta-lab` Lean four-point certificate, and the trace--energy/block assembly from `tawanerguo-cn` / `trmdy`. The exact kernel formula and monotonicity used here are already audited in WI-022.

The public trace--energy note in `tawanerguo-cn/zeta-simple-zeros` proves only the scalar implication `D+P >= Phi_m(A)` for its own operating parameters; it does not supply a span-packing recovery of the full constant `A`. Targeted searches for the exact decimal in (3), the rational constant `11781/10000`, and a 513-point four-point/span-packing refinement found no matching public statement. This is not used as a priority claim.

The new Mathia deduction is therefore deliberately narrow: combining the already established pressure ledger with an elementary packing lower bound on actual Montgomery--Taylor pair energy eliminates the envelope loss at one explicit block length and raises the strongest bound in this line that uses only the internally Lean-proved local certificate plus exact finite-dimensional deductions.

## 9. Boundaries and falsification tests

- The result concerns only the simple-critical Montgomery--Taylor Gram contribution. It does not distinguish multiple critical-line zeros from screened off-line pairs in the exceptional block and does not weaken WI-005--WI-007.
- It remains far below WI-019's `0.67361` obstruction for the collapsed single-profile Gram-defect interface; there is no conflict.
- `m=513` is an explicit successful choice, not a claim of optimality. A stronger packing/energy estimate may recover `D+P>=A_m` at larger `m`, which would feed into the same assembly formula.
- No empirical spacing law is used. The only geometric input beyond the existing certificate is deterministic occupancy in intervals and a rigorous kernel lower bound on `[0,10/11]`.
- The decisive finite audit is to verify (10), the `28`-pair occupancy count, the rational kernel enclosure (17), and the energy comparison (19). All load-bearing inequalities are exact rational comparisons after the classical Taylor/rational bounds in (14)--(16).
- A natural formalization target is the local statement (2) at `m=513`; once formalized, the existing block-frame bridge can substitute `A` directly for `Phi_m(A)`.

## 10. Consequence for `weil_inertia`

The current support-one program has now exposed three distinct layers of slack: the old rank--trace discard, the scalar trace--energy envelope, and realizability of that envelope by ordered translation Grams. The first two can be sharp in their abstract classes, but the third need not be.

At least through `m=513`, the existing four-point certificate contains enough geometric information to remove the scalar-envelope loss entirely. The next exact optimization target is therefore a **packing/energy lower bound at larger block lengths**, or a multiscale version that counts close pairs more efficiently than one uniform bin size. Any such improvement can be tested without new prime-side arithmetic and, if it proves `D+P >= A_m` for a larger `m`, immediately raises the certified proportion through the explicit assembly formula.