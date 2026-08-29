# WP-027 — Positive commutator energy radializes the Mangoldt selector

**Status:** `EXACT-DERIVED + CLASSICAL-CAR + DECISIVE-NEGATIVE` for the canonical commutator/carré-du-champ repair of the non-`Q`-invariant Boolean Mangoldt insertion from WP-018/WP-020. The exterior-algebra creation/annihilation relations and the resulting Clifford norm identity are standard finite-dimensional mathematics. The project-specific conclusion is that the most intrinsic way to turn the successful noncommutation `[R_alpha,Q_alpha] != 0` into a positive operator — squaring it, taking its modulus, or applying positive spectral functional calculus to that single commutator — destroys exactly the Möbius/Boolean cancellation that selects prime powers. The resulting positive observable is radial in the vector of distinct-prime logarithms and is nonzero on ordinary composites such as `6`.

## 1. The live escape after WP-020

WP-018 gives, for every exponent vector

\[
\alpha=v(n),
\]

the backward Boolean cube on the distinct-prime support

\[
S=S(\alpha)=\{p:\alpha_p>0\},
\qquad
\mathcal H_\alpha=\ell^2(2^S),
\]

with parity grading `Gamma` and positive residual-energy insertion

\[
R_\alpha e_T
=
\left(E(\alpha)-\sum_{p\in T}\log p\right)e_T,
\qquad T\subseteq S,
\]

such that

\[
\boxed{\operatorname{Str}R_\alpha=\Lambda(n).}
\tag{1}
\]

WP-020 then shows that for the canonical Boolean Hodge supercharge

\[
Q_\alpha=d_\alpha+d_\alpha^*,
\]

the successful arithmetic insertion is structurally non-invariant:

\[
[R_\alpha,Q_\alpha]\ne0,
\]

and its edge coefficients are exactly the prime logarithms. This left open a very natural possibility: perhaps the noncommutator itself is the missing geometric differential, and a canonical positive quantity such as

\[
[R,Q]^*[R,Q],\qquad |[R,Q]|,
\]

or a positive spectral function of it supplies the independent sign theorem.

For the intrinsic Boolean cube, that route can be evaluated exactly. It fails for a stronger reason than mere loss of a normalization: the positive repair collapses to a scalar Clifford norm and forgets prime-power support.

## 2. Exterior-algebra form of the Boolean cube

Write `r=|S|` and identify the oriented Boolean cube with the fermionic exterior algebra

\[
\mathcal H_\alpha\cong \Lambda^*\mathbb C^r.
\]

For each `p in S`, let `epsilon_p` denote exterior multiplication by the basis vector indexed by `p`, and let `iota_p=epsilon_p^*` be contraction. They satisfy the canonical anticommutation relations

\[
\{\epsilon_p,\epsilon_q\}=0,
\qquad
\{\iota_p,\iota_q\}=0,
\qquad
\{\epsilon_p,\iota_q\}=\delta_{pq}I.
\tag{2}
\]

Let

\[
N_p=\epsilon_p\iota_p,
\]

so that `N_p e_T=e_T` if `p in T` and zero otherwise. Put

\[
a_p=\log p.
\]

Then the two canonical operators are exactly

\[
Q_\alpha=\sum_{p\in S}(\epsilon_p+\iota_p),
\tag{3}
\]

and

\[
R_\alpha=E(\alpha)I-\sum_{p\in S}a_pN_p.
\tag{4}
\]

The commutators

\[
[N_p,\epsilon_p]=\epsilon_p,
\qquad
[N_p,\iota_p]=-\iota_p
\]

give

\[
[R_\alpha,Q_\alpha]
=
\sum_{p\in S}a_p(\iota_p-\epsilon_p).
\tag{5}
\]

Thus the self-adjoint version of the arithmetic edge differential is

\[
C_\alpha:=i[R_\alpha,Q_\alpha]
=
\sum_{p\in S}a_p\gamma_p,
\qquad
\gamma_p:=i(\iota_p-\epsilon_p).
\tag{6}
\]

Each `gamma_p` is self-adjoint, and (2) gives the Clifford relations

\[
\gamma_p^2=I,
\qquad
\gamma_p\gamma_q+\gamma_q\gamma_p=0
\quad(p\ne q).
\tag{7}
\]

No asymptotic, zeta identity, zero data, or analytic continuation is used here.

## 3. Exact Clifford radialization

Squaring (6) and using (7) kills every cross term:

