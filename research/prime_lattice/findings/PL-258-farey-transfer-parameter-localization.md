# PL-258 — Farey transfer operators encode the full Riemann divisor as complex parameter values, not as one fixed self-adjoint spectrum

## Claim and status

A natural escape after `PL-254`--`PL-257` is to replace designed boundary operators or Lax--Phillips compression by a canonical dynamical transfer operator coming from the modular surface. Farey/Gauss thermodynamic formalism does supply a genuinely source-determined operator family and, in a precise branch, a divisor-complete characterization of the nontrivial Riemann zeros. However the known mechanism does **not** turn those zeros into the spectrum of one fixed self-adjoint operator.

Bonanno's complex-temperature Farey family `P_q^+` has a distinguished eigenvalue-`1` problem whose admissible solutions are equivalent to `2q` being a nontrivial zero of `zeta` (apart from the separately identified `q=1` invariant-density case in the more general classification). In the infinite-matrix formulation used for the RH criterion, the relevant Hilbert norm depends explicitly on `xi = Re(q)` through the weights

\[
\frac{\Gamma(n+2\xi)}{n!}.
\]

Thus RH becomes the assertion that the parameter values `q` for which this **family** admits the required solution occur only on

\[
\Re q=\frac14,
\]

because the Riemann zero is `rho=2q`. This is a canonical dynamical reformulation of the zero-location problem, but it is not a Hilbert--Polya localization theorem: `q` is the complex temperature/spectral parameter selecting a member of the transfer-operator family, not an eigenvalue of one fixed self-adjoint operator.

