# WP-051 — positive Schatten energies of the Hardy remainder have full composite support

**Status:** `EXACT-DERIVED` + `NEGATIVE/OBSTRUCTION` + `PRIOR-ART-BOUNDARY`. The exact lower bound below is derived from the canonical Prime-Circle Hardy/Hankel remainder of `PC-075`. The Ramanujan-sum identity and Schatten-ideal facts used in the derivation are standard; no theorem-level historical novelty is claimed. The durable project-specific result is that the most direct positive higher relative invariants left open by `PC-076` are nonzero on every cyclotomic shell, including an order-one family on which the von Mangoldt coefficient vanishes identically.

`WP-050` compared two first-order readouts of the anchored Prime-Circle geometry: its positive reflection-odd current energy gives the endpoint sum

\[
\Lambda(n)+\mathbf 1_{2\mid n}\Lambda(n/2),
\]

whereas `PC-076` gives the signed Hardy relative trace

\[
2\operatorname{Tr}T_n
=\Lambda(n)-\mathbf 1_{2\mid n}\Lambda(n/2).
\]

Their arithmetic combination isolates `Lambda(n)`, but it does not produce a positive quadratic form. `PC-076` therefore left higher Schatten moments and other relative invariants of `T_n` open. The first genuinely positive version of that escape can now be killed exactly.

## 1. The canonical trace-class remainder

`PC-075` decomposes the cyclotomic logarithmic Hardy coupling as

\[
W\Gamma_nW^*
=-\frac1n C_n\otimes H+T_n,
\qquad T_n\in\mathcal S_1,
\tag{1}
\]

where `H=H_1` is the classical Hilbert matrix,

\[
(H_\alpha)_{ab}=\frac1{a+b+\alpha},
\qquad a,b\ge0,
\tag{2}
\]

and the residue blocks of the remainder are

\[
\boxed{
(T_n)_{rs}
=-\frac{c_n(r+s+1)}{n}
\left(H_{(r+s+1)/n}-H_1\right),
\qquad 0\le r,s<n.
}
\tag{3}
\]

Both `W\Gamma_nW^*` and `-(1/n)C_n\otimes H` are self-adjoint, so `T_n` is self-adjoint as well.

The most canonical positive higher relative invariant is therefore the Hilbert--Schmidt energy

\[
E_n^{\rm HS}
:=\operatorname{Tr}(T_n^2)
=\|T_n\|_{\mathcal S_2}^2
\ge0.
\tag{4}
\]

More generally, because `T_n` is trace class, every positive Schatten moment

\[
E_{n,q}:=\operatorname{Tr}|T_n|^q
=\|T_n\|_{\mathcal S_q}^q,
\qquad q\ge1,
\tag{5}
\]

is finite and nonnegative.

## 2. One forced matrix coefficient survives on every shell

Fix any `n>1` and any prime divisor `p|n`. Set

\[
t=\frac np,
\qquad r=t-1,
\qquad s=0.
\tag{6}
\]

Then `0<=r<n`, and the corresponding residue offset in (3) is

\[
\alpha_{rs}=\frac{r+s+1}{n}
=\frac1p.
\tag{7}
\]

The standard Ramanujan-sum formula

\[
c_n(k)
=\mu\!\left(\frac n{(n,k)}\right)
\frac{\varphi(n)}{\varphi\!\left(n/(n,k)\right)}
\tag{8}
\]

gives, because `(n,n/p)=n/p`,

\[
\boxed{
c_n(n/p)=-\frac{\varphi(n)}{p-1}.}
\tag{9}
\]

Now evaluate the `(a,b)=(0,0)` entry of the block in (3). Since

\[
(H_{1/p}-H_1)_{00}
=p-1,
\tag{10}
\]

we obtain the exact coefficient

\[
\begin{aligned}
\bigl((T_n)_{\,n/p-1,\,0}\bigr)_{00}
&=-\frac{c_n(n/p)}n(p-1)\\
&=\boxed{\frac{\varphi(n)}n}.
\end{aligned}
\tag{11}
\]

