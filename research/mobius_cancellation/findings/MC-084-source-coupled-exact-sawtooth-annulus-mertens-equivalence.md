# MC-084 — The source-coupled exact sawtooth annulus is Mertens-equivalent above the critical exponent

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

The nonconstant reciprocal sawtooth weight left open by `MC-083` passes the basic parity/information-retention test, but its **complete source-prescribed coupling** does not define a weaker square-scale cancellation problem.

Retain the Huxley--Watt notation

\[
M(N)=\sum_{n\le N}\mu(n),
\qquad
H(N)=\sum_{n\le N}\frac{\mu(n)}n,
\]

and

\[
z(x):=-\psi(x)
=\left\lfloor x\right\rfloor+\frac12-x,
\qquad
\psi(x)=x-\lfloor x\rfloor-\frac12.
\]

Split the exact residual quadratic form into the product-hyperbola interior and annulus:

\[
I_N
:=
\sum_{\substack{m,n\le N\\mn\le N}}
\mu(m)\mu(n)
z\!\left(\frac{N^2}{mn}\right),
\tag{1}
\]

\[
W_N
:=
\sum_{\substack{m,n\le N\\mn>N}}
\mu(m)\mu(n)
z\!\left(\frac{N^2}{mn}\right).
\tag{2}
\]

Then

\[
\mathbf m^{\rm T}Z\mathbf m=I_N+W_N,
\tag{3}
\]

and the interior is universally cheap:

\[
\boxed{|I_N|=O(N\log N).}
\tag{4}
\]

Now form the **source-coupled annular residual**

\[
\boxed{
R_N
:=
N^2H(N)^2-\frac12M(N)^2+W_N.
}
\tag{5}
\]

The exact Huxley--Watt scale-doubling identity from `MC-020` immediately gives

\[
\boxed{
R_N
=
2M(N)-M(N^2)-I_N.
}
\tag{6}
\]

Consequently, for every fixed exponent `beta>1/2`,

\[
\boxed{
R_N=O(N^{2\beta})
\quad\Longleftrightarrow\quad
M(x)=O(x^\beta).
}
\tag{7}
\]

The converse direction in (7) needs no prior power saving for `M(N)`: the trivial bound `|M(N)|\le N`, together with (4), is already smaller than `N^{2\beta}` when `beta>1/2`. Control on square arguments then propagates to all real `x` because consecutive squares are only `O(\sqrt x)` apart.

At the critical endpoint the `O(N\log N)` interior prevents a fixed `beta=1/2` equivalence without logarithmic loss, but the usual epsilon family absorbs it:

\[
\boxed{
R_N=O_\varepsilon(N^{1+\varepsilon})
\text{ for every }\varepsilon>0
}
\]

is equivalent to

\[
\boxed{
M(x)=O_\varepsilon(x^{1/2+\varepsilon})
\text{ for every }\varepsilon>0.
}
\tag{8}
\]

Thus the full exact sawtooth annulus is genuinely nonconstant, but once it is kept with the two coarse counterterms forced by the same Huxley--Watt decomposition, a target-scale estimate for the coupled object is just the Mertens target at the doubled scale, modulo an elementary `O(N log N)` interior.

This closes one specific escape left open by `MC-020`, `MC-027`, and the narrowed clue `CLUE-parity-sensitive-annular-transfer`: **"do not separate the harmonic and sawtooth terms; estimate their complete signed coupling instead" is not by itself a weaker hypothesis.** A proof may of course establish (5) from genuinely new arithmetic input, but the bound on (5) cannot itself be credited as an independently cheaper input.

The result does **not** show that `W_N` alone is Mertens-equivalent, and it does not kill proper finite Fourier truncations or other strict partial projections of the annulus. Those remain viable only if their estimates are independently available and the truncation/recombination needed to recover the full source residual does not reintroduce (8).

## 1. The exact sawtooth interior is already below every supercritical square scale

Because `z(x)=-psi(x)` and `|psi(x)|\le 1/2`,

\[
|I_N|
\le
\frac12
\sum_{\substack{m,n\le N\\mn\le N}}1.
\tag{9}
\]

The number of ordered pairs with `mn<=N` is

\[
\sum_{m\le N}\left\lfloor\frac Nm\right\rfloor
=O(N\log N),
\tag{10}
\]

so (4) follows without using a Möbius sign, a zero-free region, or any cancellation theorem.

