# MC-190 — Unit-group equivariant quadratic statistics cannot couple the rough zero mode to transverse characters

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `FRONTIER-REFINEMENT`, `CLASSICAL-MECHANISM`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

`MC-188` shows that strong arithmetic-progression dispersion for the logarithmically rough Möbius block controls the nonprincipal residue/character directions while leaving the principal character coefficient—the rough global sum—uncontrolled at fixed-power scale. `MC-189` shows the same separation in the proved function-field analogue: the principal Möbius mode is annihilated independently, while Frobenius equidistribution controls only the transverse character family.

There is a simple representation-theoretic reason that this separation cannot be repaired merely by replacing the existing residue-class variance with another **multiplicatively translation-invariant linear or Hermitian quadratic statistic on the same residue-class vector**.

Fix a modulus `q` and put

\[
G=(\mathbb Z/q\mathbb Z)^\times,
\qquad \phi=|G|=\varphi(q).
\tag{1}
\]

Equip `L^2(G)` with normalized inner product

\[
\langle F,H\rangle
=\frac1\phi\sum_{a\in G}F(a)\overline{H(a)}.
\tag{2}
\]

For `b\in G`, let multiplicative translation act by

\[
(\tau_bF)(a)=F(b^{-1}a).
\tag{3}
\]

The Dirichlet characters modulo `q`, restricted to `G`, are the complete character group `\widehat G` and form an orthonormal basis of `L^2(G)`. If a linear operator

\[
T:L^2(G)\to L^2(G)
\tag{4}
\]

commutes with every `\tau_b`, then every character is an eigenvector:

\[
\boxed{T\chi=m(\chi)\chi\qquad(\chi\in\widehat G).}
\tag{5}
\]

Consequently every translation-invariant Hermitian quadratic form

\[
Q(F)=\langle TF,F\rangle,
\qquad T=T^*,
\tag{6}
\]

has the exact character decomposition

\[
\boxed{Q(F)=\sum_{\chi\in\widehat G}m(\chi)|\widehat F(\chi)|^2,}
\qquad m(\chi)\in\mathbb R,
\tag{7}
\]

with **no cross terms between the principal character and any nonprincipal character**. If `Q` is positive semidefinite then `m(\chi)\ge0` for every `\chi`.

Apply this to the rough Möbius residue vector at the primorial modulus from `MC-188`,

\[
q_y=\prod_{p\le y}p,
\qquad
A_X(a)=\sum_{\substack{n\le X\\n\equiv a\pmod{q_y}}}\mu(n),
\qquad a\in G.
\tag{8}
\]

Because reduced residue classes modulo `q_y` are exactly the integers with no prime divisor at most `y`,

\[
\sum_{a\in G}A_X(a)=G_y(X),
\tag{9}
\]

where `G_y` is the rough Möbius summatory function of `MC-180`--`MC-188`. Thus, for the principal character `1`,

\[
\boxed{\widehat A_X(1)=\frac{G_y(X)}{\phi}.}
\tag{10}
\]

Equations `(7)`--`(10)` give a sharp dichotomy for this entire statistic class:

- if `m(1)=0`, then `Q` is completely blind to the rough zero mode; indeed `Q(A_X+c\,1)=Q(A_X)` for every complex constant `c`;
- if `m(1)>0` and `Q\ge0`, a bound for `Q(A_X)` controls `G_y(X)` only because the principal coefficient is **directly present** through the term `m(1)|G_y(X)|^2/\phi^2`, not because transverse modes force it;
- no translation-invariant Hermitian quadratic form can contain a principal/nonprincipal interference term such as `\widehat A_X(1)\overline{\widehat A_X(\chi)}` with `\chi\ne1`.

Therefore the missing fixed-power bridge after `MC-188` cannot be obtained by choosing a cleverer invariant covariance matrix, convolution kernel, character weight, positive quadratic energy, or other equivariant linear/quadratic post-processing of the **same single-modulus residue vector** while continuing to project out the principal mode. A genuine coupling must add structure outside this class: for example a non-equivariant arithmetic weight tied to the ordered interval boundary, a relation across changing moduli or scales, a nonlinear arithmetic identity, or an independently controlled principal-mode term.

This does not prove that such a coupling cannot exist. It proves something narrower and reusable: **within the natural unit-group-equivariant linear/Hermitian-quadratic category, “couple the principal mode to the transverse modes” is impossible as an off-diagonal mechanism because symmetry diagonalizes the category before any Möbius-specific estimate is used.**

## 1. Equivariance forces character diagonalization

For each character `\chi\in\widehat G`, `(3)` gives

\[
\tau_b\chi
=\overline{\chi(b)}\,\chi.
\tag{11}
\]

