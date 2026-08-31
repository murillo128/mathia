# PC-079 — Hardy refinement is commuting Möbius–Hilbert dilation

**Status:** `EXACT-DERIVED` + `CLASSICAL-IDENTITY` + `DECISIVE-NEGATIVE` for ordered-prime/refinement-holonomy mechanisms inside the cyclotomic Hardy/Hankel branch of PC-075. The Ramanujan/Möbius identities are classical; the durable Prime-Circle contribution is the exact operator-level organization and its research consequence. No theorem-level historical novelty is claimed.

PC-075 introduced the canonical Hardy interior/exterior coupling

\[
(\Gamma_n)_{jk}=-\frac{c_n(j+k+1)}{j+k+1},
\qquad j,k\ge0,
\]

and PC-078 showed that adjoining an already-present prime produces only signed tensor inflation. The complementary question is whether **new-prime insertion** can create ordered refinement dynamics, noncommuting prime steps, or a cross-level holonomy even though each single shell remains a Ramanujan/Hilbert operator.

It cannot. There is a canonical commuting semigroup of Hankel coefficient dilations `\mathfrak D_d` such that every primitive-shell operator is exactly a finite Möbius difference of dilated copies of the single Hilbert operator `\Gamma_1=-H`:

\[
\boxed{
\Gamma_n
=\sum_{d\mid n}\mu(n/d)\,\mathfrak D_d\Gamma_1.
}
\]

Equivalently, writing `\rho=\operatorname{rad}(n)`,

\[
\boxed{
\Gamma_n
=\mathfrak D_{n/\rho}
\prod_{p\mid\rho}(\mathfrak D_p-I)\Gamma_1.
}
\]

Thus repeated primes act by pure dilation, distinct new primes act by commuting first differences, and the order in which prime factors are introduced is exactly forgotten. Moreover, summing all primitive birth operators over the divisor lattice reconstructs one universal full-root Hilbert dilation:

\[
\boxed{
\sum_{d\mid n}\Gamma_d
=\mathfrak D_n\Gamma_1
\cong J_n\otimes\Gamma_1.
}
\]

This rules out refinement-order curvature/holonomy and naive cumulative-birth spectralization in this linear Hardy branch. It does **not** classify the spectral interference inside a fixed squarefree mixed-prime endpoint `\Gamma_\rho` or the higher relative spectral data left open by PC-077/PC-078.

## 1. Canonical Hankel coefficient dilation

Let

\[
A=(a_{j+k+1})_{j,k\ge0}
\]

be a Hankel matrix/operator determined by a sequence `(a_m)_{m\ge1}`. For every integer `d\ge1`, define the coefficient-dilation superoperator

\[
\boxed{
(\mathfrak D_d A)_{jk}
=
\mathbf 1_{d\mid j+k+1}\,
 a_{(j+k+1)/d}.
}
\]

This operation is forced by the root-of-unity refinement arithmetic: it keeps exactly those anti-diagonals whose Fourier index is divisible by `d` and then identifies the surviving index with the coarse one.

The dilations compose exactly:

\[
\boxed{
\mathfrak D_d\mathfrak D_e
=\mathfrak D_{de}
=\mathfrak D_e\mathfrak D_d.
}
\]

Indeed, at anti-diagonal index `m=j+k+1`, both sides vanish unless `de\mid m`, and in that case both read the original coefficient `a_{m/(de)}`. Hence the **refinement maps themselves form a commutative multiplicative semigroup**.

This statement concerns the superoperators `\mathfrak D_d`. It does not assert that the resulting embedded operators `\mathfrak D_dA` and `\mathfrak D_eA` commute under operator multiplication.

## 2. Every dilation is finite signed tensor inflation

Split the Hardy index modulo `d` by the unitary

\[
W_d:\ell^2(\mathbb Z_{\ge0})
\longrightarrow
\bigoplus_{r=0}^{d-1}\ell^2(\mathbb Z_{\ge0}),
\qquad
(W_dx)_r(a)=x_{da+r}.
\]

Write `j=da+r` and `k=db+s`, with `0\le r,s<d`. Then

\[
j+k+1=d(a+b)+(r+s+1).
\]

Since `1\le r+s+1\le2d-1`, divisibility by `d` is equivalent to

\[
r+s=d-1.
\]

On that anti-diagonal residue pair,

\[
\frac{j+k+1}{d}=a+b+1.
\]

Let `J_d` be the `d\times d` reversal matrix,

\[
(J_d)_{rs}=\mathbf1_{r+s=d-1}.
\]

Then exactly

\[
\boxed{
W_d\mathfrak D_d(A)W_d^*
=J_d\otimes A.
}
\]

Thus coefficient dilation introduces no new infinite-dimensional spectral core: it is a finite involutive channel inflation of the original Hankel operator. In particular `\|\mathfrak D_d(A)\|=\|A\|` whenever `A` is bounded, and Schatten multiplicities scale by the finite tensor factor whenever those norms are defined.

