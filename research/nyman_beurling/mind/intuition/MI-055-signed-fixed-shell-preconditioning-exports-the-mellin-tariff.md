# MI-055 — Signed fixed-shell preconditioning exports the Mellin tariff instead of removing it

**Evidence level:** exact synthesis from [NB-213](../../findings/NB-213-mellin-primitivization-recreates-the-carrier-tariff.md), [NB-214](../../findings/NB-214-positive-shell-preconditioning-cannot-remove-the-mellin-reconstruction-tariff.md), and [NB-215](../../findings/NB-215-signed-fixed-shell-preconditioning-can-only-export-the-mellin-tariff.md).

Changing a fixed Mellin shell from positive to signed/complex can suppress a local Fourier lobe, but it cannot make the global absolute reconstruction problem cheap when the normalized signal is its nonzero mean.

For a profile `h` supported in `[0,Delta]` with mean `m!=0`, let

`K_X(v)=i int_0^Delta (X+y)h(y)e^(ivy)dy`.

NB-215 uses Fourier inversion against `(X+y)^(-1)` to prove the sign-blind inequality

`||K_X||_1/|m| >= 2pi/log(1+Delta/X) >= (2pi/Delta)X`.

After `j` primitive transfers, the same dual argument gives a lower bound of order `X^j`. Thus signs can move reconstruction mass in frequency, but they cannot reduce its full source-normalized `L1` mass below the carrier scale.

The local version reveals where the moved cost goes. Write `kappa=||h||_1/|m|`, the exact `L^infinity -> C` conditioning of the signed source functional. On any contour containing a fixed central interval, NB-215 gives

`kappa max{1,C_X(I)} >= X/(5Delta)`.

Hence a signed profile that makes the central reconstruction kernel small must become correspondingly ill-conditioned, unless the proof uses source-specific correlation that is invisible to the bare operator norm. At least one of conditioning or central reconstruction costs `Omega(sqrt(X))`.

This is a general resource-transfer pattern: **preconditioning can relocate a tariff between acquisition, normalization and reconstruction without changing the final asymptotic class.** A representation should only be credited with a gain after all three currencies have been normalized to the destination signal actually being recovered.

For Nyman--Beurling, the surviving branch is therefore not generic signed preconditioning. It must exploit correlation with the actual `log zeta` integrand before absolute values, use a source-justified zero-mean/higher-moment signal for which the normalization is genuinely different, or change the fixed-shell support geometry. Those possibilities remain open because NB-215 deliberately measures worst-case absolute closure.

**Boundary.** The theorem assumes fixed logarithmic width and nonzero mean. It does not rule out zero-mean observables, growing shells, or arithmetic cancellation between `log zeta` and the kernel. It is a method boundary for source-normalized absolute-norm reconstruction, not a lower bound for the true zeta remainder or an RH consequence.