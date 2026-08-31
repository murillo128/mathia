# WP-066 — base-shell Hardy Gram recovers Mangoldt only through a nonnormalizable anchor

**Status:** `EXACT-DERIVED + SUBSTANTIVE-NEGATIVE + DECISIVE-BOUNDARY + CLASSICAL-MECHANISM`. The positive form and the obstruction below are exact consequences of the Prime-Circle Hardy operators of `PC-075`/`PC-080`. The functional-analytic mechanism — weighted Hilbert–Schmidt Gram geometry, completion of squares, trace-class convergence under finite-rank cutoffs, and loss of positivity after subtracting a divergent basepoint energy with nonzero first variation — is classical. No theorem-level historical novelty is claimed. The durable Mathia-specific content is that the **exact von Mangoldt coefficient already occurs as the boundary polarization of a genuine positive Hardy geometry**, but the canonical vector representing that polarization is the identity operator, which has infinite energy. Normalizing the anchor erases the arithmetic; subtracting its divergent self-energy retains `Lambda` but necessarily destroys the inherited sign theorem.

This narrows one of the singular/form-level escapes left open by `WP-064`–`WP-065`. It does **not** rule out another quotient, compression, closed form, or nonseparable finite–archimedean–polar geometry whose positive theorem is established before any subtraction. It rules out the most direct completion of the canonical base-shell Hardy Gram by its own identity/boundary anchor.

## 1. Exact input from the Prime-Circle Hardy shell algebra

Let

\[
H_{jk}=\frac1{j+k+1},\qquad j,k\ge0,
\tag{1}
\]

be the classical positive Hilbert matrix on `ell^2`, and let `Gamma_n` be the canonical Prime-Circle Hardy shell operators of `PC-075`:

\[
(\Gamma_n)_{jk}
=-\frac{c_n(j+k+1)}{j+k+1}.
\tag{2}
\]

The base-shell convention of `PC-080` is

\[
\boxed{\Gamma_1=-H.}
\tag{3}
\]

For every `n>1`, `PC-080` proves

\[
\Gamma_1\Gamma_n\in\mathcal S_1
\tag{4}
\]

and evaluates its trace as

\[
\operatorname{Tr}(\Gamma_1\Gamma_n)
=-\Lambda(n).
\tag{5}
\]

Combining (3) and (5) gives the exact identity

\[
\boxed{
\operatorname{Tr}(H\Gamma_n)=\Lambda(n),
\qquad n>1.
}
\tag{6}
\]

Thus the base Hilbert channel already contains the exact prime-power support and the exact von Mangoldt weight, with no zeta zeros, Euler-product differentiation, or hand-picked shell indicator inserted.

The question is whether (6) can be embedded into a positive Hardy geometry whose own positivity survives the passage to the global arithmetic functional.

## 2. The base-shell weighted Hardy form is genuinely positive

Let

\[
\mathfrak A_0
:=\operatorname{span}\{\Gamma_n:n>1\}
\tag{7}
\]

with finite sums only. Define

\[
\boxed{
\langle A,B\rangle_H
:=\operatorname{Tr}(A^*HB),
\qquad
Q_H(B):=\langle B,B\rangle_H.
}
\tag{8}
\]

This is well defined on `A_0`. Indeed, for every finite shell combination `B`, equation (4) gives

\[
HB\in\mathcal S_1,
\tag{9}
\]

and multiplication by the bounded operator `A^*` preserves trace class.

Moreover,

\[
\boxed{
Q_H(B)
=\operatorname{Tr}(B^*HB)
=\|H^{1/2}B\|_{\mathcal S_2}^2
\ge0.
}
\tag{10}
\]

The form is actually positive definite on operator vectors. The Hilbert matrix is injective: its moment representation

\[
\langle x,Hx\rangle
=\int_0^1
\left|\sum_{j\ge0}x_jt^j\right|^2dt
\tag{11}
\]

forces `x=0` when the quadratic form vanishes. Hence `H^{1/2}` is injective, and

\[
Q_H(B)=0
\Longrightarrow
H^{1/2}B=0
\Longrightarrow
B=0.
\tag{12}
\]

Therefore the shell kernel

\[
\boxed{
K_H(m,n)
:=\operatorname{Tr}(\Gamma_mH\Gamma_n)
}
\tag{13}
\]

is a bona fide positive Gram kernel on every finite set of shell labels `m,n>1`.

