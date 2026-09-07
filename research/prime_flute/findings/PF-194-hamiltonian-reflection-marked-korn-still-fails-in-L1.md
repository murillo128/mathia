# PF-194 — Hamiltonian reflection marking does not restore strong `L^1` collar rigidity

**Status:** `LITERATURE+DERIVED + EXACT-LOCAL + DECISIVE-NEGATIVE/ROUTE-BOUNDARY`. PF-192 shows that unconstrained strong-`L^1` geometric rigidity fails, while PF-193 shows that exact determinant one does not remove the bad CFM mechanism at the finite-laminate level. The remaining tempting escape was that the simultaneous **map-level** constraints actually present on the normalized prime-flute collar — exact area preservation, zero annular flux, zero-twist reflection marking, and near-identity support — might restore a generic strong endpoint estimate. They do not. Ornstein's `L^1` non-inequality, applied to a Hamiltonian stream function, gives compactly supported divergence-free reflection-equivariant vector fields on the fixed PF-185 collar slab for which the full gradient is arbitrarily larger in `L^1` than the symmetric gradient. Taking sufficiently short Hamiltonian flows upgrades this infinitesimal obstruction to smooth exact-area reflection-equivariant diffeomorphisms, arbitrarily `C^1`-close to the identity and equal to the identity near the boundary, whose `W^{1,1}` displacement is arbitrarily larger than their `L^1` metric strain. Thus there is no generic `r=1` analogue of PF-185's marked rigidity estimate even after imposing the natural conservative/marking constraints. This does **not** refute an endpoint splice theorem exploiting the special canonical PF-179--PF-184 boundary germ, because an arbitrary interior Hamiltonian oscillation may be discarded by a splice that only has to match the outer germ.

## Claim

Let

\[
A=[1,5/4]\times\mathbb R/\mathbb Z,
\qquad
a_L(x)=L^2+x^2,
\qquad
g_L=\frac{dx^2}{a_L(x)}+a_L(x)\,d\theta^2,
\tag{1}
\]

for any fixed `0<=L<=mu_*`, and let

\[
R(x,\theta)=(x,-\theta)
\tag{2}
\]

be the zero-twist reflection. The hyperbolic area form in these coordinates is exactly

\[
\omega=dx\wedge d\theta.
\tag{3}
\]

Then for every `K>0` there is a smooth compactly supported vector field

\[
u\in C_c^\infty(\operatorname{int}A;TA)
\tag{4}
\]

such that

\[
\mathcal L_u\omega=0,
\qquad
u(Rz)=DR_z\,u(z),
\qquad
\iota_u\omega=-d\Psi
\tag{5}
\]

for a compactly supported smooth Hamiltonian `Psi`, and

\[
\boxed{
\|\nabla^{g_L}u\|_{L^1(A,g_L)}
>
K\,\|\operatorname{Def}_{g_L}u\|_{L^1(A,g_L)}.
}
\tag{6}
\]

Consequently no constant `C`, even depending on the fixed collar metric, can make

\[
\|u\|_{W^{1,1}(A,g_L)}
\le C\,\|\operatorname{Def}_{g_L}u\|_{L^1(A,g_L)}
\tag{7}
\]

hold on the reflection-marked Hamiltonian subspace. In particular the uniform `1<r<infinity` estimate of PF-185 has no strong-`L^1` endpoint specialization.

There is also a nonlinear exact-area form. For every `K>0` and every prescribed `C^1` neighborhood `U` of the identity there is a smooth diffeomorphism

\[
H:A\to A
\tag{8}
\]

such that

1. `H` is Hamiltonian/exact symplectic for `omega`, hence area preserving with zero annular flux;
2. `H=id` on a neighborhood of `partial A`;
3. `HR=RH`;
4. `H in U`;
5. in the fixed PF-185 coordinate chart,

\[
\boxed{
\|H-\operatorname{id}\|_{W^{1,1}(A,g_L)}
>
K\,\|\delta_{g_L,H^*g_L}\|_{L^1(A,g_L)}.
}
\tag{9}
\]

Thus exact area, reflection marking, zero flux, boundary identity, and even arbitrarily small `C^1` displacement do not by themselves restore an energy-linear strong-`L^1` rigidity theorem.

## 1. Ornstein reduces the constrained linear problem to one scalar Hessian identity

On the Euclidean plane write a compactly supported Hamiltonian field as

\[
u=J\nabla\psi=(-\psi_y,\psi_x),
\qquad
\psi\in C_c^\infty(\mathbb R^2).
\tag{10}
\]

Then `div u=0` and `i_u(dx wedge dy)=-dpsi`. Put

