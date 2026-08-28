# PF-098 — recurrent prime tangents block even compact relative perturbations against featureless controls

**Status:** `DECISIVE-NEGATIVE` for compact-, trace-class-, relative-zeta-, and standard relative-scattering comparisons with a smooth/density-matched control whose geometry at infinity omits a recurrent prime tangent; `EXACT-GEOMETRIC + OPERATOR-THEORETIC + LITERATURE-AUDITED`.

## Claim

Let `X_prime` be the exact zero-twist hyperbolic prime-flute and let `X_0` be a marked featureless control flute, for example one obtained from a smooth prime-number-theorem sampling sequence

\[
q_n\sim p_n,
\qquad
\frac{q_{n+1}-q_n}{q_n-q_{n-1}}\to1,
\]

or from an integer/equal-spacing reference. Assume that, along one recurrent isolated prime pattern `H` supplied by PF-034/PF-046, the corresponding marked windows in `X_0` have a pointed limit `Y_0` which is not the prime tangent `Y_H` and in particular omits its short primitive separator.

After the canonical pants marking, with the volume-density correction included so that

\[
U:L^2(X_0)\to L^2(X_{\rm prime})
\]

is unitary, there exists `t_0>0` such that

\[
\boxed{
T_{t_0}
:=e^{-t_0\Delta_{X_{\rm prime}}}
-Ue^{-t_0\Delta_{X_0}}U^{-1}
\quad\text{is not compact.}
}
\tag{1}
\]

Consequently, for the nonnegative self-adjoint Laplacians,

\[
\boxed{
(\Delta_{X_{\rm prime}}+1)^{-1}
-U(\Delta_{X_0}+1)^{-1}U^{-1}
\quad\text{is not compact.}
}
\tag{2}
\]

This strictly strengthens the previous trace-class obstruction: the two Laplacians do not even define the same element modulo compact operators under this natural marking. Hence a featureless control cannot serve as a standard relatively compact background, let alone a resolvent-comparable/trace-class background for Birman--Krein spectral shift, relative scattering, or Müller/Borthwick--Judge--Perry relative determinants.

The mechanism is a **recurrent tangent-hull mismatch at infinity**. An order-one local spectral defect which recurs in disjoint regions cannot be hidden by a compact perturbation merely because its occurrences have zero density.

## 1. Exact prime geometry supplies an order-one recurrent local defect

PF-046 gives, for every sufficiently large fixed `B`, a finite offset pattern

\[
H_B=\{\eta_1<\cdots<\eta_r\}
\]

which occurs infinitely often as an isolated block of consecutive primes, with exterior prime-free collars tending to infinity. For the first two internal gaps

\[
d_1=\eta_2-\eta_1,
\qquad
d_2=\eta_3-\eta_2,
\]

one can force

\[
\boxed{
\frac{d_1}{d_2}<\frac1{B-1}.
}
\tag{3}
\]

At an occurrence near prime scale `P`, the distinguished cuffs obey

\[
\ell_i(P)=2\log\frac{4P}{d_i}+o(1),
\]

so

\[
\boxed{
\ell_1(P)-\ell_2(P)
\longrightarrow
2\log\frac{d_2}{d_1}
>2\log(B-1).
}
\tag{4}
\]

More importantly, the exact orthogonal-circle construction turns the same gap ratio into an intrinsic tangent separator

\[
\boxed{
\sinh^2\frac{L_B}{4}=\frac{d_1}{d_2},
\qquad
L_B\to0\quad(B\to\infty).
}
\tag{5}
\]

Thus the cuff fluctuation is not merely a coordinate label: it survives the pointed normalization as a primitive closed geodesic of the finite-area tangent `Y_{H_B}`.

For a smooth/equal-spacing control, every fixed normalized window converges instead to a regular model whose relevant local cross-ratios remain in a compact subset of `(0,\infty)`. Hence its corresponding primitive separator lengths are bounded away from zero. Choosing `B` large gives a strict local spectral-geometric mismatch between `Y_{H_B}` and the control limit `Y_0`.

All quantities in (3)--(5) come from the exact orthogonal-circle/cross-ratio geometry. The asymptotic cuff formula is only the translation back to the distinguished `ell_n` coordinates.

## 2. The two pointed limits have different localized heat operators

Choose a compact marked core `K` of `Y_{H_B}` containing the primitive geodesic of length `L_B`, and a smooth cutoff `chi` supported in a slightly larger core.

PF-064/PF-094 show that the isolated occurrences converge on larger and larger marked neighborhoods to `Y_{H_B}` and that the localized wave distribution detects the primitive orbit at `t=L_B`. The corresponding smooth-control windows converge to `Y_0`, which has no primitive orbit at that time after `B` is chosen as above.

Therefore the localized spectral measures of the two limits are not identical. If

\[
\chi e^{-t\Delta_{Y_{H_B}}}\chi
\]

