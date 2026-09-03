# MC-036 — Every fixed Mellin character of the Huxley–Watt annulus carries an RH-equivalent square-scale burden

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `NEGATIVE/BOUNDARY`, `RH-EQUIVALENT-BOUNDARY`, `CLASSICAL-MECHANISM`, `NO-NOVELTY-CLAIM`.

## Claim

The log-radial continuation left open by `MC-035` has a stronger scalar obstruction than the zero-frequency case alone suggests. For **every fixed real Mellin frequency** `tau`, the corresponding character of the exact Huxley–Watt product annulus already carries an RH-equivalent critical-scale estimate.

Let

\[
F_\tau(N):=\sum_{n\le N}\mu(n)n^{-i\tau},
\qquad
G_\tau(N):=\sum_{q\le N}(\mu*\mu)(q)q^{-i\tau},
\tag{1}
\]

and retain the finite-cutoff product coefficient from `MC-032`–`MC-035`,

\[
c_N(q):=\sum_{\substack{mn=q\\m,n\le N}}\mu(m)\mu(n).
\tag{2}
\]

For the fixed Mellin character of the annulus define

\[
T_\tau(N)
:=\sum_{N<q\le N^2}c_N(q)
\left(\frac{N^2}{q}\right)^{i\tau}.
\tag{3}
\]

Then the finite identity

\[
\boxed{
T_\tau(N)
=N^{2i\tau}\bigl(F_\tau(N)^2-G_\tau(N)\bigr)
}
\tag{4}
\]

holds for every real `tau` and integer `N>=1`. Moreover

\[
|G_\tau(N)|=O(N\log N)
\tag{5}
\]

uniformly in `tau` by absolute values.

For every **fixed** real `tau`, the following are equivalent:

\[
\boxed{
\mathrm{RH}
\quad\Longleftrightarrow\quad
T_\tau(N)=O_{\tau,\varepsilon}(N^{1+\varepsilon})
\ \text{for every }\varepsilon>0.
}
\tag{6}
\]

Thus the obstruction in `MC-035` is not confined to the constant log-radial mode. Isolating any one fixed Mellin character and trying to prove the square-scale `N^{1+o(1)}` estimate as an independently easier intermediate theorem already asks for an RH-equivalent bound.

The surviving possibility is genuinely **coupled or scale-dependent frequency information**: cancellation among modes, an `N`-dependent frequency family with additional structure, or an arithmetic mechanism that produces the fixed/coarse component from independently weaker input. A finite collection of fixed Mellin modes cannot provide a ladder of individually cheaper scalar estimates, because each member already has the full critical burden.

## 1. Exact annular Mellin factorization

The full finite product sum factorizes without analytic continuation:

\[
\begin{aligned}
\sum_{q\le N^2}c_N(q)q^{-i\tau}
&=\sum_{m,n\le N}\mu(m)\mu(n)(mn)^{-i\tau}\\
&=F_\tau(N)^2.
\end{aligned}
\tag{7}
\]

For `q<=N` the separate cutoffs in (2) are inactive, so

\[
c_N(q)=(\mu*\mu)(q).
\tag{8}
\]

Subtracting the interior `q<=N` contribution from (7) and multiplying by the unit-modulus factor `N^{2i\tau}` proves (4).

The interior term requires no cancellation estimate:

\[
\begin{aligned}
|G_\tau(N)|
&\le \sum_{q\le N}|(\mu*\mu)(q)|\\
&\le \sum_{ab\le N}|\mu(a)\mu(b)|\\
&\le \sum_{a\le N}\left\lfloor\frac Na\right\rfloor
=O(N\log N),
\end{aligned}
\tag{9}
\]

which is exactly the crude interior control already sufficient in `MC-035`.

Equation (4) is therefore an exact finite-cutoff statement about the same product annulus used by the Huxley–Watt branch; it does not arise from inserting an Euler product or continuing `1/zeta(s)` into the critical strip.

## 2. Fixed Möbius twists preserve the Mertens critical exponent

Let

\[
M(x)=\sum_{n\le x}\mu(n).
\tag{10}
\]

For fixed real `tau`, partial summation gives

\[
F_\tau(x)
=x^{-i\tau}M(x)
+i\tau\int_1^x M(u)u^{-i\tau-1}\,du.
\tag{11}
\]

Conversely, applying partial summation to `\mu(n)n^{-i\tau}` with the weight `n^{i\tau}` gives

\[
M(x)
=x^{i\tau}F_\tau(x)
-i\tau\int_1^x F_\tau(u)u^{i\tau-1}\,du.
\tag{12}
\]

Hence, for each fixed `tau`,

\[
M(x)=O_\varepsilon(x^{1/2+\varepsilon})
\quad\Longleftrightarrow\quad
F_\tau(x)=O_{\tau,\varepsilon}(x^{1/2+\varepsilon})
\tag{13}
\]

with the quantifier "for every positive `epsilon`" on both sides. Either integral in (11)–(12) preserves every exponent strictly larger than `1/2`; the fixed phase changes only the implied constant.

The classical Littlewood–Titchmarsh Mertens criterion identifies the left side of (13), for every `epsilon>0`, with RH. Thus every fixed phase twist has the same critical exponent boundary. This is not a new criterion: it is the ordinary Mertens criterion transported by an invertible fixed unitary phase through elementary Abel/partial summation.

## 3. Proof of the annular RH equivalence

