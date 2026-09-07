# PL-193 — Scalar phase covariance under all prime shifts collapses normal operators to a multiplicative character

## Claim

Let `H^2` be the standard Hardy Hilbert space of Dirichlet series, identified with `ell^2(N)` through the orthonormal basis

\[
e_n(s)=n^{-s},\qquad n\ge 1,
\]

and let the prime shifts be

\[
S_p e_n=e_{pn}.
\]

Fix arbitrary phases `omega_p in T`. Unique factorization extends them to the completely multiplicative unit-modulus character

\[
\chi(n)=\prod_p \omega_p^{v_p(n)}.
\]

Define the diagonal unitary

\[
U_\chi e_n=\chi(n)e_n.
\]

Then the bounded operators satisfying the exact scalar projective covariance

\[
T S_p=\omega_p S_p T\qquad\text{for every prime }p
\]

form only a gauge translate of the ordinary prime-shift commutant:

\[
\boxed{
T S_p=\omega_p S_pT\ \forall p
\quad\Longleftrightarrow\quad
T=U_\chi M_D
}
\]

for a bounded Dirichlet multiplier `M_D`. In particular, if `T` is normal, then the multiplier is forced to be constant and

\[
\boxed{T=cU_\chi.}
\]

Thus allowing a scalar phase cocycle along each prime direction does not open a new normal spectral class beyond a diagonal completely multiplicative character. If `T` itself is self-adjoint and nonzero, then `c` is real and `chi(n) in {+1,-1}` for all `n`; hence its spectrum has at most the two values `{-c,c}`. The Liouville choice `omega_p=-1` for every prime gives exactly

\[
U_\chi e_n=(-1)^{\Omega(n)}e_n=\lambda(n)e_n,
\]

so the canonical global parity twist is one of these two-point diagonal characters, not a Hilbert–Pólya spectrum.

There is an even stronger resolvent obstruction. Let `H` be self-adjoint, possibly unbounded, and suppose one nonreal resolvent

\[
R=(H-i)^{-1}
\]

satisfies

\[
R S_p=\omega_p S_pR\qquad\forall p.
\]

