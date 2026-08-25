# PF-032 — the logarithmic prime mesh is exactly the standard collar width

**Status:** `DECISIVE-NEGATIVE` for any proposed prime-specific spectral mechanism that treats the exact pair `(h_n, ell_n)` as two independent geometric variables. The collar identities are standard hyperbolic geometry; the project-specific content is the exact specialization showing that the prime logarithmic mesh is nothing more than twice the standard collar half-width.

## 1. Exact prime-flute input

Recall the exact variables

\[
u_n=\cot(\pi/p_n),\qquad
h_n=\log\frac{u_n}{u_{n-1}}>0,
\]

and the distinguished cuff identity

\[
\boxed{
 e^{-\ell_n/2}=\tanh(h_n/4).
}
\]

The first-order asymptotic is

\[
h_n\sim \frac{g_{n-1}}{p_n},
\]

up to the indexing convention for the consecutive prime gap, and hence

\[
\ell_n\sim 2\log\frac{4p_n}{g_{n-1}}.
\]

## 2. Standard hyperbolic collar width

For a simple closed geodesic of length \(\ell\), the standard collar half-width is

\[
 w(\ell)
 =\operatorname{arsinh}\!\left(\frac1{\sinh(\ell/2)}\right)
 =\log\coth(\ell/4).
\]

This is the usual collar-lemma quantity. Basmajian-Hakobyan-Saric and the tight-flute literature use the equivalent notation

\[
 c(\alpha)=\log\coth(\ell(\alpha)/4).
\]

Now put

\[
q_n=e^{-\ell_n/2}=\tanh(h_n/4).
\]

Since

\[
\coth(\ell_n/4)
=\frac{1+e^{-\ell_n/2}}{1-e^{-\ell_n/2}}
=\frac{1+q_n}{1-q_n},
\]

and

\[
\frac{1+\tanh x}{1-\tanh x}=e^{2x},
\]

we get the exact identity

\[
\boxed{
 w_n:=w(\ell_n)=\frac{h_n}{2}.
}
\]

Equivalently,

\[
\boxed{
 h_n=2\log\coth(\ell_n/4).
}
\]

Thus the logarithmic endpoint mesh introduced by the prime-circle construction is not an additional modulus dual to the cuff length. It is exactly the standard collar coordinate of that cuff.

## 3. The canonical spine distance is the universal tight-pants identity

PF-026 records the exact distance between consecutive marked cuff axes / spine locations:

\[
 d_n=\frac12(h_n+h_{n+1}).
\]

Using the collar identity above,

\[
\boxed{
 d_n=w(\ell_n)+w(\ell_{n+1}).
}
\]

But this is precisely the standard identity for a tight pair of pants with one cusp: the distance between the relevant nested axes is the sum of the collar widths of the two finite cuffs. It appears explicitly in the tight-flute literature as

\[
 d_i=c(\alpha_i)+c(\alpha_{i+1}).
\]

So both halves of the prime-flute radial construction,

\[
\ell_n\longleftrightarrow h_n
\quad\text{and}\quad
(h_n,h_{n+1})\longleftrightarrow d_n,
\]

are exactly the universal collar/seam geometry of a tight pair of pants.

## 4. Consequence: standard-collar spectral/extremal-length branches add no prime invariant

The identity

\[
 w_n=h_n/2
\]

means that any local observable built from the standard collar geometry can be rewritten as a one-variable function of \(\ell_n\), or equivalently of \(h_n\). Treating both as independent inputs double-counts the same Fenchel-Nielsen length datum.

This rules out, as a source of new prime-specific information, constructions of the form

\[
(\ell_n,h_n)
\to
\text{standard collar modulus/capacity/resistance}
\to
\text{transfer or determinant}
\]

when the construction factorizes cuff-by-cuff. Such an object can still depend on the prime gaps through the chosen cuff sequence, but it has no additional geometric coupling beyond the already-known length coordinate.

In particular, the exact telescoping law becomes an exact statement about the total standard collar width:

\[
\boxed{
\sum_{n=m}^{N}w_n
=\frac12\log\frac{u_N}{u_{m-1}}.
}
\]

Hence its divergent part sees only endpoint growth. Fine gap fluctuations survive only in nonlinear/convergent corrections, exactly as in PF-002 and PF-022.

## 5. Parabolicity/completeness is therefore coarse here

For zero-twist tight flutes, Basmajian-Hakobyan-Saric obtain the classical criterion in terms of the cuff lengths

\[
\sum_n e^{-\ell_n/2}=\infty
\]

for the relevant parabolic/first-kind regime (with the precise equivalences stated in their zero-twist theorem).

Here

\[
e^{-\ell_n/2}=\tanh(w_n/2),
\]

and \(w_n\to0\), so

\[
\tanh(w_n/2)\sim w_n/2.
\]

But

\[
\sum_n w_n
=\frac12\sum_n h_n
=\infty
\]

by exact endpoint telescoping. Thus this global type criterion is forced by the coarse radial escape and cannot distinguish fine prime-gap fluctuations. This is consistent with PF-012/PF-021/PF-023.

## 6. What remains alive

The negative result is deliberately local. It does **not** rule out:

1. nonstandard half-collars whose geometry couples a cuff to the rest of its pair of pants;
2. multi-gap cross-ratios / separating geodesics from PF-004;
3. cross-cusp scattering data after local cusp normalization;
4. the two-dimensional spherical/cyclotomic constructions in the prime-circle branch;
5. genuinely relative spectral invariants that cannot be written as independent functions of single cuffs.

The important methodological gate is:

> the exact relation `exp(-ell_n/2)=tanh(h_n/4)` must no longer be treated as a prime-specific duality. It is exactly the standard collar coordinate change.

Any future candidate based on this relation must introduce a genuinely nonlocal geometric operation before it can carry information beyond the Fenchel-Nielsen cuff sequence itself.

## 7. Literature / novelty check

- The standard collar half-width
  \(w(\ell)=\operatorname{arsinh}(1/\sinh(\ell/2))=\log\coth(\ell/4)\)
  is classical.
- In the tight-flute literature, Basmajian-Hakobyan-Saric use the same collar function and the exact tight-pants relation
  \(d_i=c(\alpha_i)+c(\alpha_{i+1})\).
- Their work also gives sharp parabolicity criteria for zero-twist flutes in terms of the Fenchel-Nielsen length sequence.
- No novelty is claimed for these general hyperbolic facts. The useful project result is the exact identification
  \(w(\ell_n)=h_n/2\), which shows that a seemingly special prime-circle/cuff duality is already the standard collar parametrization and therefore closes an important local spectral branch.

## References

- A. Basmajian, H. Hakobyan, D. Saric, *The type problem for Riemann surfaces via Fenchel-Nielsen parameters*, Proc. London Math. Soc. 125 (2022), 568-625.
- Standard collar lemma / hyperbolic pair-of-pants geometry.
- PF-001, PF-002, PF-022 and PF-026 in this research ledger.