and the corresponding marked localized heat operator for `Y_0` agreed for every `t>0`, their localized heat traces would agree for every `t`; uniqueness of the Laplace transform would then give identical localized spectral measures and hence identical localized wave distributions, contradicting the primitive singularity at `L_B`.

Thus there exists `t_0>0` for which the self-adjoint localized difference

\[
A_H(t_0)
:=
\chi e^{-t_0\Delta_{Y_{H_B}}}\chi
-
J\chi_0e^{-t_0\Delta_{Y_0}}\chi_0J^{-1}
\]

is nonzero, where `J` is the fixed unitary identification on the marked limit cores.

Because `A_H(t_0)` is self-adjoint and nonzero, there is a compactly supported unit vector `f` in the core such that

\[
\boxed{
\langle f,A_H(t_0)f\rangle=c_H\ne0.
}
\tag{6}
\]

The heat-flow passage under pointed metric-measure convergence is standard. In particular, Gigli--Mondino--Savaré prove stability of heat flows under pointed measured convergence in the `RCD(K,\infty)` setting; the present smooth constant-curvature pointed limits are a much more rigid special case. No global trace formula or global scattering theory for the infinite flute is used here.

## 3. Recurrence upgrades the local defect to noncompactness

Let `f_m` be the transplant of `f` to the `m`-th isolated occurrence of `H_B` in `X_prime`, using the same marked coordinate to choose the corresponding test vector on `X_0`.

The occurrences can be chosen pairwise disjoint and escaping every compact set. Therefore

\[
\|f_m\|=1,
\qquad
f_m\rightharpoonup0.
\tag{7}
\]

Pointed heat-flow convergence on the prime occurrences and on the corresponding control windows gives

\[
\boxed{
\langle f_m,T_{t_0}f_m\rangle
\longrightarrow c_H\ne0.
}
\tag{8}
\]

If `T_{t_0}` were compact, every bounded weakly-null sequence would be sent to a norm-null sequence:

\[
\|T_{t_0}f_m\|\to0.
\]

But Cauchy--Schwarz and (8) imply

\[
\liminf_m\|T_{t_0}f_m\|
\ge |c_H|>0,
\]

a contradiction. Hence (1) holds:

\[
\boxed{T_{t_0}\notin\mathcal K.}
\tag{9}
\]

This argument is stronger and simpler than the earlier trace-norm summation: it needs only one nonzero local matrix element repeated infinitely often, not summability estimates. In particular

\[
T_{t_0}\notin\mathcal K
\quad\Longrightarrow\quad
T_{t_0}\notin\mathcal S_p
\quad\text{for every finite }p,
\]

so the previous `S_1` obstruction follows immediately.

The recurrence frequency is irrelevant. Infinitely many disjoint occurrences with nondecaying local response suffice; zero area density does not help.

## 4. The resolvent difference is also noncompact

The heat statement is not merely a defect of the chosen semigroup observable. Let

\[
A=\Delta_{X_{\rm prime}},
\qquad
B=U\Delta_{X_0}U^{-1}.
\]

Both are nonnegative self-adjoint operators. Suppose

\[
R_A:=(A+1)^{-1},
\qquad
R_B:=(B+1)^{-1}
\]

satisfied

\[
R_A-R_B\in\mathcal K.
\tag{10}
\]

Define the continuous function on `[0,1]`

\[
F_t(r)=
\begin{cases}
\exp\!\left[-t\left(r^{-1}-1\right)\right],&r>0,\\
0,&r=0.
\end{cases}
\]

Functional calculus gives exactly

\[
F_t(R_A)=e^{-tA},
\qquad
F_t(R_B)=e^{-tB}.
\]

The quotient map to the Calkin algebra is a `C^*`-homomorphism. Equation (10) would therefore imply

\[
e^{-tA}-e^{-tB}\in\mathcal K
\qquad\text{for every }t>0,
\]

contradicting (9) at `t=t_0`.

Hence

\[
\boxed{R_A-R_B\notin\mathcal K.}
\tag{11}
\]

This is the natural operator-theoretic endpoint of the obstruction. Weyl's classical theorem says compact resolvent differences preserve essential spectrum; here the recurrent tangent mismatch prevents even entry into that perturbative equivalence class. The statement does **not** imply that the two essential spectral sets cannot coincide accidentally; it says they cannot be related by the standard compact-resolvent comparison under the natural marking.

## 5. Consequences for relative zeta, scattering and spectral shift

The classical relative constructions require hypotheses much stronger than compactness:

- Müller's relative zeta/determinant architecture assumes trace-class relative heat operators plus controlled asymptotics;
- Birman--Krein spectral-shift and standard relative-scattering frameworks use resolvent-comparable or trace-class perturbations;
- Borthwick--Judge--Perry obtain relative determinants for controlled hyperbolic perturbations near infinity.

