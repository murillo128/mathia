# AF-339 — the zero-sensitive Mangoldt-minus-uniform source has growing ordered sign complexity

**Status:** `EXACT-DERIVED`, `CLASSICAL-IDENTITY`, `SOURCE-COMPLEXITY-GATE`, `ZERO-SENSITIVE-SOURCE`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-216 and AF-338 leave a concrete source-side question: can a natural arithmetic discrepancy that still knows the Riemann zero divisor have a bounded ordered sign budget?

The most direct candidate already fails that fixed-order gate.

Let

\[
d_n:=\Lambda(n)-1,
\qquad n\ge2,
\tag{1}
\]

where `Lambda` is the von Mangoldt function. For `Re(s)>1`, its Dirichlet series is

\[
\boxed{
H(s):=\sum_{n\ge2}d_n n^{-s}
=-\frac{\zeta'(s)}{\zeta(s)}-\zeta(s)+1.
}
\tag{2}
\]

Thus `H` is not merely prime-derived. Its meromorphic continuation is directly zero-sensitive: if `rho` is a zero of `zeta` of multiplicity `m`, then

\[
\boxed{
\operatorname*{Res}_{s=\rho}H(s)=-m.
}
\tag{3}
\]

The apparent pole at `s=1` cancels between `-zeta'/zeta` and `-zeta`; the poles at the zeros remain.

Now restrict the source to a consecutive integer interval

\[
L,L+1,\ldots,U,
\qquad 3\le L<U.
\]

Let

\[
Q_{\mathrm{odd}}(L,U)
:=\#\{n\in[L,U]: n=p^k\text{ for an odd prime }p,\ k\ge1\}.
\tag{4}
\]

Then the ordered sign variation of the coefficient vector is exactly

\[
\boxed{
V(d_L,d_{L+1},\ldots,d_U)
=2Q_{\mathrm{odd}}(L,U)
-\mathbf 1_{\{L\text{ odd prime power}\}}
-\mathbf 1_{\{U\text{ odd prime power}\}}.
}
\tag{5}
\]

In particular, for every fixed `A>1`, taking `L=P` and `U=floor(AP)` gives

\[
\boxed{
V(d_P,\ldots,d_{\lfloor AP\rfloor})
=\bigl(2(A-1)+o(1)\bigr)\frac{P}{\log P}.
}
\tag{6}
\]

Therefore this canonical zero-sensitive source is **not** a bounded-sign-complexity source on escaping multiplicative windows. Any direct use of the AF-216 ordered-sign certificate on the raw window requires observation order

\[
\boxed{
r\ge V+1=\Theta(P/\log P).
}
\tag{7}
\]

Consequently, no fixed order `r` can certify the raw `Lambda-1` discrepancy on all sufficiently large multiplicative windows through the AF-216 gate. AF-338's fixed-order full-Euler transfer does not remove this obstruction: its hypothesis is useful only after a source has an order bounded independently of the escaping window.

This isolates a concrete tension that was previously only schematic in the Arithmetic Fidelity frontier:

\[
\boxed{
\text{canonical zero sensitivity}
\quad\not\Rightarrow\quad
\text{bounded ordered source complexity}.
}
\tag{8}
\]

The raw Mangoldt-minus-uniform source preserves the zero divisor extremely well, but it spends an unbounded number of source-order sign changes to do so.

## Derivation

### 1. The Dirichlet series is an exact zero-sensitive combination

For `Re(s)>1`, the classical logarithmic-derivative identity gives

\[
-\frac{\zeta'(s)}{\zeta(s)}
=\sum_{n\ge1}\frac{\Lambda(n)}{n^s},
\tag{9}
\]

while

\[
\zeta(s)-1
=\sum_{n\ge2}\frac1{n^s}.
\tag{10}
\]

Subtracting `(10)` from `(9)` proves `(2)`.

If `rho` is a zero of multiplicity `m`, write locally

\[
\zeta(s)=(s-\rho)^m g(s),
\qquad g(\rho)\ne0.
\]

Then

\[
\frac{\zeta'(s)}{\zeta(s)}
=\frac{m}{s-\rho}+\frac{g'(s)}{g(s)},
\tag{11}
\]

whereas `zeta(s)-1` is holomorphic at `rho`. Equation `(3)` follows.

At `s=1`, using

\[
\zeta(s)=\frac1{s-1}+\gamma+O(s-1)
\]

gives

\[
-\frac{\zeta'(s)}{\zeta(s)}
=\frac1{s-1}-\gamma+O(s-1),
\]

so the principal parts of `-zeta'/zeta` and `-zeta` cancel. This cancellation is not needed for the sign argument, but it makes the destination distinction clean: the meromorphic singularities retained by `H` are the zeta zeros rather than the pole at `1`.

### 2. The coefficient sign is exactly the odd-prime-power indicator

By definition,

\[
\Lambda(n)=
\begin{cases}
\log p,&n=p^k,\\
0,&\text{otherwise.}
\end{cases}
\tag{12}
\]

Hence

\[
d_n>0
\iff n=p^k\text{ with }p\ge3,
\tag{13}
\]

because `log 2<1<log 3`, while

\[
d_n<0
\]

for every non-prime-power and for every power of `2`. No coefficient vanishes.

Every positive coefficient therefore occurs at an **odd** integer. Its adjacent integers are even, and every even integer has negative coefficient: if it is a power of `2`, its coefficient is `log 2-1<0`; otherwise it is not a prime power and its coefficient is `-1`.

Thus every interior odd prime power contributes exactly the two sign-changing edges

\[
(n-1,n),\qquad(n,n+1).
\tag{14}
\]

Different positive sites cannot share either edge. An odd prime power at the left or right endpoint contributes only its single interior edge. Summing those contributions proves the exact formula `(5)`.

### 3. Prime powers have the same first-order counting scale as primes

Let

\[
Q_{\mathrm{odd}}(x)
:=\#\{p^k\le x:p\text{ odd prime},\ k\ge1\}.
\]

The terms with `k=1` contribute `pi(x)+O(1)`. The number of higher prime powers is bounded by

\[
\sum_{2\le k\le \log_2 x}x^{1/k}
=O(\sqrt{x}\log x),
\tag{15}
\]

so

\[
Q_{\mathrm{odd}}(x)
=\pi(x)+O(\sqrt{x}\log x).
\tag{16}
\]

For fixed `A>1`, the prime number theorem gives

\[
\pi(AP)-\pi(P)
=\bigl(A-1+o(1)\bigr)\frac{P}{\log P}.
\tag{17}
\]

Equations `(5)`, `(16)`, and `(17)` prove `(6)`.

The prime contribution alone already gives the lower bound of the same main order. Higher odd prime powers change only the lower-order term.

## Consequence for the AF-216 / AF-338 route

AF-216 proves that a nonzero signed source with at most `r-1` ordered sign changes cannot annihilate `r` equally spaced first-harmonic Dirichlet samples. Applied directly to the truncated vector

\[
(d_P,d_{P+1},\ldots,d_{\lfloor AP\rfloor}),
\]

its hypothesis can hold only when

\[
r\ge V+1.
\]

By `(6)`, that requested order diverges like `P/log P`. Therefore a **fixed-order** AF-216 detector is eventually outside its source-complexity hypothesis for every fixed multiplicative window ratio `A>1`.

AF-338 transfers every **fixed** requested order to the full Euler-log kernel on sufficiently remote integer windows under the sufficient depth condition `sigma>r-1`. It does not provide a theorem uniform in a growing order `r=r(P)`; its threshold `P_0` and constants depend on `r`. Therefore AF-339 does **not** extrapolate AF-338 to claim that `sigma` must grow like `P/log P`, nor does it claim that such a depth would be necessary.

What follows rigorously is narrower and more useful: the raw `Lambda-1` source does not solve AF-338's source-side requirement. To make this particular route scale, one must supply at least one genuinely new ingredient:

- a recoding or grouping that reduces **effective** ordered sign complexity while provably preserving the zero-sensitive destination;
- a growing-order sign-regularity theorem with the needed joint control in source scale and order; or
- a different source-complexity invariant whose finite certificate survives analytic continuation more efficiently than raw ordered sign variation.

The first option is exactly an Arithmetic Fidelity problem: compression is useful only if the pole/zero discriminator survives the compression that buys the simpler source geometry.

## Exact controls and boundaries

### This is not a statement that `Lambda-1` is maximally oscillatory

The support has `Theta(P)` integers but only `Theta(P/log P)` sign changes. Its sign variation is sparse relative to support size. The obstruction is specifically to **bounded absolute sign order**, not to every notion of low relative complexity.

### The obstruction is about the raw coefficient representation

A block sum, cumulative transform, summation by parts, wavelet-like regrouping, or another representation can have a different sign profile. AF-339 does not rule those out. Any such transform must be audited for whether `(2)`'s zero-sensitive meromorphic information can be recovered after the transformation.

### The zero-sensitive destination does not prove RH relevance by itself

Equation `(3)` says that the meromorphic continuation remembers the zeta zero divisor. It does not distinguish critical-line zeros from off-line zeros, prove positivity, or produce a Hilbert-Pólya mechanism. This is a destination-sensitivity statement only.

### Prime powers, not just primes, control the exact sign set

Ignoring higher prime powers gives the correct main asymptotic but not the exact sign sequence. The exact formula `(5)` uses all odd prime powers because `Lambda(p^k)=log p`.

### AF-338 remains a fixed-order theorem

The dependency `P_0=P_0(r,h,A,sigma)` matters. Combining `(6)` with the displayed sufficient inequality `sigma>r-1` is only a formal resource extrapolation unless one first proves uniform control as `r` grows with `P`. AF-339 deliberately does not make that extrapolation.

## Prior art and novelty assessment

No novelty claim is made for the constituent mathematics.

- The von Mangoldt identity `-zeta'/zeta=sum Lambda(n)n^{-s}`, its connection to prime powers, and the explicit-formula relation between `psi(x)=sum_{n<=x}Lambda(n)` and the zeta zeros are classical; see Titchmarsh, *The Theory of the Riemann Zeta-function*, 2nd ed., and Apostol's NIST DLMF Chapter 25 references.
- The prime number theorem and the fact that higher prime powers are lower-order in prime-power counting are classical.
- Karlin's total-positivity theory and its variation-diminishing consequences are the classical background for AF-216 and AF-338.

A targeted search for `Lambda(n)-1` and its sign changes did not identify a standard theorem organized in the form `(5)`--`(7)`. That absence is not used as a novelty claim: `(5)` is an elementary consequence of the definition of `Lambda`, and `(6)` is an immediate PNT corollary.

The durable contribution is the **composition** of these classical facts with the current Arithmetic Fidelity source-complexity program. It supplies a concrete, canonical counterexample to the hope that direct zero sensitivity and bounded ordered sign complexity arrive together for free.

## Consequence for Arithmetic Fidelity

The `Lambda-1` discrepancy is unusually diagnostic because the two desired resources can be seen on the same object without an arbitrary wrapper:

\[
\text{its Dirichlet transform remembers every zeta zero,}
\]

while

\[
\text{its ordered source sign budget diverges as }P/\log P.
\]

So the next useful question is no longer whether a zero-sensitive prime-derived source exists. One does. The sharper question is whether there is an **intrinsic compression of that source whose complexity drops while the zero-divisor information remains recoverable**.

That is precisely the kind of preserve-versus-forget boundary this line is meant to classify.