This is not the `q=2` positive shell of `WP-061`. Here the positive metric is the **base Hardy Hilbert channel** `H=-Gamma_1`; its significance is that the same base channel also has the exact first-order arithmetic polarization (6).

## 3. Von Mangoldt is exactly the identity-anchor polarization

Define the linear functional

\[
L(B):=\operatorname{Tr}(HB),
\qquad B\in\mathfrak A_0.
\tag{14}
\]

For

\[
B=\sum_{n>1}b_n\Gamma_n,
\]

equation (6) gives

\[
\boxed{
L(B)=\sum_{n>1}b_n\Lambda(n).
}
\tag{15}
\]

Formally, (14) is the `H`-Gram pairing with the identity operator:

\[
\boxed{
L(B)=\langle I,B\rangle_H.
}
\tag{16}
\]

This is the tempting bridge. One has found a positive Mathia-native Hardy geometry `Q_H`, and its polarization against the most canonical possible anchor — the identity on Hardy space — is precisely the von Mangoldt selector.

But the word *formally* in (16) is essential: `I` is not a finite-energy vector of this geometry.

## 4. The canonical identity anchor has logarithmically infinite energy

If the identity were an `H`-Gram vector, its squared norm would be

\[
\|I\|_H^2
=\operatorname{Tr}(H).
\tag{17}
\]

Since

\[
H_{jj}=\frac1{2j+1},
\]

one has

\[
\boxed{
\operatorname{Tr}(H)
=\sum_{j\ge0}\frac1{2j+1}
=+\infty.
}
\tag{18}
\]

So the exact arithmetic functional (15) is obtained from a **nonnormalizable boundary anchor**, not from an ordinary vector in the positive Hilbert geometry.

The natural monomial cutoffs make the divergence explicit. Let

\[
P_N:=\sum_{j=0}^{N-1}|e_j\rangle\langle e_j|.
\tag{19}
\]

Then

\[
E_N
:=Q_H(P_N)
=\operatorname{Tr}(P_NHP_N)
=\sum_{j=0}^{N-1}\frac1{2j+1}.
\tag{20}
\]

Using harmonic numbers,

\[
E_N
=H_{2N}-\frac12H_N,
\]

and therefore

\[
\boxed{
E_N
=\frac12\log N+\log2+\frac\gamma2+O(N^{-2}).
}
\tag{21}
\]

The divergence is not a numerical artifact. Equation (18) says invariantly that the positive operator `H` is not trace class, so `I` cannot have finite `H`-energy.

## 5. The unnormalized cutoffs retain `Lambda`, while normalized cutoffs erase it

Despite the divergent self-energy, the cutoffs recover the exact boundary polarization. For fixed `B in A_0`, `HB` is trace class by (9). Since `P_N -> I` strongly and the cutoffs are uniformly bounded,

\[
P_NHB\longrightarrow HB
\qquad\text{in }\mathcal S_1.
\tag{22}
\]

Hence

\[
\boxed{
\operatorname{Tr}(P_NHB)
\longrightarrow
\operatorname{Tr}(HB)
=L(B).
}
\tag{23}
\]

Thus the arithmetic is genuinely present as a boundary limit of the positive geometry.

However, make the anchor into a unit vector by putting

\[
a_N:=\frac{P_N}{\sqrt{E_N}}.
\tag{24}
\]

Then

\[
Q_H(a_N)=1,
\tag{25}
\]

but for every fixed shell combination

\[
\boxed{
\langle a_N,B\rangle_H
=\frac{\operatorname{Tr}(P_NHB)}{\sqrt{E_N}}
\longrightarrow0.
}
\tag{26}
\]

because the numerator has the finite limit (23) while `E_N -> infinity`.

Therefore the most conservative positive repair — normalize the boundary anchor rather than subtract anything — kills the entire von Mangoldt polarization.

## 6. Completing the square gives a positive energy with divergent self-energy

For every `N` and every `B in A_0`, consider the exact positive square

\[
\boxed{
\mathcal E_N(B)
:=Q_H(P_N-B)
=\operatorname{Tr}\bigl((P_N-B)^*H(P_N-B)\bigr)
\ge0.
}
\tag{27}
\]

Expanding gives

\[
\boxed{
\mathcal E_N(B)
=E_N
-2\operatorname{Re}\operatorname{Tr}(P_NHB)
+Q_H(B).
}
\tag{28}
\]

Using (23), the entire arithmetic dependence has a finite limit:

