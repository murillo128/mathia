# PL-210 — Irreducible multichannel log-prime transport remains spectrally programmable

**Status:** negative result / programmability obstruction  
**Evidence class:** `EXACT-DERIVED + CLASSICAL-FINITE-RANK-PERTURBATION + DECISIVE-NEGATIVE` for the scoped multichannel target-relative route  
**Research line:** `prime_lattice`

## Claim

`PL-209` leaves open the possibility that a useful target-relative construction might escape scalar programmability by using genuinely different operator directions for different primes rather than the single rank-one coupling

\[
H_\alpha=H+\langle\alpha,(\log p)_p\rangle P.
\]

That escape is still too weak if “multi-prime” means only noncommuting or operator-algebraically irreducible finite-rank prime channels.

There is an explicit matched-control family with all of the following properties at once:

- every prime step carries the exact coefficient `log p`;
- the prime couplings are self-adjoint, finite rank, noncommuting, and collectively irreducible;
- one distinguished target vector is cyclic for the joint operator algebra;
- every adjacent relative resolvent difference is finite rank, hence trace class;
- the compressed resolvent is operator-valued Herglotz/Nevanlinna;
- prime-edge perturbation determinants satisfy exact square/path compatibility; and
- the unperturbed target spectral measure can nevertheless be any prescribed finite atomic probability measure.

Thus even replacing the collinear rank-one prime action of `PL-209` by an infinite irreducible family of noncommuting prime directions does not force Riemann-specific spectral data. What remains necessary is not abstract operator irreducibility but a **source-forced arithmetic relation among the prime channels** whose spectral/trace consequence fails on these programmable controls.

## Construction

Enumerate the rational primes as

\[
p_1=2,p_2=3,p_3=5,\ldots
\]

and let the target multiplicity space be

\[
\mathcal K=\ell^2(\mathbb N),
\]

with orthonormal basis `e_1,e_2,...`.

Define bounded self-adjoint finite-rank operators on `K` by

\[
B_{p_1}=|e_1\rangle\langle e_1|
\]

and, for `k>=1`,

\[
B_{p_{k+1}}
=|e_k\rangle\langle e_{k+1}|
 +|e_{k+1}\rangle\langle e_k|.
\]

The first operator has rank one and every later operator has rank two. Adjacent edge operators do not commute, and the family has trivial commutant, as proved below.

Now prescribe an arbitrary finite atomic probability measure

\[
\mu=\sum_{j=1}^r w_j\,\delta_{\lambda_j},
\qquad
w_j>0,
\qquad
\sum_jw_j=1,
\]

with distinct real `lambda_j`. Let

\[
\mathcal H=\mathbb C^r\otimes\mathcal K,
\qquad
H_0=D\otimes I_{\mathcal K},
\]

where `D f_j=lambda_j f_j`, and put

\[
g=\sum_{j=1}^r\sqrt{w_j}\,f_j.
\]

Define the isometry

\[
J:\mathcal K\to\mathcal H,
\qquad
Ju=g\otimes u.
\]

For each prime set

\[
V_p=(\log p)J B_pJ^*.
\]

For a finite-support exponent vector `alpha`, define

\[
B_\alpha=\sum_p\alpha_p(\log p)B_p,
\qquad
H_\alpha=H_0+J B_\alpha J^*.
\]

Every `H_alpha` is self-adjoint because `J B_alpha J^*` is bounded finite rank. The prime-lattice law is exact:

\[
H_{\alpha+e_p}=H_\alpha+V_p.
\]

Unlike `PL-209`, the prime operators are not all scalar multiples of one fixed projection. Their joint target algebra is infinite, noncommuting, and irreducible.

## Exact irreducibility of the prime channels

Let `T` be a bounded operator on `K` commuting with every `B_p`.

Commutation with

\[
B_2=|e_1\rangle\langle e_1|
\]

implies

\[
T e_1=a e_1
\]

for some scalar `a`, with `e_1^perp` invariant as well. Since