\[
\boxed{
C_\alpha^2
=
\left(\sum_{p\mid n}(\log p)^2\right)I.
}
\tag{8}
\]

Define

\[
A(n):=
\left(\sum_{p\mid n}(\log p)^2\right)^{1/2}.
\tag{9}
\]

For every `n>1`, equation (8) gives

\[
\boxed{|[R_\alpha,Q_\alpha]|=|C_\alpha|=A(n)I.}
\tag{10}
\]

Since `C_alpha` is odd with respect to the Boolean parity and `C_alpha^2=A(n)^2 I`, its spectrum is

\[
\{+A(n),-A(n)\}
\]

with equal multiplicity `2^{r-1}`.

This is the obstruction. The successful arithmetic selector (1) depends on an **alternating finite difference over the whole Boolean cube**. The canonical positive commutator norm has forgotten the cube incidence pattern completely: it retains only the Euclidean length of the distinct-prime log vector.

For a prime power `n=p^k`,

\[
A(p^k)=\log p=\Lambda(p^k),
\]

so the route looks perfect on every one-dimensional cube. But the first matched composite control already kills it:

\[
A(6)=\sqrt{(\log2)^2+(\log3)^2}>0,
\qquad
\Lambda(6)=0.
\tag{11}
\]

Likewise every integer with at least two distinct prime factors receives a strictly positive commutator energy although the von Mangoldt selector vanishes.

The square/carré-du-champ version fails in the same way:

\[
[R,Q]^*[R,Q]
=A(n)^2I
=\left(\sum_{p\mid n}(\log p)^2\right)I.
\tag{12}
\]

The sign theorem is genuine and unconditional, but it is attached to the wrong arithmetic observable.

## 4. Spectral positivity of the single commutator cannot recover the Boolean cancellation

Because `C_alpha` has only the two eigenvalues `+/-A(n)`, every scalar spectral function has the form

\[
f(C_\alpha)=u_f(A(n))I+v_f(A(n))C_\alpha.
\tag{13}
\]

For `r>=1`,

\[
\operatorname{Tr}\Gamma=0,
\qquad
\operatorname{Tr}(\Gamma C_\alpha)=0,
\]

and therefore

\[
\boxed{
\operatorname{Str}f(C_\alpha)=0
\quad\text{for every scalar spectral }f.
}
\tag{14}
\]

So there is no hidden rescue in replacing the modulus by another function of the same commutator. The two natural readouts behave oppositely:

- an **ordinary positive trace** of a nontrivial positive `f(C_alpha)` is generically nonzero on multi-prime composites and therefore loses the Mangoldt support;
- restoring the **Boolean supertrace** annihilates every spectral function of `C_alpha` identically, rather than recovering `Lambda`.

A nonnegative spectral function could be hand-tuned to vanish at selected radii `A(n)`, but then the prime-power selector is being inserted through the zero set of `f`; it is not forced by commutator positivity. The exact intrinsic choices `C^2`, `|C|`, positive powers, heat kernels, resolvents below spectrum, and completely monotone functions all retain the same radial variable `A(n)` and do not perform the Möbius cancellation of WP-018.

## 5. Critical attenuation does not help

The finite Weil coefficient requires the additional scalar attenuation

\[
e^{-E(\alpha)/2}=n^{-1/2}.
\]

Multiplying the positive commutator energy by this factor gives, for example,

\[
n^{-1/2}|C_\alpha|
=
\frac{A(n)}{\sqrt n}I\ge0.
\tag{15}
\]

But the support defect survives unchanged:

\[
\frac{A(6)}{\sqrt6}>0,
\qquad
\frac{\Lambda(6)}{\sqrt6}=0.
\]

Thus the critical half-weight is not the missing operation. The missing operation is still the alternating Boolean selector itself.

One can multiply `R_alpha` by a positive scalar function of `|C_alpha|` and then take a supertrace, obtaining a scalar multiple of `Lambda(n)`. That does not solve the problem: the arithmetic information is still coming from the signed functional `Str(R_alpha ·)`, whose lack of positivity was the obstruction in WP-018/WP-020. The commutator norm has not converted that signed readout into an ordinary positive pairing.

## 6. Matched generalized-prime control

Nothing in (2)--(14) uses special arithmetic properties of rational primes. Replace the edge costs `log p` by arbitrary positive numbers `a_j` on a free commutative monoid. The identical calculation gives

\[
C^2=\left(\sum_j a_j^2\right)I.
\tag{16}
\]

