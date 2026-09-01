# WP-079 — The canonical cover-coinvariant quotient collapses to trace

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + CLASSICAL-COINVARIANT-REDUCTION + MATHIA-SPECIALIZATION`.

`WP-078` leaves open a narrow escape from the failure of the Möbius primitive: perhaps a **non-faithful quotient** could kill every mixed-prime trace-zero operator `M_n` for an independently geometric reason while retaining the positive prime-power classes. For the most canonical quotient suggested by the pointed-cover system itself — identify a diagonal trace-class observable with all of its cover transports — this escape can be classified exactly.

Let

\[
\mathfrak D_1^{\rm sa}
\cong \ell^1(\mathbb N_0;\mathbb R)
\]

be the real Banach space of self-adjoint diagonal trace-class operators in the Hardy basis `e_k`. The cover action from `WP-076`--`WP-078` is

\[
(\rho_n d)_k
=
\sum_{r=0}^{n-1}d_{nk+r},
\qquad n\ge2,
\tag{1}
\]

and satisfies

\[
\rho_m\rho_n=\rho_{mn},
\qquad
\rho_n\ge0,
\qquad
\operatorname{Tr}(\rho_n d)=\operatorname{Tr}d.
\tag{2}
\]

Form the Hausdorff semigroup-coinvariant quotient

\[
\boxed{
\mathcal C
:=
\mathfrak D_1^{\rm sa}
\Big/
\overline{\operatorname{span}}
\{\rho_n d-d:n\ge2,\ d\in\mathfrak D_1^{\rm sa}\}.
}
\tag{3}
\]

Then

\[
\boxed{
\mathcal C\cong\mathbb R
\quad\text{canonically via}\quad
[d]\longmapsto\operatorname{Tr}d.
}
\tag{4}
\]

In fact degree `2` alone already forces the collapse:

\[
\boxed{
\overline{\operatorname{ran}(I-\rho_2)}
=
\ker\operatorname{Tr}.
}
\tag{5}
\]

Consequently every bounded linear readout `\Phi` from the diagonal trace ideal satisfying the natural transport invariance

\[
\Phi\rho_n=\Phi
\qquad(n\ge2)
\tag{6}
\]

factors uniquely through the ordinary trace:

\[
\boxed{
\Phi(d)=\operatorname{Tr}(d)\,y_0
}
\tag{7}
\]

for one fixed vector `y_0` in the target space. If `\Phi` is positive, then `y_0\ge0`.

Applied to the positive cover defects and their Möbius primitives,

\[
[Q_n]= (\log n)[E_0],
\qquad
[M_n]=\Lambda(n)[E_0].
\tag{8}
\]

Thus the coinvariant quotient does exactly what the proposed escape asked for: every mixed-prime `M_n` becomes zero and every prime-power class is positive with mass `\log p`. But it does so only because **all trace-zero operator geometry has been quotiented away**. The resulting positivity is the scalar fact `\Lambda(n)\ge0` after the classical identity `\Lambda=\mu*\log`; no cross-prime incidence, cover-transport information, autocorrelation channel, or archimedean structure survives.

Therefore the direct route

```text
positive cover cocycle Q_n
    -> Möbius primitive M_n
    -> quotient identifying cover transports
    -> positive Mangoldt classes
    -> global Weil positivity