\[
B_3e_1=e_2,
\]

commutation with `B_3` gives

\[
T e_2=T B_3e_1=B_3T e_1=a e_2.
\]

Inductively, because

\[
B_{p_{k+1}}e_k=e_{k+1},
\]

we get

\[
T e_k=a e_k
\qquad(k\ge1).
\]

Hence

\[
\boxed{\{B_p:p\text{ prime}\}'=\mathbb C I.}
\]

The prime-channel representation on `K` is therefore irreducible.

The full control can also be made irreducible jointly with its prescribed source spectrum. Suppose `Q` commutes with `H_0` and every `V_p`. Since the `lambda_j` are distinct, commutation with `H_0` forces

\[
Q=\bigoplus_{j=1}^r Q_j
\]

on the spectral blocks `f_j tensor K`. The `(j,k)` block of `V_p` is

\[
(\log p)\sqrt{w_jw_k}\,B_p.
\]

All weights are nonzero, so `[Q,V_p]=0` yields

\[
Q_jB_p=B_pQ_k
\qquad\text{for all }j,k,p.
\]

Taking `j=k` and using the trivial commutant above gives `Q_j=c_jI`. Taking arbitrary `j,k` and any nonzero `B_p` then gives `c_j=c_k`. Thus

\[
\boxed{\{H_0,V_p:p\text{ prime}\}'=\mathbb C I.}
\]

The joint self-adjoint family is irreducible. In particular every nonzero vector, including the distinguished target

\[
\psi=Je_1=g\otimes e_1,
\]

is cyclic for the generated unital `*`-algebra after closure.

This removes the obvious objection that programmability in `PL-209` was only a consequence of using one collinear rank-one channel.

## The prescribed target spectral measure survives

The spectral measure of `psi` for `H_0` is exactly the measure chosen before any prime data were attached:

\[
\langle\psi,(H_0-z)^{-1}\psi\rangle
=\sum_{j=1}^r\frac{w_j}{\lambda_j-z}
=:m(z).
\]

Thus the base target spectrum and weights can be chosen arbitrarily among finite atomic probability measures.

More strongly, the whole target-space Weyl function is scalar before perturbation:

\[
M_0(z)
:=J^*(H_0-z)^{-1}J
=m(z)I_{\mathcal K}.
\]

For `Im z>0`, `Im m(z)>0`, so `M_0` is operator-valued Herglotz. This positivity is forced only by self-adjointness, not by arithmetic.

## Exact multichannel resolvent law

Let

\[
R_\alpha(z)=(H_\alpha-z)^{-1},
\qquad
M_\alpha(z)=J^*R_\alpha(z)J.
\]

Finite-rank Krein/Woodbury resolvent algebra gives

\[
M_\alpha(z)
=\left(M_0(z)^{-1}+B_\alpha\right)^{-1}.
\]

Because `M_0=mI`, this becomes

\[
\boxed{
M_\alpha(z)
=\left(m(z)^{-1}I+B_\alpha\right)^{-1}
=m(z)\left(I+m(z)B_\alpha\right)^{-1}.
}
\]

The scalar target seen by `psi` is therefore

\[
\boxed{
m_\alpha^{\psi}(z)
=\langle e_1,M_\alpha(z)e_1\rangle.
}
\]

This is no longer the single Möbius orbit `m/(1+tau_alpha m)` of `PL-209`. Different prime directions enter through distinct, noncommuting `B_p`, and mixed products occur in the resolvent expansion. Nevertheless `m(z)` itself remains freely prescribable through the initial atomic measure.

For every prime edge the second resolvent identity gives

\[
R_{\alpha+e_p}(z)-R_\alpha(z)
=-R_{\alpha+e_p}(z)V_pR_\alpha(z).
\]

Since `V_p` has rank at most two, every adjacent relative resolvent difference has rank at most two and belongs to `S_1`.

Thus trace-class relative resolvents survive after the prime action has become genuinely noncommuting and irreducible.

## Exact determinant flatness despite noncommutativity

Define the prime-edge perturbation determinant

\[
\Delta_{\alpha,p}(z)
=\det_{\mathcal H}\!\left(I+V_pR_\alpha(z)\right).
\]

By the finite-rank Sylvester determinant identity,

\[
\Delta_{\alpha,p}(z)
=\det_{\mathcal K}\!\left(I+(\log p)B_pM_\alpha(z)\right).
\]

Substituting the exact formula for `M_alpha` gives

\[
\boxed{
\Delta_{\alpha,p}(z)
=
\frac{
\det\!\left(I+m(z)(B_\alpha+(\log p)B_p)\right)
}{
\det\!\left(I+m(z)B_\alpha\right)
}.
}
\]

All determinants are ordinary finite-rank Fredholm determinants because `B_alpha` has finite rank for finite-support `alpha`.

The ratio telescopes along every lattice path. If a path runs from `0` to `alpha`, then

\[
\boxed{
\prod_{\text{edges}}\Delta_{\beta,p}(z)
=
\det\!\left(I+m(z)B_\alpha\right),
}
\]

independently of the order in which prime steps are taken. In particular,

\[
\Delta_{\alpha,p}\Delta_{\alpha+e_p,q}
=
\Delta_{\alpha,q}\Delta_{\alpha+e_q,p}.
\]

This exact square flatness does **not** require the `B_p` to commute. It is the ordinary chain rule for relative finite-rank determinants around an additive perturbation lattice.

Hence noncommutative prime directions plus a flat determinant cocycle are not contradictory; nor does their coexistence imply arithmetic rigidity.

## Why the control is stronger than `PL-208` and `PL-209`

`PL-208` already showed that arbitrary bounded self-adjoint labels `V_p` generate same-parameter resolvent transports with formal square flatness. That result deliberately left the labels unconstrained.

`PL-209` imposed much more arithmetic-looking structure: exact `log p` coefficients, one distinguished target, rank-one trace-class edges, Herglotz positivity, and target determinants. Its remaining weakness was that every prime acted through the same projection, so the entire family reduced to one scalar parameter.

The present construction simultaneously keeps the `PL-209` target/Herglotz/determinant package and removes that collinearity. The operators `B_p` act in infinitely many target directions, they do not commute, their commutant is scalar, and together with `H_0` they give an irreducible family. Yet an arbitrary finite target spectrum and arbitrary positive target weights were chosen *before* the rational-prime labels were attached.

Thus the implication

\[
\begin{aligned}
&\text{exact }\log p\text{ labels}
+\text{ cyclic distinguished target}
+\text{ irreducible noncommuting prime channels}\\
&\quad
+\ S_1\text{ relative resolvents}
+\text{ Herglotz positivity}
+\text{ flat Fredholm determinants}
\\[2mm]
&\hspace{35mm}\Longrightarrow
\text{Riemann-specific spectral rigidity}
\end{aligned}
\]

is false without an additional source-forced arithmetic identity.

## Analytic-continuation boundary

No Euler product, Dirichlet-series continuation, functional equation, or zero divisor is used in the control. That is intentional.

The construction shows that the operator package above can be realized in systems having no zeta function at all. It therefore cannot by itself be the mechanism that transports arithmetic information from `Re(s)>1` into the critical strip or singles out `Re(s)=1/2`.

Any successful use of a matrix/operator-valued Weyl function or a finite-rank prime determinant must add an independently proved identity tying those objects to the analytically continued completed zeta function, the Nyman target, the Weil form, Möbius data, or another arithmetic observable that the present control cannot reproduce.

## Prior art and novelty audit

The finite-rank resolvent formula, matrix/operator-valued Herglotz functions, finite-rank perturbation determinants, and their linear-fractional transformations are classical operator theory. A targeted literature audit around matrix-valued Herglotz functions, finite-rank self-adjoint perturbations, Krein/Woodbury resolvent formulas, and perturbation determinants confirmed that this ambient machinery is established and highly flexible. No novelty is claimed for those ingredients.

A second targeted search for combinations of logarithmic prime labels with matrix-valued Herglotz/finite-rank perturbation systems did not provide evidence of a theorem that turns the abstract package above into Riemann-specific rigidity. Absence of a search hit is not used as novelty evidence.

The durable delta is the exact **matched control** tailored to the current Prime-Lattice frontier: even an infinite, noncommuting, algebraically irreducible family of exact `log p` finite-rank channels can be wrapped around freely prescribed target spectral data while preserving trace-class resolvent edges, Herglotz positivity, and determinant path compatibility.

## Adversarial boundaries

**Irreducibility is operator-algebraic, not arithmetic.** The control proves precisely that these notions must not be conflated. The `B_p` are deliberately manufactured. A zeta construction in which the local operators are uniquely forced by arithmetic relations could escape this obstruction.

**The prescribed spectral measure is finite atomic.** This is sufficient for the negative conclusion: arbitrary finite spectra and positive weights already show that the structural package does not identify Riemann spectral data. No claim is made that every continuous matrix-valued spectral measure is realized by the same jointly irreducible model.

**The family is noncommutative but the perturbation endpoint is additive.** The operators `B_p` themselves do not commute, while `H_alpha` depends on their finite weighted sum. A route based on genuinely path-dependent ordered products, curvature, domain changes, or a non-additive arithmetic relation lies outside this control. Such a route must still show why its ordering/curvature is canonically forced by the commutative integer multiplication law rather than inserted by hand.

**Flat determinants are weaker than flat operator transport.** The determinant forgets matrix ordering information. This finding does not rule out a useful non-scalar holonomy before taking determinant; it only proves that noncommuting generators plus exact determinant flatness are still programmable.

**Self-adjointness remains identification-free.** The control can realize arbitrary real atomic spectra. Self-adjointness localizes its own spectrum to the real axis, but without an independent theorem identifying that spectrum with the Riemann-zero parameter it says nothing about RH.

## Falsification / audit tests

The exact control would fail if any of the following statements were false:

1. the family `B_p` above has scalar commutant;
2. the joint family `{H_0,V_p}` has scalar commutant when the atomic locations are distinct and all weights are positive;
3. `psi=g tensor e_1` has spectral measure `mu` for `H_0`;
4. the compressed resolvent satisfies `M_alpha=(m^(-1)I+B_alpha)^(-1)`;
5. every prime-edge relative resolvent difference has rank at most `rank(B_p)<=2`;
6. the finite-rank determinant ratio above is valid even when the prime matrices do not commute; and
7. the edge determinants telescope to the endpoint determinant along every factorization path.

Items 1--3 are direct finite/block-matrix calculations. Items 4--7 are standard finite-rank resolvent/determinant identities and were re-derived explicitly above. The research conclusion would be materially narrowed by a theorem showing that a **specific arithmetic** prime-channel family satisfies an additional relation incompatible with this control.

## Consequence for the research line

The operator frontier is narrower again. It is not enough to demand that different prime directions act through distinct operators, that those operators fail to commute, that the joint action be irreducible, or that a distinguished target be cyclic. All of those properties can coexist with arbitrary preselected target spectral data and exact trace-class/determinant transport.

Accordingly, “irreducibly multi-prime” must now mean more than operator-algebraic irreducibility. A surviving mechanism must supply a **canonical cross-prime arithmetic law**—for example one derived from Möbius inclusion/exclusion, Nyman approximation, the explicit formula/Weil positivity, a source-forced additive/multiplicative coupling, or another rational-prime relation—and prove a spectral/positivity/trace consequence that fails on the programmable multichannel controls above.

This does not reject the accepted trace-class clue. It sharpens its decisive test: the next candidate must make the *relations among prime channels* arithmetically nonprogrammable, not merely make the channels noncommuting or irreducible.