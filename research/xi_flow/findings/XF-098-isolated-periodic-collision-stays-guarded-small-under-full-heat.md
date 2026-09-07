# XF-098 — an isolated periodic collision stays guarded-small under full heat

**Status:** `EXACT-DERIVED` + `NEGATIVE/OBSTRUCTION` + `MATCHED-CONTROL` + `COLLISION-SAFE` + `LITERATURE-CALIBRATED`. XF-097 closes the source-to-periodic-carrier transport gate in the exact guarded resource, leaving a transition-side coercivity problem: show that a hypothetical positive-`Lambda` transition forces order-one mass in that same destination band. The first candidate mechanism is a collision itself. This finding gives an exact periodic countercontrol showing that this is too weak.

There is a real-rooted periodic backward-heat trajectory whose threshold occurs at a single simple double collision, yet for every fixed positive heat time its entire low-frequency prefix `1 <= m <= K` has guarded selector resource `o(1)` on the current Mathia scales. More generally, any bounded sparse displacement of the arithmetic lattice with total displacement `A_1` below an explicit threshold stays guarded-small for fixed heat time under the **full nonlinear log-Vieta Burgers system**. Thus a transition theorem after XF-097 cannot be based only on the existence of a collision, real-root preservation, or exact periodic heat. It must force a genuinely collective Xi-specific defect, or change the destination observable.

## 1. A one-defect lattice is an exact simple-collision transition control

Use the periodic carrier of XF-067/XF-071 with

\[
N=2M,
\qquad
x_j=sj,
\qquad
L=Ns,
\qquad
\nu_j=e^{2\pi i x_j/L}=e^{2\pi i j/N}.
\tag{1}
\]

Start from the arithmetic lattice and move the node `j=1` onto `j=0`. Modulo one period the root multiset is therefore

\[
\boxed{
\{0,0,2s,3s,\ldots,(N-1)s\}.
}
\tag{2}
\]

The trigonometric product `G` of XF-067 has one zero of exact multiplicity two at `0` and all other zeros in a period are simple. Hence the collision is a simple double collision in the sense of XF-002. If its heat time is normalized so that the collision occurs at `t=0`, XF-002 gives the local discriminant law

\[
D(t)=8t+O(t^2).
\tag{3}
\]

Thus the colliding pair is nonreal for all sufficiently small `t<0` and splits into two real zeros for `t>0`.

The global real side is not an extra assumption. Backward heat preserves real-rooted trigonometric polynomials; Kabluchko (2025), already anchored in `SOURCES.md`, records this explicitly and derives it from the Pólya--Benz real-zero-preserver theorem. Consequently the exact periodic trajectory issued from (2) is real-rooted for every `t>=0`, while (3) shows it is not real-rooted immediately below `0`. It is therefore a genuine finite periodic transition control with threshold exactly at the isolated collision.

## 2. The collision has a uniformly tiny log-Vieta prefix

For `1 <= m < N`, the perfect arithmetic lattice has zero power sum. Replacing `nu_1` by `nu_0=1` therefore gives, up to the harmless sign convention for positive root frequency,

\[
\boxed{
P_m(0)=1-e^{2\pi i m/N}.
}
\tag{4}
\]

Hence

\[
|P_m(0)|
=2\left|\sin\frac{\pi m}{N}\right|
\le \frac{2\pi m}{N}.
\tag{5}
\]

Write the collision-safe logarithmic Vieta coefficients as in XF-071/XF-079,

\[
c_m=(-1)^{m-1}\frac{P_m}{m}.
\tag{6}
\]

Since `N=2M`, (5) gives the uniform prefix bound

\[
\boxed{
M|c_m(0)|\le\pi,
\qquad 1\le m<N.
}
\tag{7}
\]

This is already the spectral reason an isolated collision is difficult for the guarded resource: the missing-point/double-point defect is a compact dipole against the lattice, so every low power sum gains one factor `m/N`.

## 3. Full nonlinear periodic heat cannot amplify this prefix on fixed time

XF-071 derives the exact log-Vieta Burgers system under the full periodic backward heat flow,

\[
\boxed{
 c_m'
 =-a\,m(N-m)c_m
 +a\sum_{i=1}^{m-1}i(m-i)c_i c_{m-i},
 \qquad
 a=\frac{4\pi^2}{L^2}.
}
\tag{8}
\]

No root labels or simplicity are needed for (8), so the equation is valid at the collision itself. For a live prefix `1<=m<=K<N`, define