This is the exact-sawtooth analogue of the cheap Fourier interior in `MC-032`. No Fourier truncation is required: the bounded source kernel itself makes the whole low-product part negligible at every scale `N^{1+\varepsilon}`.

## 2. Annular localization of the source-coupled residual

For `g=1`, Huxley and Watt give

\[
M(N^2)
=
2M(N)
-
N^2H(N)^2
+
\frac12M(N)^2
-
\mathbf m^{\rm T}Z\mathbf m.
\tag{11}
\]

Insert (3) and rearrange:

\[
N^2H(N)^2
-\frac12M(N)^2
+W_N
=
2M(N)-M(N^2)-I_N,
\tag{12}
\]

which is exactly (6).

The point is not the algebraic rearrangement by itself. `MC-020` identified signed cancellation between the RH-equivalent harmonic coarse mode and the sawtooth residual as a possible escape from separate absolute-value bounds. Equations (4) and (12) audit that escape after the hard residual has been localized to the annulus: once the complete source counterterms are retained, the annular coupled observable carries the doubled Mertens value essentially verbatim.

The only discarded part is `I_N`, and (4) proves that this discarded part is already harmless at every exponent strictly above `1/2`.

## 3. Fixed-exponent equivalence for every beta above one half

Assume first that

\[
M(x)=O(x^\beta),
\qquad \beta>\frac12.
\tag{13}
\]

Then (6) gives

\[
|R_N|
\le
2|M(N)|
+
|M(N^2)|
+
|I_N|.
\tag{14}
\]

The three terms are respectively

\[
O(N^\beta),\qquad
O(N^{2\beta}),\qquad
O(N\log N),
\]

and the latter two dominate because `2 beta>1`. Hence

\[
R_N=O(N^{2\beta}).
\tag{15}
\]

Conversely, suppose

\[
R_N=O(N^{2\beta})
\qquad(\beta>1/2).
\tag{16}
\]

Equation (6), the trivial estimate `|M(N)|<=N`, and (4) imply

\[
M(N^2)
=
O(N^{2\beta})+O(N)+O(N\log N)
=
O(N^{2\beta}).
\tag{17}
\]

Now let `N=floor(sqrt(x))`. Then

\[
N^2\le x<(N+1)^2
\]

and, since each increment of `M` has absolute value at most one,

\[
|M(x)-M(N^2)|
\le
x-N^2
\le
2N+1.
\tag{18}
\]

Using (17),

\[
M(x)
=
O(N^{2\beta})+O(N)
=
O(x^\beta),
\tag{19}
\]

because `beta>1/2`. This proves (7).

The square-scale formulation is therefore not a weaker subsequence criterion above the critical exponent. The gaps between consecutive squares are already small enough for the trivial Lipschitz bound on `M` to fill them.

## 4. The RH epsilon family is equivalent as well

Suppose first that the standard Mertens consequence of RH holds:

\[
M(x)=O_\delta(x^{1/2+\delta})
\quad\text{for every }\delta>0.
\tag{20}
\]

Given `epsilon>0`, apply (7)-style bookkeeping with `delta=epsilon/2` at the square horizon. Equation (6) and (4) give

\[
R_N=O_\varepsilon(N^{1+\varepsilon}).
\tag{21}
\]

Conversely, assume (21) for every positive `epsilon`. Given a target `delta>0`, use (21) with `epsilon=2delta`. Equations (6), (4), and the trivial lower-scale bound yield

\[
M(N^2)=O_\delta(N^{1+2\delta}).
\tag{22}
\]

Equation (18) then fills the intervals between consecutive squares and gives

\[
M(x)=O_\delta(x^{1/2+\delta}).
\tag{23}
\]

Thus (8) follows. At the literal fixed endpoint `R_N=O(N)`, the interior estimate (4) would only give `M(N^2)=O(N log N)` by this argument, so no stronger endpoint statement is being smuggled into the result.

## 5. Physical-space form of the exact nonconstant weight

The full sawtooth annulus also has an exact reciprocal-slab decomposition. For `1<=k<=N-1`, put

\[
\mathcal A_k
:=
\left\{
(m,n):
m,n\le N,\ 
\frac{N^2}{k+1}<mn\le\frac{N^2}{k}
\right\}.
\tag{24}
\]

These slabs partition `mn>N`, and on `mathcal A_k` one has

\[
\left\lfloor\frac{N^2}{mn}\right\rfloor=k.
\]