PF-098 now fails one level earlier. A smooth/PNT/integer control that omits a recurrent prime tangent is not merely non-trace-class relative to `X_prime`; its resolvent difference is not compact. Therefore no standard perturbative completion of this featureless-background idea can repair the problem by replacing `trace class` with `Hilbert--Schmidt`, another Schatten class, or ordinary relative compactness.

This closes the natural branch

\[
\boxed{
\text{prime-flute}
-
\text{smooth featureless flute}
\to
\text{compact/trace-class relative Laplacian}
\to
\text{spectral shift / relative scattering / determinant}.
}
\tag{12}
\]

A genuinely different renormalization could still exist, but it would have to retain or explicitly quotient the recurrent tangent hull rather than regard prime-gap geometry as a perturbation vanishing at infinity.

## 6. Why the prime-indexed projective reference is not contradicted

PF-087 compares the exact endpoint sequence

\[
x_n^E=\pi\cot\frac{\pi}{p_n}
\]

with the projective reference

\[
x_n^0=p_n.
\]

Those two constructions are sampled at the **same primes** and hence share every finite projective gap tangent. Their direct-channel difference begins only with the decaying nonprojective endpoint defect, controlled by

\[
S\!\left(\pi\cot\frac{\pi}{p}\right)=\frac{2\pi^2}{p^4}.
\]

That is precisely why the direct scattering difference can be trace class for `Re s>1/4`: the comparison has already matched the nondecaying tangent hull before subtracting the finite-scale exact-circle correction.

The contrast is therefore structural:

\[
\boxed{
\begin{array}{c}
\text{featureless reference}
\Rightarrow
\text{retains prime-gap contrast but mismatches recurrent tangents}
\Rightarrow
\text{not even relatively compact},\\[2mm]
\text{prime-indexed projective reference}
\Rightarrow
\text{matches the tangent hull}
\Rightarrow
\text{only a decaying exact-circle defect remains}.
\end{array}}
\tag{13}
\]

PF-088 still warns that the `Re s=1/4` threshold of the direct-channel operator is universal one-dimensional propagation rather than prime arithmetic.

## 7. Interior/exterior duality

The obstruction is intrinsic. The recurrent separator length is a cross-ratio invariant, the Laplacian and heat flow are intrinsic to the hyperbolic surface, and the test-vector argument is invariant under isometry.

The ambient inversion exchanging the interior/exterior orthogonal-circle realizations therefore transports the same recurrent tangent, the same local heat defect, and the same noncompactness statement. No preferred ambient side is introduced.

## 8. Prior-art and novelty audit

No novelty is claimed for the operator-theoretic ingredients:

- compact operators send bounded weakly-null sequences to norm-null sequences;
- compact resolvent difference is a standard form of relative compactness and, by continuous functional calculus in the Calkin algebra, implies compact differences of `C_0` functions of the operators;
- Weyl's theorem and limit-operator/right-limit theory express the general principle that nonvanishing behavior at infinity obstructs compact perturbations;
- Gigli--Mondino--Savaré establish stability of heat flows under pointed noncompact metric-measure convergence (`Proc. London Math. Soc.` 111 (2015), 1071--1129, DOI `10.1112/plms/pdv047`);
- Müller, Birman--Krein, and Borthwick--Judge--Perry provide the classical relative trace/scattering/determinant frameworks under substantially stronger perturbative hypotheses.

A directed literature search over tight flutes, infinitely generated Fuchsian groups, relative hyperbolic determinants, compact resolvent perturbations, and limit-operator formulations found no theorem specializing this mechanism to the prime-derived flute. Existing tight-flute work is primarily about type/parabolicity and Fenchel--Nielsen geometry; the abstract noncompactness principle itself is standard.

The program-specific substantive result is the exact composition

\[
\boxed{
\text{Pintz/Maynard recurrent isolated prime pattern}
\to
\text{exact orthogonal-circle tangent modulus}
\to
\text{nonzero local heat response}
\to
\text{weakly-null recurrent test vectors}
\to
\text{noncompact relative heat and resolvent differences}.
}
\tag{14}
\]

Thus the claimed novelty is an **impossibility principle for this construction**, not a new general theorem about compact operators or hyperbolic heat kernels.

## 9. Boundary of the negative result

PF-098 does not rule out every possible relative spectral object. It rules out the broad and natural class in which the prime-flute is compared with a featureless smooth/density-matched end and the difference is expected to become compact, Schatten-class, resolvent-comparable, or trace class.

Nor does it say that an individual recurrent tangent is intrinsically prime-specific: PF-097 proves the opposite. What is prime-specific here is the **selection and infinite recurrence of that tangent inside the single prime-flute**.

Any surviving global construction must therefore preserve substantially more of the asymptotic hull. In particular it cannot first erase the recurrent prime tangent geometry and then hope to recover it as a small perturbative correction.