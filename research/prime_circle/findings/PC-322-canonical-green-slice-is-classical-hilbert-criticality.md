# PC-322 — canonical Green slice is classical Hilbert criticality

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the most natural finite intermediate Mordell–Tornheim exponent left open by PC-321.

PC-316 gives the canonical nonlinear cross-level packet

\[
Z_{q,r}^{f,g}(s,t,u)
=\sum_{k,l\ge1}\frac{a(k)b(l)}{k^s l^t(k+l)^u}.
\tag{1}
\]

PC-319/PC-320 show off-critical zeros near `u=0`, whereas PC-321 proves that the canonical `(5,7)` packet is zero-free on the right `(s,t)` polyhalf-plane for `Re(u)>=5`. A live question is therefore whether some finite intermediate exponent is selected by the original Poisson geometry rather than chosen after inspecting zeros.

The coefficient-free downstream Green operation selects exactly `u=1`. At that value the additive kernel is the classical Hilbert matrix. Moreover `u=1` is the exact real `ell^2` transition: `0<u<1` is unbounded, `u=1` is bounded noncompact, and `u>1` is Hilbert–Schmidt. The same representation produces a boundary `Re(s)=Re(t)=1/2`, but that boundary is shared by every nonzero periodic source. It is therefore standard Hilbert-space criticality, not Prime-Circle arithmetic and not a zero-selection theorem.

## 1. Ordinary downstream Green inversion selects `u=1`

For the PC-316 anchored field

\[
H_{q,r}^{f,g}(x,y,z)
=\sum_{k,l\ge1}a(k)b(l)e^{-kx-ly-(k+l)z},
\tag{2}
\]

the positive radial generator has output eigenvalue `k+l`. Hence the unweighted Green operation is

\[
\boxed{
\int_0^\infty H_{q,r}^{f,g}(x,y,z)\,dz
=\sum_{k,l\ge1}\frac{a(k)b(l)}{k+l}e^{-kx-ly}.
}
\tag{3}
\]

Mellinizing the remaining depths gives, in a safe right half-plane,

\[
\boxed{
\int_0^\infty\!\int_0^\infty
x^{s-1}y^{t-1}
\left(\int_0^\infty H(x,y,z)\,dz\right)dx\,dy
=\Gamma(s)\Gamma(t)Z_{q,r}^{f,g}(s,t,1).
}
\tag{4}
\]

Thus `u=1` is not fitted to a desired zero pattern: it is the ordinary inverse of the downstream number generator. The general factor `(k+l)^{-u}` is its fractional family,

\[
(k+l)^{-u}=\Gamma(u)^{-1}
\int_0^\infty z^{u-1}e^{-(k+l)z}\,dz,
\qquad \Re u>0.
\tag{5}
\]

This does not make `u=1` the unique conceivable nonlocal operator, but it makes it the cleanest coefficient-free intermediate slice to test after PC-321.

## 2. The additive kernel has an exact operator transition at `u=1`

For real `u>0`, define

\[
(K_u)_{kl}=(k+l)^{-u},\qquad k,l\ge1.
\tag{6}
\]

If `u>1`, then

\[
\|K_u\|_{\mathcal S_2}^2
=\sum_{n\ge2}(n-1)n^{-2u}<\infty,
\tag{7}
\]

so `K_u` is Hilbert–Schmidt and compact.

At `u=1`, reindexing `k=j+1`, `l=m+1` gives the generalized Hilbert matrix

\[
(K_1)_{jm}=\frac1{j+m+2}=:(H_2)_{jm}.
\tag{8}
\]

Hilbert's inequality makes `H_2` bounded on `ell^2`. PC-075 already proves `H_alpha-H_1 in S_1` for every `alpha>0`, while the Magnus–Rosenblum theory gives the noncompact continuous Hilbert channel for `H_1`. Therefore

\[
\boxed{
K_1\text{ is bounded and noncompact, with }
\sigma_{\rm ess}(K_1)=[0,\pi].
}
\tag{9}
\]

For `0<u<1`, let `x_k^{(N)}=N^{-1/2}` for `1<=k<=N` and zero otherwise. Then

\[
\langle x^{(N)},K_ux^{(N)}\rangle
\ge 2^{-u}N^{1-u}\longrightarrow\infty,
\tag{10}
\]

so `K_u` is unbounded. Hence the exact real phase diagram is

\[
\boxed{
0<u<1:\ \text{unbounded},\qquad
u=1:\ \text{bounded noncompact Hilbert},\qquad
u>1:\ \text{Hilbert--Schmidt}.
}
\tag{11}
\]

In (11), the labels mean the same exponent `u` as in (6): the middle case is `u=1` and the final case is `u>1`. No statement about zeros follows from this operator classification alone.

## 3. The `u=1` packet is a classical Hilbert matrix coefficient

Put

\[
v_a(s)=(a(k)k^{-s})_{k\ge1},\qquad
v_b(t)=(b(l)l^{-t})_{l\ge1}.
\tag{12}
\]