If `T\tau_b=\tau_bT` for every `b`, then

\[
\tau_b(T\chi)
=T(\tau_b\chi)
=\overline{\chi(b)}\,T\chi.
\tag{12}
\]

So `T\chi` lies in the simultaneous eigenspace on which every translation `\tau_b` acts by `\overline{\chi(b)}`. For a finite abelian group that joint eigenspace is one-dimensional and is spanned by `\chi`. This proves `(5)` without any analytic input.

Writing

\[
F=\sum_{\chi\in\widehat G}\widehat F(\chi)\chi,
\qquad
\widehat F(\chi)=\langle F,\chi\rangle,
\tag{13}
\]

and using orthonormality gives `(7)`. Self-adjointness forces the multipliers `m(\chi)` to be real, and positive semidefiniteness forces them to be nonnegative by evaluating `Q` on a single character.

Equivalently, such operators are convolution/Fourier-multiplier operators on the finite abelian group. The diagonalization itself is classical finite-group harmonic analysis, not a new theorem.

## 2. Exact invisibility when the principal multiplier vanishes

Let `1` denote the constant principal character. Since all nonprincipal characters have zero group average,

\[
\widehat{F+c\,1}(\chi)
=
\widehat F(\chi)
\qquad(\chi\ne1),
\tag{14}
\]

while

\[
\widehat{F+c\,1}(1)=\widehat F(1)+c.
\tag{15}
\]

If `m(1)=0`, equation `(7)` therefore gives

\[
\boxed{Q(F+c\,1)=Q(F)\quad\text{for all }c.}
\tag{16}
\]

This is stronger than saying that a particular inequality happens to lose the mean. The statistic factors through the quotient of `L^2(G)` by the constant direction, so arbitrarily different principal coefficients have exactly the same value of every such quadratic energy whose principal multiplier is zero.

For the arithmetic vector `(8)`, adding an arbitrary constant vector need not produce another realizable Möbius residue vector. Thus `(16)` is an **information/architecture obstruction**, not an arithmetic counterexample showing that actual Möbius data can realize arbitrary zero modes. A theorem exploiting extra arithmetic constraints on the realizable vectors could still control the principal coefficient. What `(16)` rules out is obtaining that control from the invariant quadratic statistic itself.

## 3. `MC-188` is exactly the projection dichotomy

The smooth-modulus theorem specialized in `MC-188` subtracts the best-pretending character profile. In the present normalization, if `P_{\chi_1}` is orthogonal projection onto the one-dimensional character space `\mathbb C\chi_1`, its residual energy is

\[
\|(I-P_{\chi_1})A_X\|_2^2
=
\sum_{\chi\ne\chi_1}|\widehat A_X(\chi)|^2.
\tag{17}
\]

This is a translation-invariant positive quadratic form with multiplier `0` at `\chi_1` and `1` elsewhere.

If `\chi_1=1`, `(17)` has `m(1)=0`. Equation `(16)` explains structurally why the theorem can be arbitrarily strong on the residual class vector while saying nothing about `G_y(X)`.

If `\chi_1\ne1`, then the principal coefficient is retained with multiplier `1`, so

\[
\|(I-P_{\chi_1})A_X\|_2^2
\ge
|\widehat A_X(1)|^2
=
\frac{|G_y(X)|^2}{\phi^2}.
\tag{18}
\]

Multiplying by the normalization factor `\phi` recovers the Cauchy--Schwarz transfer in `MC-188`. Thus the two branches found there are not peculiar to that theorem: they are the two possible placements of the principal character inside a diagonal invariant quadratic energy.

This also clarifies why strengthening only the nonprincipal character estimates does not change the principal branch. Once the principal multiplier is zero, no improvement of `m(\chi)|\widehat A_X(\chi)|^2` for `\chi\ne1` can manufacture a cross term that symmetry forbids.

## 4. The function-field comparison has the same representation shape

`MC-189` records that the Keating--Rudnick short-interval variance over `\mathbb F_q[t]` is expressed through nontrivial even characters after the global degree-shell Möbius mean has already vanished exactly. The transverse variance is again a character-diagonal quadratic quantity with the trivial direction absent.

The present result explains the structural commonality without claiming the integer and function-field arithmetic objects are identical. In both settings, character orthogonality decomposes the quadratic energy into symmetry sectors. The difference is upstream: in the genus-zero function-field model the principal Möbius coefficient is annihilated by `1/Z_q(u)=1-qu`, whereas for the integer rough block the principal coefficient remains the unsolved `G_y` term.

So the useful lesson from the proved analogue is not that better transverse equidistribution should eventually leak into the mean. In an invariant quadratic framework there is no such leakage. The analogue succeeds because the missing symmetry sector is solved separately.

