# WI-025 — full recovery of the four-point local constant has an asymptotic `0.672855` ceiling

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE`. This is a barrier for one specific continuation of WI-023/WI-024: increasing the block length while using the existing Lean-proved four-point certificate and the same shifted-block assembly, with the local goal only of recovering the full certificate energy `D+P >= A_m`. Even perfect full recovery at every larger block size cannot raise that architecture beyond the explicit limit below. The result does **not** cap stronger local inequalities with surplus `D+P>A_m`, different certificates, multiple profiles, the global Fenchel/Bellman route, or new arithmetic information.

## 1. Setup

Retain the exact four-point constants used in WI-009--WI-024,

\[
\varepsilon=\frac{231}{100000},
\qquad
p=\frac1{2500},
\]

and the Montgomery--Taylor stability baseline

\[
H_{\rm MT}=\frac32-\frac1{\sqrt2}\cot\frac1{\sqrt2}.
\]

For a block of `m` consecutive simple critical zeros, summing the same four-point certificate over the `m-3` internal windows gives the local certificate energy

\[
A_m=\varepsilon(m-3).
\tag{1}
\]

The shifted-block assembly of WI-011/WI-023/WI-024 says that any uniform local estimate

\[
D+P\ge C_m
\]

feeds into

\[
\frac SN
\ge
R_m(C_m)+o(1),
\qquad
R_m(C):=
\frac{mH_{\rm MT}-3p(m-3)}{m-C}.
\tag{2}
\]

Here the subtraction `3p(m-3)` is the exact pressure tax already present in the established assembly.

The branch studied in this finding is the **full-recovery-only** branch:

\[
\boxed{C_m=A_m.}
\tag{3}
\]

This is exactly the achievement of WI-023 at `m=513` and the natural target suggested there for larger blocks. WI-024 already showed that the numerically best finite block need not coincide with a full-recovery point; the question here is how much could be gained even if full recovery became available for arbitrarily large `m`.

## 2. Exact closed form

Substituting (1)--(3) into (2) gives

\[
R_m^{\rm full}
=
\frac{
 m\bigl(H_{\rm MT}-3p\bigr)+9p
}{
 m(1-\varepsilon)+3\varepsilon
}.
\tag{4}
\]

Thus `R_m^full` is a ratio of two affine functions of `m`. In particular,

\[
\boxed{
\lim_{m\to\infty}R_m^{\rm full}
=
\frac{H_{\rm MT}-3/2500}{1-231/100000}
=
\frac{100000H_{\rm MT}-120}{99769}.
}
\tag{5}
\]

A high-precision non-load-bearing evaluation is

\[
\boxed{0.6728549987264697909514777\ldots}. 
\tag{6}
\]

Therefore proving `D+P >= A_m` at successively larger block sizes, with no stronger local constant and no change to the global assembly, can never reach even `0.672855` from above.

## 3. The full-recovery sequence increases monotonically to the ceiling

Write

\[
a=H_{\rm MT}-3p,
\quad b=9p,
\quad c=1-\varepsilon,
\quad d=3\varepsilon,
\]

so that `R_m^full=(am+b)/(cm+d)`. Direct subtraction yields

\[
R_{m+1}^{\rm full}-R_m^{\rm full}
=
\frac{ad-bc}{(cm+d)(c(m+1)+d)}.
\tag{7}
\]

The numerator simplifies exactly:

\[
ad-bc
=3\bigl(\varepsilon H_{\rm MT}-3p\bigr).
\tag{8}
\]

Since

\[
\frac{3p}{\varepsilon}
=
\frac{3/2500}{231/100000}
=
\frac{40}{77},
\]

and WI-024 already gives the elementary exact estimate

\[
H_{\rm MT}>\frac23>\frac{40}{77},
\]

we have `ad-bc>0`. Hence

\[
\boxed{R_m^{\rm full}\nearrow \frac{100000H_{\rm MT}-120}{99769}.}
\tag{9}
\]

There is no exceptional finite block length at which full recovery beats the limiting ceiling.

The remaining gap has the exact form

\[
\frac{100000H_{\rm MT}-120}{99769}-R_m^{\rm full}
=
\frac{3(\varepsilon H_{\rm MT}-3p)}
{(1-\varepsilon)\,[m(1-\varepsilon)+3\varepsilon]},
\tag{10}
\]

so the residual gain available from increasing `m` in this branch is only `O(1/m)`.

## 4. Comparison with the current exact four-point refinement

WI-024 proves, at `m=515`, the stronger-than-envelope but slightly sub-full-recovery local constant

\[
C_{515}=\frac{1182717}{1000000}
\]

and hence

\[
R_{515}=0.6728529261926306156\ldots.
\]

The full-recovery ceiling (6) exceeds this by only

\[
2.0725338391753\ldots\times10^{-6}
\tag{11}
\]

in proportion, i.e. about `0.0002073` percentage points.

Thus essentially all of the gain available from the narrow program

\[
\text{same four-point certificate}
\;\longrightarrow\;
\text{better packing until }D+P\ge A_m
\;\longrightarrow\;
\text{same shifted-block assembly}
\]

has already been exposed. Larger-block full recovery remains mathematically valid work, but it cannot materially move the global percentage.

## 5. What escapes the barrier

The ceiling is deliberately narrow. Equation (2) shows exactly how to escape it.

1. **Local surplus above the certificate energy.** If realizability forces
   \[
   D+P\ge A_m+\sigma_m
   \]
   with a positive surplus whose size is not negligible compared with `m`, then `C_m>A_m` and (5) no longer applies. WI-021 already demonstrates the qualitative possibility of geometric surplus, although at a much smaller block and scale.
2. **A stronger local certificate.** Replacing the four-point constant `epsilon=231/100000` or its pressure ledger changes both `A_m` and the assembly tradeoff.
3. **A different global assembly.** A Bellman/Fenchel witness that avoids the same per-window pressure tax is outside (2).
4. **Multiple profiles or independent observables.** The single-profile collapsed architecture of WI-019 and the current four-point block frame do not cover genuinely independent admissible kernels.
5. **New prime-side moments or support.** Higher-moment arithmetic, if actually established, changes the spectral information being consumed rather than merely recovering four-point Gram energy.

The useful conclusion is therefore not that support-one refinement is exhausted, but that **full recovery of the existing four-point energy is no longer a high-leverage objective by itself**.

## 6. Prior-art and novelty assessment

The ingredients of (2) are prior art already anchored in `SOURCES.md`: the `teal-sea/zeta-lab` four-point certificate and the trace--energy/shifted-block assembly developed in `tawanerguo-cn/zeta-simple-zeros` and independently re-derived in `trmdy/zeta-simple-zeros-673137`. WI-023 and WI-024 supply the exact Mathia specializations used here.

The present ceiling is an algebraic consequence of those formulas, not a new matrix inequality or arithmetic theorem. A targeted search for the decimal in (6) and for an explicit statement of this full-recovery asymptote did not locate a public theorem; no priority claim is made from that absence.

The substantive contribution for this research line is route triage: WI-023 explicitly suggested larger-block packing/full recovery as the next exact optimization target, and (5)--(10) show that this particular target has a hard quantitative payoff ceiling even under perfect success.

## 7. Falsification and boundary checks

The claim can be falsified only by violating one of its explicit hypotheses. Within the branch `C_m=A_m` and the established assembly (2), the ceiling follows by exact algebra.

- If the pressure tax in (2) is changed, recompute the affine ratio; this finding does not assert the same constant.
- If a local argument proves `C_m>A_m`, it has escaped the full-recovery-only branch rather than contradicted the result.
- If a different certificate changes `epsilon` or `p`, the ceiling changes.
- No statement is made about the broader Alpöge--Furman bandwidth-one ceiling, the Yang--Yang higher-moment candidates, Devine's multi-profile candidate, or the exceptional off-line/multiple-zero block.
- The decimal evaluations are not load-bearing. Equations (4), (5), (8), and the exact bound `H_MT>2/3` establish all qualitative conclusions.

## 8. Consequence for `weil_inertia`

The next support-one effort should not spend substantial research budget merely trying to push the one-scale packing argument to full recovery at larger and larger `m`. Even an oracle granting that statement for every `m` leaves the certified proportion below

\[
0.672854999.
\]

A meaningful continuation must instead extract **surplus beyond `A_m`**, improve the local certificate/pressure economics, alter the global assembly, or introduce genuinely independent spectral/arithmetic information. This sharply separates a nearly exhausted bookkeeping refinement from routes capable of changing the scale of the result.