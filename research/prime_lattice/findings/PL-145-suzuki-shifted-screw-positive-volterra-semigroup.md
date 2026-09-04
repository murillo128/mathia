# PL-145 — Suzuki's shifted screw family is a one-way positive Volterra semigroup toward safer half-planes

## Claim

Suzuki's shifted completed-zeta functions `Psi_omega` carry an exact one-parameter semigroup structure that sharply limits a natural interpolation route from the unconditional zero-free half-plane back to RH.

For `eta` real and for functions `f` on `[0,infinity)` for which the displayed expressions make sense, define

`(T_eta f)(t)
 = exp(-eta t) f(t)
 + 2 eta int_0^t exp(-eta u) f(u) du
 + eta^2 int_0^t (t-u) exp(-eta u) f(u) du`.

Suzuki's Section 11 identity is exactly

`Psi_(omega+eta) = T_eta Psi_omega`.

On any common exponential-order class where the one-sided Laplace transform is unique, these operators satisfy

`T_eta T_delta = T_(eta+delta)`.

For `eta>0`, `T_eta` preserves the pointwise positive cone because every coefficient and integral kernel in its definition is nonnegative. In contrast, the inverse `T_eta^(-1)=T_(-eta)` is not positivity preserving: already

`T_(-eta) 1 = 1-eta t`,

which is negative for `t>1/eta`.

This gives a precise directional obstruction. Suzuki proves that `Psi_omega>=0` globally for `omega>=1/2`, because `xi` is zero-free in `Re(s)>1`; and his Theorem 11.1 identifies eventual positivity of `Psi_omega` with zero-freeness in `Re(s)>1/2+omega`. Moving `omega` upward is therefore an order-preserving deformation toward safer half-planes. The direction required to recover `Psi_0` from the unconditional endpoint `Psi_(1/2)` is the inverse flow, which destroys the generic positive cone. Since Suzuki's Theorem 1.7 gives `RH <=> Psi_0(t)>=0` for every real `t`, **no proof that uses only positivity preservation of the shift deformation can bootstrap the known `omega=1/2` positivity down to RH**.