Since `R` is bounded and normal, the previous classification gives `R=cU_chi`. The resolvent geometry of a self-adjoint operator then forces every `omega_p=1`; consequently `R=cI` and `H` is scalar. Therefore **even projective scalar phase covariance of a self-adjoint resolvent cannot evade the scalar-collapse obstruction of `PL-023`**.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + DECISIVE-NEGATIVE` for the route “replace exact prime-shift invariance by a scalar phase/projective cocycle and seek a normal or self-adjoint zero operator.” The ordinary commutant theorem is literature (`PL-023`, Fernández Vidal–Galicer–Sevilla-Peris). The phase-gauge reduction, vacuum normality argument, and resolvent corollary are elementary exact deductions specialized to the prime-exponent representation. No novelty claim is made for lambda-commuting operator theory itself.

## 1. Scalar prime phases are exactly a diagonal gauge of the ordinary commutant

The diagonal character obeys

\[
U_\chi S_p e_n
=\chi(pn)e_{pn}
=\omega_p\chi(n)e_{pn}
=\omega_p S_pU_\chi e_n,
\]

so

\[
U_\chi S_p=\omega_p S_pU_\chi.
\]

Suppose `T` satisfies the same covariance. Since

\[
U_\chi^*S_p=\overline{\omega_p}S_pU_\chi^*,
\]

we obtain

\[
(U_\chi^*T)S_p
=U_\chi^*\omega_pS_pT
=S_p(U_\chi^*T).
\]

Thus `U_chi^* T` commutes with every prime shift. Theorem 4.1 of Fernández Vidal, Galicer, and Sevilla-Peris, already used in `PL-023`, identifies that full bounded commutant on the Hardy spaces of Dirichlet series with multiplication operators. Hence

\[
U_\chi^*T=M_D,
\qquad
T=U_\chi M_D.
\]

Conversely every `U_chi M_D` has the required covariance because `M_D` commutes with all `S_p`. Therefore the scalar-twisted commutant is not merely analogous to the untwisted one: it is unitarily gauge-equivalent to it by the canonical exponent-lattice character `U_chi`.

This is the precise reason arbitrary independent scalar phases on prime directions do not create new cross-prime structure. Unique factorization integrates them automatically into a one-dimensional completely multiplicative character.

## 2. Normality kills every nonconstant multiplier even after the twist

A direct vacuum argument avoids any need to infer normality of `U_chi^*T`. Let

\[
x=Te_1=\sum_{k\ge1}a_ke_k.
\]

The prime covariance extends multiplicatively to every integer:

\[
TS_n=\chi(n)S_nT,
\]

where `S_n e_m=e_{nm}`. Since `e_n=S_ne_1`,

\[
Te_n=\chi(n)S_nx.
\]

For every `n>1`, the vector `S_nx` is supported only on multiples of `n`, so it has zero `e_1` coefficient. Therefore

\[
T^*e_1=\overline{a_1}e_1.
\]

If `T` is normal, then `||Te_1||=||T^*e_1||`, giving

\[
\sum_{k\ge1}|a_k|^2=|a_1|^2.
\]

Hence `a_k=0` for every `k>1`, so `x=a_1e_1`. Returning to the covariance formula,

\[
Te_n=a_1\chi(n)e_n
\]

for every `n`, and therefore

\[
\boxed{T=a_1U_\chi.}
\]

This deduction uses only the vacuum vector and the divisibility triangularity of the positive prime shifts. It is unconditional and independent of zeta continuation.

If `T` is self-adjoint and nonzero, its `e_1` eigenvalue is `a_1`, so `a_1` is real. Self-adjointness then requires every `a_1 chi(n)` to be real. Because `|chi(n)|=1`,

\[
\chi(n)\in\{+1,-1\}.
\]

Thus any self-adjoint scalar-covariant operator has at most two spectral values. In particular the all-minus prime assignment is exactly the Liouville parity operator, while arbitrary unit-circle prime phases can only survive in the larger normal, non-self-adjoint class.

## 3. A self-adjoint resolvent cannot carry even a nontrivial phase twist

The bounded-self-adjoint statement still leaves a possible objection: a Hilbert–Pólya operator should normally be unbounded, so perhaps one could impose scalar projective covariance only on a bounded resolvent. That escape also collapses.

Let

\[
R=(H-i)^{-1}
\]

for self-adjoint `H`, and assume

\[
RS_p=\omega_pS_pR.
\]

The resolvent is bounded and normal, hence the preceding theorem gives

\[
R=cU_\chi,
\qquad c\ne0.
\]

Because `U_chi` is unitary, `R` is onto. Therefore `Dom(H)=Ran(R)=H^2`, so `H` is in fact bounded. Moreover each basis vector is an eigenvector of both `R` and `H`. Write

\[
He_n=h_ne_n,
\qquad h_n\in\mathbb R.
\]

Then

\[
c\chi(n)=(h_n-i)^{-1}.
\]

All resolvent eigenvalues have the same modulus `|c|`, so

\[
h_n^2+1=|c|^{-2}
\]

for every `n`. Hence the real sequence `{h_n}` takes at most two values, `+a` and `-a`.

Now fix a prime `p`. Along its axis,

\[
R e_{p^k}=c\omega_p^k e_{p^k}.
\]

Since the corresponding `h_(p^k)` take at most two values, the powers `omega_p^k` take at most two values. Thus `omega_p` has order at most two. The only nontrivial possibility is `omega_p=-1`, but then both `c` and `-c` would be resolvent eigenvalues. This is impossible for `(H-i)^{-1}`, because for every real `h`

\[
\operatorname{Im}(h-i)^{-1}=\frac1{h^2+1}>0,
\]

whereas `c` and `-c` have opposite imaginary parts. Therefore

\[
\omega_p=1
\]

for every prime. The twisted covariance reduces to ordinary commutation, `R=cI`, and consequently `H` is scalar.

So the unbounded Hilbert–Pólya route is even more rigid than the bounded normal statement:

\[
\boxed{
H=H^*,\ (H-i)^{-1}S_p=\omega_pS_p(H-i)^{-1}\ \forall p
\quad\Longrightarrow\quad
\omega_p=1\ \forall p,\ H\text{ scalar}.
}
\]

## 4. Prior art and novelty audit

The direct Dirichlet-series anchor is the same theorem already recorded as source 41 for `PL-023`:

- Tomás Fernández Vidal, Daniel Galicer, Pablo Sevilla-Peris, “Multipliers for Hardy spaces of Dirichlet series,” *Annales de l'Institut Fourier* **75**(2) (2025), 541–577, DOI `10.5802/aif.3658`, arXiv `2205.07961`. Their Theorem 4.1 identifies operators commuting with every prime monomial shift as multipliers.

Scalar commutation up to a phase is itself classical operator-theory language. A targeted novelty search found, among nearby references, Sungeun Jung, Hyoungji Kim, and Eungil Ko, “On extended commuting operators,” *Filomat* **35**(3) (2021), 883–893, DOI `10.2298/FIL2103883J`, which studies `lambda`-commuting operators and states that operators `lambda`-commuting with the unilateral shift are weighted composition operators. Its introductory examples include the standard normal diagonal character satisfying `DS=lambda SD`. This is the one-variable analogue of the diagonal `U_chi` appearing here.

The present result is therefore **not** claimed as a new abstract operator theorem. Its durable contribution is the line-specific classification and obstruction: once all prime directions are required simultaneously, every scalar phase cocycle integrates to a completely multiplicative diagonal gauge, and normality removes the multiplier freedom. Requiring the covariance at the resolvent level of a self-adjoint operator removes even the nontrivial character.

No update to `research/prime_lattice/SOURCES.md` is required for the proof: the only external theorem actually invoked is already source 41. The Jung–Kim–Ko paper is a novelty-audit adjacency, not an evidentiary dependency.

## 5. Adversarial boundaries

The result is deliberately narrow.

First, **normality is essential** for the scalar collapse. Without normality, the whole twisted multiplier family `U_chi M_D` survives. The finding does not rule out nonnormal transfer operators, resonances, or scattering constructions; it says only that scalar projective covariance does not produce a new normal/self-adjoint spectral class.

Second, the phases are **scalars**. An operator-valued cocycle, a noncommuting matrix representation attached to prime directions, a target-relative model-space action, or a coupling through additional adelic/archimedean data is not gauge-equivalent to a one-dimensional completely multiplicative character by this argument. This is exactly where any genuinely relational prime-shift mechanism must now live.

Third, the covariance is exact for **every prime shift**. Approximate covariance, covariance modulo compact/trace ideals, or relations imposed only on a sparse family require separate estimates; several such routes are already treated elsewhere in this line. No stability theorem is inferred from the exact result.

Fourth, additive energy covariance such as

\[
[H,S_p]=(\log p)S_p
\]

is not a scalar projective relation of the form studied here. `PL-024` already identifies its canonical Bost–Connes realization. The present negative therefore complements rather than replaces the additive-covariance analysis.

Finally, no Euler product or analytic continuation appears anywhere in the proof. The obstruction is pure operator geometry on the exponent-lattice representation. Accordingly it cannot itself prove RH; its role is to remove a natural but insufficient spectral design class before any zero-sensitive continuation machinery is introduced.

## Consequence for the research line

`PL-023` ruled out exact **commutation** with all prime-coordinate shifts for a nontrivial normal/self-adjoint spectrum. The present result closes the immediate projective escape:

\[
\text{scalar prime phase covariance}
\quad\Longrightarrow\quad
\text{multiplicative-character gauge of the same commutant}
\quad\Longrightarrow\quad
\text{normal slice }cU_\chi.
\]

At the self-adjoint-resolvent level even that character disappears. Therefore a surviving “relational prime-shift” mechanism cannot consist merely of assigning one scalar phase to each prime direction. It must carry genuinely non-scalar joint information — operator-valued cocycles, target-relative couplings, completed local/global structure, or another relation not removable by a completely multiplicative diagonal gauge.
