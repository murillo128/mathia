# MC-140 — Unique high-temperature Bost–Connes equilibrium projects out nontrivial cyclotomic characters

**Status:** `LITERATURE+EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-CLASSICALIZED`, `NO-NOVELTY-CLAIM`.

## Claim

Let `(A,sigma)` be the standard Bost–Connes system and let

\[
G=\widehat{\mathbb Z}^{\times}\cong \operatorname{Aut}(\mathbb Q/\mathbb Z)
\]

be its cyclotomic symmetry group. The `G`-action commutes with the Bost–Connes time evolution. For every inverse temperature

\[
0<\beta\le 1,
\]

the Bost–Connes phase-transition theorem gives a unique `KMS_beta` state `phi_beta`. Therefore that state is `G`-invariant. Consequently every nontrivial `G`-character spectral subspace is annihilated exactly:

\[
\boxed{
\alpha_g(x)=\chi(g)x\ \forall g\in G,
\quad \chi\ne 1
\quad\Longrightarrow\quad
\phi_\beta(x)=0
\qquad (0<\beta\le1).
}
\tag{1}
\]

This is the symmetry analogue of the time-evolution selection rule in `MC-139`, but it acts **inside the degree-zero sector** left open there. In particular, simply moving from semigroup-energy modes to nontrivial cyclotomic/Galois coefficient modes does not create a critical-half equilibrium first-moment channel: at `beta=1/2` every such nontrivial symmetry harmonic is projected out by the unique KMS state.

A concrete finite-modulus specialization makes the obstruction explicit. Let `q>=3`, let `chi` be a nonprincipal primitive Dirichlet character modulo `q`, and write `e(r)` for the standard group-algebra generator attached to `r in Q/Z`. Define

\[
A_{\chi,q}
=
\sum_{u\in(\mathbb Z/q\mathbb Z)^\times}
\overline{\chi(u)}\,e(u/q).
\tag{2}
\]

For `g in G`, reduced modulo `q`, the cyclotomic action sends `e(u/q)` to `e(gu/q)`, so

\[
\alpha_g(A_{\chi,q})=\chi(g)A_{\chi,q}.
\tag{3}
\]

Equation `(1)` therefore gives

\[
\boxed{
\phi_\beta(A_{\chi,q})=0
\qquad(0<\beta\le1,\ \chi\ne1).
}
\tag{4}
\]

The same harmonic becomes visible only in the symmetry-broken low-temperature phase `beta>1`. If `phi_{beta,rho}` is an extremal KMS state with

\[
\rho(\zeta_q)=\zeta_q^c,
\qquad c\in(\mathbb Z/q\mathbb Z)^\times,
\]

then the classical Bost–Connes Gibbs formula

\[
\phi_{\beta,\rho}(e(r))
=
\frac{1}{\zeta(\beta)}
\sum_{n\ge1}\frac{\rho(\xi_r)^n}{n^\beta}
\qquad(\beta>1)
\tag{5}
\]

and the primitive Gauss-sum identity give

\[
\boxed{
\phi_{\beta,\rho}(A_{\chi,q})
=
\tau(\overline\chi)\,\chi(c)
\frac{L(\beta,\chi)}{\zeta(\beta)}
\qquad(\beta>1).
}
\tag{6}
\]

Thus the nontrivial cyclotomic character channel has an exact phase boundary: it carries normalized Dirichlet-`L` information in the broken-symmetry Gibbs phase, but its equilibrium first moment is identically zero throughout the entire `0<beta<=1` phase containing the Riemann critical half.

This closes one of the explicit residuals left by `MC-139`. A Bost–Connes continuation relevant to Möbius cancellation must use information not reducible to a **linear nontrivial symmetry character expectation in a positive-temperature KMS state**. Possible survivors include symmetry-neutral nonlinear combinations of character modes, arithmetic incidence data not represented by one KMS first moment, or a non-KMS/non-equilibrium construction. Each still needs a non-tautological transfer to the anchored additive order defining `M(x)`.

## 1. Uniqueness forces symmetry invariance

The Bost–Connes symmetry action commutes with the time evolution. Hence if `phi_beta` is a `KMS_beta` state and `g in G`, then

\[
\phi_\beta\circ\alpha_g
\]

is again a `KMS_beta` state. For `0<beta<=1` there is only one such state, so

\[
\phi_\beta\circ\alpha_g=\phi_\beta
\qquad\forall g\in G.
\tag{7}
\]

Now let `x` lie in the spectral subspace for a nontrivial continuous character `chi`:

\[
\alpha_g(x)=\chi(g)x.
\]

Choose `g` with `chi(g) != 1`. Then invariance gives