\[
B(t):=M\max_{1\le m\le K}|c_m(t)|.
\tag{9}
\]

At a maximizing mode, the dissipative linear term can be discarded in an upper Dini-derivative estimate. Since

\[
\sum_{i=1}^{m-1}i(m-i)=\frac{m^3-m}{6},
\tag{10}
\]

(8) yields

\[
\boxed{
D^+B(t)
\le
\frac{aK^3}{6M}B(t)^2.
}
\tag{11}
\]

On the current Xi scales

\[
q\asymp\log^2T,
\qquad
M=q^2,
\qquad
K=O(q\log\log T),
\qquad
L\asymp q^{3/2},
\tag{12}
\]

so

\[
\frac{aK^3}{M}
=O\!\left(\frac{(\log\log T)^3}{q^2}\right)
=o(1).
\tag{13}
\]

Together with `B(0)<=pi`, scalar Riccati comparison gives, for every fixed `tau_0<infinity`,

\[
\boxed{
\sup_{0\le t\le\tau_0}B(t)
\le
\frac{\pi}{1-o(1)}
=O(1).
}
\tag{14}
\]

Thus the exact nonlinear convolution in (8) does not replenish a macroscopic low-frequency defect on any fixed heat interval. This is stronger than the static sparse escape of XF-061: the control survives the **full coefficient-level periodic heat**, not merely the initial slice or the tangent semigroup.

## 4. The exact guarded selector resource remains `o(1)`

For any mode band `B subset {1,...,K}`, XF-079 gives the exact one-center resource

\[
\mathcal R_B(t)
=
\frac1{4M^2}
\sum_{m\in B}|P_m(t)|^2 I_m,
\qquad
I_m=
\int_{-1}^{1}(\pi m+u)^4|\chi(u)|^2\,du.
\tag{15}
\]

Because `|u|<1`, there is a fixed constant `C_chi` with `I_m<=C_chi m^4` for every `m>=1`. Equations (6), (9), and (14) imply

\[
|P_m(t)|
=m|c_m(t)|
\le C\frac{m}{M}
\tag{16}
\]

uniformly for `m<=K` and `0<=t<=tau_0`. Therefore

\[
\boxed{
\sup_{0\le t\le\tau_0}
\mathcal R_B(t)
\le
C_{\chi,\tau_0}\frac{K^7}{M^4}.
}
\tag{17}
\]

At (12), with `ell=log log T`,

\[
\frac{K^7}{M^4}
=O\!\left(\frac{\ell^7}{q}\right)
=o(1).
\tag{18}
\]

In particular (17) holds for the full prefix `1<=m<=K`, so it holds a fortiori for every current guarded destination band such as `J_+<=m<=K`. The exact collision at `t=0` and its entire fixed-time real-rooted aftermath are invisible at order one to the XF-079/XF-097 destination normalization.

## 5. Sparse bounded lattice defects obey the same obstruction with an explicit threshold

The one-collision witness is the smallest member of a larger exact class. Start from the arithmetic lattice and change a set `S` of nodes by lattice-unit displacements `a_j`, writing

\[
A_1:=\sum_{j\in S}|a_j|.
\tag{19}
\]

For `m<N`, arithmetic-lattice cancellation and `|e^{iu}-1|<=|u|` give

\[
|P_m(0)|
\le
\frac{2\pi m}{N}A_1
=
\frac{\pi m}{M}A_1,
\tag{20}
\]

hence `B(0)<=pi A_1`. The same comparison as above yields

\[
B(t)
\le
\frac{\pi A_1}
{1-C\,A_1(\log\log T)^3t/q^2}
\tag{21}
\]

while the denominator stays positive. In particular, whenever the resource can be small at the scales below, the nonlinear stability condition is automatically much weaker. For every fixed `tau_0`,

\[
\boxed{
\sup_{0\le t\le\tau_0}\mathcal R_B(t)
\ll_{\chi,\tau_0}
A_1^2\frac{K^7}{M^4}.
}
\tag{22}
\]

Thus any defect family satisfying

\[
\boxed{
A_1
=o\!\left(\frac{M^2}{K^{7/2}}\right)
=
o\!\left(
\frac{q^{1/2}}{(\log\log T)^{7/2}}
\right)
}
\tag{23}
\]

remains guarded-invisible for fixed heat time. A single simple collision has `A_1=1`, far inside this cone. More generally, a sparse collection of bounded local defects must accumulate at least roughly `q^(1/2)/(log log T)^(7/2)` total lattice displacement before this crude but exact estimate even permits order-one guarded mass.

