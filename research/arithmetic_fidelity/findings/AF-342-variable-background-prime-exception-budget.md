# AF-342 — variable backgrounds must spend prime-scale exceptions to reduce sign complexity

**Status:** `EXACT-DERIVED`, `CLASSICAL-BRIDGE`, `ARITHMETIC-FIDELITY`, `ZERO-SENSITIVE-SOURCE`, `SOURCE-COMPLEXITY-GATE`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-340 classifies constant backgrounds and AF-341 shows that deleting all higher prime-power layers leaves both the RH right-half-plane pole discriminator and the leading `P/log P` source sign complexity in the ordinary-prime layer. The remaining obvious escape is therefore to subtract a **nonconstant** background from that prime layer.

There is an exact combinatorial obstruction to doing this cheaply.

Let

\[
a(n):=
\begin{cases}
\log p,&n=p\text{ is prime},\\
0,&\text{otherwise},
\end{cases}
\]

and let `b(n)` be an arbitrary real sequence. Define the residual

\[
h_b(n):=a(n)-b(n).
\tag{1}
\]

For an integer interval `[L,U]` with `5\le L<U`, let

\[
N(L,U):=\pi(U)-\pi(L-1)
\tag{2}
\]

be its number of primes. Introduce two exceptional sets:

\[
E_b(L,U)
:=\{p\in[L,U]:p\text{ prime and }b(p)\ge\log p\},
\tag{3}
\]

and

\[
C_b(L,U)
:=\left\{\begin{array}{l|l}
m\in[L-1,U+1]&
\begin{array}{l}
m\text{ composite},\ b(m)\le0,\\
\text{and }|m-p|=1\text{ for some prime }p\in[L,U]
\end{array}
\end{array}\right\}.
\tag{4}
\]

Using the AF-216 convention that zero coefficients are deleted before ordered sign changes are counted, one has the exact lower bound

\[
\boxed{
V\bigl(h_b(L),\ldots,h_b(U)\bigr)
\ge
2N(L,U)-2|E_b(L,U)|-4|C_b(L,U)|-4.
}
\tag{5}
\]

Consequently, for every fixed `B>1`, with `U=\lfloor BP\rfloor`, the prime number theorem gives

\[
\boxed{
V\bigl(h_b(P),\ldots,h_b(U)\bigr)
\ge
2(B-1+o(1))\frac{P}{\log P}
-2|E_b(P,U)|-4|C_b(P,U)|.
}
\tag{6}
\]

In particular, if

\[
|E_b(P,U)|+2|C_b(P,U)|=o\!\left(\frac{P}{\log P}\right),
\tag{7}
\]

then

\[
\boxed{
V\bigl(h_b(P),\ldots,h_b(U)\bigr)
\ge
\bigl(2(B-1)+o(1)\bigr)\frac{P}{\log P}.
}
\tag{8}
\]

Conversely, sub-prime-scale sign complexity

\[
V\bigl(h_b(P),\ldots,h_b(U)\bigr)
=o\!\left(\frac{P}{\log P}\right)
\tag{9}
\]

forces

\[
\boxed{
|E_b(P,U)|+2|C_b(P,U)|
\ge
(1-o(1))\bigl(\pi(U)-\pi(P-1)\bigr).
}
\tag{10}
\]

Thus a variable background cannot suppress the leading prime-layer sign burden merely by being nonconstant. On a prime-scale set it must do at least one of two things:

1. rise to prime height, `b(p)\ge\log p`, at actual primes; or
2. become nonpositive at composite neighbors of actual primes, preventing the isolated positive prime spike from being bracketed by negative residuals.

The information has not disappeared. It has been transferred into a **prime-scale exceptional structure of the background**.

A particularly clean corollary covers every eventually positive, sub-prime-height background. If for all sufficiently large integers

\[
b(n)>0
\tag{11}
\]

and for all sufficiently large primes

\[
b(p)<\log p,
\tag{12}
\]

then on every fixed multiplicative window

\[
\boxed{
V\bigl(h_b(P),\ldots,h_b(\lfloor BP\rfloor)\bigr)
=
\bigl(2(B-1)+o(1)\bigr)\frac{P}{\log P}.
}
\tag{13}
\]

This strictly contains the positive-constant backgrounds of AF-340 and the uniform background `b\equiv1` used in AF-341.

There is also a direct analytic-fidelity specialization. Suppose

\[
B_b(s):=\sum_{n\ge2}b(n)n^{-s}
\tag{14}
\]