Thus the relative remainder is never zero:

\[
\boxed{T_n\ne0\qquad(n>1).}
\tag{12}
\]

More quantitatively, a matrix coefficient is bounded by the operator norm, hence

\[
\boxed{
\|T_n\|\ge\frac{\varphi(n)}n.
}
\tag{13}
\]

This lower bound is obtained from a single canonical residue block; no spectral computation, asymptotic approximation, or cancellation argument is involved.

## 3. Every positive Schatten size has full shell support

For every `q>=1`, the largest singular value is dominated by the Schatten norm. Equations (5) and (13) therefore imply

\[
\boxed{
E_{n,q}
=\operatorname{Tr}|T_n|^q
\ge
\left(\frac{\varphi(n)}n\right)^q
>0,
\qquad n>1.
}
\tag{14}
\]

In particular,

\[
\boxed{
E_n^{\rm HS}
=\operatorname{Tr}(T_n^2)
\ge
\left(\frac{\varphi(n)}n\right)^2
>0.
}
\tag{15}
\]

Since `T_n` is self-adjoint, all even relative moments satisfy

\[
\operatorname{Tr}(T_n^{2k})
=\operatorname{Tr}|T_n|^{2k}
>0,
\qquad k\ge1.
\tag{16}
\]

So the positivity operation that removes the sign ambiguity of the first trace does not sharpen its arithmetic support. It does the opposite: every shell survives.

## 4. The false support remains order one on `n=2p`

The mismatch with the finite Weil coefficient is not a tiny tail effect. Let `p` be an odd prime and set

\[
n=2p.
\]

Then `n` is not a prime power, so

\[
\Lambda(2p)=0.
\tag{17}
\]

But

\[
\frac{\varphi(2p)}{2p}
=\frac{p-1}{2p},
\tag{18}
\]

and hence

\[
\boxed{
E_{2p,q}
\ge
\left(\frac{p-1}{2p}\right)^q
\longrightarrow 2^{-q}.
}
\tag{19}
\]

For the Hilbert--Schmidt energy,

\[
E_{2p}^{\rm HS}
\ge
\left(\frac{p-1}{2p}\right)^2
\longrightarrow\frac14.
\tag{20}
\]

Thus there is an infinite family of exact non-prime-power controls on which the target Mangoldt shell coefficient is identically zero while the canonical positive higher relative energy stays uniformly away from zero.

The same conclusion is visible already in the exact block coefficient (11): on `n=2p`, the remainder contains a matrix entry tending to `1/2`. Critical attenuation can scale this leakage but cannot turn it into prime-power support.

## 5. Why this closes the direct positive higher-moment escape from PC-076

`PC-076` correctly left `Tr(T_n^k)`, perturbation determinants, and other relative spectral data open after showing that the first trace collapses to the endpoint difference. The present result distinguishes two materially different continuations.

The **positive shell-size continuation** is now exhausted for all ordinary Schatten powers:

\[
T_n
\longmapsto
|T_n|^q
\longmapsto
\operatorname{Tr}|T_n|^q.
\tag{21}
\]

It cannot provide the finite Weil birth coefficient because its support is every `n>1`, whereas

\[
\Lambda(n)=0
\quad\text{unless }n\text{ is a prime power}.
\tag{22}
\]

Repairing (21) by multiplying the shell energy by an external indicator of prime-power support, by `Lambda(n)`, or by a hand-picked vanishing weight would simply insert the target arithmetic selection rather than derive it from the Hardy geometry.

This does **not** show that the full remainder contains no useful arithmetic. It says specifically that making its higher relative data positive by taking singular-value size or even moments destroys the cancellation needed for Mangoldt sparsity.

## 6. Relation to WP-050 and the finite--archimedean problem

`WP-050` found that the canonical local reflection-odd current has too much support because positivity forces the endpoint sum

\[
\Lambda(n)+\mathbf1_{2\mid n}\Lambda(n/2),
\]