Classical Farey transfer-operator spectral theory does provide self-adjoint realizations for a one-parameter signed family at real temperature, with absolutely continuous spectrum and no nonzero point spectrum on the Hilbert space studied by Bonanno--Graffi--Isola. That self-adjoint theorem therefore does not localize the Riemann zeros appearing in the complex-temperature branch. The RH-relevant parameter values have nonzero imaginary part, while the cited self-adjoint spectral result belongs to the real-parameter theory.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART-REDIRECT + DECISIVE-NEGATIVE` for the route "use the existing Farey/Gauss transfer-operator eigenvalue problem, dynamical determinant, or real-temperature self-adjointness as the missing fixed self-adjoint Riemann-zero spectrum." This is not a no-go theorem for a new arithmetic linearization of the complex parameter family.

## 1. The modular transfer-operator route is canonical and genuinely global

The Farey map is not an arbitrary repackaging of the exponent lattice. It is tied to continued fractions and, by inducing, to the Gauss map; the corresponding transfer operators are part of the thermodynamic formalism for the modular surface. Their relation to modular spectral theory is mediated by the Selberg zeta function, period functions, Eisenstein series, and scattering theory. Consequently this route passes an important source test that many bare prime-lattice constructions fail: the operator family is fixed by an independent modular dynamical system rather than chosen after inspecting the Riemann zeros.

For complex `q` with `Re(q)>0`, Bonanno studies the signed generalized Farey operators

\[
(P_q^\pm f)(x)
=(1+x)^{-2q}
\left[f\left(\frac{x}{1+x}\right)
\pm f\left(\frac1{1+x}\right)\right].
\]

The complex-temperature extension is required precisely because the modular spectral and scattering parameters are complex. Bonanno's classification separates the cusp-form/Laplace spectrum branch from a special `+` branch. In the latter, the admissibility condition with the specified nonzero boundary coefficient is equivalent to `2q` being a nontrivial zero of the Riemann zeta function. The paper then translates that problem into an explicit infinite linear-algebra problem.

This supplies something stronger than a loose determinant analogy. The Riemann zero divisor is represented by a canonical existence condition in a concrete modular transfer-operator family. The continuation is inherited from the modular/period-function framework, not from formally continuing an Euler product outside `Re(s)>1`.

## 2. Divisor completeness occurs in parameter space

Let `q=xi+i eta`. In the matrix formulation, Bonanno expands the unknown in a generalized Laguerre basis and obtains a vector `Phi(q)` satisfying an infinite linear system. Membership in the required Hilbert space is measured by

\[
\|\Phi(q)\|_{q}^{2}
=
\sum_{n\ge0}|\Phi_n(q)|^2
\frac{\Gamma(n+2\xi)}{n!}.
\]

The important structural point is that the norm itself depends on `xi=Re(q)`. Bonanno states the resulting RH formulation explicitly: because the relevant problem has a solution exactly when `2q` is a nontrivial zeta zero, RH is equivalent to finiteness/admissibility occurring only for parameters with

\[
\xi=\frac14.
\]

Under `rho=2q`, this is exactly `Re(rho)=1/2`.

There is therefore no spectral-theorem step of the form

\[
H=H^* \quad\Longrightarrow\quad q\in\mathbb R
\quad\Longrightarrow\quad \Re\rho=\frac12.
\]

Instead one has a holomorphic/meromorphic **family** `P_q^+` and asks for which complex `q` the fixed value `1` lies in the appropriate point-spectrum/admissibility relation. The zero location is encoded in the set of parameter values solving that family problem. Calling this a spectral realization is legitimate in the transfer-operator sense, but it does not make the critical line automatic.

This distinction is the same load-bearing one isolated abstractly in `PL-208`: parameter-dependent operator transport can be highly structured without converting the parameter locus into the spectrum of one self-adjoint operator. Here the family is far less programmable because modular dynamics fixes it, but the logical gap remains.

## 3. Real-temperature self-adjointness does not repair the gap

Bonanno--Graffi--Isola studied a one-parameter family of signed Farey transfer operators on a suitable Hilbert space of analytic functions and proved that the operators in that real-parameter spectral theory are self-adjoint, have absolutely continuous spectrum, and have no nonzero point spectrum (with special polynomial eigenfunctions at negative half-integer parameters treated separately).

This is an especially useful matched control because it prevents a misleading inference: the presence of self-adjoint Farey transfer operators in the literature does not mean that the complex parameters `q=rho/2` corresponding to Riemann zeros have become eigenvalues of those self-adjoint operators. The two roles are different. In the RH formulation the transfer operator varies with complex `q` and one fixes the eigenvalue at `1`; in the self-adjoint real-temperature theory one fixes a real parameter and studies the spectrum of that operator.

No stronger statement is needed here. In particular, this finding does **not** claim that every possible complex-temperature realization is non-self-adjoint, or that no change of Hilbert space can produce another symmetric model. The precise negative is only that the existing canonical self-adjoint Farey theory is not the zero-bearing fixed-operator Hilbert--Polya mechanism.

## 4. Why a Fredholm/dynamical determinant does not by itself change the conclusion

Mayer's transfer-operator program for the Gauss map famously relates Fredholm determinants of nuclear transfer operators to the Selberg zeta function of the modular group. Bonanno's Farey formulation is part of that same modular thermodynamic-formalism lineage. This provides a canonical determinant and genuine meromorphic continuation, but it also clarifies the target: the natural determinant is fundamentally a **family determinant in the complex spectral/temperature variable**.

A zero of such a determinant identifies a parameter at which an operator in the family loses invertibility or acquires a prescribed eigenvalue. It does not follow that the same parameter is an eigenvalue of a fixed normal operator. This is exactly why the modular transfer-operator construction can encode both modular spectral data and Riemann scattering data without solving their localization problem.

The conclusion is compatible with `PL-033` and `PL-257`. Automorphic Lax--Phillips scattering already puts the complete Riemann divisor into the eigenvalues of a non-self-adjoint interaction generator, while an ambient unitary/self-adjoint dynamics coexists with possible complex resonances. Farey transfer operators supply a different canonical modular encoding, but their complex-temperature divisor condition also stops before the missing positivity/self-adjoint localization theorem.

## 5. Relation to the prime-exponent lattice

The exponent lattice enters the zeta side through the usual prime/Euler data and the logarithmic frequencies `log p`, but the continuation and dynamical realization in the Farey/Gauss route come from additional modular geometry. That is consistent with the canonical mandate: the useful part of this prior art is precisely that it tests whether a **global completion with canonical dynamics** supplies more than the bare Bohr torus.

It does supply more: a canonical transfer family, period-function equations, Selberg/scattering continuation, and an exact Riemann-zero parameter criterion. What it still does not supply is a source-determined positive/self-adjoint relation whose own spectrum is the entire Riemann divisor. The distinction matters because the prime-lattice program has already accumulated many constructions that can store or select zero data without forcing the critical line.

A future proposal should therefore not count any of the following, by themselves, as the missing mechanism:

- a canonical Farey/Gauss transfer operator depending holomorphically on a complex parameter;
- a Fredholm/dynamical determinant whose zeros are parameter values where that operator has eigenvalue `1`;
- a parameter-dependent Hilbert-space admissibility condition equivalent to `zeta(2q)=0`;
- self-adjointness of a related real-temperature transfer-operator family.

The missing theorem must connect these ingredients in a way that makes the zero-bearing parameter itself subject to spectral reality or positivity.

## 6. Prior-art and novelty audit

The principal source is Claudio Bonanno, *On the Generalised Transfer Operators of the Farey Map with Complex Temperature*, `Mathematics` **11**(1) (2023), 134, DOI `10.3390/math11010134`. The paper explicitly extends the Farey matrix/Hilbert-space method to complex temperature, records the branch in which the relevant eigenvalue-`1` problem is equivalent to `2q` being a nontrivial Riemann-zeta zero, and states the resulting infinite-matrix formulation of RH with the `Gamma(n+2 Re(q))/n!` Hilbert weights.

The matched self-adjoint control is Claudio Bonanno, Sandro Graffi, Stefano Isola, *Spectral analysis of transfer operators associated to Farey fractions*, `Atti Accad. Naz. Lincei Rend. Lincei Mat. Appl.` **19**(1) (2008), 1--23, DOI `10.4171/RLM/505`. Its abstract theorem-level summary states self-adjointness on a suitable Hilbert space, absolutely continuous spectrum, and absence of nonzero point spectrum for the signed one-parameter Farey family studied there.

The novelty audit against the current `prime_lattice` corpus found no stored Farey/Mayer transfer-operator finding and no corresponding literature anchor in `SOURCES.md`. The mathematical content is nevertheless prior art: the durable new value for this line is the **negative classification of what that prior art does and does not solve** relative to the current `PL-254`--`PL-257` frontier.

## 7. Adversarial boundaries and falsification test

1. **Do not conflate the general classification with the clean Riemann branch.** Bonanno's wider `P_q^+ f=f` classification includes the ordinary `q=1` invariant-density solution and modular Laplace-spectrum phenomena. The RH statement uses the more specific admissibility/matrix problem singled out in the paper, for which the author states the equivalence with `2q` being a nontrivial Riemann zero.
2. **Do not claim complex-temperature non-self-adjointness as a theorem here.** The cited positive self-adjoint result is for the real-parameter Farey spectral theory. The negative conclusion needs only the mismatch between that theorem and the complex parameter locus carrying the Riemann zeros.
3. **The family is canonical, so generic programmability is not the objection.** Unlike the abstract boundary data of `PL-256`, the Farey family is independently fixed by modular dynamics. The obstruction is specifically `family parameter != spectrum of one fixed self-adjoint operator`.
4. **A new linearization is not ruled out.** An independently canonical construction could conceivably linearize the nonlinear/holomorphic `q`-family into a single operator pencil or fixed operator. To advance RH it would have to prove self-adjointness/positivity and two-way divisor completeness without importing the zero set into the construction.
5. **A determinant identity is not enough.** The decisive audit for any proposed transfer-operator repair is to identify what is held fixed and what is the spectral variable. If zeta zeros remain values of an external complex parameter for which `1` is an eigenvalue, the spectral-theorem localization gap is unchanged.
6. **Analytic continuation is legitimate but external to the bare exponent monoid.** The continuation comes from modular transfer/scattering/period-function theory. No termwise Euler-product continuation in the critical strip is used.

## Research implication

This prior art closes a particularly plausible thermodynamic-formalism shortcut at the present frontier. Canonical modular dynamics can indeed supply a divisor-complete Riemann-zero condition and a Hilbert-space matrix formulation, while related real-temperature transfer operators can be genuinely self-adjoint. Those facts still do not combine into one fixed self-adjoint Riemann-zero spectrum.

The surviving target is consequently sharper: **derive from rational-prime/global arithmetic a fixed self-adjoint or Herglotz-positive relation whose spectral variable is the centered Riemann zero parameter itself and whose spectrum is divisor-complete.** If a proposal instead leaves `q` as the external complex temperature and merely asks when a member of a transfer family has eigenvalue `1`, Bonanno's construction shows that the formulation is already classical and that RH remains exactly the unresolved localization of that parameter locus.