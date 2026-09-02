# MC-021 — The Huxley–Watt `g(n)=1/n` endpoint centers to a bounded bilinear kernel

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CANDIDATE-NEW-STRUCTURE`, `NO-NOVELTY-CLAIM`.

## Claim

The `g(n)=1/n` endpoint suggested in `MC-020` has a sharper structure than the unweighted `g=1` decomposition. After centering the harmonic-number kernel at the pole of zeta, the explicit linear coarse term cancels against the classical logarithmic-derivative constant and the entire unresolved square-scale transfer is concentrated in one bounded bilinear kernel.

Write

\[
H(N)=\sum_{n\le N}\frac{\mu(n)}n,
\qquad
J(N)=\sum_{n\le N}\frac{\mu(n)\log n}{n}.
\tag{1}
\]

For `y>=1`, define

\[
\kappa(y)
:=y\left(
H_{\lfloor y\rfloor}^{(1)}-\log y-\gamma
\right),
\qquad
H_q^{(1)}=\sum_{k=1}^q\frac1k,
\tag{2}
\]

and the Möbius bilinear form

\[
B(N)
:=\sum_{m,n\le N}
\mu(m)\mu(n)
\kappa\!\left(\frac{N^2}{mn}\right).
\tag{3}
\]

Then the Huxley–Watt scale-doubling identity specialized to `g(n)=1/n` gives the exact formula

\[
\boxed{
H(N^2)
=2H(N)(1+J(N))
-(2\log N+\gamma)H(N)^2
-\frac{B(N)}{N^2}.
}
\tag{4}
\]

The kernel `\kappa` is uniformly bounded on `[1,infinity)`. An elementary bound is

\[
|\kappa(y)|\le 4.
\tag{5}
\]

Thus the direct absolute estimate gives only `B(N)=O(N^2)`, whereas RH implies and is compatible with the much sharper scale

\[
B(N)=O_\varepsilon(N^{1+\varepsilon}).
\tag{6}
\]

Equation (6) is therefore a concrete cancellation target: after division by `N^2`, it has exactly the `N^{-1+\varepsilon}` size required for `H(N^2)` at the RH boundary. Unlike the rank-one harmonic mode isolated in `MC-020`, `B(N)` is not being assumed through an already RH-equivalent one-dimensional coefficient; it is a signed quadratic form with a bounded product kernel.

There is an important qualification. A bound such as (6) by itself does **not** prove RH from the currently known subpolynomial bounds for `H` and `J+1`: the first two terms in (4) still have to be controlled at a compatible polynomial scale. What (4) supplies is a precise square-scale closure interface. If at scale `N` one already has

\[
H(N)=O_\varepsilon(N^{-1/2+\varepsilon}),
\qquad
1+J(N)=O_\varepsilon(N^{-1/2+\varepsilon}),
\tag{7}
\]

then (6) propagates the same critical exponent to scale `N^2`.

The residual question is therefore narrower than the endpoint suggestion in `MC-020`: **can the bounded bilinear form `B(N)` be controlled at essentially square-root scale from arithmetic information that is genuinely weaker than RH, and can such control be coupled to a non-circular multiscale estimate for the two centered coefficients in (7)?**

## 1. Exact endpoint specialization

Huxley and Watt prove for every totally multiplicative `g` the identity

\[
M(g,N^2)
=2M(g,N)-\mathbf m_g^{\rm T}A_g\mathbf m_g,
\tag{8}
\]

where

\[
M(g,X)=\sum_{n\le X}\mu(n)g(n),
\quad
(\mathbf m_g)_n=\mu(n)g(n),
\quad
(A_g)_{mn}=\sum_{k\le N^2/(mn)}g(k).
\tag{9}
\]

Take `g(n)=1/n`. Then `M(g,X)=H(X)` and

\[
(A_g)_{mn}
=H_{\lfloor N^2/(mn)\rfloor}^{(1)}.
\tag{10}
\]

Put

\[
y_{mn}=\frac{N^2}{mn}.
\]

By definition of `\kappa`,

\[
H_{\lfloor y_{mn}\rfloor}^{(1)}
=\log y_{mn}+\gamma+\frac{\kappa(y_{mn})}{y_{mn}}.
\tag{11}
\]

Since

\[
\log y_{mn}=2\log N-\log m-\log n,
\tag{12}
\]

the quadratic form in (8) is

\[
\begin{aligned}
\mathbf m_g^{\rm T}A_g\mathbf m_g
&=\sum_{m,n\le N}\frac{\mu(m)\mu(n)}{mn}
H_{\lfloor y_{mn}\rfloor}^{(1)}\\
&=(2\log N+\gamma)H(N)^2
-2H(N)J(N)
+\frac{B(N)}{N^2}.
\end{aligned}
\tag{13}
\]

The last term follows exactly from `1/y_{mn}=mn/N^2`. Substituting (13) into (8) gives

\[
H(N^2)
=2H(N)
-(2\log N+\gamma)H(N)^2
+2H(N)J(N)
-\frac{B(N)}{N^2},
\]

which is (4).

This is not an asymptotic expansion: the floor in the inner harmonic number is retained exactly inside `\kappa`.

## 2. Why the apparent linear instability cancels

The finite coefficient `J(N)` is naturally centered at `-1`. For `Re(s)>1`,

\[
\frac1{\zeta(s)}
=\sum_{n\ge1}\frac{\mu(n)}{n^s},
\qquad
\left(\frac1{\zeta(s)}\right)'
=-\sum_{n\ge1}\frac{\mu(n)\log n}{n^s}.
\tag{14}
\]

Since zeta has a simple pole of residue `1` at `s=1`,

\[
\frac1{\zeta(s)}=(s-1)+O((s-1)^2),
\tag{15}
\]

so the boundary derivative equals `1`. The classical unconditional zero-free-region bound for the Mertens function is strong enough to make

\[
\sum_{n\ge1}\frac{\mu(n)\log n}{n}
\tag{16}
\]

converge in the ordinary sense; Abel/partial summation then identifies its value as

\[
\boxed{
\sum_{n\ge1}\frac{\mu(n)\log n}{n}=-1.
}
\tag{17}
\]

Hence `1+J(N)` is a genuine tail coefficient tending to zero, and the first two terms `2H(N)+2H(N)J(N)` in the raw endpoint recursion combine exactly into

\[
2H(N)(1+J(N)).
\tag{18}
\]

This cancellation is the structural difference between the endpoint `g(n)=1/n` and the first natural `g=1` decomposition in `MC-020`. The endpoint does not simply replace one RH-equivalent coarse scalar by another linear scalar: the coefficient of the linear term is centered by the derivative of `1/zeta` at its zero at `s=1`.

The cancellation is nevertheless not itself an RH gain. Unconditionally, the known zero-free region gives only subpolynomial decay for both `H(N)` and `1+J(N)`. Their product is smaller than either factor but is not automatically `N^{-1+epsilon}`.

## 3. The centered kernel is uniformly bounded

Let `q=floor(y)`. The classical integral comparison for harmonic numbers gives

\[
0< H_q^{(1)}-\log q-\gamma < \frac1q.
\tag{19}
\]

Also, because `q<=y<q+1`,

\[
|\log q-\log y|
=\log(y/q)
\le \frac{y-q}{q}
<\frac1q.
\tag{20}
\]

Therefore

\[
\left|
H_q^{(1)}-\log y-\gamma
\right|<\frac2q.
\tag{21}
\]

For `y>=1`, `q=floor(y)>=y/2`, so multiplying by `y` yields (5).

Consequently,

\[
|B(N)|
\le 4\left(\sum_{n\le N}|\mu(n)|\right)^2
=O(N^2).
\tag{22}
\]

This reproduces the same one-full-factor loss that appeared for the unweighted fractional-part residual in `MC-020`: the target (6) requires cancellation of order `N` beyond the direct absolute budget.

But the information carrier is different. The factor `1/(mn)` from `g=1/n` is exactly cancelled by the `1/y_{mn}` scale of the centered harmonic remainder, leaving a **bounded** kernel on the original Möbius signs:

\[
\frac{\mu(m)\mu(n)}{mn}
\left(H_{\lfloor y\rfloor}^{(1)}-\log y-\gamma\right)
=\frac{\mu(m)\mu(n)}{N^2}\kappa(y).
\tag{23}
\]

Thus the endpoint isolates a normalized two-dimensional sign-cancellation problem rather than an unbounded reciprocal-weight mode.

## 4. Critical-scale compatibility

Under RH, the classical Mertens criterion gives

\[
M(x)=O_\varepsilon(x^{1/2+\varepsilon}).
\tag{24}
\]

Partial summation then yields

\[
H(N)=O_\varepsilon(N^{-1/2+\varepsilon})
\tag{25}
\]

and, using (17),

\[
1+J(N)=O_\varepsilon(N^{-1/2+\varepsilon}\log N).
\tag{26}
\]

Equations (25)--(26) make the two explicit terms in (4) `O_epsilon(N^{-1+epsilon})` after relabelling epsilon. Since the left side has the RH scale

\[
H(N^2)=O_\varepsilon(N^{-1+\varepsilon}),
\tag{27}
\]

(4) also gives the necessary RH consequence

\[
B(N)=O_\varepsilon(N^{1+\varepsilon}).
\tag{28}
\]

Conversely, at a single scale, (4) shows directly that (7) together with (28) implies (27). This is the precise sense in which `B(N)` is a square-scale closure target.

The statement is deliberately not upgraded to an equivalence `B bound <=> RH`. With only currently known unconditional decay for `H` and `J+1`, (28) does not force the two explicit terms of (4) down to polynomial critical size. A viable bootstrap must therefore control the centered coefficients and the bilinear residual as a coupled system rather than prove (28) in isolation.

## 5. Prior art and novelty boundary

The parent identity (8)--(9) is prior art: M. N. Huxley and N. Watt, *Mertens Sums requiring Fewer Values of the Möbius function*, Chebyshevskii Sbornik 19(3) (2018), 20--34, DOI `10.22405/2226-8383-2018-19-3-20-34`, arXiv `1807.05890`. Their theorem explicitly permits arbitrary totally multiplicative `g`; the paper's detailed matrix analysis concentrates on `g=1`.

Nigel Watt subsequently studied the unweighted residual kernel

\[
\frac12+\left\lfloor\frac1{xy}\right\rfloor-\frac1{xy}
\]

and its eigenvalues in *On eigenvalues of the kernel ...*, Journal de Theorie des Nombres de Bordeaux 31 (2019), 653--662, DOI `10.5802/jtnb.1099`, with related arXiv work `1812.01039`. That is direct adjacent prior art for the idea that the Huxley--Watt residual quadratic form may carry nontrivial signed spectral information, but it is the `g=1` fractional-part kernel, not the centered `g=1/n` harmonic kernel (2).

The harmonic-number asymptotic, the Laurent expansion of zeta at `1`, the derivative of `1/zeta`, and partial summation are classical. No novelty is claimed for any of them individually, and no novelty is claimed for the bare specialization `g(n)=1/n`, which is immediate from the general Huxley--Watt theorem.

A targeted search for Huxley--Watt together with `g(n)=1/n`, harmonic-number kernels, and weighted Mertens sums found the general 2018 identity and Watt's unweighted-kernel program, but no authoritative source explicitly presenting the centered formula (4) or the bounded kernel (2) as a square-scale cancellation interface. This negative search is not evidence of novelty; the status therefore remains `NO-NOVELTY-CLAIM`.

The durable contribution is the exact information audit: the endpoint suggested but not developed in `MC-020` has a nontrivial centering cancellation, and after that cancellation its unresolved part is a normalized bounded bilinear form with an explicit `O(N^{1+epsilon})` critical target.

## 6. Boundaries and decisive continuation

The kernel `\kappa(N^2/(mn))` depends on the product `mn` and has floor-induced jumps. Standard fixed-shift Chowla estimates do not directly control (3), and `MC-006` already warns against converting averaged correlation information into a polynomial global gain without auditing the exceptional/coarse contribution.

Likewise, an operator-norm or entrywise estimate that discards the Möbius signs returns only (22) and loses the required factor `N`. A successful estimate must preserve the bilinear sign coupling.

The next decisive tests are therefore concrete:

- determine whether existing bilinear-form, hyperbola, Type I/II, or multiplicative-correlation technology can prove any fixed power saving for `B(N)` beyond `N^2`, and identify the exact barrier to the critical `N^{1+epsilon}` scale;
- test whether `B(N)` admits a decomposition into ranges where known Möbius cancellation is genuinely effective without recreating an RH-equivalent coarse coefficient;
- derive the `g(n)=n^{-s}` family near `s=1` and determine whether differentiating the scale-doubling identity supplies a closed multiscale system for `H(N)` and the centered coefficient `1+J(N)`, or merely generates an infinite hierarchy of equally hard derivative moments;
- construct matched multiplicative controls for any proposed bilinear estimate before interpreting bounded-kernel cancellation as rational-prime-specific.

This endpoint therefore survives `MC-020`'s first negative audit as a narrower candidate mechanism: **not because the Huxley--Watt identity itself proves more cancellation, but because at `g=1/n` the zeta-pole centering removes the raw linear coarse mode and exposes a bounded, cancellation-sensitive bilinear residue that can be attacked independently.**