Hence the commutator positivity is a universal Clifford/Fock-space fact. It survives arbitrary generalized-prime controls, including systems whose zeta functions have zero behavior incompatible with the Riemann RH target.

This is an important falsification check: the positive theorem is too universal to be the global arithmetic sign mechanism by itself.

## 7. Prior-art and novelty audit

No novelty is claimed for the CAR relations, the exterior-algebra realization of a cube, the Clifford identity `(sum a_j gamma_j)^2=(sum a_j^2)I`, or for using Dirac commutators and their squares/moduli as positive metric/energy data. Those are standard constructions in fermionic Fock/Clifford algebra, spectral-triple differential calculus, and Dirichlet/carré-du-champ geometry.

WP-020 already places the surrounding supersymmetric route against McKean--Singer, equivariant index theory, and Quillen superconnections. The present result does not propose another index theorem and does not repackage a zeta identity. Its durable Mathia-specific content is the exact evaluation of the **one noncommuting operator that WP-020 left alive**: the weighted Boolean commutator carrying the prime-log edge differences.

The novelty audit therefore changes the status of a concrete escape route rather than claiming a new general theorem. The route

```text
exact WP-018 residual energy R_alpha
    -> noncommutation [R_alpha,Q_alpha]
    -> canonical positive commutator norm / square
    -> arithmetic positivity
```

is closed at the third arrow: positivity radializes the edge vector and destroys the prime-power selector.

This is also distinct from WP-016. WP-016 shows that ordinary positive Hodge spectrum cancels from the arithmetic supertrace. WP-027 treats the opposite side of the WP-020 fork, where the exact arithmetic insertion deliberately fails to commute with the Hodge differential, and shows that the canonical **positive repair of that failure** still loses the arithmetic support.

## 8. Boundary of the obstruction

This finding is deliberately narrower than a no-go for every noncommuting or noncommutative-geometric construction.

It does **not** rule out:

- a globally coupled finite/archimedean operator formed **before** the commutator is squared, whose commutator has new mixed curvature terms and a nontrivial order theorem;
- a boundary, relative, APS/eta, transgression, or trace-defect mechanism in which the relevant information is not a scalar spectral function of the finite `C_alpha`;
- a higher multilinear expression using several distinct commutators, provided its sign and Mangoldt support follow canonically rather than from an inserted alternating projector;
- a compression or quotient whose positivity theorem is sensitive to cube incidence and not merely to the Clifford norm;
- a genuinely global differential for which `R_alpha` is only the finite shadow of one coupled object that also generates the archimedean and polar terms.

In particular, the result says that **global coupling must occur before the standard positive norm forgets the Boolean orientation data** if the WP-018 mechanism is to remain useful.

## 9. Falsification criterion and research consequence

Withdraw or narrow this finding if any of the following exact statements fails:

1. the canonical Boolean cube admits the exterior/contraction operators satisfying (2);
2. `R_alpha` and `Q_alpha` have the forms (3)--(4);
3. their self-adjoint commutator is the weighted Clifford element (6);
4. its square is the scalar operator (8);
5. therefore its modulus is (10) and is strictly positive for every `n>1`, including multi-prime composites where `Lambda(n)=0`;
6. every scalar spectral function of `C_alpha` has the two-dimensional form (13);
7. its Boolean supertrace vanishes as in (14).

All seven statements are finite-dimensional exact algebra. They can be checked on the first two-dimensional control `n=p^k` and the first four-dimensional control `n=p^a q^b` before any analytic completion is considered.

The research consequence is a sharpened version of the WP-020 fork. Merely saying “the arithmetic insertion does not commute with the supercharge, so use its commutator as geometry” is no longer a live mechanism. The first canonical positivity operations on that commutator erase the very inclusion-exclusion structure that makes `Lambda` appear.

A surviving construction must therefore preserve the **oriented/multilinear Boolean information through the finite--archimedean coupling**, and obtain positivity only after that coupling, from a theorem stronger than the universal Clifford norm identity.

## Internal dependencies

- `research/weil_positivity/findings/WP-018-local-boolean-energy-supertrace-recovers-von-mangoldt-but-is-not-positive.md`
- `research/weil_positivity/findings/WP-020-q-invariant-coupled-hodge-insertions-still-collapse-to-index.md`
- `research/weil_positivity/findings/WP-016-prime-lattice-hodge-positivity-cancels-out-of-the-arithmetic-supertrace.md`