\[
D^2\psi=
\begin{pmatrix}
a&b\\
b&c
\end{pmatrix}.
\tag{11}
\]

A direct calculation gives

\[
Du=
\begin{pmatrix}
-b&-c\\
a&b
\end{pmatrix},
\qquad
\operatorname{Def}u
=
\begin{pmatrix}
-b&(a-c)/2\\
(a-c)/2&b
\end{pmatrix}.
\tag{12}
\]

Therefore

\[
|Du|^2=a^2+2b^2+c^2=|D^2\psi|^2,
\tag{13}
\]

while

\[
|\operatorname{Def}u|^2
=2b^2+\frac12(a-c)^2.
\tag{14}
\]

So the full Hamiltonian gradient is exactly the full Hessian, whereas its strain sees only the trace-free Hessian components `psi_xy` and `psi_xx-psi_yy`.

Suppose a strong endpoint Korn estimate existed on all such fields:

\[
\|Du\|_1\le C\|\operatorname{Def}u\|_1.
\tag{15}
\]

Equations (13)--(14), together with `|Delta psi|<=sqrt(2)|D^2 psi|`, would imply an estimate of the form

\[
\|\Delta\psi\|_{L^1}
\le C'
\left(
\|\psi_{xx}-\psi_{yy}\|_{L^1}
+
\|\psi_{xy}\|_{L^1}
\right)
\tag{16}
\]

for every compactly supported smooth scalar `psi`.

Ornstein's theorem rules out (16). For homogeneous constant-coefficient differential operators of the same order, an `L^1` estimate of one operator by finitely many others can hold only if the first operator is a constant linear combination of the others. But

\[
\partial_{xx}+\partial_{yy}
\notin
\operatorname{span}
\{\partial_{xx}-\partial_{yy},\partial_{xy}\}:
\tag{17}
\]

comparing the `partial_xx` and `partial_yy` coefficients would require the same scalar to equal both `1` and `-1`. Hence (16), and therefore (15), is impossible. Equivalently, for every `K` there is a compactly supported smooth Hamiltonian field with

\[
\|Du\|_1>K\|\operatorname{Def}u\|_1.
\tag{18}
\]

This is not a new form of Ornstein's theorem. It is the exact two-dimensional stream-function specialization relevant to the conservative PF collar.

## 2. Reflection marking does not remove the Ornstein sequence

Let `S(x,y)=(x,-y)`. Start with a bad stream function from (18), translate and rescale it into a disk `B_+` disjoint from the reflection axis, and choose `B_+` so that `B_-=S(B_+)` is disjoint. Define

\[
\widetilde\psi(z)=\psi_+(z)-\psi_+(Sz).
\tag{19}
\]

Then

\[
\widetilde\psi(Sz)=-\widetilde\psi(z).
\tag{20}
\]

For `\widetilde u=J nabla \widetilde\psi`, (20) gives

\[
\widetilde u(Sz)=DS_z\,\widetilde u(z):
\tag{21}
\]

the first component is even and the second odd, exactly the PF-142/PF-185 marking parity. Because the two supports are disjoint and reflection is orthogonal, both sides of (18) are simply doubled. The arbitrarily bad ratio is unchanged.

Thus the reflection condition kills the **finite-dimensional Killing mode** at `r>1`, as PF-185 proves, but it cannot cure Ornstein's infinite-dimensional endpoint failure. The two statements are compatible: PF-185 removes the kernel of the symmetric-gradient operator, while PF-194 shows that injectivity modulo that kernel is not enough for an `L^1` coercive estimate.

## 3. The Euclidean obstruction localizes inside every normalized PF collar

The family (1) is uniformly smooth and elliptic on the fixed thick slab. Fix an interior point

\[
z_+=(x_0,1/4)
\tag{22}
\]

and its reflected point `z_-=Rz_+`. Put `a_0=L^2+x_0^2` and use the same area-preserving orthonormal linear frame as PF-186,

\[
B_L=\operatorname{diag}(\sqrt{a_0},a_0^{-1/2}),
\qquad
\det B_L=1,
\qquad
B_L^Tg_L(z_+)B_L=I.
\tag{23}
\]

The matrices `B_L,B_L^{-1}` remain uniformly bounded for `0<=L<=mu_*` and commute with the local reflection derivative. Insert the reflected Euclidean stream function from Section 2 into the two patches at scale `rho`, using

\[
\Psi_{\rho,L}(z)
=
\rho^2\widetilde\psi\!\left(
\frac{B_L^{-1}(z-z_+)}{\rho}
\right)
\tag{24}
\]