For the base cyclotomic shell `n=1`, `c_1(m)=1`, so

\[
\boxed{
\Gamma_1=-H,
\qquad
H_{jk}=\frac1{j+k+1},
}
\]

the classical Hilbert matrix of PC-075.

## 3. Primitive-shell extraction is Möbius differencing of Hilbert dilations

The classical divisor formula for Ramanujan sums is

\[
\boxed{
c_n(m)=\sum_{d\mid(n,m)}d\,\mu(n/d).}
\]

For `\Gamma_1=-H`, the coefficient at anti-diagonal index `m` after dilation is

\[
(\mathfrak D_d\Gamma_1)[m]
=-\mathbf1_{d\mid m}\frac{d}{m}.
\]

Therefore

\[
\begin{aligned}
\left[
\sum_{d\mid n}\mu(n/d)\mathfrak D_d\Gamma_1
\right][m]
&=-\frac1m
\sum_{\substack{d\mid n\\d\mid m}}
d\,\mu(n/d)\\
&=-\frac{c_n(m)}m.
\end{aligned}
\]

Hence, coefficient by coefficient,

\[
\boxed{
\Gamma_n
=\sum_{d\mid n}\mu(n/d)\mathfrak D_d\Gamma_1.
}
\]

This is the Hardy/Hankel image of the field-level cyclotomic Möbius decomposition in PC-027. The point here is not a new Ramanujan identity; it is that the entire **cross-level operator family** factors through one universal Hilbert operator and one explicit commutative dilation semigroup.

For squarefree `\rho`, multiplicativity of Möbius inversion gives

\[
\boxed{
\Gamma_\rho
=\prod_{p\mid\rho}(\mathfrak D_p-I)\Gamma_1.
}
\]

If `n=\rho m` with `\rho=\operatorname{rad}(n)`, every extra prime power is a repeated-prime dilation, so

\[
\boxed{
\Gamma_n
=\mathfrak D_m
\prod_{p\mid\rho}(\mathfrak D_p-I)\Gamma_1.
}
\]

## 4. New-prime and repeated-prime refinement laws

The factorization yields two exact prime-step rules.

If `p\nmid n`, then

\[
\boxed{
\Gamma_{pn}
=(\mathfrak D_p-I)\Gamma_n.
}
\]

If `p\mid n`, then

\[
\boxed{
\Gamma_{pn}
=\mathfrak D_p\Gamma_n.
}
\]

The second identity is precisely the operator form behind PC-078: after residue splitting modulo `p`,

\[
\Gamma_{pn}\cong J_p\otimes\Gamma_n.
\]

The first identity supplies the missing new-prime rule. If `p` and `q` are distinct primes not dividing `n`, then

\[
\begin{aligned}
\Gamma_{pqn}
&=(\mathfrak D_p-I)(\mathfrak D_q-I)\Gamma_n\\
&=(\mathfrak D_q-I)(\mathfrak D_p-I)\Gamma_n.
\end{aligned}
\]

Therefore two prime-refinement paths with the same endpoint give **exactly the same Hardy operator**. There is no commutator, curvature, ordered-prime memory, or refinement holonomy generated by the canonical linear birth operation in this branch.

This is structurally parallel to the path-independence no-go results PC-039 and PC-049, but the mechanism is different: here flatness is already present in the Ramanujan/Hankel coefficient-dilation algebra, before any Schur reduction or cotangent fiber averaging is performed.

## 5. Summing all birth shells collapses to one universal full-root Hilbert dilation

The divisor-lattice sum is even more rigid. Using the Möbius factorization,

\[
\begin{aligned}
\sum_{d\mid n}\Gamma_d
&=\sum_{d\mid n}\sum_{e\mid d}
\mu(d/e)\mathfrak D_e\Gamma_1\\
&=\sum_{e\mid n}
\mathfrak D_e\Gamma_1
\sum_{q\mid n/e}\mu(q).
\end{aligned}
\]

The inner Möbius sum vanishes unless `e=n`. Hence

\[
\boxed{
\sum_{d\mid n}\Gamma_d
=\mathfrak D_n\Gamma_1.
}
\]

Equivalently, this is the operator form of the classical full-root identity

\[
\sum_{d\mid n}c_d(m)=n\mathbf1_{n\mid m}.
\]

After residue splitting,

\[
\boxed{
W_n\left(\sum_{d\mid n}\Gamma_d\right)W_n^*
=J_n\otimes\Gamma_1
=-J_n\otimes H.
}
\]

For every `n>1`, `J_n` has both signs, so the spectral set of this cumulative full-root Hardy operator is simply the universal Hilbert band `[-\pi,\pi]`, with only finite reversal-channel multiplicities depending on `n`. Thus the route

\[
\boxed{
\text{sum all primitive birth operators up to a divisor endpoint}
\to
\text{Hardy/Hankel spectrum}
\to
\text{new RH mechanism}
}
\]