converges for `Re(s)>1` and extends meromorphically to `Re(s)>1/2`, with a simple pole of residue `+1` at `s=1` and no other poles in that open half-plane. Then, with the prime-layer transform `A(s)` from AF-341,

\[
H_b(s):=A(s)-B_b(s)
\tag{15}
\]

is meromorphic on `Re(s)>1/2`, is holomorphic at `s=1`, and has residue `-m` at every zeta zero `rho` with `Re(rho)>1/2` and multiplicity `m`. Hence

\[
\boxed{
\mathrm{RH}
\iff
H_b\text{ is holomorphic on }\Re(s)>\tfrac12.
}
\tag{16}
\]

Within this broad class of pole-cancelling but zero-pole-blind backgrounds, `(5)`--`(10)` give a source-side price for reducing the residual sign complexity: **if the residual is much simpler than the centered prime layer, the baseline itself must acquire prime-scale exceptional behavior.**

## Derivation

### 1. Every nonexceptional interior prime contributes two sign changes

Take a prime `p\in[L+1,U-1]`. Since `p\ge5`, both `p-1` and `p+1` are even integers greater than `2`, hence composite.

If `p\notin E_b(L,U)`, then

\[
h_b(p)=\log p-b(p)>0.
\tag{17}
\]

If neither neighbor belongs to `C_b(L,U)`, then by the definition of `C_b`

\[
b(p-1)>0,
\qquad
b(p+1)>0,
\]

and because the neighbors are composite,

\[
h_b(p-1)=-b(p-1)<0,
\qquad
h_b(p+1)=-b(p+1)<0.
\tag{18}
\]

So every such prime appears in the local sign pattern

\[
-\quad+\quad-
\]

and contributes the two distinct sign-changing edges `(p-1,p)` and `(p,p+1)`.

These contributions survive the AF-216 zero-deletion convention because the three displayed coefficients are all nonzero. Moreover, no edge can be counted for two different primes: above `2`, two primes cannot be consecutive integers.

### 2. Exceptional sites can shield only boundedly many prime spikes

An interior prime fails the previous argument only if it lies in `E_b`, or one of its two composite neighbors lies in `C_b`. Each composite integer can neighbor at most two primes. Therefore the number of interior primes not certified to contribute two sign changes is at most

\[
|E_b(L,U)|+2|C_b(L,U)|.
\tag{19}
\]

At most two further primes can occur at the interval endpoints. Hence at least

\[
N(L,U)-|E_b(L,U)|-2|C_b(L,U)|-2
\tag{20}
\]

primes contribute two distinct sign-changing edges. Multiplying `(20)` by two proves `(5)`; when the right-hand side is negative, the bound is of course merely vacuous.

### 3. Prime-scale asymptotics

For fixed `B>1`, the prime number theorem gives

\[
\pi(BP)-\pi(P)
=
\bigl(B-1+o(1)\bigr)\frac{P}{\log P}.
\tag{21}
\]

Endpoint rounding changes only `O(1)`, so `(5)` yields `(6)`. Condition `(7)` then gives `(8)`.

Conversely, combining `(6)` with `(9)` and dividing by two gives `(10)`. Thus any variable baseline that reduces the residual below prime-scale ordered variation must pay for an exceptional set comparable in size to the primes themselves.

### 4. Eventually positive, sub-prime-height baselines retain the exact leading pattern

Under `(11)`--`(12)`, for all sufficiently large `n`,

\[
h_b(n)>0\iff n\text{ is prime},
\tag{22}
\]

because prime coefficients satisfy `log p-b(p)>0`, while every composite coefficient equals `-b(n)<0`.

Therefore, apart from endpoint effects, every prime contributes exactly two sign changes and no composite-composite edge contributes one. This gives

\[
V\bigl(h_b(P),\ldots,h_b(\lfloor BP\rfloor)\bigr)
=2\bigl(\pi(\lfloor BP\rfloor)-\pi(P-1)\bigr)+O(1),
\tag{23}
\]

and `(13)` follows from the prime number theorem.

### 5. Pole-cancelling zero-pole-blind backgrounds preserve the RH discriminator

AF-341 proves that

\[
A(s)=\sum_p(\log p)p^{-s}
\tag{24}
\]

extends meromorphically to `Re(s)>1/2`, has residue `+1` at `s=1`, and has residue `-m` at every zeta zero `rho` in that half-plane, where `m` is the multiplicity.

