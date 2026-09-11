# AF-273 — Reflection-symmetric cyclotomic splits defeat every fixed source prefix

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SOURCE`, `REFLECTION-SYMMETRY`, `PRIME-POWER-SPECTRUM`, `FINITE-PREFIX-OBSTRUCTION`, `CYCLOTOMIC-FILTER`, `QUOTIENT-COMPLEXITY`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-270 shows that an infinite reflection-symmetric zero transport can remain periodic and stay on a single rational-prime-power source ray. AF-272 then shows that finite source prefixes detect rational periodic divisor changes only after a bound on the **cancelled quotient divisor complexity** is supplied. The remaining question is whether the Riemann-type reflection symmetry and exact ordinate matching present in AF-270 might themselves collapse that complexity enough to make some fixed finite prefix universally decisive.

They do not.

Fix a rational prime `p`, set

\[
\lambda:=\log p,
\qquad
L:=\frac{2\pi}{\lambda},
\qquad
z:=p^{-s},
\tag{1}
\]

and let `M>=2` be an integer. For `a in (0,1)` define

\[
H_{a,M}(s)
:=
\bigl(1-p^{M(a-s)}\bigr)
\bigl(1-p^{M(a-1+s)}\bigr).
\tag{2}
\]

Then `H_{a,M}` is an order-one exponential polynomial satisfying

\[
H_{a,M}(1-s)=H_{a,M}(s),
\qquad
\overline{H_{a,M}(\overline s)}=H_{a,M}(s).
\tag{3}
\]

Its zero divisor is

\[
Z(H_{a,M})
=
\left\{a+i\frac{nL}{M}:n\in\mathbb Z\right\}
\sqcup
\left\{1-a+i\frac{nL}{M}:n\in\mathbb Z\right\},
\tag{4}
\]

with multiplicity. At `a=1/2` the two lattices coincide, producing a double critical-line lattice. For `a!=1/2` the same two zeros at every ordinate split to the symmetric off-critical pair `Re(s)=a` and `Re(s)=1-a`. Consequently

\[
N_{a,M}(T)=N_{1/2,M}(T)
\tag{5}
\]

for every `T`, counting multiplicity by ordinate exactly as in AF-270.

Now compare the off-critical and critical controls through

\[
Q_{a,M}(s)
:=
\frac{H_{a,M}(s)}{H_{1/2,M}(s)}.
\tag{6}
\]

Up to a nonzero constant, this quotient is rational in `z=p^{-s}`:

\[
Q_{a,M}(s)
\doteq
\frac{\bigl(1-p^{Ma}z^M\bigr)
      \bigl(1-p^{M(1-a)}z^M\bigr)}
     {\bigl(1-p^{M/2}z^M\bigr)^2}.
\tag{7}
\]

On every right half-plane `Re(s)>max(a,1-a)`, its logarithmic derivative has an absolutely convergent ordinary Dirichlet expansion

\[
\boxed{
\frac{Q_{a,M}'}{Q_{a,M}}(s)
=
\lambda\sum_{k\ge1}q_k p^{-ks},
}
\tag{8}
\]

with

\[
\boxed{
q_k=0\quad(M\nmid k),
}
\tag{9}
\]

and, for `n>=1`,

\[
\boxed{
q_{Mn}
=
M\left(
 p^{Mna}+p^{Mn(1-a)}-2p^{Mn/2}
\right)
>0
\qquad(a\ne1/2).
}
\tag{10}
\]

Thus the first `M-1` source coefficients of the critical and off-critical controls agree **exactly**, even though their differing zero lattices are respectively critical and off-critical. Given any prescribed finite prefix length `K`, choosing `M>K` produces such a matched pair with

\[
q_1=\cdots=q_K=0
\tag{11}
\]

and a nontrivial reflection-symmetric off-critical divisor change.

This remains true even if one insists that both complete controls have nonzero coefficients at every frequency on the full prime-power ray. Let

\[
B_p(s):=H_{1/2,1}(s)
\tag{12}
\]

and define

\[
F_{0,M}(s):=B_p(s)H_{1/2,M}(s),
\qquad
F_{a,M}(s):=B_p(s)H_{a,M}(s).
\tag{13}
\]

The common factor `B_p` supplies every frequency `k\log p`, while

\[
\frac{F_{a,M}'}{F_{a,M}}
-
\frac{F_{0,M}'}{F_{0,M}}
=
\frac{Q_{a,M}'}{Q_{a,M}}
\tag{14}
\]

still vanishes through degree `M-1`. Hence both controls have the same full rational-prime-power frequency alphabet, exact Riemann-type reflection/conjugation symmetry, and identical zero counts by ordinate, yet an arbitrarily long initial coefficient window can fail to see the off-critical split.

Therefore:

\[
\boxed{
\text{reflection symmetry}
+\text{exact ordinate matching}
+\text{full prime-power support}
\not\Longrightarrow
\text{complexity-independent finite-prefix fidelity}.
}
\tag{15}
\]

Any finite source certificate still needs an independent bound on effective quotient complexity, a stronger cross-frequency coefficient law, or another resource capable of excluding these cyclotomic cancellation blocks.

## Exact derivation

### 1. The matched zero lattices

The first factor in `(2)` vanishes when

\[
p^{M(a-s)}=1,
\tag{16}
\]

so

\[
s=a+i\frac{nL}{M},
\qquad n\in\mathbb Z.
\tag{17}
\]

The second factor similarly gives

\[
s=1-a+i\frac{nL}{M}.
\tag{18}
\]

Equations `(17)` and `(18)` prove `(4)`. At `a=1/2` both factors have the same zero set; away from `1/2` they have the same ordinate set but different real parts. This proves `(5)` without any asymptotic argument.

The symmetry `(3)` is equally direct: `s -> 1-s` swaps the two factors in `(2)`, while real `p,a,M` give conjugation symmetry. Thus the construction does not obtain its long source-prefix collision by dropping the symmetry class used in AF-270.

### 2. The quotient is a cyclotomic block in the prime coordinate

With `z=p^{-s}`, the first factor of `(2)` is

\[
1-p^{Ma}z^M.
\tag{19}
\]

For the reflected factor,

\[
1-p^{M(a-1)}z^{-M}
=
-p^{M(a-1)}z^{-M}
\left(1-p^{M(1-a)}z^M\right).
\tag{20}
\]

The same monomial factor appears in the critical denominator. It cancels in the quotient, leaving `(7)` up to the harmless nonzero constant `p^{M(a-1/2)}`.

If `omega_M=e^{2\pi i/M}`, then the elementary cyclotomic factorization

\[
1-(Az)^M
=
\prod_{j=0}^{M-1}
\left(1-A\omega_M^jz\right)
\tag{21}
\]

shows that the cancelled quotient divisor has three radial `M`-gons in the `z`-plane:

\[
p^a\omega_M^j,
\qquad
p^{1-a}\omega_M^j,
\qquad
p^{1/2}\omega_M^j,
\tag{22}
\]

with signed multiplicities `+1,+1,-2`. For `a!=1/2` these are `3M` distinct signed divisor nodes. This places the family exactly inside the rational periodic quotient class audited by AF-272, but with the additional reflection and count-matching structure inherited from AF-270.

### 3. Root-of-unity filtering hides the first `M-1` coefficients

Logarithmically differentiating a factor `1-cz^M` gives

\[
\frac{d}{ds}\log(1-cz^M)
=
M\lambda\frac{cz^M}{1-cz^M}
=
M\lambda\sum_{n\ge1}c^n z^{Mn},
\tag{23}
\]

on the corresponding right half-plane. Applying `(23)` to `(7)` yields

\[
\frac{Q_{a,M}'}{Q_{a,M}}(s)
=
M\lambda\sum_{n\ge1}
\left(
 p^{Mna}+p^{Mn(1-a)}-2p^{Mn/2}
\right)
p^{-Mns},
\tag{24}
\]

which is `(8)`--`(10)`.

The same cancellation can be read directly from the power-sum form in AF-272. For `1<=k<M`,

\[
\sum_{j=0}^{M-1}\omega_M^{jk}=0,
\tag{25}
\]

so each radial `M`-gon has zero `k`th power sum. At `k=M` the root-of-unity sum equals `M`, and the three radii leave

\[
q_M
=
M\left(p^{Ma}+p^{M(1-a)}-2p^{M/2}\right).
\tag{26}
\]

Writing `u=M\lambda(a-1/2)` gives

\[
q_M
=
2Mp^{M/2}(\cosh u-1)>0
\tag{27}
\]

for `a!=1/2`. Thus the hidden prefix is not caused by an actually trivial quotient: the first possible visible coefficient is strictly nonzero.

### 4. Full frequency support can be restored without changing the collision

The logarithmic derivative of `B_p=H_{1/2,1}` has, by the AF-270 calculation,

\[
\frac{B_p'}{B_p}(s)
=
\lambda
+2\lambda\sum_{k\ge1}p^{k/2}p^{-ks}.
\tag{28}
\]

Every prime-power frequency on the `p`-ray is therefore present with a nonzero coefficient. Multiplying both controls by this same background adds `(28)` to both logarithmic derivatives and adds the same zero divisor to both functions. It cannot alter either the difference `(14)` or the equality of their ordinate-counting functions.

Hence the obstruction is not merely that the cyclotomic pair has sparse support. The sparse **difference** can be hidden inside two controls whose complete observed sources each have full prime-power support.

### 5. Relation to the AF-272 complexity certificate

AF-272 proves that a quotient with `R` distinct signed divisor nodes cannot have its first `R` source moments all vanish. Here `R=3M`, whereas `(9)` gives an exact vanishing window of length `M-1`. The family therefore does not contradict AF-272; it identifies how much of the generic quotient complexity survives after imposing the AF-270 reflection geometry.

Reflection symmetry organizes the divisor nodes into reciprocal radial blocks and reduces the effective pattern, but it does **not** make the necessary coefficient budget uniformly bounded. Increasing the cyclotomic orbit size `M` simultaneously increases the divisor complexity and pushes the first visible source defect to frequency `p^M`.

The resulting information boundary is sharper than either predecessor alone:

- AF-270: recurrence, reflection symmetry, exact ordinate counts, and prime-power provenance do not force criticality;
- AF-272: a finite coefficient prefix is complete once quotient divisor complexity is bounded;
- AF-273: the AF-270 symmetries themselves do not supply such a bound, because symmetric cyclotomic blocks realize arbitrarily long exact prefix collisions.

The next zeta-specific gate must therefore restrict the **admissible complexity/coupling of coefficient defects**, not merely their symmetry or frequency labels.

## Stress tests and failure modes

1. **No hidden change of period is being treated as equality of controls.** The `M`-block has period `L/M`, but both members of the matched pair use the same `M`. Their source difference is compared in the common ambient `p^{-s}` coordinate, where `(9)` is an exact coefficient statement.

2. **The zero-count statement is exact only by ordinate with multiplicity.** The real parts change, so disk counts need not agree pointwise. This is the same counting notion isolated in AF-270.

3. **The construction does not preserve the von-Mangoldt coefficient law.** It preserves an arbitrarily long finite prefix and the complete prime-power frequency alphabet after the common background `(12)` is added. Exact equality of all coefficients would fall back into the rigid regime discussed in AF-017--AF-019.

4. **No complexity-independent stability claim follows.** The result is an exact collision statement. AF-272's separated-node conditioning analysis remains the relevant quantitative layer once a complexity budget is supplied.

5. **This is a one-prime-ray obstruction.** It does not establish that a globally Euler-coupled, zeta-normalized control can realize the same block independently at arbitrary primes. That cross-prime coupling is precisely a possible stronger resource left open by the line mandate.

6. **The common full-support factor is not a hidden side channel.** It is identical in both controls and cancels from their quotient. Its only role is to show that the collision persists even when the complete observed sources are not sparse.

## Prior art and novelty assessment

The algebra behind the construction is classical. The factorization `(21)` and cancellation `(25)` are the elementary roots-of-unity filter / discrete-Fourier orthogonality mechanism. Reciprocal and self-inversive polynomial zero symmetries are also classical; F. F. Bonsall and Morris Marden, **“Zeros of Self-Inversive Polynomials,”** *Proceedings of the American Mathematical Society* 3(3), 471--475 (1952), DOI `10.2307/2031905`, is early primary literature for that symmetry class. No novelty is claimed for these ingredients.

The periodic divisor/source setting is already classical almost-periodic and exponential-polynomial mathematics, as audited in AF-270 through Jessen--Tornehave and Favorov. The finite-moment detection layer is classical Prony/Vandermonde mathematics, as audited in AF-272 through Kunis--Peter--Römer--von der Ohe and the Vandermonde-conditioning literature.

The Arithmetic Fidelity contribution is the **specific compatibility obstruction obtained by combining those two predecessor layers**: the exact Riemann-type reflection and count-matching geometry of AF-270 still admits cyclotomic quotient blocks whose logarithmic-derivative defect begins arbitrarily far down the same rational-prime-power ray. Thus symmetry does not secretly close the complexity loophole in AF-272.

## Consequence for the research frontier

A fixed number of right-half-plane source coefficients cannot certify critical-line fidelity merely because the candidate class has Riemann-type reflection symmetry, real conjugation, exact ordinate counts, Bohr periodicity, and the correct prime-power frequency alphabet. The missing assumption must constrain something that the family `(2)` is forced to violate.

Two concrete possibilities remain mathematically distinct:

- a **zeta-specific effective-complexity bound** on admissible quotient divisor/source defects; or
- a **cross-prime/cross-power coefficient law** strong enough that a high-order cyclotomic defect on one ray cannot be inserted without producing an earlier detectable inconsistency elsewhere.

Either route is now falsifiable: it must exclude the explicit family `(7)` for a reason stronger than reflection symmetry, recurrence, zero counting, or source support.