collapses exactly to classical Hilbert data.

## 6. Prior-art and novelty audit

The ingredients surrounding the factorization are classical and already anchored in `research/prime_circle/SOURCES.md`.

1. Ramanujan's divisor formula and Möbius inversion supply the coefficient identity. PC-027 already shows at field level that primitive cyclotomic logarithms are a unimodular Möbius re-basing of the complete-root fields.
2. Magnus and Rosenblum supply the classical Hilbert-matrix spectral theory used in PC-075. PC-075 already identifies universal Hilbert channels in each single-shell cyclotomic Hankel operator.
3. PC-078 proves the repeated-prime tensor-inflation specialization. The present derivation extends the organization to arbitrary conductors by adding the exact new-prime difference rule.
4. PC-010 is the relevant novelty warning for abstract refinement: roots of unity plus power maps already form the Bost–Connes cyclotomic tower. The commuting `\mathfrak D_d` semigroup should therefore be read as a concrete Hardy/Hankel representation of classical cyclotomic refinement, not as a newly discovered Hecke or noncommutative dynamical system.

Directed searches for Ramanujan-sum Hankel operators, Hilbert-matrix coefficient dilations, root-of-unity filters, and refinement semigroups found the surrounding classical Ramanujan/Hilbert/Bost–Connes theories but no authoritative source using this exact Prime-Circle factorization as an RH mechanism. Absence of that wording is not evidence of historical priority.

The durable contribution is a **scope classification inside the research object**: the canonical Hardy operator family has no hidden ordered-prime refinement dynamics. Its cross-level birth rule is an exact commuting Möbius finite-difference calculus acting on one universal Hilbert operator.

## 7. Boundary of the obstruction

The result does **not** say that the individual operators appearing in the Möbius sum commute under composition. In particular,

\[
\mathfrak D_p\mathfrak D_q
=\mathfrak D_q\mathfrak D_p
\]

as superoperators does not imply

\[
[\mathfrak D_p\Gamma_1,\mathfrak D_q\Gamma_1]=0.
\]

Accordingly, this finding does not classify or trivialize:

- the full spectrum of `\Gamma_\rho` for squarefree `\rho` with several distinct primes;
- higher relative traces `\operatorname{Tr}(T_\rho^k)` for `k\ge3` or Fredholm/perturbation determinants left open by PC-077/PC-078;
- nonlinear products or commutators of distinct embedded Hilbert copies at a fixed endpoint;
- cross-level operators that retain several shell spaces simultaneously rather than replacing refinement by the canonical coefficient action;
- shell-dependent/nonlinear geometries, the old/new cotangent coupling, or the global uniformization/monodromy branch rooted in PC-017.

The exact negative statement is narrower and stronger where it applies: **insertion history itself contains no information**. Any surviving mixed-prime Hardy mechanism must depend on the endpoint interaction of the resulting embedded channels, not on the order by which those primes were introduced.

## 8. Falsification surface

The result has direct finite/coefficient-level failure tests.

1. For any Hankel sequence, verify that residue splitting modulo `d` gives `W_d\mathfrak D_d(A)W_d^*=J_d\otimes A`.
2. Verify `\mathfrak D_d\mathfrak D_e=\mathfrak D_{de}` coefficient by coefficient.
3. Insert the classical divisor formula for `c_n(m)` and recover `\Gamma_n=\sum_{d|n}\mu(n/d)\mathfrak D_d\Gamma_1`.
4. For a new prime `p`, compare the exact coefficients of `\Gamma_{pn}` with `(\mathfrak D_p-I)\Gamma_n`; for a repeated prime compare with `\mathfrak D_p\Gamma_n`.
5. Sum over all `d|n` and verify that every Möbius coefficient cancels except the `\mathfrak D_n\Gamma_1` term.

For example,

\[
\Gamma_6
=(\mathfrak D_2-I)(\mathfrak D_3-I)\Gamma_1
=(\mathfrak D_6-\mathfrak D_2-\mathfrak D_3+I)\Gamma_1,
\]

independently of whether `2` or `3` is inserted first, while

\[
\Gamma_1+\Gamma_2+\Gamma_3+\Gamma_6
=\mathfrak D_6\Gamma_1.
\]

Failure of any of these exact identities would invalidate the corresponding conclusion.

## Research consequence

The cross-level Hardy/Hankel branch now has an exact refinement calculus:

\[
\boxed{
\text{primitive cyclotomic Hardy birth}
=
\text{commuting Möbius differences of universal Hilbert dilations}.
}
\]

Repeated primes are tensor inflation, distinct new primes are commuting finite differences, and cumulative divisor-shell aggregation is one universal full-root Hilbert channel. Consequently the next meaningful Hardy question, if this branch is continued, is **endpoint mixed-prime spectral interference or higher relative data**, not refinement order, holonomy, or cumulative birth-shell spectra.