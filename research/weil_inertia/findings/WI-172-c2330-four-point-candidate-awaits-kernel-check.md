# WI-172 — The `c=2330/10^6` four-point source certificate is kernel-checked and gives a strict exact improvement

**Status:** `FORMALLY-CHECKED + EXACT-DERIVED + LITERATURE+DERIVED + STRICT-PROPORTION-IMPROVEMENT + SOURCE-SPECIFIC-ESCAPE + PRIOR-ART-REDIRECT + NO-NOVELTY-CLAIM`

## Claim

The previously conditional `teal-sea/zeta-lab` four-point candidate at

\[
n=4,\qquad c=\frac{2330}{10^6},\qquad p=2500
\]

has now passed an independent complete Lean kernel replay at the frozen source commit

`d28df5f992479cd32751cb90c8c88551550582a3`.

Research Watch independently rechecked the formal-to-mathematical correspondence of the frozen source. The certificate is for the actual Montgomery--Taylor overlap kernel used by the zeta bridge, with the same ordered-gap functional and pressure ledger consumed by `Zeta23Ext.Bridge.n_point_bound`. At the maximal admissible block size `m=432`, the checked downstream theorem therefore gives

\[
\boxed{
\liminf_{T\to\infty}
\frac{N_0^s(T,2T)}{N(T,2T)}
\ge
B_{2330}:=
\frac{14400000H_{\rm MT}-17240}{14366681}
}
\tag{1}
\]

where

\[
H_{\rm MT}
=
\frac32-\frac1{\sqrt2}\cot\frac1{\sqrt2}.
\]

Numerically,

\[
\boxed{
B_{2330}
=
0.6728603588388666595002053005\ldots
}
\tag{2}
\]

This strictly exceeds WI-036's exact four-point bound

\[
B_{36}
=
\frac{1609375H_{\rm MT}-1920}{1605679}
=
0.6728529301211843197511878001\ldots .
\tag{3}
\]

The comparison is exact:

\[
B_{2330}-B_{36}
=
\frac{400365625H_{\rm MT}-97878440}{23068277981399}.
\tag{4}
\]

Since `H_MT>2/3`, the numerator in (4) is bounded below by

\[
400365625\cdot\frac23-97878440
=
\frac{507095930}{3}>0.
\]

Thus no decimal evaluation is needed for strictness. At the actual value of `H_MT` the gain is

\[
\boxed{
B_{2330}-B_{36}
=
7.4287176823397490175\ldots\times10^{-6}.
}
\tag{5}
\]

The improvement is quantitatively small, but it is structurally important for the line: the genuine Montgomery--Taylor kernel/gap coupling has a certified local surplus beyond the sharp arbitrary-positive-weight relaxation isolated by WI-166.

## 1. Exact source correspondence

The frozen candidate's `lean/bridge/Zeta23Ext/Bridge/Defs.lean` defines

\[
K(x)
=
\int_{-1/2}^{1/2}
\cos(\sqrt2\,t)\cos(2\pi xt)\,dt,
\qquad
k(x)=\frac{K(x)}{K(0)},
\qquad
w(x)=k(x)^2.
\tag{6}
\]

It then defines the `n`-point functional on nonnegative consecutive gaps by

\[
F_{n,p}(g)
=
\frac1p\sum_i g_i
+
\sum_{0\le i<j<n}
\frac{2}{n-(j-i)}
\,w(y_j-y_i),
\tag{7}
\]

where `y_0=0` and the remaining `y_j` are the partial sums of the gaps.

For `n=4`, the frozen `FourPoint/Main.lean` proves the exact unfolding

\[
\begin{aligned}
F_{4,2500}(x,y,z)
={}&
\frac{x+y+z}{2500}
+\frac23\bigl(w(x)+w(y)+w(z)\bigr)\\
&+w(x+y)+w(y+z)+2w(x+y+z),
\end{aligned}
\tag{8}
\]

and then proves

\[
\boxed{
\forall x,y,z\ge0,\qquad
\frac{2330}{10^6}
\le
F_{4,2500}(x,y,z).
}
\tag{9}
\]

