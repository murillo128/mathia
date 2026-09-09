# PC-236 — equicontinuous fresh-fiber observables close in bilateral-shift calculus

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the growing-support / non-Laurent fresh-fiber escape left explicitly open by PC-235. At fixed coarse conductor `N`, a fresh prime `q` supplies the intrinsic fiber coordinate `z^N in mu_q`. PC-235 proves that every fixed Laurent polynomial in this coordinate becomes the corresponding finite Laurent polynomial in the bilateral packet shift `S`. The present result removes the fixed-degree hypothesis for every bounded equicontinuous family of fiber observables.

An exact finite-`q` observable `V_q(z^N)` may have a discrete Fourier/Laurent representation with `O(q)` nonzero shifts and degree growing all the way to `q-1`. Nevertheless, if the profiles `V_q:T->C` are uniformly bounded and equicontinuous, every subsequence has a further subsequence converging uniformly to some `V in C(T)`, and on the PC-227 source-forced packet state

\[
V_q(z^N)\longrightarrow V(S)
\]

in the packet limit. Thus every accumulation operator belongs to the single commutative algebra

\[
C^*(S)\cong C(\mathbb T).
\]

The apparent growth of the finite cyclic shift support is therefore not a new operator carrier: regular fresh-fiber observables are uniformly approximable by fixed Laurent degree before the limit. A particularly geometric non-Laurent example is the **unsquared fresh-fiber chord length** `|1-z^N|`. Its finite cyclic Fourier representation is genuinely long-range, but its packet limit is only

\[
|1-S|=(2I-S-S^{-1})^{1/2},
\]

a universal bounded convolution operator with spectrum `[0,2]`. Hence passing from the polynomial squared chord to the nonlocal chord-length functional calculus does not escape the classical bilateral-shift packet algebra.

This does **not** cover non-equicontinuous profiles resolving the `1/q` mesh, jump or singular symbols, inverse-chord singularities, regularizations whose modulus of continuity degenerates with `q`, simultaneous `N,q->infinity`, operators depending jointly on coarse and fresh coordinates, old/new geometry that mixes different packet centers, several genuinely noncommuting source coordinates, or the global uniformization/accessory sector.

## 1. Exact fresh-fiber functional calculus at finite level

Keep the notation of PC-227 and PC-235. Fix `N>1`, let `q \nmid N` be prime, put

\[
M=Nq,
\]

and let `Z_{N,q}` be multiplication on the full regular `M`-gon by the intrinsic fresh-fiber coordinate

\[
(Z_{N,q}F)(z)=z^N F(z).
\tag{1}
\]

Since `z^N` ranges over `mu_q`, `Z_{N,q}` is unitary and

\[
Z_{N,q}^q=I.
\tag{2}
\]

In the full Fourier basis PC-235 gives

\[
Z_{N,q}e_k=e_{k+N}.
\tag{3}
\]

For any continuous profile `V_q in C(T)`, define its exact finite-level fiber observable by continuous functional calculus,

\[
B_{N,q}:=V_q(Z_{N,q}).
\tag{4}
\]

Because the spectrum is the finite set `mu_q`, equation (4) is simply multiplication by `V_q(z^N)` in the vertex basis. After discrete Fourier transform it is a circulant operator on each fresh fiber. Equivalently there is an exact cyclic Laurent expansion

\[
\boxed{
B_{N,q}
=\sum_{h\in\mathbb Z/q\mathbb Z}
\widehat V_q^{(q)}(h) Z_{N,q}^{h},
}
\tag{5}
\]

where the coefficients are the discrete Fourier transform of the sampled values `V_q(mu_q)`.

There is no bounded-degree hypothesis in (5). For a generic non-polynomial profile essentially every one of the `q` cyclic shifts may occur. The question is whether that growing exact support creates a new fixed-base packet operator beyond PC-235.

## 2. Equicontinuity makes growing cyclic support uniformly finite-degree approximable

Assume

\[
\sup_q\|V_q\|_\infty<\infty
\tag{6}
\]

and that the family `{V_q}` is equicontinuous on `T`. By Arzela--Ascoli, from every sequence of fresh primes one can choose a subsequence, still denoted `q`, for which

\[
\boxed{
\|V_q-V\|_\infty\longrightarrow0
}
\tag{7}
\]

for some `V in C(T)`.

For every `epsilon>0`, the Stone--Weierstrass/Fejer approximation theorem supplies a Laurent polynomial of **fixed** degree,

\[
P(z)=\sum_{|h|\le H}p_hz^h,
\tag{8}
\]

such that

\[
\|V-P\|_\infty<\epsilon.
\tag{9}
\]

For all sufficiently large `q`, (7) then gives

\[
\|V_q-P\|_\infty<2\epsilon.
\tag{10}
\]

