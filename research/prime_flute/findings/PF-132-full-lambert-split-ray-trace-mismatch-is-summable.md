# PF-132 — the full Lambert split-ray trace mismatch is summable

**Status:** `EXACT-DERIVED + NEGATIVE/BOUNDARY`. PF-131 proved that the left/right PF-121 boundary traces on the common artificial split ray have summable mismatch on every fixed bounded Busemann-height interval measured from the finite endpoint. A remaining loophole was that the interval from such a fixed height to the cusp grows without bound with the pant parameters, so a nonsummable mode could in principle reappear at intermediate or deep height. The present calculation closes that one-dimensional loophole. On the whole split ray, the exact tail trace is a one-parameter family `arcosh(e^beta cosh tau)`; its `L^infinity + homogeneous W^{1,1}` distance is Lipschitz in `beta`, and the adjacent `beta`-variation for the exact prime/shift clone is summable. Therefore the complete nonlinear split-ray mismatch is summable from its finite endpoint all the way to infinity. This does not construct a two-dimensional boundary correction, prove a global strong-`L^1` marking, control the inverse-unit-ball scattering weight, establish a Schatten class, or imply any RH statement.

## Claim

Use the PF-131 trace functions

\[
\Phi_n(\tau)=\Phi_{a_n,a_n^+}(\tau),
\qquad \tau\ge0,
\]

for the exact prime/shift-clone half-cuffs

\[
a_n=\frac{\ell_n}{2},
\qquad a_n^+=\frac{\ell_n^+}{2}.
\]

For an absolutely continuous function `f` on `[0,infinity)` with finite variation derivative, define the trace seminorm

\[
\boxed{
\|f\|_{\mathcal T}
:=
\|f\|_{L^\infty(0,\infty)}
+
\int_0^\infty |f'(\tau)|\,d\tau .
}
\tag{1}
\]

This is an `L^infinity cap dot W^{1,1}` norm rather than the usual inhomogeneous `W^{1,1}` norm: the trace difference may converge to a nonzero constant at infinity and therefore need not lie in `L^1(d tau)`.

Put

\[
\epsilon_n
=
\log\frac{\cosh a_n^+}{\cosh a_n},
\qquad
\beta_n
=
\log\frac{\sinh a_n^+}{\sinh a_n}.
\tag{2}
\]

Then

\[
\boxed{
\sum_n \|\Phi_n-\Phi_{n+1}\|_{\mathcal T}<\infty.
}
\tag{3}
\]

Equivalently, after restoring the physical pant placement exactly as in PF-131, the full left/right split-ray mismatch satisfies

\[
\boxed{
\sum_n
\left[
\sup_{\tau\ge0}
\left|\log\frac{y_{L,n}^+(\tau)}{y_{R,n}^+(\tau)}\right|
+
\int_0^\infty
\left|\frac d{d\tau}
\log\frac{y_{L,n}^+(\tau)}{y_{R,n}^+(\tau)}\right|d\tau
\right]
<\infty .
}
\tag{4}
\]

The limiting mismatch is also explicit:

\[
\boxed{
\Phi_n(\tau)-\Phi_{n+1}(\tau)
\longrightarrow
\beta_n-\beta_{n+1}
\qquad (\tau\to\infty),
}
\tag{5}
\]

and

\[
\boxed{
\sum_n|\beta_n-\beta_{n+1}|<\infty.
}
\tag{6}
\]

Thus no nonsummable reciprocal-prime common mode reappears anywhere along the complete split ray. The deep trace can retain a nonzero scalar offset on each individual pant, but those offsets themselves have summable adjacent variation and can be handed to the finite-height cusp synchronization mechanism of PF-129.

## 1. The exact PF-121 tail is a uniformly tame one-parameter family

PF-131 proves that once the trace is past the unique splice, it has the exact form

