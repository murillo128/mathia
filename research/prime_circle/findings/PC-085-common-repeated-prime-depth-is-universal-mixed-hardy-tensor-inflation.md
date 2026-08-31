# PC-085 — common repeated-prime depth is universal mixed Hardy tensor inflation

**Status:** `EXACT-DERIVED` + `NEGATIVE/OBSTRUCTION` + `PRIOR-ART-REDIRECTION`. The simultaneous tensor factorization and all mixed-word consequences below are exact consequences of the Prime-Circle Hardy operator together with the classical prime-power lifting law for Ramanujan sums. No theorem-level historical novelty is claimed. The durable contribution is a scope classification: common repeated-prime depth cannot create new finite mixed-shell spectral shape.

PC-084 showed that every finite nonconstant completed-shell Hardy word has a canonical ordinary trace-class meaning under the natural finite Hardy sections. It therefore leaves the arithmetic content of those higher mixed words as a genuine finite-order question. PC-078 had already shown that repeated-prime depth is only signed tensor inflation for one completed shell,

\[
\Gamma_{pn}\cong J_p\otimes\Gamma_n
\qquad (p\mid n),
\]

and likewise for the single-level trace-class remainder.

The remaining question is whether repeated-prime depth can become nontrivial **after several different shell operators are multiplied on the same Hardy space**. It cannot whenever that repeated depth is common to all shell labels in the word.

For a finite tuple of conductors

\[
n_1,\ldots,n_\ell,
\]

put

\[
g=\gcd(n_1,\ldots,n_\ell),
\qquad
h=\frac{g}{\operatorname{rad}(g)},
\qquad
\widehat n_i=\frac{n_i}{h}.
\]

Then there is a finite self-adjoint involution `K_g` of dimension `h` and one unitary identification

\[
U_g:\ell^2(\mathbb Z_{\ge0})
\longrightarrow
\mathbb C^h\otimes\ell^2(\mathbb Z_{\ge0})
\]

such that **simultaneously for every shell in the tuple**

\[
\boxed{
U_g\Gamma_{n_i}U_g^*
=
K_g\otimes\Gamma_{\widehat n_i}.
}
\]

Consequently the whole finite word satisfies the exact operator identity

\[
\boxed{
U_g
\left(
\Gamma_{n_1}\Gamma_{n_2}\cdots\Gamma_{n_\ell}
\right)
U_g^*
=
K_g^\ell\otimes
\left(
\Gamma_{\widehat n_1}\Gamma_{\widehat n_2}\cdots
\Gamma_{\widehat n_\ell}
\right).
}
\]

Thus the exponents that are repeated **in every conductor simultaneously** contribute only a universal finite signed multiplicity. They do not alter the residual mixed Hardy interaction.

## 1. One common repeated prime factors from every shell at once

Recall the Prime-Circle Hardy operator

\[
(\Gamma_n)_{jk}
=
-\frac{c_n(j+k+1)}{j+k+1},
\qquad j,k\ge0.
\]

For `p|n`, PC-078 uses the classical Ramanujan lifting identity

\[
c_{pn}(m)
=
\begin{cases}
p\,c_n(m/p),&p\mid m,\\
0,&p\nmid m,
\end{cases}
\]

and the residue split

\[
W_p:\ell^2(\mathbb Z_{\ge0})
\longrightarrow
\mathbb C^p\otimes\ell^2(\mathbb Z_{\ge0}),
\qquad
j=pa+r,
\]

to prove

\[
\boxed{
W_p\Gamma_{pn}W_p^*=J_p\otimes\Gamma_n,
}
\]

where

\[
(J_p)_{rs}=\mathbf 1_{r+s=p-1}
\]

is the `p x p` reversal matrix.

The point needed here is that **the unitary `W_p` depends only on `p`, not on the conductor `n`**. Therefore if

\[
p\mid n_i
\qquad\text{for every }i=1,\ldots,\ell,
\]

the same decomposition applies simultaneously:

\[
W_p\Gamma_{pn_i}W_p^*
=
J_p\otimes\Gamma_{n_i}
\qquad\text{for every }i.
\]

Multiplication then preserves the common finite factor:

\[
\begin{aligned}
W_p
\left(
\Gamma_{pn_1}\cdots\Gamma_{pn_\ell}
\right)
W_p^*
&=
(J_p\otimes\Gamma_{n_1})
\cdots
(J_p\otimes\Gamma_{n_\ell})\\
&=
\boxed{
J_p^\ell\otimes
\left(
\Gamma_{n_1}\cdots\Gamma_{n_\ell}
\right).
}
\end{aligned}
\]