Continuous functional calculus for the finite-order unitary `Z_{N,q}` gives the exact operator-norm estimate

\[
\boxed{
\|V_q(Z_{N,q})-P(Z_{N,q})\|
=\max_{\omega\in\mu_q}|V_q(\omega)-P(\omega)|
\le2\epsilon.
}
\tag{11}
\]

Thus, although the exact discrete interpolant (5) may use `O(q)` shifts, its action is uniformly approximated by a Laurent operator with a degree `H` independent of `q`. Growing Fourier support alone is therefore not an asymptotically new degree of freedom inside the equicontinuous class.

## 3. Packet convergence upgrades fixed Laurent closure to all continuous profiles

Let

\[
\psi_q:=T_{N,q}e_u
\tag{12}
\]

be one exact-order source column of the normalized PC-227 transfer, along a fixed residue class `q mod N`, and use the same canonical packet identification as PC-227/PC-235. PC-227 proves

\[
\psi_q\longrightarrow
\psi
:=\bigoplus_{(a,t)}
\left(
\frac{C_{N,r}(a,t)}{j+\sigma_{a,t,r}}
\right)_{j\in\mathbb Z}
\tag{13}
\]

in `ell^2`, with only finitely many nonzero packet sectors at fixed `N`.

For every fixed Laurent polynomial `P`, PC-235 gives exactly

\[
P(Z_{N,q})\psi_q
\longrightarrow
P(S)\psi,
\qquad
(Sf)(j)=f(j+1).
\tag{14}
\]

On the bilateral shift, continuous functional calculus similarly gives

\[
\|V(S)-P(S)\|\le\|V-P\|_\infty<\epsilon.
\tag{15}
\]

Combining (11), (14), and (15), and using the bounded norms of the normalized transfer columns, yields

\[
\boxed{
V_q(Z_{N,q})\psi_q
\longrightarrow
V(S)\psi
}
\tag{16}
\]

under packet identification along every uniformly convergent profile subsequence. Since the exact-order source space has fixed dimension `phi(N)`, the same argument is columnwise Hilbert--Schmidt, hence operator-norm, convergence on the whole fixed source sector.

If `V_q=V` is one fixed continuous profile, no subsequence is needed. More generally, equicontinuity says that **every** possible accumulation model has the form `V(S)` for some continuous `V`; the set of accumulation operators is contained in

\[
\boxed{C^*(S)\cong C(\mathbb T).}
\tag{17}
\]

The isomorphism is the standard continuous functional calculus for the bilateral shift. It is commutative. Consequently, finitely many equicontinuous fresh-fiber observables retained jointly still have accumulation operators `V_1(S),...,V_m(S)` that commute, and products, adjoints, continuous functional calculus, and resolvents away from the spectrum remain inside the same algebra.

Equation (17) is the structural obstruction. A profile may still carry a scalar or continuous `q`-dependent coefficient supplied by some separate arithmetic construction; the theorem does not erase such coefficients. It says that **regular dependence on the intrinsic fresh coordinate does not create a new noncommutative or growing fixed-base operator carrier merely because its exact finite cyclic Fourier support grows with `q`**.

## 4. The unsquared chord is already a genuinely nonlocal control

PC-235 tests the squared anchored fresh-fiber chord

\[
|1-z^N|^2=2-z^N-z^{-N},
\tag{18}
\]

which is Laurent polynomial and becomes `2I-S-S^{-1}`. A natural concern is that this is too local in packet coordinate. The original circle geometry itself supplies a stronger control: keep the actual chord length

\[
\boxed{
V_{\rm chord}(z)=|1-z|.
}
\tag{19}
\]

This is continuous on `T` but not a Laurent polynomial. Its Fourier series has infinitely many nonzero coefficients,

\[
2|\sin(\theta/2)|
=
\frac4\pi-
\frac8\pi\sum_{h\ge1}
\frac{\cos(h\theta)}{4h^2-1},
\tag{20}
\]

so on the finite `q`-fiber its exact cyclic Fourier realization is genuinely long-range rather than a fixed-band mixer.

Nevertheless (16) applies directly and gives

\[
\boxed{
|1-Z_{N,q}|\,\psi_q
\longrightarrow
|1-S|\,\psi
=
(2I-S-S^{-1})^{1/2}\psi.
}
\tag{21}
\]

The bilateral shift has spectrum `T`, so spectral mapping gives

\[
\boxed{
\operatorname{Spec}(|1-S|)=[0,2].
}
\tag{22}
\]

This continuum is universal and prime-blind. It is not a discrete divisor, and no zeta zero set or critical-line condition is created. The source Cauchy packets still retain their cyclotomic amplitudes and fractional shifts from PC-227, but the nonlocal chord observable acts through the same universal commutative fiber calculus.