\[
\phi_\beta(x)
=
\phi_\beta(\alpha_g(x))
=
\chi(g)\phi_\beta(x),
\]

hence `phi_beta(x)=0`. This proves `(1)` without using a Gibbs trace, analytic continuation, or any zeta-zero information.

The mechanism itself is established prior art, not a new operator-algebra theorem. Expositions of the Bost–Connes uniqueness proof explicitly decompose the algebra into spectral subspaces for `G` and note that KMS states in the high-temperature phase vanish on every nontrivial character subspace. The line-specific role here is to apply that classical projection theorem to the exact degree-zero residual left by `MC-139`.

## 2. Dirichlet characters give an explicit finite cyclotomic test

For `(2)`, let `g` denote also its image in `(Z/qZ)^times`. Then

\[
\begin{aligned}
\alpha_g(A_{\chi,q})
&=
\sum_u\overline{\chi(u)}e(gu/q)\\
&=
\sum_v\overline{\chi(g^{-1}v)}e(v/q)\\
&=
\chi(g)
\sum_v\overline{\chi(v)}e(v/q),
\end{aligned}
\]

which proves `(3)`. No limit over primes or moduli is involved: every nonprincipal finite cyclotomic harmonic already vanishes exactly under the unique state.

There is an equivalent direct check from the known high-temperature restriction of `phi_beta` to `C^*(Q/Z)`: for a reduced fraction `a/b`, its value depends on the denominator `b` and not on the numerator `a`. Therefore all `e(u/q)` with `u` a unit modulo `q` have the same expectation, and the weighted sum `(2)` vanishes because

\[
\sum_{u\in(\mathbb Z/q\mathbb Z)^\times}\overline{\chi(u)}=0
\]

for nonprincipal `chi`.

This denominator-only form makes the information loss concrete. In the unique phase the equilibrium state retains conductor/divisor information but averages away the nontrivial cyclotomic orientation at that conductor.

## 3. The broken-symmetry phase recovers `L(beta,chi)/zeta(beta)`

For `beta>1`, the extremal KMS states are parametrized by cyclotomic embeddings. Insert `(5)` into `(2)` and interchange the finite `u`-sum with the absolutely convergent `n`-series:

\[
\phi_{\beta,\rho}(A_{\chi,q})
=
\frac1{\zeta(\beta)}
\sum_{n\ge1}\frac1{n^\beta}
\sum_{u\in(\mathbb Z/q\mathbb Z)^\times}
\overline{\chi(u)}\zeta_q^{cnu}.
\tag{8}
\]

For primitive `chi`, the inner sum is

\[
\tau(\overline\chi)\chi(cn),
\]

with the usual convention that `chi(n)=0` when `(n,q)>1`. Hence `(8)` becomes `(6)`.

This calculation gives a useful diagnostic but not an RH mechanism. The formula is a genuine Gibbs/KMS expectation only in `beta>1`, exactly where both `zeta(beta)` and `L(beta,chi)` are represented by absolutely convergent Dirichlet series and `zeta(beta)` is nonzero. Meromorphically continuing the scalar ratio in `(6)` into the critical strip does **not** continue the corresponding extremal KMS state through the phase transition.

For a nonprincipal primitive character, `L(s,chi)` is finite and nonzero at `s=1`, while `zeta(s)` has its simple pole there. Therefore the broken-symmetry order parameter in `(6)` tends to zero as `beta downarrow 1`, consistently with the exact restoration of symmetry in `(4)`. This is a phase-transition boundary, not a route for transporting the low-temperature character value to `beta=1/2`.

## 4. Relation to `MC-138` and `MC-139`

`MC-138` shows that the divisibility diagonal is a product state across prime valuations. Connected diagonal cross-prime covariances therefore vanish, while restoring an undamped Möbius-oriented local phase raises the natural unweighted variance threshold from `beta=1/2` back to `beta=1`.

`MC-139` then shows that non-diagonal semigroup energy does not fix that problem. Every nonzero time-evolution degree is annihilated by a KMS state, and unique factorization forces rational energy neutrality prime by prime. It leaves degree-zero coefficient/cyclotomic information as a possible carrier.

The present result narrows that residue in the independent symmetry direction. Degree zero under the time evolution is not sufficient: if the degree-zero observable transforms under a nontrivial cyclotomic character, the unique `0<beta<=1` equilibrium state annihilates it exactly. The two selection rules are logically distinct:

\[
\text{time-evolution neutrality}
\quad\text{and}\quad
\text{cyclotomic-symmetry neutrality}
\]

are separate necessary conditions for a nonzero high-temperature KMS first moment.