This is an equality of bounded operators. No trace, asymptotic limit, commutativity assumption among the `Gamma_n`, or finite-section argument is used.

The hypothesis is sharp for this stripping operation. If `p` is not already present in every base conductor, the Ramanujan lifting identity above does not apply simultaneously and there is no common `J_p` factor to remove from the whole tuple.

## 2. Iterating strips exactly the repeated part of the common gcd

Write

\[
g=\prod_p p^{a_p}.
\]

For every prime with `a_p>=2`, all conductors `n_i` contain at least `p^{a_p}`. We may therefore apply the simultaneous one-prime factorization `a_p-1` times while leaving one common copy of `p` in every residual conductor.

Doing this for every prime dividing `g` gives

\[
h=\prod_{p\mid g}p^{a_p-1}
=
\frac{g}{\operatorname{rad}(g)}
\]

and

\[
\widehat n_i=\frac{n_i}{h}.
\]

Up to permutation of finite tensor coordinates, define

\[
\boxed{
K_g
=
\bigotimes_{p\mid g}
J_p^{\otimes(a_p-1)}.
}
\]

Then

\[
\dim K_g=h,
\qquad
K_g^*=K_g,
\qquad
K_g^2=I_h.
\]

Composing the common residue splittings produces one unitary `U_g` for which

\[
\boxed{
U_g\Gamma_{n_i}U_g^*
=
K_g\otimes\Gamma_{\widehat n_i}
\qquad
\text{for every }i.
}
\]

Different orders of stripping the repeated primes merely permute finite tensor factors. They cannot alter the resulting operator class.

The residual tuple has

\[
\boxed{
\gcd(\widehat n_1,\ldots,\widehat n_\ell)
=
\operatorname{rad}(g).
}
\]

This identifies the exact boundary of the reduction: **all common prime-power depth above exponent one disappears, but the common squarefree radical does not.** The latter cannot be stripped by this argument because removing its last copy of a prime would violate the condition `p|n` required by the lifting law.

## 3. Every finite mixed word inherits the tensor reduction

Let

\[
W(n_1,\ldots,n_\ell)
=
\Gamma_{n_1}\cdots\Gamma_{n_\ell}
\]

and

\[
\widehat W
=
W(\widehat n_1,\ldots,\widehat n_\ell).
\]

Multiplying the simultaneous shell factorizations gives

\[
\boxed{
U_g W(n_1,\ldots,n_\ell)U_g^*
=
K_g^\ell\otimes\widehat W.
}
\]

Because `K_g^2=I_h`,

\[
K_g^\ell
=
\begin{cases}
I_h,&\ell\text{ even},\\
K_g,&\ell\text{ odd}.
\end{cases}
\]

Thus even-length words receive only an `h`-fold copy. Odd-length words receive signed copies determined by the eigenspaces of `K_g`.

If the original tuple is nonconstant, then the residual tuple is also nonconstant. PC-084 therefore applies to both words and gives

\[
W,\widehat W\in\mathcal S_1.
\]

The operator factorization can then be read as a complete finite mixed-word spectral reduction.

### Schatten data

Since `K_g^\ell` is unitary, the singular values of `W` are exactly the singular values of `\widehat W`, each repeated `h` times. Hence for every Schatten exponent `q>=1`,

\[
\boxed{
\|W\|_{\mathcal S_q}^q
=
h\,\|\widehat W\|_{\mathcal S_q}^q.
}
\]

Common repeated-prime depth cannot create a new singular-value shape.

### Trace

The reversal matrix has

\[
\operatorname{tr}J_p
=
\begin{cases}
0,&p=2,\\
1,&p\text{ odd}.
\end{cases}
\]

Therefore

\[
\tau_g:=\operatorname{tr}K_g
=
\begin{cases}
0,&4\mid g,\\
1,&4\nmid g.
\end{cases}
\]

For every nonconstant finite word,

\[
\boxed{
\operatorname{Tr}W
=
\begin{cases}
h\,\operatorname{Tr}\widehat W,
&\ell\text{ even},\\[4pt]
\tau_g\,\operatorname{Tr}\widehat W,
&\ell\text{ odd}.
\end{cases}
}
\]

In particular,