```

classicalizes at the quotient step. A viable quotient escape from `WP-078` must be **strictly richer than the universal semigroup coinvariants of the diagonal trace ideal**: it must retain additional non-diagonal/internal/cohomological data, or use a selective quotient whose nullspace is forced by geometry for a reason other than identifying every `rho_n` transport.

## 1. The cover transfer is a positive trace-preserving block sum

For a diagonal operator

\[
D e_j=d_j e_j,
\qquad d\in\ell^1(\mathbb N_0),
\]

`WP-078` gives

\[
\rho_n(D)=nW_n^*DW_n,
\]

hence (1). Positivity is immediate: nonnegative diagonal entries remain nonnegative. Moreover

\[
\begin{aligned}
\operatorname{Tr}(\rho_nD)
&=\sum_{k\ge0}\sum_{r=0}^{n-1}d_{nk+r}\\
&=\sum_{j\ge0}d_j\\
&=\operatorname{Tr}D.
\end{aligned}
\tag{9}
\]

Thus every cover difference `rho_nD-D` has trace zero, so the closed coinvariant subspace in (3) is contained in `ker Tr`.

The nontrivial statement is that there is **nothing else** in the quotient.

## 2. Degree two generates every finite trace-zero direction

Let `E_j` denote the diagonal rank-one basis vector with a `1` at index `j`. Equation (1) gives

\[
\boxed{
\rho_2(E_j)=E_{\lfloor j/2\rfloor}.
}
\tag{10}
\]

For any `j>=1`, follow the finite ancestor chain

\[
j=j_0,
\qquad
j_{r+1}=\lfloor j_r/2\rfloor,
\qquad
j_R=0.
\]

Then

\[
(I-\rho_2)E_{j_r}
=E_{j_r}-E_{j_{r+1}},
\]

and telescoping gives

\[
\boxed{
E_j-E_0
=
\sum_{r=0}^{R-1}(I-\rho_2)E_{j_r}.
}
\tag{11}
\]

Every finitely supported trace-zero diagonal sequence `d` can be written as

\[
d=\sum_{j\ge1}d_j(E_j-E_0),
\tag{12}
\]

so (11) places it in `ran(I-rho_2)`.

Finitely supported trace-zero sequences are dense in `ker Tr`. Explicitly, if `d in ell^1` and `sum_j d_j=0`, let

\[
t_N:=\sum_{j>N}d_j
\]

and set

\[
d^{(N)}
:=
\sum_{j=0}^N d_jE_j+t_NE_0.
\]

Then `Tr d^(N)=0` and

\[
\|d-d^{(N)}\|_1
\le
\sum_{j>N}|d_j|+|t_N|
\longrightarrow0.
\tag{13}
\]

Combining (9), (11), and (13) proves (5):

\[
\overline{\operatorname{ran}(I-\rho_2)}
=
\ker\operatorname{Tr}.
\]

Since the full coinvariant span contains the degree-two range and is itself contained in `ker Tr`, its closure is exactly the same kernel. This proves (4).

## 3. The universal transport-invariant readout is ordinary trace

Let `Y` be any Banach space and let

\[
\Phi:\mathfrak D_1^{\rm sa}\to Y
\]

be bounded linear with `Phi rho_2=Phi`. Then `Phi` annihilates `ran(I-rho_2)`, hence by continuity it annihilates its closure `ker Tr`.

Write

\[
d=(\operatorname{Tr}d)E_0+
\left[d-(\operatorname{Tr}d)E_0\right].
\]

The bracketed term has trace zero, so

\[
\Phi(d)
=(\operatorname{Tr}d)\Phi(E_0).
\tag{14}
\]

This is (7), with `y_0=Phi(E_0)`. Full semigroup invariance is therefore stronger than needed: invariance under the single intrinsic degree-two cover already forces trace-only dependence.

If `Y` is ordered and `Phi` is positive, `E_0>=0` implies `y_0>=0`. Equivalently, the positive cone of the quotient (3) is identified under (4) with

\[
\boxed{\mathbb R_{\ge0}.}
\tag{15}
\]

Indeed positive trace-class diagonals have nonnegative trace, and every `a>=0` is represented by the positive element `aE_0`.

Thus there is no hidden operator-valued positive invariant left after cover transport is quotiented out.

## 4. The quotient kills the mixed Möbius defects, but only by forgetting them

`WP-074` gives

\[
Q_n\succeq0,
\qquad
\operatorname{Tr}Q_n=\log n.
\tag{16}
\]

`WP-078` defines

\[
M_n=\sum_{d\mid n}\mu(d)Q_{n/d},
\qquad
\operatorname{Tr}M_n=\Lambda(n).
\tag{17}
\]

For `n=p^k`, `M_n` is itself positive. If `n` has at least two distinct prime factors, `WP-078` proves that `M_n` is a nonzero indefinite trace-zero operator.

Passing to (3) gives immediately

\[
\boxed{
[M_n]=0
\quad\text{for every mixed-prime }n,
}
\tag{18}
\]

while

\[
\boxed{
[M_{p^k}]
=(\log p)[E_0]\ge0.
}
\tag{19}
\]

At first sight this looks like the desired intrinsic positive support selector. But (4) shows exactly what happened: the quotient identifies *every* two diagonal trace-class operators with the same trace. In particular it kills not only the unwanted mixed `M_n`, but every possible trace-zero correction, interaction, fluctuation, and transported defect in this representation.

The support statement is therefore nothing more than

\[
\operatorname{Tr}M_n
=\sum_{d\mid n}\mu(d)\log(n/d)
=\Lambda(n).
\tag{20}
\]

The quotient has converted the operator problem back into the classical scalar Möbius identity.

This is importantly different from obtaining a positive operator whose nullspace geometrically singles out mixed composites. Here mixed composites disappear because the quotient's entire nullspace is `ker Tr`, a codimension-one space far larger than the mixed-prime span.

## 5. Matched controls and the archimedean failure

The proof of (4) uses only the block-refinement action (1). It does not use primality, cyclotomic arithmetic, the zeta functional equation, zero data, or any distinguished property of the rational primes. The same collapse holds for any matched cyclic-cover degree system carrying the same Hardy block representation.

This also makes the global limitation exact. The finite coinvariant sector has only one real coordinate, ordinary trace. Hence within this diagonal representation it can remember

\[
\log n
\quad\text{and, after signed Möbius extraction,}\quad
\Lambda(n),
\]

but it cannot retain the operator-valued prime-ray Poisson covariance of `WP-074`, the mixed differences of `WP-078`, or any new cross-prime coupling.

Nor can the quotient itself generate the archimedean Gamma/polar sector. `WP-074`--`WP-076` show that the digamma profile arose from spectral dependence on the half-integer operator `L`, while the coinvariant quotient here remembers only the total trace of diagonal trace-class defects. Appending an external archimedean coordinate after taking (3) would merely form a finite-plus-archimedean direct sum; it would not produce the nonseparable common sign theorem required by the research mandate.

A global candidate must therefore couple additional data **before** this collapse, or use a different geometric object whose relevant quotient has nontrivial higher structure.

## 6. Prior-art and novelty audit

No theorem-level novelty is claimed for coinvariants, quotient Banach spaces, transfer operators, or the elementary fact that a continuous invariant readout factors through the corresponding Hausdorff coinvariant quotient. The calculation above is deliberately self-contained.

The block-sum maps `rho_n` are the transfer side of the same multiplicative cover semigroup already audited in `WP-073`--`WP-078`. The broader warning is consistent with the Bost--Connes/endomotive literature already anchored in `SOURCES.md`: meaningful arithmetic cohomology is not obtained merely by quotienting a flat multiplicative semigroup action at degree zero; Connes--Consani--Marcolli introduce a substantially richer cokernel/cyclic-homology object and a scaling action when seeking Frobenius/Lefschetz-type structure.

A directed audit around semigroup coinvariants, positive transfer operators on `L^1/ell^1`, and block-sum/Perron--Frobenius operators found the expected broad classical transfer-operator literature but no reason to treat (4) as a new general functional-analytic theorem. The durable Mathia content is the exact classification of the specific quotient escape left by `WP-078`: for this pointed-cover trace-class representation, the universal transport-identifying quotient is **exactly trace and nothing more**.

## 7. Exact falsification surface

The result can be falsified by any of the following:

1. failure of the block-sum formula (1) for the `rho_n` used in `WP-078`;
2. a `j>=1` for which the telescoping identity (11) fails;
3. a trace-zero `ell^1` diagonal that cannot be approximated by finite trace-zero diagonals;
4. a nonzero class in the Hausdorff coinvariant quotient with zero trace;
5. a bounded linear degree-two-invariant readout on the diagonal trace ideal that is not proportional to ordinary trace;
6. a quotient satisfying the same universal transport-identification relation but retaining a nonzero mixed `M_n` class.

Items 2--6 are ruled out directly by the proof above.

The boundary is equally important. This finding does **not** rule out:

- a quotient on a larger non-diagonal operator or cohomological space where cover transport has nontrivial coinvariants;
- a selective geometric quotient that kills the mixed `M_n` without imposing `rho_n d=d` for every diagonal observable;
- higher homology/cohomology retaining information discarded by the zeroth coinvariant quotient;
- a nonlinear rank/volume mechanism such as `WP-030`;
- a genuinely nonseparable finite--archimedean coupling introduced before the quotient and before positivity is read out.

## Research consequence

`WP-078` showed that the direct Möbius primitive of the positive cover cocycle is indefinite off prime powers and listed a non-faithful quotient as one possible escape. `WP-079` closes the **canonical semigroup-coinvariant version** of that escape:

\[
\boxed{
\mathfrak D_1^{\rm sa}
/\overline{\langle\rho_nD-D\rangle}
\cong\mathbb R\operatorname{Tr}.
}
\]

The quotient does recover positive Mangoldt classes,

\[
[M_n]=\Lambda(n)[E_0]\ge0,
\]

but only after erasing every trace-zero operator direction. It therefore supplies no independent geometry capable of assembling the finite prime data with the archimedean/polar terms into Weil's quadratic form.

The pointed-cover frontier is now sharper: any surviving quotient/cohomological route must preserve **more than zeroth semigroup coinvariants of the diagonal defect algebra**. It must introduce nontrivial internal or noncommutative data before quotienting, and that extra structure must carry the missing finite autocorrelation and archimedean coupling while its positivity follows independently of RH or inserted zero data.