on the positive patch and the exact odd reflected copy on the negative patch. Because `det B_L=1` and the collar area form is exactly (3), the resulting vector field

\[
u_{\rho,L}=J\nabla\Psi_{\rho,L}
\tag{25}
\]

is **exactly Hamiltonian** for the PF area form, not merely divergence-free up to an error. It is compactly supported away from the annulus boundary and satisfies (21) with `S` replaced by `R`.

After division by the common area factor `rho^2`, the covariant-gradient and strain integrals converge to their Euclidean values as `rho->0`:

\[
\rho^{-2}\|\nabla^{g_L}u_{\rho,L}\|_1
=
\|D\widetilde u\|_1+O(\rho C_{\widetilde u}),
\tag{26}
\]

\[
\rho^{-2}\|\operatorname{Def}_{g_L}u_{\rho,L}\|_1
=
\|\operatorname{Def}\widetilde u\|_1+O(\rho C_{\widetilde u}).
\tag{27}
\]

The error comes only from smooth metric variation and the connection term, whose coefficient multiplies a vector field of amplitude `O(rho)`. For a fixed Ornstein test field all relevant smooth norms are finite, so one first chooses its Euclidean ratio and then sends `rho` sufficiently small. The compactness of the metric family makes the localization constants uniform in `L`, although only the fixed-`L` conclusion is needed to refute an endpoint Korn estimate.

Equations (18), (26), and (27) prove (6). Since the `L^1` norm of the localized vector field itself is lower order under the same scaling, they also rule out (7).

## 4. Short Hamiltonian flow gives an exact-area nonlinear counterexample

Let `u` be one of the compactly supported reflection-equivariant Hamiltonian fields obtained above and let `H_t` be its flow. Every `H_t` is a smooth Hamiltonian diffeomorphism, hence

\[
H_t^*\omega=\omega
\tag{28}
\]

exactly; it equals the identity near the boundary, has zero annular flux, and commutes with `R` because its generating vector field does.

For this fixed smooth `u`, standard flow expansion on the compact slab gives as `t->0`

\[
H_t=\operatorname{id}+t u+O_u(t^2)
\quad\text{in }C^1,
\tag{29}
\]

and the first variation of the metric is

\[
H_t^*g_L-g_L
=t\,\mathcal L_u g_L+O_u(t^2)
=2t\,\operatorname{Def}_{g_L}u+O_u(t^2).
\tag{30}
\]

Inside a sufficiently small fixed quasi-isometry neighborhood, the multiplicative deviation `delta` used in PF-175/PF-185 is uniformly equivalent to the norm of the relative metric tensor. Therefore

\[
\|H_t-\operatorname{id}\|_{W^{1,1}}
\ge
t\|\nabla^{g_L}u\|_1-C_u t^2,
\tag{31}
\]

while

\[
\|\delta_{g_L,H_t^*g_L}\|_1
\le
C_0t\|\operatorname{Def}_{g_L}u\|_1+C_u t^2.
\tag{32}
\]

Choose the linear ratio in (6) much larger than `K C_0`, then choose `t` small enough that the quadratic remainders are negligible. This proves (9). Shrinking `t` further puts `H_t` in any prescribed `C^1` neighborhood of the identity.

This nonlinear step is important for interpreting PF-193. The specific question of realizing the transported CFM laminate by an incompressible gradient may remain open, but it is no longer needed to answer the generic rigidity question: there are already smooth **map-level** exact-area, zero-flux, reflection-marked near-identity diffeomorphisms for which strong `L^1` metric rigidity has arbitrarily bad constant.

## 5. Why this still does not kill the canonical PF endpoint splice

PF-194 is a route boundary, not a no-go theorem for the actual prime/shift body map. The constructed Hamiltonian oscillation is compactly supported in the interior of the normalized slab and is the identity near both boundary circles. A splice whose only obligation is to equal the identity on the inner germ and match the **outer boundary germ** may simply discard such an artificial interior oscillation. Therefore (9) does not prove that every exact-area interpolation between the canonical PF-177 collar gauge and the PF-179--PF-184 outer germ has large cost.

What it does prove is that the missing `r=1` step cannot be a generic analogue of PF-185's whole-germ estimate based only on

\[
\text{small metric strain}
+\text{ exact area/zero flux}
+\text{ reflection marking}
+\text{ near-identity chart entry}.
\tag{33}
\]

Those hypotheses already hold for the counterexamples. A strong endpoint proof must use **source-specific canonical information that constrains the outer germ or permits a direct boundary-to-boundary conservative extension**, rather than first controlling the entire raw germ in `W^{1,1}`. Alternatively, the weak/Lorentz route in `CLUE-weak-trace-reassembly-with-summable-local-mass.md` avoids asking for a false generic strong endpoint coercivity theorem.