\[
\boxed{
4\mid \gcd(n_1,\ldots,n_\ell),
\quad
\ell\text{ odd},
\quad
(n_i)\text{ nonconstant}
\Longrightarrow
\operatorname{Tr}
(\Gamma_{n_1}\cdots\Gamma_{n_\ell})=0.
}
\]

This vanishing is not a new arithmetic cancellation in the residual mixed interaction. It is exactly the zero trace of the universal reversal factor `J_2`.

### Fredholm determinant

For a nonconstant word define

\[
D_W(z)=\det(I-zW).
\]

If `ell` is even,

\[
\boxed{
D_W(z)=D_{\widehat W}(z)^h.
}
\]

If `ell` is odd, let

\[
M_\pm=\frac{h\pm\tau_g}{2}
\]

be the multiplicities of `+1` and `-1` in `K_g`. Then

\[
\boxed{
D_W(z)
=
D_{\widehat W}(z)^{M_+}
D_{\widehat W}(-z)^{M_-}.
}
\]

Thus common repeated-prime depth cannot generate a new zero set for any finite mixed-word Fredholm determinant. It only repeats the residual zeros and, for odd word length, reflects them through `z -> -z`.

## 4. Exact controls

The theorem has immediate finite controls.

For the odd mixed word

\[
(4,8,12)
=
2\,(2,4,6),
\]

all base conductors `(2,4,6)` are divisible by `2`. Hence

\[
W_2
\Gamma_4\Gamma_8\Gamma_{12}
W_2^*
=
J_2\otimes
\Gamma_2\Gamma_4\Gamma_6.
\]

Since `tr J_2=0` and the word is trace class by PC-084,

\[
\boxed{
\operatorname{Tr}
(\Gamma_4\Gamma_8\Gamma_{12})=0.
}
\]

For

\[
(9,18,27)=3\,(3,6,9),
\]

the word length is odd but `tr J_3=1`, so

\[
\boxed{
\operatorname{Tr}
(\Gamma_9\Gamma_{18}\Gamma_{27})
=
\operatorname{Tr}
(\Gamma_3\Gamma_6\Gamma_9).
}
\]

For the even word

\[
(25,50,75,100)
=
5\,(5,10,15,20),
\]

we obtain

\[
\boxed{
\operatorname{Tr}
(\Gamma_{25}\Gamma_{50}\Gamma_{75}\Gamma_{100})
=
5\,
\operatorname{Tr}
(\Gamma_5\Gamma_{10}\Gamma_{15}\Gamma_{20}).
}
\]

Aligned finite truncations of the exact matrix entries reproduce the simultaneous tensor identity for representative steps `p=2,3,5`, including the three tuples above. These checks are falsification controls only; the claim rests on the exact Ramanujan lifting calculation.

A deliberately mismatched control is equally important: if one attempts to strip `p` from a tuple for which some base conductor is not divisible by `p`, the common tensor identity fails. The result therefore does **not** erase relative prime-power information that is present in only part of the tuple.

## 5. Prior-art and novelty audit

The ingredients surrounding the result are classical or already established inside this line.

1. Ramanujan's prime-power formulas and multiplicativity give the lifting identity used in PC-078. The classical Ramanujan-sum sources are already anchored in `research/prime_circle/SOURCES.md`.
2. Tensor products with finite reversal matrices and the resulting trace/Schatten/Fredholm formulas are elementary operator theory.
3. PC-078 already proves the one-shell factorization and its consequences for the canonical single-level remainder `T_n`. The present result uses the fact, not emphasized there for mixed words, that the residue unitary `W_p` is conductor-independent and therefore factors **several simultaneously lifted completed shells on the same Hardy space at once**.
4. PC-084 supplies the exact trace-class gate needed to turn the bounded-operator factorization into trace and Fredholm statements for every finite nonconstant completed-shell word.

A targeted literature search for Ramanujan-sum Hankel operators, prime-power tensor decompositions of Ramanujan Hankel matrices, and cyclotomic/Hilbert mixed products found the surrounding classical Ramanujan and finite-matrix literature but no authoritative source stating this exact mixed-shell Hardy specialization. That absence is not treated as evidence of historical novelty.

The durable content is therefore not a claim of a new abstract tensor theorem. It is the exact **information audit for Prime Circle**:

\[
\boxed{
\text{common repeated-prime depth in a finite mixed Hardy word}
=
\text{universal finite signed tensor multiplicity}.
}
\]