By hypothesis, `B_b` has the same residue `+1` at `s=1` and is holomorphic at every other point of `Re(s)>1/2`. Thus `H_b=A-B_b` is holomorphic at `1`, while no zeta-zero pole of `A` can be cancelled by `B_b`. This proves the stated residue claim.

There are no other poles of `A` in the open half-plane. Therefore `H_b` is holomorphic there exactly when zeta has no zero with real part greater than `1/2`. By the functional-equation symmetry of nontrivial zeros, this is equivalent to RH, proving `(16)`.

## Consequence for the AF-339--AF-341 frontier

AF-340 leaves a nonconstant or multiscale background as the simplest untested repair of the centered-source obstruction. AF-342 shows that **nonconstancy alone does not buy anything**. If the background remains positive at almost every prime-adjacent composite and remains below `log p` at almost every prime, the full `P/log P` sign burden survives.

To lower that burden materially, the baseline must track the arithmetic source at prime-scale resolution: it must either neutralize a positive proportion of prime spikes at the prime sites themselves or alter a prime-scale collection of their neighboring composite sites. This is a source-side information-conservation statement in the particular currency consumed by AF-216.

The next useful question is therefore sharper than "try a varying baseline." One must exhibit a canonical nonconstant transform whose exceptional structure is generated by genuinely cheaper retained data, or prove recoverability of the zero discriminator from a different source-complexity certificate. Merely moving the prime indicator from the residual into the baseline is not a compression.

## Exact controls and boundaries

### The theorem prices ordered sign complexity, not every notion of source complexity

A background may have a compact formula while possessing many exceptional sites, or may permit another downstream theorem that does not consume ordered sign variation. Equations `(5)`--`(10)` say only that the AF-216 sign currency cannot be reduced without prime-scale baseline exceptions.

### Exceptional-set cardinality is not an information-theoretic lower bound

The result counts where the background must behave differently; it does not prove a bit-complexity, Kolmogorov-complexity, entropy, or circuit lower bound for describing those sites. A highly structured rule could in principle generate them cheaply in another representation.

### The analytic hypothesis forbids hiding the zero divisor in the background

The condition that `B_b` be holomorphic away from `s=1` in `Re(s)>1/2` is essential. The matched control

\[
b(n)=\Lambda(n)
\]

shows why. Then

\[
A(s)-B_b(s)=-R(s),
\]

with `R` the higher-prime-power tail from AF-341, so the residual transform is holomorphic on `Re(s)>1/2` and has lost every zeta-zero pole there. The source may become sign-simple only because the background itself has absorbed the zero-sensitive singularities. Such a transfer is not fidelity-preserving for the residual discriminator addressed here.

### The exceptional cover is deliberately local and sufficient, not claimed minimal

The weights `1` on `E_b` and `2` on `C_b` arise because one exceptional composite can shield at most two neighboring primes. Another exact accounting may sharpen lower-order constants or exploit longer-range structure. The durable conclusion is the prime-scale necessity in `(10)`, not optimality of this particular cover functional.

### This does not create a growing-order theorem for AF-338

As in AF-339--AF-341, the `P/log P` source variation cannot be substituted into AF-338's fixed-order sufficient sign-regularity theorem to infer a necessary observation depth of the same order. AF-342 narrows the source recoding problem only; the growing-order observation question remains separate.

## Prior art and novelty assessment

No novelty claim is made for the constituent number theory.

- The prime number theorem and the isolation of every sufficiently large prime between composite even neighbors are classical.
- The analytic continuation and pole structure of the prime-only Dirichlet series used in `(24)` are exactly the classical bridge already audited in AF-341 through the logarithmic derivative of zeta and the holomorphic higher-prime-power tail; Titchmarsh, *The Theory of the Riemann Zeta-function*, is a standard reference.
- A targeted search for sign-change lower bounds for `a(n)-b(n)` organized by variable-background exceptional prime sites and prime-adjacent composite sites did not identify a standard theorem in this exact form. That search failure is not evidence of novelty, and the result is classified only as an elementary exact consequence of the prime sign geometry plus the prime number theorem.

The Arithmetic Fidelity contribution is the **resource accounting** against the live AF-340/AF-341 escape route: lowering the ordered sign complexity of a zero-sensitive prime-layer residual forces the proposed background itself to acquire prime-scale exceptional structure. This turns "use a nonconstant baseline" from a broad escape hatch into a falsifiable requirement on where the retained arithmetic provenance must go.