Thus the first exact geometry-forced example with infinitely many packet shifts already lies inside the closure (17). Replacing squared chord by chord length changes locality but not the operator species.

## 5. Stress tests and falsification controls

The theorem is deliberately stronger than a statement about one convenient Fourier truncation.

First, the exact discrete Fourier polynomial (5) is allowed to have degree proportional to `q`; no sparsity or uniform coefficient-support bound is assumed. Only the underlying sampled profile must have a uniform continuous modulus. This separates genuine fine-scale variation from the artificial growth of the interpolation degree on a denser cyclic mesh.

Second, the conclusion is stable under highly non-polynomial continuous profiles. Besides (19), any fixed continuous function of the chord variable `2-z-z^{-1}` belongs to the same algebra. Smoothness, analyticity, and absolute Fourier summability are unnecessary.

Third, an abstract non-arithmetic family of `ell^2` Cauchy packets with the same cyclic-to-bilateral local identification obeys exactly the same argument. The closure is a consequence of cyclic Fourier calculus plus uniform approximation, not of primality. Prime-Circle arithmetic enters through the source-forced packet state `psi`, not through the limiting regular fiber algebra.

Finally, the equicontinuity hypothesis is essential. For example symbols oscillating like `V_q(e^{i\theta})=e^{iq\theta}` are uniformly bounded but have no common modulus of continuity and can resolve the fresh mesh rather than being approximable by one fixed Laurent degree. Likewise approximations to a jump, an inverse chord, or a delta window can concentrate on scales shrinking with `q`. Such families are not claimed to classicalize by (16).

## 6. Prior art and novelty audit

The operator theory used here is classical. Philip J. Davis, *Circulant Matrices* (Wiley, 1979), is a standard reference for circulant matrices, cyclic convolution, and discrete-Fourier diagonalization. Yitzhak Katznelson, *An Introduction to Harmonic Analysis*, 3rd ed. (Cambridge University Press, 2004, DOI `10.1017/CBO9781139165372`), is a standard reference for Fourier analysis on the circle and locally compact abelian groups; uniform approximation of continuous circle functions by trigonometric/Laurent polynomials is classical Stone--Weierstrass/Fejer theory. The identification of the bilateral-shift C*-algebra with `C(T)` is standard continuous functional calculus for a unitary operator; modern operator-theory texts such as Garcia, Mashreghi and Ross, *Operator Theory by Example* (Oxford University Press, 2023, DOI `10.1093/oso/9780192863867.001.0001`) cover the surrounding shift and functional-calculus framework.

A directed search over circulant/group-algebra, harmonic-approximation, and shift-operator literature found no reason to regard the abstract ingredients of (5)--(17) as new; they are standard finite-cyclic and commutative C*-algebra machinery. No historical novelty is claimed for Arzela--Ascoli, Laurent approximation, circulant diagonalization, or the continuous functional calculus.

The durable Prime-Circle content is narrower: PC-227 supplies a very specific cyclotomic Cauchy-packet state, PC-235 identifies the intrinsic `z^N` coordinate with its bilateral packet shift, and equations (11)--(16) show that **even exact growing-support finite cyclic observables cannot exploit that state to create a new fixed-base carrier when their geometry stays uniformly regular in the fresh coordinate**. This directly closes one of the explicit escape clauses of PC-235 without assuming bounded Fourier degree.

No Riemann-zeta factor, completed functional equation, gamma factor, zero divisor, or distinguished real part `1/2` appears in this closure theorem. Adding one through the scalar profile `V_q` would be external unless independently forced by Prime-Circle geometry.

## 7. Consequence for the live Prime-Circle frontier

The route

\[
\boxed{
\text{PC-227 fixed-base fresh-prime packet}
\longrightarrow
\text{bounded equicontinuous function of }z^N
\longrightarrow
\text{growing exact cyclic Fourier support}
\longrightarrow
\text{new RH-facing operator carrier}
}
\]

is closed. Fixed Fourier degree was not the real obstruction in PC-235. The real boundary is **regularity at the fresh-fiber scale**: if the family has a common modulus of continuity, its entire growing discrete shift support collapses in the packet limit to the ordinary commutative bilateral-shift calculus `C^*(S)`.

The next tests should therefore not spend effort merely increasing the exact Laurent degree of a regular fiber observable. A surviving mechanism must use at least one feature excluded above: a `q`-scale or singular profile with a justified domain/renormalization; an operator coupling coarse and fresh coordinates before packet separation; source-forced old/new mode mixing that does not reduce to a function of `Z_{N,q}`; several noncommuting refinement coordinates retained jointly; simultaneous coarse/fresh conductor growth; or global uniformization/accessory data.