The Hilbert matrix defines a bounded complex-bilinear form `B(x,y)=sum_k x_k(K_1y)_k`, so wherever both vectors lie in `ell^2`,

\[
\boxed{
Z_{q,r}^{f,g}(s,t,1)=B(v_a(s),v_b(t)).
}
\tag{13}
\]

For a nonzero periodic sequence `a` of period `q`, let

\[
\mu_a=\frac1q\sum_{h=1}^{q}|a(h)|^2>0.
\tag{14}
\]

Then

\[
\|v_a(s)\|_2^2
=\sum_{k\ge1}|a(k)|^2k^{-2\Re s}.
\tag{15}
\]

Because `|a(k)|^2` is periodic with positive mean, its Dirichlet series has a simple pole at exponent `1` with residue `mu_a`. Consequently

\[
\boxed{
v_a(s)\in\ell^2\iff\Re s>\frac12,
\qquad
\|v_a(\sigma+i\tau)\|_2^2
\sim\frac{\mu_a}{2\sigma-1}
\quad(\sigma\downarrow\tfrac12).
}
\tag{16}
\]

The same holds for `b`. Equation (13) therefore gives a bounded-Hilbert-form continuation of the `u=1` slice to

\[
\boxed{\Re s>\frac12,\qquad\Re t>\frac12.}
\tag{17}
\]

For the canonical `(5,7)` sources, finite Fourier Parseval gives

\[
\mu_{a_5}=\frac45,\qquad
\mu_{b_7}=\frac5{14},
\tag{18}
\]

so both canonical source norms genuinely diverge at the same one-half boundary.

## 4. The one-half boundary is universal, not arithmetic

The matched control is decisive. Equation (16) holds for **every** nonzero periodic coefficient sequence, including arbitrary residue masks with no prime interpretation. Thus

\[
(c(k)k^{-s})_{k\ge1}\in\ell^2
\iff \Re s>\frac12
\tag{19}
\]

is a square-summability fact, not a Prime-Circle discriminator.

This is precisely the classical Hilbert space of Dirichlet series introduced by Hedenmalm–Lindqvist–Seip: square-summable Dirichlet coefficients naturally live on the half-plane `Re(s)>1/2`. The Prime-Circle source changes the vector inside that universal space, not the position of its boundary.

Nor is (13) a Hilbert–Pólya construction. `Z(s,t,1)` is a matrix coefficient of a fixed classical Hilbert operator between parameter-dependent vectors; its zeros are not eigenvalues of `K_1`. Boundedness supplies neither an `s <-> 1-s` functional equation nor any theorem forcing zeros onto the boundary where the vectors cease to belong to `ell^2`. Indeed the literal Hilbert-space realization fails on `Re(s)=1/2`; reaching that line requires a separate limiting or analytic-continuation prescription.

Therefore

\[
\boxed{
\text{Hilbert-space threshold at }\Re s=\tfrac12
\neq
\text{zero-selection theorem on }\Re s=\tfrac12.
}
\tag{20}
\]

The numerical coincidence cannot itself count as an RH bridge.

## 5. Prior art, consequence, and boundary

The load-bearing analysis is classical and already anchored in `research/prime_circle/SOURCES.md`: Magnus and Rosenblum for the Hilbert matrix, PC-075 for the Prime-Circle generalized-Hilbert reduction, and Hedenmalm–Lindqvist–Seip for square-summable Dirichlet-series Hilbert space and its `Re(s)>1/2` domain. Brevig–Perfekt–Seip–Siskakis–Vukotic provide an additional RH-adjacent warning that zeta/Dirichlet-series structure and Hilbert-type operators can coexist without yielding a Riemann-zero spectral realization. Directed literature search also returns the expected modern generalized-Hilbert and Hardy-space-of-Dirichlet-series treatments. No novelty is claimed for either threshold separately.

The durable Prime-Circle content is the exact combination: the most canonical coefficient-free intermediate Green slice of PC-316 lands **exactly** on classical Hilbert criticality, and its apparent one-half line survives matched non-arithmetic periodic controls. This closes the tempting implication

\[
\text{ordinary downstream Green inverse }(u=1)
\longrightarrow
\text{Hilbert threshold at }1/2
\longrightarrow
\text{RH critical-line mechanism}.
\tag{21}
\]

It does **not** determine the actual zero set of `Z_{5,7}(s,t,1)`, rule out every intermediate `0<u<5`, or exclude determinants/quotients made from several packets, a different source-forced kernel, or a growing-level construction. Any continuation of the intermediate-coupling branch must therefore produce a zero-sensitive invariant beyond the universal Hilbert-space boundary.

## Audit tests

The claim is falsified if any of the following fails: direct downstream integration must give `(k+l)^{-1}`; `K_1` must reindex to `H_2`; the Hilbert–Schmidt sum (7) and lower bound (10) must establish the phase transition; (13) must reconstruct the packet in an absolute-convergence region; and a nonzero arbitrary periodic matched source must exhibit the same `Re(s)=1/2` square-summability boundary. Passing these checks establishes only the operator/representation classicalization above, not a theorem about the zeros of the `u=1` slice.