## 6. What this rules out

PC-084 leaves finite higher Hardy traces as genuine arithmetic invariants beyond pairwise resultants. The present theorem shows that one natural source of additional complexity is illusory.

If every conductor in a finite mixed word is simultaneously multiplied by another copy of a prime already present in every conductor, then no new mixed spectral geometry appears. Repeating that operation to arbitrary common depth changes only

- finite multiplicity;
- an elementary sign split for odd word length;
- the universal parity cancellation when the common gcd is divisible by `4`.

Therefore a proposal of the form

\[
\boxed{
\text{increase common prime-power depth}
\to
\text{higher mixed Hardy trace/determinant}
\to
\text{new RH-sensitive spectral structure}
}
\]

is ruled out for every finite nonconstant completed-shell word.

In particular, common repeated depth supplies no intrinsic complex parameter, functional equation, gamma factor, or critical-line symmetry. A Dirichlet or Mellin aggregation over that depth would be an externally formed transform of universal multiplicities unless some additional Prime-Circle structure is first derived.

## 7. What survives

The obstruction is deliberately narrower than a no-go for the whole cross-level Hardy branch.

It does **not** classify:

- relative prime-power exponents that are not common to all conductors;
- the squarefree residual tuple `(\widehat n_i)`, whose common gcd is `rad(g)`;
- genuinely mixed squarefree endpoint interaction of the kind left open by PC-079/PC-082;
- infinite-shell limits in which the number or range of conductors grows;
- block operators that retain several conductor spaces before multiplying completed shell operators;
- nonlinear or shell-dependent operators not equivalent to the canonical `Gamma_n` Hardy family;
- the old/new cotangent branch or the nonlinear uniformization/monodromy branch.

For pure same-shell words, the bounded-operator tensor identity still holds, but PC-084's trace-class conclusion does not: for example `Gamma_n^2` is not trace class. The trace and Fredholm formulas above are therefore asserted only for nonconstant finite words.

The reduction also does not permit stripping the final common squarefree copy of a prime. That copy is exactly where the prime is still part of the residual primitive-shell arithmetic rather than merely repeated depth.

## Falsification surface

The finding has six direct failure points.

1. For `p|n`, the exact Ramanujan lifting identity
   \[
   c_{pn}(m)=p\,c_n(m/p)\mathbf1_{p\mid m}
   \]
   must hold with the PC-078 normalization.
2. The residue unitary `W_p` must be independent of `n`, so the same decomposition simultaneously factors every shell `Gamma_{pn_i}` when `p|n_i` for all `i`.
3. Multiplication under that common unitary must give
   \[
   W_p(\Gamma_{pn_1}\cdots\Gamma_{pn_\ell})W_p^*
   =
   J_p^\ell\otimes
   (\Gamma_{n_1}\cdots\Gamma_{n_\ell}).
   \]
4. Iterating all common repeated primes must leave residual gcd exactly `rad(g)` and produce a finite involution of dimension `h=g/rad(g)`.
5. For nonconstant words, PC-084 must supply trace class for both the original and residual products before trace/Fredholm consequences are invoked.
6. The parity controls must agree with `tr J_2=0`, `tr J_p=1` for odd `p`, and with direct aligned finite truncations.

Failure of points 1--4 invalidates the operator theorem. Failure of point 5 invalidates only the trace-class consequences. Point 6 is a direct consistency check on the finite tensor factor.

## Research consequence

Finite mixed Hardy data should henceforth be normalized for **common repeated-prime depth** before being credited with new arithmetic structure:

\[
\boxed{
(n_1,\ldots,n_\ell)
\longmapsto
\left(
\frac{n_1}{g/\operatorname{rad}(g)},
\ldots,
\frac{n_\ell}{g/\operatorname{rad}(g)}
\right),
\qquad
g=\gcd(n_1,\ldots,n_\ell).
}
\]

All discarded depth is exact finite tensor inflation. Any genuinely new finite mixed-shell information must already be present in the residual tuple, where no prime occurs with exponent greater than one in **every** conductor simultaneously.

This narrows, but does not close, the higher Hardy frontier left by PC-082--PC-084. The meaningful remaining finite-order questions are the arithmetic/classicalization of the residual mixed invariants and interactions that depend on relative rather than common prime-power structure. Genuinely new analytic parameters still have to come from an intrinsic infinite/cross-level construction rather than from universal common-depth multiplicity.