\[
\mathcal E_N(B)
=E_N
-2\operatorname{Re}L(B)
+Q_H(B)
+o(1).
\tag{29}
\]

This is an unusually clean local-to-boundary decomposition:

```text
positive Hardy square
    = divergent universal base-anchor self-energy
      - 2 * exact von Mangoldt polarization
      + positive shell Gram energy
      + o(1).
```

So the failure is not that the positive geometry cannot see `Lambda`. It sees `Lambda` **exactly**. The issue is whether the divergent first term can be removed without losing the positivity theorem that produced the square.

## 7. Subtracting the canonical self-energy retains `Lambda` but necessarily loses positivity

The canonical finite-part subtraction is forced if one wants to retain a finite nontrivial limit while preserving the exact cross term:

\[
\widetilde{\mathcal E}_N(B)
:=\mathcal E_N(B)-E_N.
\tag{30}
\]

Then

\[
\boxed{
\widetilde{\mathcal E}_N(B)
\longrightarrow
\mathcal R(B)
:=Q_H(B)-2\operatorname{Re}L(B).
}
\tag{31}
\]

But `R` cannot be nonnegative. The obstruction is elementary and exact: a quadratic form with a nonzero linear first variation cannot have a minimum at the origin.

Choose any prime power `m=p^k` and put

\[
q_m:=Q_H(\Gamma_m)>0.
\tag{32}
\]

For real `t`, equations (15) and (31) give

\[
\boxed{
\mathcal R(t\Gamma_m)
=t^2q_m-2t\log p.
}
\tag{33}
\]

For every sufficiently small positive `t`, the linear term dominates and

\[
\mathcal R(t\Gamma_m)<0.
\tag{34}
\]

Indeed the exact minimum is attained at

\[
t=\frac{\log p}{q_m}
\]

and equals

\[
\boxed{
\min_t\mathcal R(t\Gamma_m)
=-\frac{(\log p)^2}{q_m}<0.
}
\tag{35}
\]

Thus the positivity of the parent square (27) is carried partly by the divergent anchor self-energy. Once that self-energy is removed to expose the arithmetic finite part, **the inherited sign theorem is gone**.

The opposite sign convention `Q_H(P_N+B)` does not help: its finite part is `Q_H(B)+2 Re L(B)` and is negative for sufficiently small `t` of the opposite sign. The obstruction is the nonzero first variation itself, not a convention.

## 8. The direct positive-boundary trilemma

Equations (21), (26), and (31)–(35) give a sharp trilemma for this Mathia-native route.

1. **Keep the positive square without subtraction.** Then `E_N(B) -> +infinity` for every fixed `B`; there is no finite global form.
2. **Normalize the positive anchor/self-energy.** Dividing by `E_N`, or equivalently using the unit anchors (24), makes the exact arithmetic polarization vanish by (26).
3. **Subtract the divergent anchor self-energy.** Then the von Mangoldt term survives exactly, but the finite part is already negative on every prime-power shell by (33)–(35).

This is the Hardy/operator analogue of the radial self-energy tradeoff in `WP-047`, but it is not a restatement of that result. `WP-047` concerned Schur complements of positive radial Dirichlet Gram blocks and attenuation of the Prime-Circle birth form. Here the parent geometry is the **Hardy shell algebra itself**, the arithmetic functional is the exact `PC-080` mixed trace, and the divergent object is the identity anchor in the base-shell `H` metric.

The result also complements `WP-061`–`WP-065`. Those findings show that making the selected full-root `q=2` channel positive by bounded or unbounded self-adjoint metric multiplication forces its polar sign. The present obstruction addresses a different surviving possibility: perhaps one could avoid repairing the indefinite `q=2` operator and instead derive arithmetic as the boundary polarization of an already-positive Hardy Gram. The answer is that the direct base-shell realization does this only through an infinite-energy anchor.

## 9. Why this is not yet a global Weil form

Nothing above inserts zeta zeros or assumes RH. The finite arithmetic coefficient is exact, and the parent Gram positivity is independent. That makes the route more serious than a formal repackaging of the explicit formula.

Nevertheless it does **not** satisfy the branch mandate:

- `Q_H` by itself contains no Riemann Gamma contribution or polar counterterm;
- the exact Mangoldt functional occurs as a boundary **linear polarization**, not yet as the completed Weil quadratic form on test functions;
- the canonical boundary anchor has infinite energy;
- the finite-part operation needed to retain the arithmetic term destroys the inherited nonnegativity before any archimedean completion is attempted.