## 5. What kinds of continuation remain outside the no-go

The theorem deliberately does **not** rule out mechanisms that add a second structure not diagonalized by the same unit-group action. Several mathematically distinct escape classes remain open:

1. **Boundary-sensitive operators.** The integer order and the cutoff `n\le X` distinguish residue classes through where their representatives meet the interval boundary. A useful operator may therefore fail to commute with multiplicative translations on `G` in a source-forced way.
2. **Cross-scale or cross-modulus relations.** A family of vectors for nested primorials carries restriction/lifting information absent from one fixed `L^2(G)`. Such a mechanism must be audited explicitly; merely summing diagonal energies over scales remains diagonal at each scale and does not suffice.
3. **Nonlinear arithmetic identities.** Higher-degree observables can contain products of several Fourier coefficients consistent with character multiplication. The present quadratic theorem says nothing about whether Möbius multiplicativity forces a useful nonlinear constraint.
4. **Independent principal input.** A statistic may retain the principal coefficient with positive weight and prove a fixed-power bound for the whole energy by a genuinely new arithmetic theorem. In that case the zero mode is controlled honestly rather than inferred from transverse dispersion.

These are escape categories, not evidence that any one works. The decisive requirement remains the `MC-185` fixed-power zero-mode budget.

## 6. Prior art and novelty audit

The diagonalization in `(5)`--`(7)` is standard Fourier analysis on finite abelian groups. A targeted prior-art search located it in the classical framework represented by Audrey Terras, *Fourier Analysis on Finite Groups and Applications*, Cambridge University Press, London Mathematical Society Student Texts 43 (1999), especially Part I on finite abelian groups and the DFT on finite abelian groups (book DOI `10.1017/CBO9780511626265`). No novelty is claimed for simultaneous diagonalization of translations, convolution operators, character orthogonality, or Fourier multipliers.

The arithmetic residue-class setting is the one already established in `MC-188` from Klurman--Mangerel--Teräväinen (`MC-S45`). The present contribution is the **frontier specialization**: identifying the exact symmetry class of post-processings for which the desired principal/transverse coupling is structurally impossible, and showing that the principal/nonprincipal dichotomy of `MC-188` is precisely the multiplier `m(1)=0` versus `m(1)>0` dichotomy.

A targeted search for finite-abelian translation-invariant operators and character diagonalization found the standard harmonic-analysis theorem but no basis for presenting `(5)`--`(7)` as new mathematics. The useful new repository content is therefore the no-go classification relative to the current rough-Möbius frontier, not the underlying representation theorem.

## 7. Boundaries and falsification tests

- The result concerns one fixed finite unit group and linear operators/Hermitian quadratic forms invariant under its full multiplicative translation action. It is not a no-go for arbitrary arithmetic statistics.
- A nonlinear invariant may combine principal and transverse Fourier magnitudes in the same scalar observable. Such a construction is outside `(6)`--`(7)` and would need an independent arithmetic inequality; no claim is made that invariance alone forbids every nonlinear coupling.
- A non-equivariant operator can have principal/nonprincipal cross terms. The point is that its symmetry breaking must then be mathematically justified by source data such as interval order, boundaries, scale change, or multiplicative structure; an arbitrary coordinate choice would not explain Möbius cancellation.
- The constant-shift witness `(16)` lives in the ambient residue-vector space. It does not assert that all shifted vectors are realizable by Möbius sums. Therefore this finding does not rule out a theorem using additional constraints peculiar to the actual arithmetic orbit.
- If a proposed statistic is only approximately equivariant, the size of its commutator with translations becomes part of the problem. A small symmetry-breaking defect could in principle mediate coupling, but the gain must be quantified at the fixed-power scale rather than assumed.
- The modulus `q_y` varies with `X`, but the diagonalization is exact separately for every `q_y`; variation of the modulus helps only if relations between different groups add information absent at a single scale.

The finding is falsified as an application to a proposed route if that route exhibits a source-forced principal/nonprincipal coupling while still commuting with every multiplicative translation on the same residue-class space and remaining Hermitian quadratic. Equations `(11)`--`(13)` show that this cannot occur.

## Consequence for the live frontier

After `MC-188` and `MC-189`, the instruction "couple the principal rough mode to the transverse characters" was still broad enough to invite another invariant covariance or weighted character-energy construction. That subfamily can now be removed from the search.

The next useful candidate must **break the single-modulus character diagonalization in a controlled arithmetic way** or pay for the principal coefficient directly. In particular, more powerful covariance estimation, better nonprincipal large-sieve/dispersion bounds, or alternative translation-invariant kernels cannot by themselves cross the fixed-power zero-mode boundary while the principal character remains projected out.