Equation (23) is a necessary scale warning, not a sufficiency theorem in the opposite direction: coherent power sums, cancellation, and the precise band location still matter once `A_1` reaches that size.

## 6. This is a matched obstruction to universal transition coercivity

The witness passes the controls that a transition-side theorem would naturally demand:

- it is an exact periodic trigonometric heat solution, not an arbitrary static point set;
- the collision is a genuine simple double zero, with the universal XF-002 discriminant orientation;
- all zeros are real for every positive heat time by the classical backward-heat real-zero-preserver theorem;
- the log-Vieta evolution is the exact nonlinear collision-safe system of XF-071, not a tangent approximation;
- the resource is exactly the one-center weighted selector norm of XF-079 that XF-097 now transports from Xi.

Yet its guarded mass is `o(1)` throughout every fixed positive heat interval. Therefore the implication

\[
\text{``real-root transition/collision''}
\quad\Longrightarrow\quad
\text{``order-one guarded }X(B)\text{ mass''}
\tag{24}
\]

is false even in the matched periodic model.

There is no conflict with XF-062. That finding proves that **if** an order-one normalized critical tangent flux survives a fixed positive heat time, then its energy is forced into the slow cone. The present witness shows that an isolated exact collision need not supply such surviving critical mass in the first place. Likewise there is no conflict with XF-071: ultra-infrared modes cannot repopulate the destination band strongly, and here the entire live prefix starts too small for the nonlinear convolution to change that conclusion.

## 7. Consequence after XF-097

XF-097 removes the source/carrier existence and fixed-time transport gates. The remaining destination theorem must now use information stronger than local transition geometry. At least one of the following kinds of genuinely Xi-specific input is required:

1. prove that a positive-`Lambda` transition cannot occur through only `A_1=o(q^(1/2)/(log log T)^(7/2))` sparse local defect mass on the relevant periodic window, and in particular forces a collective family of near-collisions or a comparable coherent power-sum defect;
2. find an invariant or observable whose normalization sees an isolated collision without losing the source-side `o(1)` bound already achieved by the guarded selector architecture; or
3. derive a global transition mechanism from the infinite Xi zero system showing that the boundary `t=Lambda` cannot be modeled by any sparse finite-period transition control.

The first route is the most direct continuation of the current architecture: convert positive `Lambda` into a **density/coherence theorem for transition defects**, then feed that theorem into the exact power-sum resource. A proof that merely identifies one Lehmer pair, one double collision, or one singular local gap is insufficient.

## 8. Prior-art and novelty boundary

The ingredients are classical or already established inside `xi_flow`. Real-root preservation under backward heat is classical Pólya--Benz/Pólya--Schur machinery; Kabluchko, *Lee--Yang zeroes of the Curie--Weiss ferromagnet, unitary Hermite polynomials, and the backward heat flow* (Annales Henri Lebesgue 8, 2025) states the trigonometric version explicitly. Newton identities, root-of-unity cancellation, and Riccati comparison are classical. XF-002 supplies the exact collision orientation, XF-071 the exact log-Vieta Burgers equation, and XF-079 the exact guarded sideband identity.

A targeted literature audit around real-rooted trigonometric backward heat, unitary Hermite/Lee--Yang flows, and Pólya--Benz preservation found the expected classical preservation theory and large-degree root-distribution results, but no result matching the Mathia-specific conjunction proved here: a sparse root-of-unity collision, propagated by the exact finite periodic heat, with the explicit `K^7/M^4` guarded-resource bound and the threshold (23). No novelty is claimed for the individual classical ingredients. `SOURCES.md` already contains the needed Kabluchko and real-zero-preserver anchors, so no source-list change is required.

## 9. Boundary conditions and decisive next test

This finding is a **negative control**, not evidence that Xi can have `Lambda>0`. The periodic witness does not satisfy the zeta explicit formula, the Xi zero-counting law at all scales, or the global analytic source constraints. It only proves that exact heat dynamics plus an isolated real-root transition do not by themselves coerce the destination resource.

The decisive next test is therefore quantitative and Xi-specific: assume `Lambda>0`, choose the XF-097 carrier window at the transition scale, and lower-bound a collective defect quantity that dominates either `A_1` at the threshold in (23) or, preferably, the actual weighted power-sum resource directly. The proof must explain why the infinite Xi transition cannot concentrate in finitely many or too few local collisions. If such a lower bound can be forced from zero counting, repulsion/correlation, or the analytic structure of `H_t`, the existing source-to-carrier machinery can consume it without another dictionary change.