Assume RH. By the classical Mertens criterion and (11), for every `eta>0`,

\[
F_\tau(N)=O_{\tau,\eta}(N^{1/2+\eta}).
\tag{14}
\]

Equations (4)–(5) then give, after choosing `eta` smaller than the requested exponent and absorbing logarithms,

\[
T_\tau(N)=O_{\tau,\varepsilon}(N^{1+\varepsilon})
\tag{15}
\]

for every `epsilon>0`.

Conversely, suppose (15) holds for one fixed real `tau` and every positive `epsilon`. Since `|N^{2i\tau}|=1` and `|F_\tau(N)^2|=|F_\tau(N)|^2`, (4) and (5) imply

\[
|F_\tau(N)|^2
\le |T_\tau(N)|+|G_\tau(N)|
\ll_{\tau,\varepsilon}N^{1+\varepsilon}+N\log N.
\tag{16}
\]

Using a smaller auxiliary exponent and absorbing the logarithm yields

\[
F_\tau(N)=O_{\tau,\delta}(N^{1/2+\delta})
\tag{17}
\]

for every `delta>0`. Equation (12) transfers the same critical exponent back to `M(N)`, and the classical criterion gives RH. This proves (6).

The case `tau=0` reduces to the constant annular kernel

\[
T_0(N)=M(N)^2-\sum_{q\le N}(\mu*\mu)(q),
\tag{18}
\]

which is the coarse statistic appearing inside the zero log-frequency term of `MC-035`. The present result shows that the same hardness persists at every fixed nonzero Mellin frequency rather than being a special accident of the constant mode.

## 4. What this does and does not kill

A natural response to `MC-035` is to remove the logarithmic mean of the source sawtooth and hope that its nonzero log frequencies can be controlled one at a time. Equation (6) rules out the simplest version of that route. Any proof that supplies the critical annular estimate for even one **fixed** character `x^{i\tau}` already supplies RH.

This conclusion must not be overextended to an `N`-dependent Fourier basis. On the finite interval `0<=u<=log N`, a fixed Fourier index `k` has physical Mellin frequency

\[
\tau_N=\frac{2\pi k}{\log N},
\tag{19}
\]

which varies with `N`. The two-way partial-summation argument above compares one fixed twist at all scales; it does not say that endpoint estimates available only at the varying frequencies `tau_N` automatically untwist to `M(x)` at all smaller `x`. A useful `N`-dependent or coupled-frequency theorem is therefore not excluded by (6).

Nor does (6) give a lower bound for the complete Huxley–Watt sawtooth functional. The fixed-character contributions can cancel each other, and `MC-035` already identified such coupling as the essential unresolved possibility. Taking absolute values mode by mode can only destroy that opportunity.

Finally, `MC-034` shows that matched random multiplicative sign controls place every bounded radial annular functional at the critical `N^{1+o(1)}` power scale in RMS. The present theorem demonstrates why that probabilistic normalization does not make a fixed deterministic Mellin mode an independently weaker target for Möbius: at the all-minus prime-sign point, its critical deterministic estimate is equivalent to RH.

## 5. Prior art and novelty assessment

The equivalence between RH and

\[
M(x)=O_\varepsilon(x^{1/2+\varepsilon})
\tag{20}
\]

for every positive `epsilon` is classical Littlewood–Titchmarsh theory and is already represented by `research/prior_art/mobius-summatory-criterion.md`. A standard monograph anchor is E. C. Titchmarsh, revised by D. R. Heath-Brown, *The Theory of the Riemann Zeta-Function*, 2nd ed., Clarendon Press / Oxford University Press (1986), §14.25. Twisting and untwisting partial sums by `n^{-i\tau}` through Abel summation is standard Dirichlet-polynomial technology. Likewise, (7) is the elementary finite product factorization underlying the Huxley–Watt cutoff identities already audited in this line and anchored by `MC-S24`.

A targeted check of the Huxley–Watt literature, logarithmic/Mellin decompositions of the cutoff annulus, and twisted Mertens formulations did not identify a source that warrants a novelty claim for this specialization. None is made.

The durable contribution is the line-specific **information audit**: the exact annular coefficient maps every fixed Mellin character to the square of a fixed twisted Mertens sum plus an absolutely controlled interior term. Therefore every individually isolated fixed log-frequency component has the same RH-scale obstruction, sharpening `MC-035` from one coarse zero mode to an entire fixed-frequency family.

## 6. Consequence for the live reciprocal-phase clue

`MC-033` reduces the annular Huxley–Watt coefficient to deterministic parity against a central-divisor occupancy weight; `MC-034` gives the matched multiplicative RMS normalization; and `MC-035` shows that the source sawtooth has a nonzero log-radial mean whose separately controlled coarse mode is RH-equivalent.

The present result removes another scalar escape: replacing the zero mode by one or finitely many **fixed** nonzero Mellin characters does not produce a sequence of weaker intermediate obligations. Each critical fixed-character bound is already equivalent to RH.

The remaining live target in `CLUE-reciprocal-phase-prime-log-slab-coupling` must therefore exploit at least one genuinely different ingredient: coupled signed cancellation among log frequencies, an `N`-dependent frequency family with a source-natural transfer law, or arithmetic information that forces the fixed/coarse components from hypotheses independently weaker than Mertens-scale cancellation. Any proposal that isolates a fixed Mellin mode and then estimates it at `N^{1+o(1)}` has simply relocated the full RH burden.