Therefore

\[
z\!\left(\frac{N^2}{mn}\right)
=
k+\frac12-\frac{N^2}{mn}
\qquad ((m,n)\in\mathcal A_k).
\tag{25}
\]

If

\[
U_k:=\sum_{(m,n)\in\mathcal A_k}\mu(m)\mu(n),
\qquad
V_k:=\sum_{(m,n)\in\mathcal A_k}\frac{\mu(m)\mu(n)}{mn},
\tag{26}
\]

then exactly

\[
\boxed{
W_N
=
\sum_{k=1}^{N-1}
\left(
\left(k+\frac12\right)U_k-N^2V_k
\right).
}
\tag{27}
\]

So the **complete** source sawtooth is piecewise affine in the reciprocal product. Its Fourier representation is useful for partial approximations, but after all frequencies are recombined the physical-space carrier is the floor-slab object (27), not an additional independent frequency observable.

Equation (27) does not make the slab sums easy: the product masks couple the factor coordinates, and neither `U_k` nor `V_k` is estimated nontrivially here. Its role is a representation audit. A surviving Fourier mechanism must exploit a proper partial family before recombination; it cannot cite the mere existence of many Fourier modes as new information once their full sum has returned to (25).

## 6. Prior art and novelty boundary

The parent identity (11), the matrix `Z`, the sawtooth convention, and the Fourier representation of that residual are prior art from M. N. Huxley and N. Watt, *Mertens Sums requiring Fewer Values of the Möbius function* (`MC-S24`). The source already presents

\[
Z_{mn}=-\psi(N^2/(mn))
\]

and discusses Fourier truncation of this kernel.

The decomposition of a floor/sawtooth function into regions of constant floor, the divisor-hyperbola count in (10), and the interpolation from perfect squares in (18) are elementary classical mechanisms. A targeted literature check around the Huxley--Watt Mertens identity, its sawtooth residual, and Fourier treatment found the source formulation but no reason to assert a new number-theoretic theorem here. No novelty claim is made.

The durable contribution is the line-specific **independence audit** demanded by the current clue: after `MC-083` kills the constant-weight annulus, (6)--(8) show that the opposite extreme—the complete exact nonconstant sawtooth together with all source-prescribed coarse counterterms—also fails as an independently weaker carrier. One extreme discards too much weighting and recovers `M(N)^2`; the other keeps the complete source coupling and recovers `M(N^2)`.

## 7. Boundaries and decisive continuation

This finding does not prove any useful estimate for `W_N`, `U_k`, `V_k`, or an individual Fourier mode. It does not show that reciprocal-phase cancellation is impossible.

Its obstruction applies to the **complete exact sawtooth annulus with the exact Huxley--Watt coarse counterterms**. A proper finite Fourier truncation

\[
\sum_{h\le H}\frac{Q_h(N)}{\pi h},
\qquad H<N,
\]

is not equal to `W_N` and is not classified by (7). `MC-031` gives the source truncation budget such a route must still pay, while `MC-032`--`MC-033` identify the annular coefficient and its sign-coherent product fibers.

Accordingly, the annular clue survives only in a stricter form. A candidate must select a **strict partial** source-forced statistic—such as a finite Fourier family, a justified proper slab subfamily, or another nonconstant coupling—whose estimate is independently available below the Mertens burden. It must then prove that the omitted/recombination error is compatible with the desired iteration in `MC-027`.

A candidate is killed if its decisive estimate is merely a bound for `R_N`, or if completing its partial statistic to the exact sawtooth necessarily demands the same `O_\varepsilon(N^{1+\varepsilon})` estimate for `R_N`. Equations (6)--(8) show that this is exactly the target Mertens problem.

## Consequence for the research line

`MC-083` showed that the constant-weight parity annulus is too close to the target: it is `M(N)^2` modulo a cheap hyperbola interior. The present finding shows that retaining the **entire** exact sawtooth and its source-prescribed coarse coupling is also too close to the target: it is `-M(N^2)` modulo lower-scale and cheap interior terms.

The viable window is therefore genuinely intermediate. The next useful attack must extract a strict partial, nonconstant, parity-sensitive annular statistic before full sawtooth recombination, and it must come with an arithmetic estimate that is independently weaker than the Mertens conclusion. The finite Fourier family remains the clearest source-forced candidate, but only if its truncation and scale-iteration ledgers close without recreating `R_N`.
