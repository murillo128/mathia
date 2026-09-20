# PC-375 — Unimodular Chebyshev branch twists have universal disk spectrum

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` for the most direct orientation/phase escape left open by PC-374. After the shell-2 refinement has reduced to the source-forced Chebyshev map and the endpoint singularity has selected the canonical half-density completion, keeping a unit-modulus phase on each inverse branch — including the intrinsic orientation sign of the branch — cannot create an arithmetic spectrum. On the invariant arcsine Hilbert space the resulting weighted transfer operator is the adjoint of a proper isometry, so its spectrum is exactly the closed unit disk for every degree and every measurable unimodular branch weight. On `Re(s)=1/2` the corresponding Jacobian-weighted operator is unitarily equivalent to this universal model after the same scalar degree normalization as PC-374.

This closes phase-only and orientation-only repairs of the canonical PC-372--PC-374 Chebyshev transfer. It does **not** classify non-unimodular amplitudes, cross-level matrix couplings, nonlinear shell interactions, different source-forced domains, or operators that leave the one-map Chebyshev/arcsine completion.

## 1. The branch-phase transfer is an adjoint weighted Koopman operator

Retain the source-forced shell-2 refinement of PC-372,

\[
C_m(\lambda)=\frac{1+T_m(2\lambda-1)}2,
\qquad m\ge2,
\tag{1}
\]

on the invariant arcsine space

\[
H_\mu=L^2\!\left((0,1),d\mu\right),
\qquad
d\mu(\lambda)=\frac{d\lambda}{\pi\sqrt{\lambda(1-\lambda)}}.
\tag{2}
\]

Let

\[
(V_mf)(\lambda)=f(C_m(\lambda)).
\tag{3}
\]

Because `C_m` preserves `mu`, `V_m` is an isometry. Its adjoint is the equal inverse-branch average

\[
(V_m^*g)(x)=\frac1m\sum_{C_m(y)=x}g(y)
\tag{4}
\]

for almost every interior `x`.

Now let `omega:(0,1)->C` be any measurable phase with

\[
|\omega|=1\quad\text{a.e.}
\tag{5}
\]

and define the phase-retaining branch transfer

\[
(P_{m,\omega}g)(x)
:=\frac1m\sum_{C_m(y)=x}\omega(y)g(y).
\tag{6}
\]

Then exactly

\[
\boxed{P_{m,\omega}=V_m^*M_\omega.}
\tag{7}
\]

Equivalently, with

\[
W_{m,\omega}:=M_{\overline\omega}V_m,
\tag{8}
\]

one has

\[
\boxed{P_{m,\omega}=W_{m,\omega}^*.}
\tag{9}
\]

Since `M_{bar omega}` is unitary and `V_m` is an isometry,

\[
W_{m,\omega}^*W_{m,\omega}=I.
\tag{10}
\]

Thus every unit-modulus branch decoration produces an adjoint isometry, independently of how irregular, arithmetic-looking, or orientation-sensitive the phase itself may be.

## 2. The isometry is always proper, with infinite shift defect

PC-374 uses the Chebyshev basis

\[
e_0=1,
\qquad
e_k(\lambda)=\sqrt2\,T_k(2\lambda-1),\quad k\ge1,
\tag{11}
\]

for which

\[
V_me_k=e_{mk}.
\tag{12}
\]

Therefore `Ran(V_m)` is a proper closed subspace: among the nonconstant Chebyshev modes it contains only indices divisible by `m`. Its orthogonal complement is infinite dimensional. Multiplication by the unitary `M_{bar omega}` preserves codimension, so

\[
\operatorname{Ran}(W_{m,\omega})
=M_{\overline\omega}\operatorname{Ran}(V_m)
\tag{13}
\]

is also a proper closed subspace with infinite-dimensional orthogonal complement. Hence

\[
\boxed{
\dim\ker W_{m,\omega}^*
=\dim\bigl(H_\mu\ominus\operatorname{Ran}W_{m,\omega}\bigr)
=\aleph_0.
}
\tag{14}
\]

The Wold decomposition of an isometry therefore gives

\[
W_{m,\omega}\simeq S^{(\aleph_0)}\oplus U_{m,\omega},
\tag{15}
\]

where `S` is the unilateral shift and `U_{m,omega}` is a possibly absent unitary part. Purity is not needed. The nonzero shift summand already forces the full closed disk into the spectrum of the adjoint, while the norm bound gives the reverse inclusion. Consequently

\[
\boxed{
\sigma(P_{m,\omega})
=\sigma(W_{m,\omega}^*)
=\overline{\mathbb D}
}
\tag{16}
\]

for every `m>=2` and every measurable unimodular `omega`.

This is stronger than saying that a particular phase is removable by a pointwise gauge. Even a phase that is not removed by the smooth coboundary mechanism of PC-373 still has the same complete spectrum on the canonical Hilbert completion.

## 3. The critical-line Jacobian family remains the same disk

Let

\[
h(\lambda)=2\sqrt{\lambda(1-\lambda)}.
\tag{17}
\]

PC-373 proved the exact derivative identity

\[
|C_m'(y)|
=m\,\frac{h(C_m(y))}{h(y)}.
\tag{18}
\]

Decorate the natural Jacobian transfer by the same branch phase:

\[
(\mathcal L^{\omega}_{m,s}f)(x)
:=\sum_{C_m(y)=x}
\omega(y)|C_m'(y)|^{-s}f(y).
\tag{19}
\]

Using (18) and the definition (6),

\[
\boxed{
\mathcal L^{\omega}_{m,s}
=m^{1-s}M_{h^{-s}}P_{m,\omega}M_{h^s}.
}
\tag{20}
\]

PC-374 identifies, for `Re(s)=1/2`, the unitary half-density map

\[
J_s=\sqrt{\frac\pi2}\,M_{h^s}:
L^2((0,1),d\lambda)\longrightarrow H_\mu.
\tag{21}
\]

Hence on the critical half-density line,

\[
\boxed{
m^{s-1}\mathcal L^{\omega}_{m,s}
=J_s^{-1}P_{m,\omega}J_s.
}
\tag{22}
\]

Combining (16) and (22) yields

\[
\boxed{
\sigma\!\left(m^{s-1}\mathcal L^{\omega}_{m,s}\right)
=\overline{\mathbb D},
\qquad \operatorname{Re}s=\frac12,
}
\tag{23}
\]

and therefore, as an unnormalized set,

\[
\boxed{
\sigma(\mathcal L^{\omega}_{m,s})
=\sqrt m\,\overline{\mathbb D},
\qquad \operatorname{Re}s=\frac12.
}
\tag{24}
\]

The disk is independent of `Im(s)` and of the complete branch-phase field. Thus retaining phase at exactly the point where PC-374 produced the suggestive half-density line still supplies no zeta ordinates, no discrete divisor, and no arithmetic distinction between prime and composite refinement degrees.

## 4. The intrinsic orientation sign is included and is not the PC-373 coboundary

A source-forced phase requiring no arbitrary choice is the branch orientation

\[
\omega_m(y)=\operatorname{sgn}C_m'(y),
\tag{25}
\]

with arbitrary unit-modulus values assigned on the finite critical set where the derivative vanishes. This keeps information discarded when PC-373 passed from `C_m'` to `|C_m'|`.

It is worth separating this orientation field from the positive endpoint coboundary already classified there. For `m=3`, the interior point `lambda=1/2` is fixed by `C_3` and

\[
C_3'(1/2)=-3,
\qquad
\omega_3(1/2)=-1.
\tag{26}
\]

Therefore `omega_3` cannot be represented pointwise on the full interior dynamics as a nonvanishing multiplicative coboundary `u/(u o C_3)`: at a fixed point every such coboundary equals `1`. This does **not** claim an obstruction to an almost-everywhere measurable coboundary, since one periodic orbit has measure zero. It only shows that the intrinsic sign twist is a genuine escape from the smooth/pointwise positive gauge identity of PC-373.

Nevertheless (16) applies without asking whether the phase is a coboundary at all. The orientation-retaining transfer still has exactly the universal disk spectrum. Thus the failure is spectral, not merely a consequence of having chosen a removable phase.

## 5. Matched non-prime controls are exact

No part of (7)--(24) uses primality. For every integer `m>=2` and every measurable unimodular branch field, the same proper-isometry argument gives the same normalized disk. In particular, replacing a prime degree `p` by a composite degree, by `2p`, or by an unrelated integer changes neither the half-density line nor the normalized spectrum.

This is the decisive matched control required by the Prime-Circle mandate. The architecture

\[
\text{Chebyshev refinement}
+\text{half-density endpoint completion}
+\text{branch phase/orientation}
\]

is entirely generic to the expanding polynomial map and its invariant measure. It does not retain primitive/new-vertex arithmetic at the spectral level.

## 6. Prior-art and novelty audit

The abstract operator ingredients are classical. Weighted Frobenius--Perron operators are standard adjoints/preduals of weighted Koopman or composition operators; see M. R. Jabbarzadeh and R. Hajipouri, *Weighted Frobenius-Perron operators and their spectra*, **Mathematica Bohemica** 142 (2017), 113--124, DOI `10.21136/MB.2016.0079-15`. The Wold decomposition of an isometry into unilateral-shift and unitary parts is classical, and PC-209/PC-244 already used it elsewhere in the Prime-Circle line for Hardy weighted-cover operators.

Signed transfer operators can carry genuine number-theoretic information in other dynamical systems and other function spaces. A relevant warning is C. Bonanno, S. Graffi and S. Isola, *Spectral analysis of transfer operators associated to Farey fractions*, **Rendiconti Lincei - Matematica e Applicazioni** 19 (2008), 1--23, DOI `10.4171/RLM/505`, and the later Bonanno--Isola work connecting signed Farey transfer operators to Ruelle/Selberg zeta functions. Therefore PC-375 is **not** a general claim that signs in transfer operators are spectrally trivial.

The project-local negative is narrower and exact: after PC-372--PC-374 force the Chebyshev map, arcsine invariant measure and half-density completion, *every unimodular inverse-branch decoration* lands in the adjoint-of-a-proper-isometry class, whose spectrum is already fixed to the disk. The literature search did not reveal a Prime-Circle/RH mechanism hidden in this specialization, but the conclusion does not rely on absence of prior art; equations (7)--(24) prove the obstruction directly.

No new `SOURCES.md` dependency is required for the proof: the load-bearing operator theorem is the same classical Wold machinery already used in PC-209/PC-244, while the weighted-transfer references above serve only to place the operator class and signed-transfer comparison in established literature.

## 7. Sharp boundary of the no-go

PC-375 rules out a broad but precise family: keep the canonical one-map Chebyshev refinement, stay on its canonical arcsine/half-density `L^2` completion, and attempt to recover lost branch information only through a unit-modulus factor before inverse-branch averaging. Within that class, arbitrary phase complexity cannot change the normalized spectrum.

The theorem does not cover:

- non-unimodular branch amplitudes that change norms rather than phases;
- finite- or infinite-dimensional shell labels coupled across different conductors before reduction to one Chebyshev map;
- sums of different refinement directions whose relative ranges cannot be represented by one weighted isometry;
- nonlinear phase selection or source-dependent domains/boundary conditions;
- genuinely two-dimensional operators that retain several shell coordinates simultaneously;
- analytic function spaces whose compact/nuclear transfer spectra are not the canonical `L^2(mu)` completion classified here.

Those are changes of mechanism rather than loopholes in (16) or (23).

## 8. Falsification checks

The claim has direct exact tests.

1. On the Chebyshev basis verify `V_m e_k=e_{mk}` and hence that `Ran(V_m)` has infinite codimension.
2. For any sampled unit-modulus `omega`, verify `W_{m,omega}^*W_{m,omega}=I`; a failure would contradict only the assumption `|omega|=1` or measure invariance.
3. Verify `P_{m,omega}=W_{m,omega}^*` from the inverse-branch conditional expectation formula.
4. Any proper isometry has a nonzero unilateral-shift Wold summand; since the defect here is infinite dimensional, the backward-shift disk is unavoidable.
5. Insert (18) into (19) and recover (20); on `Re(s)=1/2`, conjugate with `J_s` to obtain (22).
6. Repeat for a composite degree `m` and an arbitrary non-arithmetic phase. The normalized spectrum must remain the same closed disk.

A counterexample inside these hypotheses would have to violate one of these explicit identities. A discrete or zeta-sensitive spectrum obtained only after changing the function space, amplitude class, domain, or cross-level architecture lies outside the theorem rather than refuting it.

## Research consequence

PC-374 showed that the natural endpoint completion turns the apparent critical line into a universal half-density gauge. PC-375 closes the most immediate attempt to restore arithmetic information without leaving that completion: **even branch orientation and arbitrary unimodular phase survive pointwise but disappear from the complete normalized spectrum.** A viable continuation must therefore change more than the phase of the canonical inverse-branch transfer; it must introduce a source-forced amplitude, domain, cross-shell coupling, or non-Chebyshev structure that is not the adjoint of one proper weighted isometry.