This is the declaration `Zeta23Ext.Bridge.FourPoint.four_point_cert`.

The bridge source `Zeta23Ext/Bridge/S11.lean` proves that summing exactly this window functional over consecutive retained zeros charges each pair-energy coefficient without overspending and charges every single gap at most `n-1` times. `S13.lean` transfers that source energy to the actual simple-critical-zero Gram block through the uniform Montgomery--Taylor kernel limit and the spectral defect. The assembled theorem `Zeta23Ext.Bridge.n_point_bound` states, with no conjectural zero hypothesis,

\[
(\Phi_n-\varepsilon)N(T,2T)\le N_0^s(T,2T)
\]

for every `epsilon>0` and all sufficiently large `T`, provided only the finite certificate and the explicit finite side conditions hold.

The frozen `FourPoint/Main.lean` instantiates that theorem at

\[
(n,c,m,p)
=
\left(
4,\frac{2330}{10^6},432,2500
\right),
\]

proves the exact identity

\[
\Phi_4
=
\frac{14400000H_{\rm MT}-17240}{14366681},
\tag{10}
\]

and exposes both `four_point_bound` and `four_point_bound_ratio`. The ratio theorem explicitly uses eventual positivity of `Ncount` before division, so its conclusion is literally about `N0simple/Ncount`, not an informal reinterpretation of a matrix quantity.

Thus the checked finite source is connected end to end to the intended count of zeros that are both simple and on the critical line.

## 2. The block-size correction remains load-bearing

The generic bridge requires

\[
c\bigl(m-(n-1)\bigr)\le1.
\tag{11}
\]

At the checked parameters,

\[
\frac{2330}{10^6}(432-3)
=
\frac{999570}{10^6}<1,
\tag{12}
\]

whereas the older exploratory `m=433` row would give

\[
\frac{2330}{10^6}(433-3)
=
\frac{1001900}{10^6}>1.
\tag{13}
\]

Therefore `m=432` is the admissible block used in the theorem. The nearby historical `m=433` table entry must not be imported into any zeta bound at this `c`.

## 3. Independent kernel replay and trust footprint

