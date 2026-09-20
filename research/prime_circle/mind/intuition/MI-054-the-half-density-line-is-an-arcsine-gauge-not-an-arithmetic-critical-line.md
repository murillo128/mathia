# MI-054 — The half-density line and unimodular branch phases are universal Chebyshev gauges, not arithmetic spectrum

**Evidence level:** exact synthesis from PC-371--[PC-375](../../findings/PC-375-unimodular-chebyshev-branch-twists-have-universal-disk-spectrum.md). The conclusion classifies the canonical Chebyshev/arcsine endpoint completion and its unimodular branch decorations; it does not rule out source-forced amplitudes, domains or cross-shell couplings that leave this class.

PC-371--PC-372 isolate genuine shell-2 radial order but identify its natural refinement law with the real-cyclotomic/Chebyshev tower. PC-373 shows that the canonical derivative weight carries no extra arithmetic: for `h(lambda)=2 sqrt(lambda(1-lambda))`, the Chebyshev Jacobian is a degree scalar times the multiplicative coboundary `h(C_m(lambda))/h(lambda)`.

PC-374 asks whether the natural singular endpoint `L^2` completion can nevertheless turn that geometry into a meaningful critical line. The invariant arcsine measure satisfies `dmu=2/(pi h(lambda)) dlambda`. Multiplication by `h(lambda)^s` transports ordinary `L^2(dlambda)` unitarily to `L^2(dmu)` exactly when `Re(s)=1/2`. The apparent critical line is therefore the half-density exponent of the Radon--Nikodym change of measure. On that line the normalized transfer is conjugate to the adjoint of Chebyshev composition and has the closed unit disk as spectrum for every integer degree, not only primes.

PC-375 tests the obvious information-restoring escape: keep a unit-modulus phase on each inverse branch, including the intrinsic orientation sign discarded by the absolute Jacobian. For any measurable `|omega|=1`, the branch transfer is `P_{m,omega}=V_m^* M_omega=W_{m,omega}^*`, where `W_{m,omega}=M_{bar omega}V_m` is a proper isometry. Its range has infinite codimension, so the Wold shift part forces

`sigma(P_{m,omega}) = closed unit disk`

for every `m>=2` and every such phase. On `Re(s)=1/2`, the Jacobian-weighted phase transfer is unitarily equivalent to the same operator after the canonical degree normalization. Even a phase that is not removed by the smooth positive coboundary therefore fails to change the complete normalized spectrum.

This closes a broad false-positive class. Neither the visual appearance of a critical `1/2` line nor survival of branch orientation/phase pointwise is arithmetic evidence when the completed operator is still one proper weighted Chebyshev isometry. The matched composite-degree control is exact and has the same disk.

The remaining source-sensitive possibilities must change more than phase: non-unimodular amplitudes, source-forced domains or boundary conditions, cross-level matrix couplings, nonlinear shell interactions, several refinement coordinates retained simultaneously, or a function/operator category not reducible to the canonical `L^2(mu)` weighted-isometry model. Each such candidate must still be tested against non-prime refinement controls.

**Boundary.** PC-374--PC-375 do not classify those mechanism changes. In particular they do not claim that signs or phases are spectrally trivial for transfer operators in general; the no-go is specific to the source-forced Chebyshev map, arcsine half-density completion and unimodular inverse-branch decoration considered here.