\[
\boxed{
\Phi_{a,a'}(\tau)
=
\varphi_\beta(\tau)
:=
\operatorname{arcosh}(e^\beta\cosh\tau),
\qquad
\beta=\log\frac{\sinh a'}{\sinh a}.
}
\tag{7}
\]

The splice height tends to `1`, so on a sufficiently far tail every trace is already on branch (7) for `tau>=2`. Finite head terms never affect a summability statement.

For `tau>=2` and `beta` in the small fixed interval containing all sufficiently far prime/shift parameters,

\[
\frac{\partial\varphi_\beta}{\partial\beta}
=
\frac{\cosh\tau}
{\sqrt{\cosh^2\tau-e^{-2\beta}}}.
\tag{8}
\]

After enlarging the finite head if necessary, the denominator is uniformly separated from zero. In particular,

\[
\boxed{
\sup_{\tau\ge2}
\left|\partial_\beta\varphi_\beta(\tau)\right|
\le C.
}
\tag{9}
\]

The `tau` derivative is

\[
\varphi_\beta'(\tau)
=
\frac{\sinh\tau}
{\sqrt{\cosh^2\tau-e^{-2\beta}}},
\tag{10}
\]

and differentiating in `beta` gives

\[
\boxed{
\partial_\beta\varphi_\beta'(\tau)
=
-
\frac{e^{-2\beta}\sinh\tau}
{(\cosh^2\tau-e^{-2\beta})^{3/2}}.
}
\tag{11}
\]

For nonnegative `beta` the right-hand side is bounded in absolute value by `csch^2(tau)`; the same estimate up to a harmless constant holds on any sufficiently small two-sided parameter interval. Hence

\[
\int_2^\infty
\left|\partial_\beta\varphi_\beta'(\tau)\right|d\tau
\le C
\int_2^\infty\operatorname{csch}^2\tau\,d\tau
<\infty.
\tag{12}
\]

The mean-value theorem in the parameter now gives the uniform full-tail estimate

\[
\boxed{
\sup_{\tau\ge2}|\varphi_\beta(\tau)-\varphi_{\tilde\beta}(\tau)|
+
\int_2^\infty
|\varphi_\beta'(\tau)-\varphi_{\tilde\beta}'(\tau)|d\tau
\le C|\beta-\tilde\beta|.
}
\tag{13}
\]

This is the missing uniform-in-height strengthening of PF-131. The fixed-`H` constant there need not be followed through a growing interval; the exact tail formula supplies an integrable parameter derivative directly.

Finally, `arcosh(e^beta cosh tau)-tau -> beta`, so (5) follows from (7).

## 2. The tail parameter has summable adjacent variation

PF-119/PF-131 already prove

\[
\boxed{
\sum_n|\epsilon_n-\epsilon_{n+1}|<\infty.
}
\tag{14}
\]

The difference between the tail parameter and this canonical cosh parameter is exact:

\[
\boxed{
\beta_n-\epsilon_n
=
\log\frac{\tanh a_n^+}{\tanh a_n}.
}
\tag{15}
\]

Since

\[
\frac d{dx}\log\tanh x
=
\frac1{\sinh x\cosh x},
\tag{16}
\]

for `a_n^+=a_n+delta_n` with `delta_n` bounded on the tail,

\[
|\beta_n-\epsilon_n|
\le C|\delta_n|e^{-2a_n}.
\tag{17}
\]

PF-131 proves

\[
\sum_n e^{-2a_n}<\infty,
\tag{18}
\]

and PF-107 gives `delta_n->0`, so in particular `sup |delta_n|<infinity` after a finite head. Thus

\[
\boxed{
\sum_n|\beta_n-\epsilon_n|<\infty.
}
\tag{19}
\]

Taking first differences in (15) and using the triangle inequality,

\[
\begin{aligned}
\sum_n|\beta_n-\beta_{n+1}|
&\le
\sum_n|\epsilon_n-\epsilon_{n+1}|\\
&\quad+
2\sum_n|\beta_n-\epsilon_n|,
\end{aligned}
\tag{20}
\]

which proves (6). The deep-tail parameter therefore carries only the same summable adjacent mode already isolated in PF-119, plus an absolutely summable finite-`a` correction.

## 3. PF-131 controls the finite base and the exact tail controls everything else

Apply PF-131 with the fixed height `H=2`. Its estimate gives, after discarding a finite head,

\[
\begin{aligned}
&\|\Phi_n-\Phi_{n+1}\|_{L^\infty(0,2)}
+
\int_0^2|\Phi_n'-\Phi_{n+1}'|d\tau\\
&\qquad\le
C\left(
|\epsilon_n-\epsilon_{n+1}|
+e^{-2a_n}+e^{-2a_{n+1}}
\right).
\end{aligned}
\tag{21}
\]

For `tau>=2`, both traces are on their exact tail branches, so (13) gives

\[
\begin{aligned}
&\|\Phi_n-\Phi_{n+1}\|_{L^\infty(2,\infty)}
+
\int_2^\infty|\Phi_n'-\Phi_{n+1}'|d\tau\\
&\qquad\le C|\beta_n-\beta_{n+1}|.
\end{aligned}
\tag{22}
\]

Summing (21)--(22) and using (14), (18), and (20) proves (3).

PF-131 also proves the exact physical-placement identity

\[
\log\frac{y_{L,n}^+(\tau)}{y_{R,n}^+(\tau)}
=
\Phi_n(\tau)-\Phi_{n+1}(\tau).
\tag{23}
\]

Therefore no chart scale, extreme neighboring gap ratio, or physical split placement changes the estimate, and (4) follows immediately.

## 4. Consequence for the operator/scattering frontier

PF-130 left boundary synchronization as a possible source of failure for turning the independent strong-`L^1` Lambert comparisons into a global comparison. PF-131 showed that the full nonlinear trace mismatch is summable on every fixed bounded-height slab, but it still left an apparent growing-height interval between such a slab and the deep cusp.

PF-132 removes that **one-dimensional intermediate-height loophole**:

```text
finite split endpoint -> fixed height:
    PF-131 summable Linf + derivative-L1 mismatch

fixed height -> infinity:
    exact arcosh(e^beta cosh tau) tail
    + beta adjacent variation in l1
    -> summable Linf + derivative-L1 mismatch
```

The nonsummable single-cuff displacement never returns. The whole boundary mismatch is controlled by adjacent differences plus a summable finite-`a` correction.

This does **not** finish either accepted operator clue. A two-dimensional correction with these boundary data must still be constructed while preserving the finite-cuff trace and the exact deep-cusp normalization. In particular, a nonzero limiting shift in (5) cannot simply be propagated unchanged to infinite cusp depth in the Güneysu--Thalmaier wave integral; PF-129's finite-height cutoff remains necessary. The ambient inverse-unit-ball weight can also be small near noncanonical thin geometry, and no Schatten estimate follows from a one-dimensional trace bound.

The narrowed remaining question is therefore geometric/operatorial rather than one-dimensional:

\[
\boxed{
\text{summable full-ray boundary data}
\quad\Longrightarrow?\quad
\text{summable 2D correction compatible with cusp/cuff gluing}.
}
\tag{24}
\]

Any future failure now has to occur in the extension, weighted thin geometry, commutators, or infinite operator assembly, not because the PF-121 split trace accumulates a hidden reciprocal-prime mode at large height.

## 5. Prior-art and novelty audit

No novelty is claimed for the elementary derivatives of `arcosh(e^beta cosh tau)`, for bounded-variation trace norms, or for standard hyperbolic Lambert-quadrilateral geometry. Vuorinen--Wang, *Hyperbolic Lambert quadrilaterals and quasiconformal mappings*, Ann. Acad. Sci. Fenn. Math. 38 (2013), 433--453, DOI `10.5186/aasfm.2013.3845`, remains the closest general Lambert-quadrilateral prior-art anchor already recorded in `SOURCES.md`; it studies hyperbolic distance inequalities and quasiconformal images, not the PF-121 trace family or the prime/shift summation above.

Directed searches by structure -- hyperbolic Lambert boundary traces, prescribed bilipschitz boundary maps for pants/strips, and `W^{1,1}`/bounded-variation boundary extension -- found standard extension and quasiconformal machinery but no theorem whose conclusion is the project-specific estimate (3). That absence is not used as a novelty claim. The durable Mathia content is the exact composition

\[
\boxed{
\text{PF-121/PF-131 exact tail trace}
+
\text{PF-119 finite variation of }\epsilon_n
+
\text{summable }(\beta_n-\epsilon_n)
\Longrightarrow
\text{full-ray trace summability}.
}
\tag{25}
\]

This is a boundary lemma for the all-composite control program, not a new general theorem about hyperbolic surfaces and not evidence for RH.

## 6. Audit / falsification core

A later adversary can check PF-132 through a short exact chain:

1. import PF-131's exact tail formula (7) and its fixed-height estimate with `H=2`;
2. differentiate (7) in `beta` and `tau` and verify (8)--(11);
3. integrate the bound `|partial_beta varphi_beta'| <= C csch^2(tau)` on `[2,infinity)` to obtain (13);
4. verify the exact identity (15) and derivative (16);
5. combine PF-131's `sum e^-2a_n<infinity` with bounded `delta_n` to obtain (19);
6. combine (14) and (19) to prove finite variation of `beta_n` as in (20);
7. add the fixed-base and full-tail estimates to obtain (3), then use PF-131's physical identity (23) for (4);
8. do not interpret `mathcal T` as ordinary inhomogeneous `W^{1,1}` on the half-line, and do not infer a two-dimensional extension, weighted scattering criterion, Schatten membership, determinant, or spectral equality without an additional theorem.

A refutation would have to break the exact PF-131 tail formula, the parameter-derivative estimate, or one of the persisted summability inputs. Failure of a later two-dimensional extension would not refute PF-132; it would identify precisely the next gate left open by (24).