This also cleanly separates PF-186 from PF-194. PF-186 shows that tiny metric strain need not force entry into a fixed `C^1` chart because order-one micro-rotations can hide on small scales. PF-194 shows that **even after one is already arbitrarily close in `C^1`**, strong `L^1` linear coercivity fails. The two obstructions attack different stages of the high-regularity route.

## Prior art and novelty assessment

**D. Ornstein**, *A non-equality for differential operators in the `L^1` norm*, Archive for Rational Mechanics and Analysis **11** (1962), 40--49. DOI `10.1007/BF00253928`. Ornstein's theorem is the authoritative source for the same-order constant-coefficient `L^1` non-inequality used in (16)--(18).

**K. Kazaniecki, D. M. Stolyarov, M. Wojciechowski**, *Anisotropic Ornstein noninequalities*, Analysis & PDE **10** (2017), 351--366. DOI `10.2140/apde.2017.10.351`; arXiv:1505.05416. Their introduction states the isotropic Ornstein criterion in exactly the form used here: if one homogeneous constant-coefficient differential operator of a fixed order is `L^1`-controlled by finitely many others of the same order, it must be their linear combination. They also note that the framework extends to vector-valued operators, although PF-194 needs only the scalar second-order case.

**D. Faraco, A. Guerra**, *Remarks On Ornstein's Non-Inequality In `R^{2x2}`*, Quarterly Journal of Mathematics **73** (2022), 17--21. DOI `10.1093/qmath/haab016`. This gives a concise two-dimensional proof of the first- and second-order Ornstein non-inequality by a three-point laminate and is nearby modern prior art for the two-dimensional endpoint mechanism.

No novelty is claimed for Ornstein's theorem, stream-function parametrization of divergence-free fields, Hamiltonian flows, or localization of a constant-coefficient counterexample in a smooth Riemannian chart. The project-specific deduction is the exact conjunction of these classical facts with the PF normalized collar: **the conservative and reflection-marked constraints that survive PF-142/PF-184 do not restore the strong `L^1` rigidity estimate needed by a naive endpoint continuation of PF-185.** A targeted literature search did not locate an authoritative theorem stated in this exact prime-flute collar language; that absence is not a novelty claim.

## Falsification and boundary checks

A later adversary can test the finding through a short chain:

1. verify the exact matrix identities (12)--(14);
2. verify that a hypothetical Hamiltonian Korn estimate implies (16);
3. apply Ornstein's same-order theorem and check the symbol non-membership (17);
4. antisymmetrize the stream function across reflection and check that disjoint support preserves the bad ratio and yields the PF parity (21);
5. use the area-preserving orthonormal frame (23) and standard small-chart localization to verify (26)--(27);
6. integrate the Hamiltonian vector field and verify (28)--(32), choosing the bad vector field before the small flow time;
7. keep the boundary of the conclusion explicit: the example is an arbitrary admissible interior Hamiltonian perturbation, not the canonical PF-179--PF-184 outer germ.

The finding would be overclaimed if read as any of the following, none of which is asserted:

- the exact PF-183 endpoint conservative splice is impossible;
- the canonical prime/shift relative germ realizes an Ornstein microstructure;
- every boundary-to-boundary exact-area extension has bad `L^1` cost;
- weak-`L^1` geometric control is already sufficient for weak-`S_1` resolvent reassembly;
- the specific determinant-one CFM laminate of PF-193 has now been realized as a gradient distribution;
- any spectral, scattering, determinant, zeta, or RH conclusion follows.

## Consequences for the research line

PF-192 removed generic unconstrained strong-`L^1` rigidity; PF-193 removed determinant one as a laminate-level cure; PF-194 now removes **Hamiltonian exactness, zero flux, reflection marking, boundary identity, and near-identity chart entry as a generic map-level cure**. The remaining strong endpoint route is therefore genuinely canonical: it must use the special source/target boundary trace or another structural property of the assembled prime/shift germ that arbitrary Hamiltonian perturbations do not share.

For the active weak-trace program this is a useful pruning result. PF-191's summable endpoint coefficient mass remains available, but one should not spend effort proving a whole-germ strong `W^{1,1}` estimate from the already-persisted conservative/marking hypotheses. The sharper alternatives are a direct energy-linear conservative extension theorem for the **canonical outer germ**, or a weak/Lorentz localization and operator reassembly that never requires the false generic strong endpoint coercivity step.