while the first Hardy trace supplies the opposite signed endpoint difference. The present obstruction shows that passing from that signed Hardy trace to its canonical positive spectral sizes does not rescue the situation: the support expands from a parity-twisted Mangoldt set to **all shells**.

This is useful because the Hardy remainder is genuinely nonlocal and lies outside the finite-range scalar reflection-odd class ruled out in `WP-050`. The failure is therefore not caused by the Laurent-factorization obstruction there. It comes from a different fact: the residue-class remainder has a forced nonzero channel at `alpha=1/p` for every divisor prime `p|n`.

Consequently the route

```text
cyclotomic Hardy coupling
    -> trace-class arithmetic remainder T_n
    -> positive Schatten/even-moment energy
    -> finite Weil Mangoldt selector
```

fails before the archimedean completion question is even reached.

## 7. Prior-art and novelty audit

No historical novelty is claimed for the ingredients of the proof.

- Formula (8) is the standard closed form for Ramanujan sums.
- Trace-class inclusion in every `S_q`, `q>=1`, positivity of `Tr|T|^q`, and the identification `Tr(T^2)=||T||_2^2` for self-adjoint Hilbert--Schmidt operators are standard trace-ideal facts.
- General Schatten-class theory for Hankel operators is classical and substantially broader than the special operator considered here. `PC-075` already audits the surrounding Hilbert/Hankel and multichannel operator theory.

A directed literature search for Ramanujan-sum/cyclotomic Hankel Schatten invariants and the exact remainder family (3) did not provide a basis for claiming a new general operator theorem. The durable result is the Mathia-specific obstruction obtained by combining the exact `PC-075` residue decomposition with the divisor choice `t=n/p`: it proves that the direct positive higher relative invariants explicitly left open by `PC-076` have the wrong arithmetic support.

## 8. Boundary of the obstruction

The result does **not** rule out:

- odd or signed higher moments `Tr(T_n^{2k+1})`, where cancellation can occur;
- Fredholm or perturbation determinants of `T_n`;
- isolated eigenvalues, threshold resonances, or spectral-shift data relative to the Hilbert core;
- cross-level Hardy operators that couple distinct exact-order shells before taking a positive form;
- matrix-valued or graded constructions in which cancellation occurs before positivity;
- a nonseparable finite--archimedean compression or cohomological quotient with an independent sign theorem.

Those routes would be genuinely different from the positive shell-size invariant killed here. In particular, a global positive form may have nontrivial off-diagonal shell couplings; this finding does not infer its impossibility from the positivity of the diagonal blocks alone.

## 9. Falsification surface

The obstruction has four short exact checks.

1. Verify the `PC-075` remainder block formula (3).
2. For any `p|n`, verify `c_n(n/p)=-phi(n)/(p-1)`.
3. Evaluate the `(0,0)` entry of `H_{1/p}-H_1` and obtain `p-1`, giving (11).
4. Use the operator-norm/Schatten-norm inequalities to obtain (14).

Failure of item 1 invalidates the connection to the canonical Prime-Circle remainder. Failure of 2 or 3 invalidates the full-support lower bound. If all four hold, every positive Schatten moment is strictly positive on every `n>1`, and the `n=2p` family gives an exact matched control against Mangoldt support.

## Research consequence

The simplest genuinely positive higher relative invariants of the canonical Hardy/Hankel remainder are not a hidden finite Weil measure:

\[
\boxed{
\operatorname{Tr}|T_n|^q
\ge
\left(\frac{\varphi(n)}n\right)^q
>0
\quad(n>1,\ q\ge1).
}
\]

The next viable Hardy-based mechanism must therefore preserve cancellation **before** the final positivity theorem rather than obtain positivity by taking absolute values, squares, or even Schatten moments shell by shell. Any successful continuation still needs a global or cross-shell operation that simultaneously derives the prime-power birth support, couples the intrinsic `q=2` archimedean channel, and yields nonnegativity from geometry rather than from a post hoc positive spectral size.