Therefore adding the known Gamma/polar terms after equation (31) would not count as an independent geometric positivity theorem. A successful continuation must supply new coupled geometry whose sign survives the finite–archimedean–polar assembly rather than repairing the signed finite part after this subtraction.

The finding deliberately does not claim that `L` has no representing vector in every conceivable quotient or completion of the shell span. Nonnormalizability of the canonical identity anchor alone would not prove that stronger statement. Nor does it rule out a closed form defined on a different core, a quotient/compression selected by extra Mathia geometry, or a nonseparable block in which the archimedean sector participates **before** the divergent self-energy is eliminated.

## 10. Matched control and novelty audit

The sign mechanism is universal. Let `H>=0` be any bounded injective non-trace-class operator and let `B_i` be bounded operators with `HB_i in S_1`. Then

\[
Q_H(B)=\operatorname{Tr}(B^*HB)
\]

is positive on finite combinations, while any approximate identity `P_N` with `Tr(P_NHP_N)->infinity` has the same completion-square decomposition

\[
Q_H(P_N-B)
=Q_H(P_N)-2Re\operatorname{Tr}(P_NHB)+Q_H(B).
\]

Whenever the boundary linear functional has a nonzero limit, subtracting the basepoint self-energy leaves a finite part with nonzero first variation and therefore cannot remain nonnegative at the origin.

So there is no general operator-theoretic novelty in the sign obstruction. The classical Hilbert matrix is a bounded positive injective operator with continuous spectral behavior; the surrounding Hilbert/Hankel theory is already audited in `PC-075` and `PC-080`. A directed literature check found only this standard operator-theoretic neighborhood, not a reason to claim a new abstract theorem.

The Mathia-specific content is the exact arithmetic specialization

\[
\boxed{
\operatorname{Tr}(H\Gamma_n)=\Lambda(n),
}
\]

which turns the generic divergent-anchor phenomenon into a precise boundary statement about the same Prime-Circle Hardy geometry currently under investigation.

## 11. Falsification surface

The finding has a short exact audit surface.

1. Verify the `PC-080` base convention `Gamma_1=-H` and trace identity `Tr(Gamma_1 Gamma_n)=-Lambda(n)` for `n>1`.
2. Deduce `Tr(H Gamma_n)=Lambda(n)` and `H Gamma_n in S_1`.
3. For finite shell combinations, verify `Q_H(B)=Tr(B* H B)=||H^(1/2)B||_2^2 >=0` and use injectivity of `H` to obtain strict positivity for nonzero `B`.
4. Check `Tr(H)=sum_j (2j+1)^(-1)=infinity` and the exact cutoff asymptotic (21).
5. Use trace-class convergence under `P_N -> I` strongly to verify (23).
6. Expand the positive square (27) and obtain (28).
7. Subtract `E_N`, take the limit, and test `B=t Gamma_{p^k}` to obtain the negative value (35).
8. Normalize by `sqrt(E_N)` and verify that every fixed arithmetic polarization tends to zero as in (26).

Failure of items 1–3 invalidates the claimed Mathia-positive geometry. Failure of 4–5 invalidates the boundary-anchor obstruction. If all eight checks hold, the direct identity-anchor completion has no route that simultaneously retains a finite nonzero Mangoldt polarization and inherits the positivity of the parent Hardy square.

## Research consequence

Prime Circle contains a stronger finite positivity/arithmetic bridge than the previous no-go language might suggest:

\[
\boxed{
\text{positive base-shell Hardy Gram}
\quad+\quad
\text{identity boundary polarization}
\quad\Longrightarrow\quad
\Lambda(n)\ \text{exactly}.
}
\]

But the identity is an infinite-energy vector for that same geometry. The canonical boundary limit therefore obeys

\[
\boxed{
\text{retain positivity} \Rightarrow \text{arithmetic vanishes after normalization},
\qquad
\text{retain arithmetic} \Rightarrow \text{self-energy subtraction loses positivity}.
}
\]

The viable search space should now move away from **single-anchor renormalization of an already-positive Hardy Gram**. A successful Weil mechanism must instead make the finite Hardy data, the independently selected `q=2` archimedean channel, and the polar/global sector interact before the final sign theorem — through a genuinely coupled quotient, compression, boundary/cohomological construction, or another geometry whose positivity is not the finite part of a divergent completed square.