This does not rule out every continuity or interpolation argument in `omega`. It rules out the generic cone/order mechanism: a successful inward continuation must use additional arithmetic or completed global structure that controls the sign-changing inverse on the special zeta datum.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART-REDIRECT + NEGATIVE/OBSTRUCTION`. Suzuki's definition, transform, zero-free criterion, explicit prime formula, and two-parameter shift identity are literature. The semigroup law, inverse formula, and explicit failure of reverse positivity are elementary exact consequences derived here. No novelty claim is made for the shift identity itself; the durable contribution is the route diagnostic for the prime-lattice program.

## 1. Suzuki's shifted family is already a zero-free-region filtration

Suzuki defines, for real `omega` and `t>0`,

`Psi_omega(t)
 = exp(-omega t) Psi(t)
 + 2 omega int_0^t exp(-omega u) Psi(u) du
 + omega^2 int_0^t (t-u) exp(-omega u) Psi(u) du`,

with even extension to the real line. His one-sided Fourier transform is

`int_0^infinity Psi_omega(t) exp(i z t) dt
 = -(1/z^2) (xi'/xi)(1/2+omega-i z)`

in the stated half-plane of convergence.

Theorem 11.1 then says

`xi(s) != 0 for Re(s)>1/2+omega`

if and only if there is a `t_0>0` for which

`Psi_omega(t)>=0 for all t>=t_0`.

Moreover, from the Nevanlinna/screw argument preceding that theorem, zero-freeness in this half-plane gives global nonnegativity of `Psi_omega`. Hence `omega>=1/2` is unconditionally on the positive side because the classical Euler-product region gives zero-freeness in `Re(s)>1`.

At `omega=0`, Suzuki's Theorem 1.7 gives the sharper zeta-specific equivalence

`RH <=> Psi_0(t)>=0 for every real t`.

Thus `omega` is not a cosmetic regularization parameter. It indexes the exact zero-free boundary `Re(s)=1/2+omega`, with the unconditional endpoint `omega=1/2` and the RH endpoint `omega=0`.

## 2. Exact Laplace multiplier and semigroup law

Let

`F(q)=int_0^infinity f(t) exp(-q t) dt`

in a right half-plane where the transform exists. Direct Fubini calculations give

`L[exp(-eta t)f(t)](q)=F(q+eta)`,

`L[int_0^t exp(-eta u)f(u)du](q)=F(q+eta)/q`,

and

`L[int_0^t (t-u)exp(-eta u)f(u)du](q)=F(q+eta)/q^2`.

Therefore

`L[T_eta f](q)
 = (1+2 eta/q+eta^2/q^2)F(q+eta)
 = ((q+eta)/q)^2 F(q+eta)`.

Apply this twice:

`L[T_eta T_delta f](q)
 = ((q+eta)/q)^2
   ((q+eta+delta)/(q+eta))^2
   F(q+eta+delta)`

`= ((q+eta+delta)/q)^2 F(q+eta+delta)`

`= L[T_(eta+delta)f](q)`.

Uniqueness of the Laplace transform on the common domain yields

`T_eta T_delta = T_(eta+delta)`.

In particular, on Suzuki's family this is compatible with and strengthens the bookkeeping content of his two-parameter identity

`Psi_(omega+eta)=T_eta Psi_omega`:

the `omega`-shift is a genuine additive flow, not a collection of unrelated integral formulas.

No analytic continuation of an Euler product is used in this derivation. The completed `xi'/xi` transform is already the analytically continued object supplied by Suzuki's theorem.

## 3. Forward positivity is automatic, reverse positivity is false

For `eta>0` and `f(t)>=0` on `[0,infinity)`, every term in

`T_eta f(t)
 = exp(-eta t)f(t)
 +2eta int_0^t exp(-eta u)f(u)du
 +eta^2 int_0^t(t-u)exp(-eta u)f(u)du`

is nonnegative. Thus

`f>=0 => T_eta f>=0  (eta>0)`.

The same statement holds on any initial interval `[0,T]`, because `T_eta f(t)` only uses values `f(u)` with `0<=u<=t`. This is precisely the forward positivity propagation that Suzuki records after his shift identity.

The semigroup is algebraically invertible on the Suzuki family by reversing the parameter. Formally, and exactly whenever both sides are defined,

`T_eta^(-1)=T_(-eta)`.

But

`T_(-eta)g(t)
 = exp(eta t)g(t)
 -2eta int_0^t exp(eta u)g(u)du
 +eta^2 int_0^t(t-u)exp(eta u)g(u)du`.

The negative middle term already warns that the inverse is not an order map. The constant positive test function gives an exact witness. Since

`int_0^t exp(eta u)du=(exp(eta t)-1)/eta`

and

`int_0^t(t-u)exp(eta u)du=(exp(eta t)-1-eta t)/eta^2`,

one obtains

`T_(-eta)1=1-eta t`.

Hence the positive cone is not invariant under the reverse flow.

This is the decisive asymmetry. From the unconditional datum `Psi_(1/2)>=0`, the identity needed to reach the RH datum is

`Psi_0 = T_(-1/2) Psi_(1/2)`.

Generic positivity gives no sign control on the right-hand side. Any argument that merely says that the shifted family depends smoothly on `omega`, or that positivity propagates under the Volterra transform, points in the wrong direction unless it introduces an additional estimate that controls the non-positive inverse specifically for the completed zeta function.

## 4. Prime-lattice meaning: `omega` is an energy tilt on the prime-axis skeleton

Suzuki's explicit formula for `Psi_omega` contains the finite prime-power term

`- sum_(n<=exp(t)) Lambda(n) n^(-1/2-omega) (t-log n)`

plus the completed pole and archimedean terms. Since `Lambda(n)` is supported on `n=p^k`, the non-archimedean contribution lies exactly on the prime-axis rays

`v(p^k)=k e_p`.

With the canonical lattice energy

`E(v(n))=<v(n),(log p)_p>=log n`,

changing `omega` to `omega+eta` multiplies the prime-axis weight by

`n^(-eta)=exp(-eta E(v(n)))`.

Thus increasing `omega` exponentially damps high-energy points on the prime-power axes. Decreasing `omega` back toward zero removes that damping. This gives the prime-lattice interpretation of the one-way order flow: the easy direction suppresses arithmetic high-energy contributions while moving the completed logarithmic derivative farther into a zero-free half-plane.

This interpretation must not be overextended. `T_eta` acts on the **entire completed function** `Psi_omega`; the pole and gamma/Lerch terms change together with the prime term. The semigroup is therefore not a proof that prime damping alone creates positivity. It is an exact completed deformation whose prime component happens to be the canonical energy tilt on the axis skeleton.

## 5. Adversarial checks and limits

### Eventual versus global positivity

Theorem 11.1 uses eventual positivity, while the cone argument above is a statement about global or initial-interval positivity. These are not interchangeable: if a function is only nonnegative after some `t_0`, the Volterra memory still integrates values from `[0,t_0]`. The obstruction claimed here therefore uses the unconditional **global** positivity at `omega=1/2` and the global RH criterion at `omega=0`; it does not assert a generic semigroup theorem for eventual-positive cones.

### Invertibility is not positivity

The identity `T_eta T_(-eta)=I` is algebraic/transform-theoretic on a common domain. It does not make `T_eta` an order isomorphism. The explicit constant-function witness proves that inverse positivity fails independently of zeta.

### The result does not disprove special reverse estimates

A zeta-specific theorem could still prove that `T_(-1/2)Psi_(1/2)>=0`, or control a sequence of smaller inward shifts, by exploiting information absent from the generic positive cone. But that conclusion is already RH-equivalent at the endpoint. The semigroup itself supplies no monotone order principle that forces it.

### The critical line is not selected by the abstract Volterra semigroup

The family `T_eta` is defined without primes or zeta. The distinguished parameters arise only after coupling it to Suzuki's completed transform `xi'/xi(1/2+omega-iz)`. Therefore the abstract semigroup cannot be advertised as an independent geometric explanation of `1/2`; it is a transport mechanism for a zeta-specific completed family.

## 6. Prior-art and novelty audit

Suzuki explicitly supplies the definition of `Psi_omega`, the transform involving the shifted completed logarithmic derivative, Theorem 11.1, the explicit prime-power formula, the relation between `Psi_(omega+eta)` and `Psi_omega`, and the forward implication that nonnegativity on an initial interval propagates when `eta>0`.

The exact semigroup law follows immediately after passing that relation through the one-sided Laplace transform, and the inverse counterexample is elementary. Searches using the structural terms `Psi_omega`, shifted screw functions, Volterra operators, positive semigroups, and zero-free half-planes did not reveal a separate result whose mathematical content is stronger than Suzuki's Section 11 for this purpose. This finding therefore makes **no claim that the integral shift formula is new** and no strong priority claim for naming it a semigroup. Its value is as a falsifiable route restriction inside this research line.

This also sharpens rather than duplicates `PL-144`. `PL-144` shows that, at fixed `omega=0`, the completed screw/CND/Lévy/Hilbert avatars collapse back to the scalar sign problem. The present finding identifies a second collapse in the deformation parameter: the obvious positive interpolation transports that sign only outward toward easier zero-free half-planes, whereas RH requires the non-positive inverse direction.

## Consequence for the prime-lattice program

Do not pursue a proof strategy whose only new ingredient is monotone or positivity-preserving interpolation in Suzuki's shift parameter from the known `Re(s)>1` region to the critical boundary. The exact transport operator has the wrong order direction.

A surviving mechanism must add information that is invisible to the generic positive Volterra semigroup and that controls inward undamping of the prime-axis energy tilt. Examples of potentially relevant additional structure include a genuinely arithmetic inequality coupling the prime-power axes to the archimedean completion, a target-relative/model-space constraint, or another global duality that yields quantitative control of `T_(-eta)` on the special zeta trajectory. Merely repackaging the forward semigroup as a flow, heat-like smoothing, or Hilbert-space evolution does not add RH rigidity.

## Sources

- Masatoshi Suzuki, “Aspects of the screw function corresponding to the Riemann zeta-function,” *Journal of the London Mathematical Society* **107** (2023), 2143–2176. DOI: https://doi.org/10.1112/jlms.12785. Section 11 is the primary source for `Psi_omega`, equations (11.1)–(11.2), Theorem 11.1, the explicit shifted prime formula, and the two-parameter shift identity.
- `PL-120`, `PL-143`, and `PL-144` are the local canonical context for the completed screw/positivity mechanism and its scalarization boundary.