The public upstream state of record remains deliberately conservative. The archival [`hunts/four_point_pressure/RUNS.md`](https://github.com/teal-sea/zeta-lab/blob/main/hunts/four_point_pressure/RUNS.md) records that the upstream GitHub Actions attempt at the frozen candidate commit was canceled during dependency compilation, before any candidate proof module ran, and therefore did not register a new proved constant. The exact source replayed here is [`FourPoint/Main.lean`](https://github.com/teal-sea/zeta-lab/blob/d28df5f992479cd32751cb90c8c88551550582a3/hunts/ainta_seven_point/lean-four-point/FourPoint/Main.lean) at that frozen commit.

[Mathia issue #119](https://github.com/murillo128/mathia/issues/119) performed the bounded independent replay that WI-172 had identified as the decisive missing gate. The preserved preflight reproduced exactly

- `1516` cell lemmas,
- `11863` leaves,
- `220` chunks,
- `13` boxes,
- `64` dispatch cases,
- zero preflight problems.

The replay used the frozen toolchain and dependencies: Lean `4.33.0-rc2`, Mathlib `51e6992efd06126df61a496bebf8f49482a4e129`, and Zeta23 `3635e74826a4c1fcece7d1cd2b6fa75e43a00510`. `lake exe cache get`, `lake build Zeta23Ext.Bridge.Main`, and `lake build FourPoint.Base` succeeded.

Native Lake then encountered a package-resolution collision because the candidate package and `Zeta23Bridge` both expose a module named `FourPoint.Base`; this happened before cell elaboration. The replay did not edit source or package configuration. Instead it continued with the same pinned `lean` executable and explicit module setup maps retaining the already-successful Base compiler options, plugins, dynamic libraries and upstream import artifacts while selecting the candidate package's checked `FourPoint` modules.

All 48 candidate source modules then compiled, through `Cells0`--`Cells25`, `Cells`, `Cover`, `Chunks0`--`Chunks15`, `Boxes`, `Main`, and the root `FourPoint` module. Original source, toolchain and manifest hashes remained unchanged. The forbidden-token audit passed all 48 candidate Lean files.

Most importantly, the executed `#print axioms` reports for

`F4_eq`, `cover1`, `four_point_cert`, `Phi_four`, `four_point_bound`, and `four_point_bound_ratio`

were all exactly

\[
[\texttt{propext},\ \texttt{Classical.choice},\ \texttt{Quot.sound}].
\tag{14}
\]

The floating-point screen in the source preflight is only diagnostic; equation (9), the bridge identity (10), and the downstream zeta statements are carried by the elaborated exact Lean proofs with the standard trust footprint (14).

The remaining native-Lake name collision is therefore a packaging/tooling defect of that frozen candidate checkout, not a mathematical premise or an unchecked proof step.

## 4. What the result says about the surviving source information

WI-166 proves that the positive-cover relaxation is sharp when the four-point local problem is allowed arbitrary nonnegative pair weights under the shared coefficient budget. WI-171 then realizes the saturation witness by uniformly positive-definite Toeplitz Gram matrices, ruling out generic PSD, principal-minor, determinant, interlacing, conditioning, Toeplitz, or stationary-Gram constraints as an automatic escape.

The checked certificate here is different because its six pair weights are not free: they are the values of the single function `w` in (6) at the additive distances

\[
x,\ y,\ z,\ x+y,\ y+z,\ x+y+z,
\]

while the same gaps simultaneously pay the pressure term `(x+y+z)/2500`. The certificate proves that this coupled source family cannot realize the relaxed WI-166 saturation value. Uniformly,

\[
\inf_{x,y,z\ge0}F_{4,2500}(x,y,z)
\ge
\frac{2330}{10^6}
=
\frac{2310}{10^6}
+\frac{20}{10^6}.
\tag{15}
\]

Hence the actual MT source coupling contributes at least a

\[
\boxed{2\times10^{-5}}
\]

local surplus over the already Lean-checked `2310/10^6` certificate used in the earlier four-point line.

This validates the first, bounded source-specific escape anticipated by `CLUE-kernel-constrained-positive-cover-escape`. It does **not** establish the optimal source-constrained local constant, an extensive surplus for every positive-cover architecture, or a mechanism that forces the exceptional off-line mass to vanish.

## 5. Prior art, novelty, and scope

The number `2330/10^6`, its generated proof tree, and the candidate bridge expression were already public in `teal-sea/zeta-lab`. The earlier `FOUR-POINT.md` had tabulated this floor, and the 5 September 2026 archival `RUNS.md` preserved the exact source and explicitly recorded the canceled upstream build. **No novelty or priority claim is made for the constant, certificate design, or bridge.**

The durable Mathia contribution in this finding is evidence integration: independently replaying the frozen exact proof, checking its trust footprint, rechecking the formal correspondence to the actual Montgomery--Taylor kernel and simple-critical-zero bridge, retaining the corrected admissible `m=432`, and comparing the resulting exact theorem to the stronger WI-036 Mathia frontier rather than only to the older upstream registered four-point theorem.

This result improves only the certified proportion of simple critical-line zeros. It does not identify the uncertified complement as off-line zeros; multiple critical-line zeros and proof slack remain separate. It does not defeat WI-026's broader single-profile pressure-family ceiling, and it does not provide the individual-exception coercivity required by the canonical RH objective.

## Consequence for the research line

The bounded verification question that previously occupied WI-172 is closed positively. The broader source-constrained clue remains live, but its first branch is no longer hypothetical: **specific MT kernel/gap coupling really does escape the sharp arbitrary-weight relaxation.**

The next substantive question is therefore not another replay of `c=2330/10^6`. It is to characterize how much source-specific surplus survives at larger/global scale, or to construct an actual MT-kernel gap configuration approaching the relaxed saturation resource. Any such work must preserve the common kernel-value/additive-gap/pressure coupling from the start; generic Gram feasibility has already been shown insufficient.