Consequently the most obvious linear Bost–Connes carriers have now been filtered twice. A surviving equilibrium first moment at `beta=1/2` must lie simultaneously in the zero-energy and symmetry-invariant sectors. That condition alone does not make it useful: `MC-138` already illustrates that invariant positive or quadratic information can retain support while losing the sign/orientation needed for Möbius cancellation.

## Prior art and novelty assessment

The underlying phase transition and symmetry theorem is classical:

- Jean-Benoît Bost and Alain Connes, *Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory*, Selecta Mathematica (N.S.) **1** (1995), no. 3, 411–457, DOI `10.1007/BF01589495`. The paper constructs the symmetry action commuting with the dynamics, proves uniqueness in the high-temperature regime, and parametrizes the `beta>1` extremal phases by embeddings of the cyclotomic field.
- Sergey Neshveyev, *Ergodicity of the action of the positive rationals on the group of finite adeles and the Bost-Connes phase transition theorem*, Proceedings of the American Mathematical Society **130** (2002), no. 10, 2999–3003, DOI `10.1090/S0002-9939-02-06449-3`, arXiv `math/0002141`. It gives an ergodic proof of uniqueness for `0<beta<=1`.

A targeted prior-art search also located an explicit exposition of the exact spectral-subspace statement used in `(1)`: Konrad Pilch, *Noncommutative Geometry Methods in Number Theory*, M.Phil. thesis, University of Adelaide (2014), §7.3, records the character subspaces for `G` and states that the high-temperature KMS projection vanishes completely on the nontrivial ones. This confirms that the symmetry-character annihilation mechanism itself should be treated as established prior art.

The finite Dirichlet-character sum `(2)` and formula `(6)` are elementary specializations of the standard cyclotomic KMS formula and the classical Gauss-sum identity. No novelty is claimed for them. The durable Mathia contribution is only the **frontier audit**: the degree-zero cyclotomic/Galois escape left by `MC-139` cannot be realized as a nontrivial linear symmetry harmonic of a `KMS_beta` state at or below the phase transition.

## Boundaries and falsification tests

- The obstruction concerns **linear expectations** of nontrivial symmetry spectral subspaces. Products whose total symmetry character is trivial, such as `x_chi^* x_chi` or more general character-balanced correlations, can survive and are not classified by `(1)`.
- Symmetry-neutral nonlinear combinations may still carry arithmetic information. They require a separate audit of whether absoluteization or character pairing destroys the orientation relevant to Möbius cancellation.
- The result does not say that the high-temperature fixed-point algebra is trivial. It says only that nontrivial `G`-isotypic first moments vanish.
- The low-temperature formula `(6)` is restricted to `beta>1`; treating its meromorphic continuation as an equilibrium expectation below the phase transition would change the mathematical object.
- Non-KMS states, non-equilibrium correlation functions, distributions obtained from a trace formula, or zero-temperature limiting constructions are outside the claim.
- A character-balanced multi-point observable can involve several primes or conductors while remaining symmetry invariant. This finding does not prove such an observable factors or is phase-blind.
- None of `(1)`--`(6)` yields a bound for `M(x)`. Even a surviving Bost–Connes statistic must still recover anchored integer-prefix excursion at a cost strictly cheaper than an RH-equivalent Mertens estimate.
- The use of Dirichlet characters here probes cyclotomic/Galois orientation, not the full Möbius sign law. The result must not be read as proving that Bost–Connes high-temperature equilibrium erases every possible encoding of Möbius parity.

A counterexample to `(1)` would require either a nonunique `KMS_beta` state for some `0<beta<=1`, a purported symmetry that fails to commute with the Bost–Connes dynamics, or an element claimed to transform by a nontrivial character whose expectation nevertheless violates invariance. All three conditions are directly testable against the classical phase-transition theorem and the stated symmetry action.

## Consequence for the line

The Bost–Connes residual after `MC-139` is now narrower. **At the critical half, a canonical equilibrium first moment must be both energy-neutral and cyclotomic-symmetry-neutral.** Nontrivial degree-zero character harmonics do exist as arithmetic order parameters in the `beta>1` broken phase and are explicitly proportional to `L(beta,chi)/zeta(beta)`, but the unique `0<beta<=1` KMS state projects them to zero before the critical line is reached.

Future Bost–Connes work in Möbius Cancellation should therefore not search for an RH-relevant signal in a single nontrivial cyclotomic KMS harmonic at `beta=1/2`. The remaining meaningful tests are symmetry-neutral nonlinear/correlation carriers, genuinely non-equilibrium constructions, or another arithmetic object altogether — and any survivor must still supply the missing source-to-Mertens-amplitude theorem rather than merely exposing another analytic continuation of an `L/zeta` ratio.